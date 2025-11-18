"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Recommend an IoT framework to monitor and display battery and liquid levels in Elfworld vape devices, and provide a sample implementation in Python.
Generated: DETERMINISTIC_3f50842db01ad8a0
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample Implementation of an IoT Framework to Monitor and Display Battery
and Liquid Levels in Elfworld Vape Devices using Python.

This example uses Flask for the API, MQTT for IoT messaging, and SQLite for data storage.

Requirements:
- Install Flask: `pip install flask`
- Install Paho MQTT: `pip install paho-mqtt`
- SQLite is included with Python by default.
"""

import sqlite3
import json
from flask import Flask, jsonify, request
import paho.mqtt.client as mqtt

# Flask Application
app = Flask(__name__)

# Database setup
DB_NAME = "vape_device_data.db"


def init_db():
    """Initialize SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS device_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            battery_level INTEGER NOT NULL,
            liquid_level INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


# MQTT Setup
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "elfworld/vape_data"

mqtt_client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    """Handle MQTT connection event."""
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client, userdata, msg):
    """Handle incoming MQTT messages."""
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
        device_id = payload.get("device_id")
        battery_level = payload.get("battery_level")
        liquid_level = payload.get("liquid_level")

        # Validate data
        if device_id and battery_level is not None and liquid_level is not None:
            # Save data to SQLite database
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO device_data (device_id, battery_level, liquid_level)
                VALUES (?, ?, ?)
            """, (device_id, battery_level, liquid_level))
            conn.commit()
            conn.close()
        else:
            print("Invalid data received via MQTT.")
    except Exception as e:
        print(f"Error processing MQTT message: {e}")


# Flask Routes
@app.route("/data", methods=["GET"])
def get_data():
    """Fetch all vape device data."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM device_data")
        rows = cursor.fetchall()
        conn.close()

        # Format data as JSON
        data = [
            {
                "id": row[0],
                "device_id": row[1],
                "battery_level": row[2],
                "liquid_level": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch data: {e}"}), 500


@app.route("/data/<device_id>", methods=["GET"])
def get_device_data(device_id):
    """Fetch data for a specific vape device."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM device_data WHERE device_id = ?", (device_id,))
        rows = cursor.fetchall()
        conn.close()

        # Format data as JSON
        data = [
            {
                "id": row[0],
                "device_id": row[1],
                "battery_level": row[2],
                "liquid_level": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch data: {e}"}), 500


# Main Function
if __name__ == "__main__":
    # Initialize database
    init_db()

    # Setup MQTT client
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)

    # Start MQTT client in a background thread
    mqtt_client.loop_start()

    # Start Flask application
    app.run(host="0.0.0.0", port=5000)
```
