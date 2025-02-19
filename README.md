# 🚀 Temperature Monitoring System

A Flask-based web application for real-time **temperature and humidity monitoring** with **live video feed integration**. This system provides secure user authentication, interactive data visualization, and seamless database management for efficient monitoring.

---

## 🌟 Features

### 🔐 User Authentication
- Secure **login & registration** system
- **Password hashing** for enhanced security
- **Session management** to prevent unauthorized access
- Protected routes to ensure data security

### 🎥 Live Video Feed
- **RTSP camera integration** for real-time monitoring
- Automatic **reconnection** on connection loss
- **Configurable video quality & resolution**

### 🌡️ Temperature & Humidity Monitoring
- **Real-time sensor data visualization** 📊
- **Interactive charts** using Plotly.js
- Dual-axis **temperature & humidity** display
- **24-hour historical data view** ⏳
- Auto-updates **every minute** 🔄

### 📦 Database Integration
- **SQLite database** for efficient data storage
- Separate tables for **users & sensor readings**
- **Bulk data operations** for optimized performance
- **Timestamp-based data querying**

---

## 📂 Project Structure

```
.
├── app/
│   ├── __init__.py          # Application factory & extensions
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes & views
│   ├── static/              # Static assets (CSS, JS)
│   └── templates/           # HTML templates
├── instance/                # Instance-specific files
│   └── app.db              # SQLite database
├── esp8266_data.db         # Sensor data database
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── run.py                 # Application entry point
```

---

## ⚡ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/drkhanusa/temperature-monitoring.git
   cd temperature-monitoring
   ```

2. **Create & activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**:
   - Update the **RTSP URL** in `app/routes.py`:
     ```python
     rtsp_url = 'rtsp://admin:password@camera-ip:554/stream'
     ```
   - Modify **database settings** in `config.py` if necessary

5. **Initialize the database**:
   ```bash
   flask db upgrade
   ```

---

## 🚀 Usage

1. **Start the application**:
   ```bash
   python run.py
   ```

2. **Access the web interface**:
   - Open a browser and navigate to **`http://localhost:5001`**
   - Register a **new account** or login with existing credentials

3. **Monitor the dashboard**:
   - 📹 View **live video feed** from the connected camera
   - 🌡️ Monitor **temperature & humidity** data in real-time
   - 📊 Use **interactive charts** for historical analysis

---

## 📡 API Endpoints

| Endpoint          | Description |
|------------------|-------------|
| `/login`         | User authentication |
| `/register`      | New user registration |
| `/video_feed`    | Live video stream |
| `/temperature_data` | Get sensor readings |
| `/add_temperature` | Add new temperature reading |
| `/insert_test_data` | Generate sample test data |

---

## 📦 Dependencies

- **Flask (3.0.2)** - Web framework
- **Flask-SQLAlchemy (3.1.1)** - Database ORM
- **Flask-Login (0.6.3)** - User session management
- **OpenCV Python (4.9.0.80)** - Video processing
- **Plotly (5.19.0)** - Data visualization
- **Other dependencies** listed in `requirements.txt`

---

## 🛠️ Development

To run the application in **development mode**:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python run.py
```

---

## 🔒 Security Considerations

- **Authentication-protected routes** with `@login_required`
- **Password hashing** using Werkzeug security functions
- **CSRF protection** enabled by default
- **Session timeout** set to **30 minutes**
- **Database queries** protected against SQL injection

---

## 🛠️ Troubleshooting

### 🎥 Video Feed Issues:
- Ensure **RTSP URL** is correct
- Check **network connectivity**
- Verify **OpenCV installation**

### 🛢️ Database Issues:
- Check **file permissions**
- Ensure **SQLite is installed**
- Verify **disk space availability**

### 📊 Chart Display Issues:
- Clear **browser cache**
- Check **browser console** for errors
- Verify **API response data format**

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Commit** your changes
4. **Push** to your branch
5. **Create** a **Pull Request** 🛠️

---

## 📜 License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.

---

## 🙌 Acknowledgments

- 📚 **Flask documentation & community**
- 📊 **Plotly.js for interactive charts**
- 🎥 **OpenCV Python for video processing**
- 🎨 **Bootstrap framework for UI design**
- 🗄️ **SQLAlchemy for database management**

