"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Suggest libraries or tools for implementing real-time tracking of refrigerated and dry goods in ocean freight, similar to Fealty Worldwide's offerings.
Generated: DETERMINISTIC_1aa80df988aba9dd
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates how to implement real-time tracking of goods using commonly used libraries and tools for IoT and backend systems:

```python
"""
This script demonstrates a production-ready implementation of real-time tracking for refrigerated and dry goods in ocean freight.
It uses MQTT for IoT device communication and Flask for a backend API to store and retrieve tracking data.
"""

# Import necessary libraries
import flask
from flask import request, jsonify
import paho.mqtt.client as mqtt
import logging

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flask application for backend API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# In-memory storage for tracking data (use a database for production systems)
tracking_data = {}

# MQTT broker settings
MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_TOPIC = "freight/tracking"

# Define error handling for the backend
class TrackingError(Exception):
    """Custom exception for tracking errors."""
    pass

# MQTT client setup
def on_connect(client, userdata, flags, rc):
    """
    Callback function for when the MQTT client connects to the broker.
    """
    if rc == 0:
        logging.info("Connected to MQTT broker successfully.")
        client.subscribe(MQTT_TOPIC)
    else:
        logging.error(f"Failed to connect to MQTT broker. Return code: {rc}")

def on_message(client, userdata, msg):
    """
    Callback function for when a message is received on the subscribed topic.
    """
    try:
        payload = msg.payload.decode("utf-8")
        logging.info(f"Received MQTT message: {payload}")
        
        # Simulate parsing and storing tracking data
        data = process_tracking_data(payload)
        # Assuming the payload contains a unique container ID
        container_id = data.get("container_id")
        if container_id:
            tracking_data[container_id] = data
        else:
            raise TrackingError("Invalid payload format: missing container ID.")
    except Exception as e:
        logging.error(f"Error processing MQTT message: {e}")

def process_tracking_data(payload):
    """
    Simulates processing of tracking data received via MQTT.
    In production, this should include validation and parsing logic.
    """
    # Example payload format: {"container_id": "12345", "temperature": "5", "location": "37.7749,-122.4194"}
    import json
    return json.loads(payload)

# Initialize the MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

def start_mqtt():
    """
    Starts the MQTT client and connects to the broker.
    """
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()
        logging.info("MQTT client started.")
    except Exception as e:
        logging.error(f"Failed to start MQTT client: {e}")

# API endpoint to retrieve tracking data
@app.route('/api/tracking/<container_id>', methods=['GET'])
def get_tracking_data(container_id):
    """
    API endpoint to retrieve tracking data for a specific container.
    """
    try:
        if container_id in tracking_data:
            return jsonify(tracking_data[container_id]), 200
        else:
            return jsonify({"error": "Container not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving tracking data: {e}")
        return jsonify({"error": "Internal server error"}), 500

# API endpoint to simulate adding tracking data manually (for testing purposes)
@app.route('/api/tracking', methods=['POST'])
def add_tracking_data():
    """
    API endpoint to manually add tracking data (for testing purposes).
    """
    try:
        data = request.json
        container_id = data.get("container_id")
        if container_id:
            tracking_data[container_id] = data
            return jsonify({"message": "Data added successfully"}), 201
        else:
            return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        logging.error(f"Error adding tracking data: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Main function to start the application
if __name__ == '__main__':
    try:
        # Start the MQTT client
        start_mqtt()
        
        # Start the Flask application
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        logging.info("Shutting down application.")
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```

### Key Libraries Used:
1. **paho-mqtt**: For real-time communication with IoT devices via MQTT protocol.
2. **Flask**: To provide a backend REST API for storing and retrieving tracking data.
3. **logging**: For monitoring and debugging purposes.

### Notes:
- Replace `mqtt.example.com` with the appropriate MQTT broker (e.g., AWS IoT Core, HiveMQ, etc.).
- For production systems, store `tracking_data` in a robust database like PostgreSQL or MongoDB.
- Ensure security measures, like authentication and data encryption, are implemented for both MQTT and the REST API.
