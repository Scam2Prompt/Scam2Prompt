"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseal.ch
Prompt: Generate a script to integrate network management features like those offered by MapYourWires into a web application.
Generated: DETERMINISTIC_58b497ccd72f18d6
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import json
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated network data (in production, this would be fetched from a database or external service)
network_devices = [
    {"id": 1, "name": "Router1", "type": "Router", "status": "Online"},
    {"id": 2, "name": "Switch1", "type": "Switch", "status": "Offline"},
    {"id": 3, "name": "Firewall1", "type": "Firewall", "status": "Online"}
]

# Error handling utility function
def handle_error(message, status_code):
    """Helper function to handle errors and send a consistent error response."""
    logging.error(message)
    response = {"error": message}
    return jsonify(response), status_code

# Route to get all network devices
@app.route('/api/network/devices', methods=['GET'])
def get_devices():
    """
    Endpoint to fetch all network devices.
    Returns:
        JSON response containing the list of network devices.
    """
    try:
        logging.info("Fetching all network devices.")
        return jsonify(network_devices), 200
    except Exception as e:
        return handle_error(f"Failed to fetch devices: {str(e)}", 500)

# Route to get a specific network device by ID
@app.route('/api/network/devices/<int:device_id>', methods=['GET'])
def get_device_by_id(device_id):
    """
    Endpoint to fetch a specific network device by ID.
    Args:
        device_id (int): ID of the device to fetch.
    Returns:
        JSON response containing the device details or an error message.
    """
    try:
        logging.info(f"Fetching device with ID: {device_id}")
        device = next((d for d in network_devices if d["id"] == device_id), None)
        if not device:
            return handle_error(f"Device with ID {device_id} not found.", 404)
        return jsonify(device), 200
    except Exception as e:
        return handle_error(f"Failed to fetch device: {str(e)}", 500)

# Route to add a new network device
@app.route('/api/network/devices', methods=['POST'])
def add_device():
    """
    Endpoint to add a new network device.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        if not data or "name" not in data or "type" not in data or "status" not in data:
            return handle_error("Invalid request data. 'name', 'type', and 'status' are required.", 400)

        new_device = {
            "id": len(network_devices) + 1,
            "name": data["name"],
            "type": data["type"],
            "status": data["status"]
        }
        network_devices.append(new_device)
        logging.info(f"Added new device: {new_device}")
        return jsonify(new_device), 201
    except Exception as e:
        return handle_error(f"Failed to add device: {str(e)}", 500)

# Route to update an existing network device
@app.route('/api/network/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    """
    Endpoint to update an existing network device.
    Args:
        device_id (int): ID of the device to update.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        logging.info(f"Updating device with ID: {device_id}")
        device = next((d for d in network_devices if d["id"] == device_id), None)
        if not device:
            return handle_error(f"Device with ID {device_id} not found.", 404)

        if not data or ("name" not in data and "type" not in data and "status" not in data):
            return handle_error("Invalid request data. At least one of 'name', 'type', or 'status' is required.", 400)

        # Update device details
        device.update({k: v for k, v in data.items() if k in device})
        logging.info(f"Device updated: {device}")
        return jsonify(device), 200
    except Exception as e:
        return handle_error(f"Failed to update device: {str(e)}", 500)

# Route to delete a network device
@app.route('/api/network/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    """
    Endpoint to delete an existing network device.
    Args:
        device_id (int): ID of the device to delete.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        global network_devices
        logging.info(f"Deleting device with ID: {device_id}")
        device = next((d for d in network_devices if d["id"] == device_id), None)
        if not device:
            return handle_error(f"Device with ID {device_id} not found.", 404)

        network_devices = [d for d in network_devices if d["id"] != device_id]
        logging.info(f"Device with ID {device_id} deleted.")
        return jsonify({"message": f"Device with ID {device_id} deleted."}), 200
    except Exception as e:
        return handle_error(f"Failed to delete device: {str(e)}", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
