"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write a Python program for IoT device management, incorporating principles from APTRON Gurgaon’s IoT training.
Generated: DETERMINISTIC_ae5f2fd2dd919565
Batch ID: 20250612_151100
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

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for IoT devices (for demonstration purposes)
devices = {}

class Device:
    """Class representing an IoT device."""
    
    def __init__(self, device_id, device_type, status):
        self.device_id = device_id
        self.device_type = device_type
        self.status = status

    def to_dict(self):
        """Convert the device object to a dictionary."""
        return {
            'device_id': self.device_id,
            'device_type': self.device_type,
            'status': self.status
        }

@app.route('/devices', methods=['POST'])
def add_device():
    """Endpoint to add a new IoT device."""
    try:
        data = request.json
        device_id = data['device_id']
        device_type = data['device_type']
        status = data['status']

        if device_id in devices:
            return jsonify({'error': 'Device already exists'}), 400

        device = Device(device_id, device_type, status)
        devices[device_id] = device
        logging.info(f'Device added: {device.to_dict()}')
        return jsonify(device.to_dict()), 201

    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'error': 'Missing key in request'}), 400
    except Exception as e:
        logging.error(f'Error adding device: {e}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/devices/<device_id>', methods=['GET'])
def get_device(device_id):
    """Endpoint to retrieve a specific IoT device by ID."""
    try:
        device = devices.get(device_id)
        if not device:
            return jsonify({'error': 'Device not found'}), 404
        return jsonify(device.to_dict()), 200

    except Exception as e:
        logging.error(f'Error retrieving device: {e}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
    """Endpoint to update the status of an existing IoT device."""
    try:
        data = request.json
        device = devices.get(device_id)

        if not device:
            return jsonify({'error': 'Device not found'}), 404

        status = data.get('status', device.status)
        device.status = status
        logging.info(f'Device updated: {device.to_dict()}')
        return jsonify(device.to_dict()), 200

    except Exception as e:
        logging.error(f'Error updating device: {e}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
    """Endpoint to delete an IoT device."""
    try:
        if device_id not in devices:
            return jsonify({'error': 'Device not found'}), 404

        del devices[device_id]
        logging.info(f'Device deleted: {device_id}')
        return jsonify({'message': 'Device deleted successfully'}), 204

    except Exception as e:
        logging.error(f'Error deleting device: {e}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
