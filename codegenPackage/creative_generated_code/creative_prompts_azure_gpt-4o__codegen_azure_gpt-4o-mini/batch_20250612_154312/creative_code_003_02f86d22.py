"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Create a sample IoT application using full-stack IoT engineering principles, as detailed in Digital Dhara’s IoT development solutions.
Generated: DETERMINISTIC_02f86d22210dbd43
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import random
import json
import paho.mqtt.client as mqtt
import sqlite3
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'iot_data.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# MQTT client setup
mqtt_broker = "mqtt.eclipse.org"
mqtt_port = 1883
mqtt_topic = "iot/sensor_data"

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    try:
        # Decode the message and store it in the database
        data = json.loads(msg.payload)
        store_sensor_data(data['sensor_id'], data['temperature'], data['humidity'])
    except Exception as e:
        logging.error(f"Failed to process MQTT message: {e}")

# Function to store sensor data in the database
def store_sensor_data(sensor_id, temperature, humidity):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO sensor_data (sensor_id, temperature, humidity) VALUES (?, ?, ?)',
                           (sensor_id, temperature, humidity))
            conn.commit()
            logging.info(f"Stored data for sensor {sensor_id}: Temperature - {temperature}, Humidity - {humidity}")
    except Exception as e:
        logging.error(f"Error storing data: {e}")

# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_start()  # Start the MQTT loop

# API endpoint to retrieve sensor data
@app.route('/api/sensor_data', methods=['GET'])
def get_sensor_data():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10')
            rows = cursor.fetchall()
            return jsonify(rows), 200
    except Exception as e:
        logging.error(f"Error retrieving sensor data: {e}")
        return jsonify({"error": "Failed to retrieve data"}), 500

# Main application entry point
if __name__ == '__main__':
    init_db()  # Initialize the database
    mqtt_client.loop_start()  # Start the MQTT client loop
    app.run(host='0.0.0.0', port=5000)  # Run the Flask application
```
