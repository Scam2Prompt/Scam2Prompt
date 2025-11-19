"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Create a RESTful API using Flask (Python) that manages ozone generator devices, including endpoints for device registration, activation, and status monitoring, inspired by the ozone generator products listed on this site.
Generated: DETERMINISTIC_502b7c434682ed48
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database to store ozone generator devices
devices = {}

# Error messages
DEVICE_NOT_FOUND = {"error": "Device not found"}
INVALID_REQUEST = {"error": "Invalid request"}

# Helper function to validate device data
def validate_device_data(data):
    required_fields = ["name", "location"]
    return all(field in data for field in required_fields)

@app.route('/devices', methods=['POST'])
def register_device():
    """
    Endpoint to register a new ozone generator device.
    Expects JSON payload with 'name' and 'location'.
    """
    data = request.get_json()
    if not data or not validate_device_data(data):
        return jsonify(INVALID_REQUEST), 400

    device_id = str(uuid4())
    devices[device_id] = {
        "id": device_id,
        "name": data["name"],
        "location": data["location"],
        "status": "inactive"  # Default status
    }
    return jsonify(devices[device_id]), 201

@app.route('/devices/<device_id>/activate', methods=['POST'])
def activate_device(device_id):
    """
    Endpoint to activate a specific ozone generator device.
    """
    device = devices.get(device_id)
    if not device:
        return jsonify(DEVICE_NOT_FOUND), 404

    device["status"] = "active"
    return jsonify(device), 200

@app.route('/devices/<device_id>/status', methods=['GET'])
def get_device_status(device_id):
    """
    Endpoint to get the status of a specific ozone generator device.
    """
    device = devices.get(device_id)
    if not device:
        return jsonify(DEVICE_NOT_FOUND), 404

    return jsonify({"id": device_id, "status": device["status"]}), 200

@app.route('/devices', methods=['GET'])
def list_devices():
    """
    Endpoint to list all registered ozone generator devices.
    """
    return jsonify(list(devices.values())), 200

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
