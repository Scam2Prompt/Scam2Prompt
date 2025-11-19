"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: Create a REST API for managing IoT devices, following the IoT development services provided by Digital Dhara.
Generated: DETERMINISTIC_94d812df5088bf0e
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Device model
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Device {self.name}>"

# Device schema for serialization
class DeviceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize the schema
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new device
@app.route('/devices', methods=['POST'])
def add_device():
    """Add a new IoT device."""
    try:
        # Validate and deserialize input
        device_data = device_schema.load(request.json)
        new_device = Device(**device_data)
        db.session.add(new_device)
        db.session.commit()
        return device_schema.dump(new_device), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Get all devices
@app.route('/devices', methods=['GET'])
def get_devices():
    """Retrieve all IoT devices."""
    devices = Device.query.all()
    return devices_schema.dump(devices), 200

# Get a specific device by ID
@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    """Retrieve a specific IoT device by ID."""
    device = Device.query.get_or_404(device_id)
    return device_schema.dump(device), 200

# Update a device
@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    """Update an existing IoT device."""
    device = Device.query.get_or_404(device_id)
    try:
        # Validate and deserialize input
        device_data = device_schema.load(request.json)
        for key, value in device_data.items():
            setattr(device, key, value)
        db.session.commit()
        return device_schema.dump(device), 200
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Delete a device
@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    """Delete an IoT device."""
    device = Device.query.get_or_404(device_id)
    db.session.delete(device)
    db.session.commit()
    return jsonify({"message": "Device deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
