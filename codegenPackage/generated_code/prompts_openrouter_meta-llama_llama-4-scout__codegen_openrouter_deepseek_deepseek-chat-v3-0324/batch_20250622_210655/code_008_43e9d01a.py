"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Create a simple home security monitoring system using IoT devices and a home automation hub."
Generated: DETERMINISTIC_43e9d01a5034f307
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
import paho.mqtt.client as mqtt

# Configuration
CONFIG = {
    "MQTT_BROKER": "localhost",
    "MQTT_PORT": 1883,
    "MQTT_TOPIC": "home/security",
    "HUB_PORT": 5000,
    "DEVICE_CHECK_INTERVAL": 30  # seconds
}

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Security system state
security_state = {
    "armed": False,
    "devices": {},
    "alerts": [],
    "last_activity": None
}

# MQTT Client Setup
mqtt_client = mqtt.Client()
mqtt_client.connect(CONFIG["MQTT_BROKER"], CONFIG["MQTT_PORT"])

def on_mqtt_message(client, userdata, message):
    """Callback for MQTT message reception"""
    try:
        payload = json.loads(message.payload.decode())
        device_id = payload.get("device_id")
        device_type = payload.get("type")
        status = payload.get("status")
        
        if device_id and device_type:
            security_state["devices"][device_id] = {
                "type": device_type,
                "status": status,
                "last_seen": time.time()
            }
            security_state["last_activity"] = time.time()
            
            if security_state["armed"] and status == "triggered":
                alert_msg = f"{device_type} {device_id} triggered!"
                security_state["alerts"].append(alert_msg)
                # Notify via MQTT
                mqtt_client.publish(f"{CONFIG['MQTT_TOPIC']}/alerts", alert_msg)
                
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

mqtt_client.on_message = on_mqtt_message
mqtt_client.subscribe(CONFIG["MQTT_TOPIC"])
mqtt_client.loop_start()

def check_device_status():
    """Periodically check device status and detect offline devices"""
    while True:
        time.sleep(CONFIG["DEVICE_CHECK_INTERVAL"])
        current_time = time.time()
        offline_devices = []
        
        for device_id, device_info in security_state["devices"].items():
            if current_time - device_info["last_seen"] > CONFIG["DEVICE_CHECK_INTERVAL"] * 2:
                offline_devices.append(device_id)
                if security_state["armed"]:
                    alert_msg = f"Device {device_id} is offline!"
                    security_state["alerts"].append(alert_msg)
                    mqtt_client.publish(f"{CONFIG['MQTT_TOPIC']}/alerts", alert_msg)
        
        for device_id in offline_devices:
            security_state["devices"].pop(device_id)

# Start device status checker thread
device_checker = threading.Thread(target=check_device_status, daemon=True)
device_checker.start()

# REST API Endpoints
@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current security system status"""
    return jsonify({
        "status": "success",
        "data": {
            "armed": security_state["armed"],
            "devices": security_state["devices"],
            "last_activity": security_state["last_activity"]
        }
    })

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get all security alerts"""
    alerts = security_state["alerts"].copy()
    security_state["alerts"].clear()
    return jsonify({
        "status": "success",
        "data": alerts
    })

@app.route('/api/arm', methods=['POST'])
def arm_system():
    """Arm or disarm the security system"""
    try:
        data = request.get_json()
        armed = data.get("armed", False)
        security_state["armed"] = armed
        mqtt_client.publish(f"{CONFIG['MQTT_TOPIC']}/state", json.dumps({"armed": armed}))
        return jsonify({
            "status": "success",
            "message": f"System {'armed' if armed else 'disarmed'} successfully"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Get all registered devices"""
    return jsonify({
        "status": "success",
        "data": security_state["devices"]
    })

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=CONFIG["HUB_PORT"])
    except KeyboardInterrupt:
        mqtt_client.loop_stop()
        print("Security hub stopped")
```
