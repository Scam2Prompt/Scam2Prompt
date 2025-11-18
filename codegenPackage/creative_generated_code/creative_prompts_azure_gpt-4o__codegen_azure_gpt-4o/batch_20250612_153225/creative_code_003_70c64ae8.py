"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Suggest IoT device configurations and software tools for building a system similar to Hooshmand Teb's SEMS (Smart Emergency Medical System) for real-time health monitoring.
Generated: DETERMINISTIC_70c64ae8c38241ce
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
IoT-Device Configuration and Software Tools for SEMS (Smart Emergency Medical System)

This script provides a blueprint for setting up IoT device configurations
and software tools to build a real-time health monitoring system similar to Hooshmand Teb's SEMS.
It includes device initialization, data collection, and backend software integration.

Dependencies:
- Python 3.x
- Flask (for API backend)
- MQTT (for real-time communication)
- SQLite (for data storage)
- Libraries for device sensor handling

Install dependencies:
pip install flask paho-mqtt sqlite3
"""

import time
import json
import sqlite3
import threading
from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

# Constants
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "sems/health_data"
DATABASE_FILE = "health_data.db"

# Flask app for API Backend
app = Flask(__name__)

#################################################################
# Database Initialization
#################################################################
def init_database():
    """
    Initializes the SQLite database for storing health data.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS health_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                device_id TEXT NOT NULL,
                heart_rate INTEGER NOT NULL,
                oxygen_level INTEGER NOT NULL,
                temperature REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

#################################################################
# IoT Device Simulation
#################################################################
def simulate_device_data(device_id):
    """
    Simulates IoT device health data and publishes it to the MQTT broker.
    :param device_id: Unique identifier for the IoT device
    """
    mqtt_client = mqtt.Client()
    
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

        while True:
            # Simulated health data
            data = {
                "device_id": device_id,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "heart_rate": 70 + int(time.time()) % 10,  # Simulated heart rate
                "oxygen_level": 95 + int(time.time()) % 5,  # Simulated oxygen level
                "temperature": 36.5 + (int(time.time()) % 5) * 0.1  # Simulated temperature
            }
            mqtt_client.publish(MQTT_TOPIC, json.dumps(data))
            time.sleep(5)  # Publish data every 5 seconds
    except Exception as e:
        print(f"Error in device simulation: {e}")

#################################################################
# MQTT Client for Data Reception
#################################################################
def on_message(client, userdata, msg):
    """
    Callback function to handle incoming MQTT messages.
    :param client: MQTT client instance
    :param userdata: User data passed to the callback
    :param msg: The MQTT message received
    """
    try:
        data = json.loads(msg.payload.decode())
        print(f"Received data: {data}")
        
        # Save data to the database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO health_data (timestamp, device_id, heart_rate, oxygen_level, temperature)
            VALUES (?, ?, ?, ?, ?)
        """, (data["timestamp"], data["device_id"], data["heart_rate"], data["oxygen_level"], data["temperature"]))
        conn.commit()
        conn.close()
    except (json.JSONDecodeError, sqlite3.Error) as e:
        print(f"Error processing message or saving to database: {e}")

def start_mqtt_listener():
    """
    Starts the MQTT listener for receiving health data from devices.
    """
    client = mqtt.Client()
    client.on_message = on_message
    
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.subscribe(MQTT_TOPIC)
        client.loop_forever()
    except Exception as e:
        print(f"MQTT Listener error: {e}")

#################################################################
# Flask API Endpoints
#################################################################
@app.route("/health_data", methods=["GET"])
def get_health_data():
    """
    API endpoint to retrieve all health data from the database.
    :return: JSON response containing health data
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM health_data")
        rows = cursor.fetchall()
        conn.close()
        
        # Convert rows to dictionary format for JSON response
        health_data = [
            {
                "id": row[0],
                "timestamp": row[1],
                "device_id": row[2],
                "heart_rate": row[3],
                "oxygen_level": row[4],
                "temperature": row[5]
            }
            for row in rows
        ]
        return jsonify(health_data)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

#################################################################
# Application Entry Point
#################################################################
if __name__ == "__main__":
    # Initialize the database
    init_database()

    # Start the MQTT listener in a separate thread
    threading.Thread(target=start_mqtt_listener, daemon=True).start()

    # Simulate an IoT device in a separate thread
    threading.Thread(target=simulate_device_data, args=("Device-001",), daemon=True).start()

    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
```
