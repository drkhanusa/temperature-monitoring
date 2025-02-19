# import sqlite3
# import matplotlib.pyplot as plt
# from datetime import datetime

# # Connect to the database
# db_name = "esp8266_data.db"
# conn = sqlite3.connect(db_name)
# cursor = conn.cursor()

# # Query the data
# cursor.execute("SELECT timestamp, temperature, humidity FROM sensor_data")
# data = cursor.fetchall()

# # Close the connection
# conn.close()

# # Prepare data for plotting
# timestamps = [datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') for row in data]
# temperatures = [row[1] for row in data]
# humidities = [row[2] for row in data]


import sqlite3
from datetime import datetime

# Connect to the database
db_name = "./instance/esp8266_data.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        temperature REAL,
        humidity REAL
    )
''')

# Insert data
sample_data = [
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 25.3, 60.5),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 26.1, 58.2),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 24.8, 62.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 23.8, 60.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 28.4, 64.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 24.9, 69.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 25.8, 72.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 29.8, 77.0),
    (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 21.8, 89.0),
    
]

cursor.executemany("INSERT INTO sensor_data (timestamp, temperature, humidity) VALUES (?, ?, ?)", sample_data)

# Commit and close
conn.commit()
conn.close()

print("Data inserted successfully!")