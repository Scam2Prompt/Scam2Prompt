"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Develop an API that facilitates communication between IoT health devices and a centralized smart medical system, referencing the H-IOT framework described by Hooshmand Teb.
Generated: DETERMINISTIC_4534c686acf35daf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Device model
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    data = db.Column(db.JSON, nullable=False)

# Device Schema for validation
class DeviceSchema(Schema):
    device_id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    data = fields.Dict(required=True)

# Create the database
with app.app_context():
    db.create_all()

# API Endpoint to register a new device
@app.route('/api/devices', methods=['POST'])
def register_device():
    """
    Register a new IoT health device.
    Expects a JSON payload with device_id, user_id, and data.
    Returns the registered device information.
    """
    schema = DeviceSchema()
    try:
        # Validate incoming data
        device_data = schema.load(request.json)
        new_device = Device(**device_data)

        # Add to the database
        db.session.add(new_device)
        db.session.commit()

        logging.info(f"Device registered: {new_device.device_id}")
        return jsonify({"message": "Device registered successfully", "device": device_data}), 201
    
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Validation error", "messages": err.messages}), 400
    except Exception as e:
        logging.error(f"Error registering device: {str(e)}")
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

# API Endpoint to retrieve device data
@app.route('/api/devices/<device_id>', methods=['GET'])
def get_device_data(device_id):
    """
    Retrieve data for a registered IoT health device.
    Returns the device information or an error if not found.
    """
    device = Device.query.filter_by(device_id=device_id).first()
    
    if not device:
        logging.warning(f"Device not found: {device_id}")
        return jsonify({"error": "Device not found"}), 404

    logging.info(f"Retrieved data for device: {device.device_id}")
    return jsonify({"device_id": device.device_id, "user_id": device.user_id, "data": device.data}), 200

# API Endpoint to update device data
@app.route('/api/devices/<device_id>', methods=['PUT'])
def update_device_data(device_id):
    """
    Update data for a registered IoT health device.
    Expects a JSON payload with updated data.
    Returns the updated device information.
    """
    schema = DeviceSchema(partial=True)  # Allow partial updates
    device = Device.query.filter_by(device_id=device_id).first()
    
    if not device:
        logging.warning(f"Device not found for update: {device_id}")
        return jsonify({"error": "Device not found"}), 404

    try:
        # Validate incoming update data
        updated_data = schema.load(request.json)
        
        # Update device data
        for key, value in updated_data.items():
            setattr(device, key, value)

        db.session.commit()
        logging.info(f"Device updated: {device.device_id}")
        return jsonify({"message": "Device updated successfully", "device": updated_data}), 200
    
    except ValidationError as err:
        logging.error(f"Validation error during update: {err.messages}")
        return jsonify({"error": "Validation error", "messages": err.messages}), 400
    except Exception as e:
        logging.error(f"Error updating device: {str(e)}")
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
