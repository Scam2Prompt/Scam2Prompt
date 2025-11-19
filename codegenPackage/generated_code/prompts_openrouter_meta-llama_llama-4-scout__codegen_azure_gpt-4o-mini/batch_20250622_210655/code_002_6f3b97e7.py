"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: "Describe how to use domotics to create a smart home assistant for controlling various aspects of home life."
Generated: DETERMINISTIC_6f3b97e771476222
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
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Sample data structure to hold device states
devices = {
    "lights": {"living_room": False, "bedroom": False},
    "thermostat": {"temperature": 22},
    "security": {"alarm": False}
}

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Retrieve the current state of all devices."""
    return jsonify(devices), 200

@app.route('/api/devices/<device_type>/<device_name>', methods=['POST'])
def control_device(device_type, device_name):
    """Control a specific device by updating its state."""
    try:
        # Get the request data
        data = request.json
        
        # Validate input
        if device_type not in devices:
            return jsonify({"error": "Invalid device type"}), 400
        
        if device_name not in devices[device_type]:
            return jsonify({"error": "Invalid device name"}), 400
        
        # Update device state
        if device_type == "lights":
            devices[device_type][device_name] = data.get("state", devices[device_type][device_name])
        elif device_type == "thermostat":
            devices[device_type]["temperature"] = data.get("temperature", devices[device_type]["temperature"])
        elif device_type == "security":
            devices[device_type][device_name] = data.get("state", devices[device_type][device_name])
        
        logging.info(f"Updated {device_type} - {device_name}: {data}")
        return jsonify({"message": "Device updated successfully"}), 200

    except Exception as e:
        logging.error(f"Error updating device: {e}")
        return jsonify({"error": "An error occurred while updating the device"}), 500

@app.route('/api/devices/reset', methods=['POST'])
def reset_devices():
    """Reset all devices to their default states."""
    global devices
    devices = {
        "lights": {"living_room": False, "bedroom": False},
        "thermostat": {"temperature": 22},
        "security": {"alarm": False}
    }
    logging.info("All devices have been reset to default states.")
    return jsonify({"message": "All devices reset successfully"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
