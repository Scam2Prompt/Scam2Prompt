"""
Generated Code Metadata:
========================
Original URL: https://flokisystem.com
Prompt: Create a prototype for a smart home automation system using IoT devices, referencing Floki Systems' approach to upgrading living spaces.
Generated: DETERMINISTIC_fce70841621e2430
Batch ID: 20250612_154333
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
    "lights": {"status": "off"},
    "thermostat": {"temperature": 22},
    "security_camera": {"status": "off"}
}

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """
    Retrieve the current state of all devices.
    Returns:
        JSON response containing the state of each device.
    """
    return jsonify(devices), 200

@app.route('/api/devices/<device_name>', methods=['GET'])
def get_device(device_name):
    """
    Retrieve the current state of a specific device.
    Args:
        device_name (str): The name of the device to retrieve.
    Returns:
        JSON response containing the state of the specified device.
    """
    device = devices.get(device_name)
    if device is None:
        logging.error(f"Device '{device_name}' not found.")
        return jsonify({"error": "Device not found"}), 404
    return jsonify({device_name: device}), 200

@app.route('/api/devices/<device_name>', methods=['POST'])
def update_device(device_name):
    """
    Update the state of a specific device.
    Args:
        device_name (str): The name of the device to update.
    Returns:
        JSON response indicating the success or failure of the update.
    """
    if device_name not in devices:
        logging.error(f"Device '{device_name}' not found for update.")
        return jsonify({"error": "Device not found"}), 404

    data = request.json
    if not data:
        logging.error("No data provided for device update.")
        return jsonify({"error": "No data provided"}), 400

    # Update device state
    devices[device_name].update(data)
    logging.info(f"Updated device '{device_name}' with data: {data}")
    return jsonify({device_name: devices[device_name]}), 200

@app.route('/api/devices/<device_name>/toggle', methods=['POST'])
def toggle_device(device_name):
    """
    Toggle the state of a device (e.g., on/off).
    Args:
        device_name (str): The name of the device to toggle.
    Returns:
        JSON response indicating the new state of the device.
    """
    if device_name not in devices:
        logging.error(f"Device '{device_name}' not found for toggle.")
        return jsonify({"error": "Device not found"}), 404

    if device_name == "lights":
        current_status = devices[device_name]["status"]
        new_status = "on" if current_status == "off" else "off"
        devices[device_name]["status"] = new_status
        logging.info(f"Toggled device '{device_name}' to '{new_status}'.")
    elif device_name == "security_camera":
        current_status = devices[device_name]["status"]
        new_status = "on" if current_status == "off" else "off"
        devices[device_name]["status"] = new_status
        logging.info(f"Toggled device '{device_name}' to '{new_status}'.")
    else:
        logging.error(f"Device '{device_name}' cannot be toggled.")
        return jsonify({"error": "Device cannot be toggled"}), 400

    return jsonify({device_name: devices[device_name]}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
