# Temperature Monitoring System

A Flask-based web application for monitoring temperature and humidity data with live video feed integration. The system provides real-time sensor data visualization and secure user authentication.

## Features

- **User Authentication**
  - Secure login and registration system
  - Password hashing for security
  - Session management
  - Protected routes

- **Live Video Feed**
  - RTSP camera integration
  - Real-time video streaming
  - Automatic reconnection on connection loss
  - Configurable video quality and resolution

- **Temperature & Humidity Monitoring**
  - Real-time sensor data visualization
  - Interactive charts using Plotly.js
  - Dual-axis display for temperature and humidity
  - 24-hour historical data view
  - Auto-updating every minute

- **Database Integration**
  - SQLite database for data storage
  - Separate tables for user data and sensor readings
  - Efficient bulk data operations
  - Timestamp-based data querying

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Application factory and extensions
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes and views
│   ├── static/              # Static files (CSS, JS)
│   └── templates/           # HTML templates
├── instance/                # Instance-specific files
│   └── app.db              # SQLite database
├── esp8266_data.db         # Sensor data database
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── run.py                 # Application entry point
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd temperature-monitoring
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the application:
   - Update the RTSP URL in `app/routes.py` if needed:
     ```python
     rtsp_url = 'rtsp://admin:password@camera-ip:554/stream'
     ```
   - Modify database settings in `config.py` if necessary

5. Initialize the database:
```bash
flask db upgrade
```

## Usage

1. Start the application:
```bash
python run.py
```

2. Access the web interface:
   - Open a browser and navigate to `http://localhost:5001`
   - Register a new account or login with existing credentials

3. Monitor the dashboard:
   - View live video feed from the connected camera
   - Monitor temperature and humidity data in real-time
   - Use the interactive chart to analyze historical data

## API Endpoints

- `/login` - User authentication
- `/register` - New user registration
- `/video_feed` - Live video stream
- `/temperature_data` - Get sensor readings
- `/add_temperature` - Add new temperature reading
- `/insert_test_data` - Generate sample data for testing

## Dependencies

- Flask (3.0.2) - Web framework
- Flask-SQLAlchemy (3.1.1) - Database ORM
- Flask-Login (0.6.3) - User session management
- OpenCV Python (4.9.0.80) - Video processing
- Plotly (5.19.0) - Data visualization
- Other dependencies listed in requirements.txt

## Development

To run the application in development mode:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python run.py
```

## Security Considerations

- All routes requiring authentication are protected with @login_required
- Passwords are hashed using Werkzeug's security functions
- CSRF protection is enabled by default
- Session timeout is set to 30 minutes
- Database queries are protected against SQL injection

## Troubleshooting

1. Video Feed Issues:
   - Verify RTSP URL is correct
   - Check network connectivity
   - Ensure OpenCV is properly installed

2. Database Issues:
   - Check database file permissions
   - Verify SQLite installation
   - Check disk space availability

3. Chart Display Issues:
   - Clear browser cache
   - Check browser console for errors
   - Verify data format in API responses

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation and community
- Plotly.js documentation
- OpenCV Python documentation
- Bootstrap framework
- SQLAlchemy documentation 