"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokisystem.com
Prompt: Create a prototype for a smart home automation system using IoT devices, referencing Floki Systems' approach to upgrading living spaces.
Generated: DETERMINISTIC_fce70841621e2430
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Simulated database for devices
devices = {}

# Device class to represent IoT devices
class Device:
    def __init__(self, name, device_type, status=False):
        self.name = name
        self.device_type = device_type
        self.status = status

    def toggle_status(self):
        """Toggle the device's status between on and off."""
        self.status = not self.status

    def to_dict(self):
        """Convert device information to dictionary format."""
        return {
            "name": self.name,
            "device_type": self.device_type,
            "status": self.status
        }

@app.route('/devices', methods=['POST'])
def add_device():
    """Add a new IoT device to the system."""
    try:
        data = request.json
        device_name = data['name']
        device_type = data['device_type']

        # Create a new device instance
        new_device = Device(device_name, device_type)
        devices[device_name] = new_device

        logging.info(f"Device '{device_name}' added.")
        return jsonify(new_device.to_dict()), 201
    except KeyError as e:
        logging.error(f"Missing key: {e}")
        return jsonify({"error": "Missing device name or type"}), 400
    except Exception as e:
        logging.error(f"Error adding device: {e}")
        return jsonify({"error": "An error occurred while adding the device"}), 500

@app.route('/devices/<device_name>', methods=['GET'])
def get_device(device_name):
    """Retrieve information about a specific device."""
    device = devices.get(device_name)
    if device:
        return jsonify(device.to_dict()), 200
    else:
        logging.warning(f"Device '{device_name}' not found.")
        return jsonify({"error": "Device not found"}), 404

@app.route('/devices/<device_name>/toggle', methods=['POST'])
def toggle_device(device_name):
    """Toggle the status of a specific device."""
    device = devices.get(device_name)
    if device:
        device.toggle_status()
        logging.info(f"Device '{device_name}' status toggled to {device.status}.")
        return jsonify(device.to_dict()), 200
    else:
        logging.warning(f"Device '{device_name}' not found for toggle.")
        return jsonify({"error": "Device not found"}), 404

@app.route('/devices', methods=['GET'])
def list_devices():
    """List all devices in the system."""
    return jsonify([device.to_dict() for device in devices.values()]), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Install Flask if not already present: `pip install Flask`
- Run the code in an environment that supports Python and Flask.
