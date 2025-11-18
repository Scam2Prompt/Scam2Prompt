"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Create a REST API for managing IoT devices, following the IoT development services provided by Digital Dhara.
Generated: DETERMINISTIC_94d812df5088bf0e
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database to store IoT devices (for demonstration purposes)
iot_devices = {}

# Error handling function
def handle_error(message, status_code):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# Endpoint to retrieve all IoT devices
@app.route('/devices', methods=['GET'])
def get_all_devices():
    """
    Get a list of all IoT devices.
    Returns:
        JSON response with all devices.
    """
    return jsonify({"devices": list(iot_devices.values())})

# Endpoint to retrieve a specific IoT device by ID
@app.route('/devices/<device_id>', methods=['GET'])
def get_device(device_id):
    """
    Get details of a specific IoT device by ID.
    Args:
        device_id (str): The ID of the device to retrieve.
    Returns:
        JSON response with the device details or an error message.
    """
    device = iot_devices.get(device_id)
    if not device:
        return handle_error(f"Device with ID {device_id} not found.", 404)
    return jsonify(device)

# Endpoint to add a new IoT device
@app.route('/devices', methods=['POST'])
def add_device():
    """
    Add a new IoT device.
    Payload:
        device_id (str): Unique ID for the device.
        name (str): Name of the device.
        type (str): Type of the device.
    Returns:
        JSON response with the created device or an error message.
    """
    data = request.json
    device_id = data.get("device_id")
    name = data.get("name")
    device_type = data.get("type")
    
    if not device_id or not name or not device_type:
        return handle_error("Missing required fields: device_id, name, type.", 400)
    
    if device_id in iot_devices:
        return handle_error(f"Device with ID {device_id} already exists.", 409)
    
    new_device = {
        "device_id": device_id,
        "name": name,
        "type": device_type
    }
    iot_devices[device_id] = new_device
    return jsonify(new_device), 201

# Endpoint to update an existing IoT device
@app.route('/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
    """
    Update details of an existing IoT device.
    Args:
        device_id (str): The ID of the device to update.
    Payload:
        name (str): Updated name of the device.
        type (str): Updated type of the device.
    Returns:
        JSON response with the updated device or an error message.
    """
    data = request.json
    device = iot_devices.get(device_id)
    
    if not device:
        return handle_error(f"Device with ID {device_id} not found.", 404)
    
    name = data.get("name")
    device_type = data.get("type")
    
    if not name or not device_type:
        return handle_error("Missing required fields: name, type.", 400)
    
    device.update({
        "name": name,
        "type": device_type
    })
    return jsonify(device)

# Endpoint to delete an IoT device
@app.route('/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
    """
    Delete an IoT device by ID.
    Args:
        device_id (str): The ID of the device to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    device = iot_devices.pop(device_id, None)
    if not device:
        return handle_error(f"Device with ID {device_id} not found.", 404)
    return jsonify({"message": f"Device with ID {device_id} has been deleted."})

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a fully functional REST API for managing IoT devices, with error handling and adherence to best practices. You can run it using Python, provided Flask is installed.
