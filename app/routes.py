import cv2
import base64
from io import BytesIO
from datetime import datetime, timedelta
import json
from urllib.parse import urlparse
from flask import Blueprint, render_template, redirect, url_for, request, Response, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, TemperatureData
from app import db
import random

auth = Blueprint('auth', __name__)
main = Blueprint('main', __name__)

# Authentication routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('auth.register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Main routes
@main.route('/')
@login_required
def index():
    return render_template('index.html')

# Video stream generation
def gen_frames():
    # Use RTSP stream instead of webcam
    rtsp_url = 'rtsp://admin:Fitdnu12@192.168.167.163:554/Streaming/Channels/101/'
    camera = cv2.VideoCapture(rtsp_url)
    
    # Set buffer size and timeout
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    while True:
        success, frame = camera.read()
        if not success:
            camera.release()
            camera = cv2.VideoCapture(rtsp_url)  # Reconnect if connection lost
            continue
            
        # Resize frame for better performance
        frame = cv2.resize(frame, (800, 600))
        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
            
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    camera.release()

@main.route('/video_feed')
@login_required
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Temperature data routes
@main.route('/insert_test_data')
@login_required
def insert_test_data():
    try:
        # Clear existing data
        TemperatureData.query.delete()
        db.session.commit()
        
        # Generate 24 hours of test data
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=24)
        current_time = start_time
        
        records = []
        while current_time <= end_time:
            temperature = round(random.uniform(20, 30), 2)
            humidity = round(random.uniform(40, 60), 2)
            
            data = TemperatureData(
                temperature=temperature,
                humidity=humidity,
                timestamp=current_time
            )
            records.append(data)
            current_time += timedelta(minutes=30)
        
        db.session.bulk_save_objects(records)
        db.session.commit()
        
        print(f"Successfully inserted {len(records)} test records")
        return jsonify({
            'message': 'Test data inserted successfully',
            'count': len(records)
        })
    except Exception as e:
        db.session.rollback()
        print(f"Error inserting test data: {str(e)}")
        return jsonify({'error': str(e)}), 500

@main.route('/temperature_data')
@login_required
def get_temperature_data():
    try:
        # Get the last 24 hours of temperature data
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=24)
        
        data = TemperatureData.query.filter(
            TemperatureData.timestamp.between(start_time, end_time)
        ).order_by(TemperatureData.timestamp.asc()).all()
        
        if not data:
            print("No data found in the specified time range")
            return jsonify([])
        
        result = []
        for record in data:
            dict_record = record.to_dict()
            if dict_record:
                result.append(dict_record)
        
        print(f"Returning {len(result)} records")
        return jsonify(result)
    except Exception as e:
        print(f"Error fetching temperature data: {str(e)}")
        return jsonify({'error': str(e)}), 500

@main.route('/add_temperature', methods=['POST'])
@login_required
def add_temperature():
    data = request.get_json()
    if 'temperature' not in data:
        return jsonify({'error': 'No temperature value provided'}), 400
    
    new_record = TemperatureData(temperature=data['temperature'])
    db.session.add(new_record)
    db.session.commit()
    
    return jsonify(new_record.to_dict()), 201

@main.route('/generate_sample_data')
@login_required
def generate_sample_data():
    # Generate sample data for the last 24 hours
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)
    
    # Generate a data point every 30 minutes
    current_time = start_time
    while current_time <= end_time:
        # Generate random temperature between 20 and 30 degrees
        temperature = 20 + (datetime.now().timestamp() % 10)
        
        new_record = TemperatureData(
            temperature=temperature,
            timestamp=current_time
        )
        db.session.add(new_record)
        current_time += timedelta(minutes=30)
    
    db.session.commit()
    return jsonify({'message': 'Sample data generated successfully'}) 