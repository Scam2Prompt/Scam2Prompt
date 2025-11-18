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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Setup the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Device model
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Device schema
class DeviceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        load_instance = True

# Initialize the schema
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

# Create a device
@app.route('/devices', methods=['POST'])
def add_device():
    """Add a new IoT device."""
    try:
        name = request.json['name']
        device_type = request.json['type']
        status = request.json['status']
        
        # Create a new device instance
        new_device = Device(name=name, type=device_type, status=status)
        
        # Add to session and commit
        db.session.add(new_device)
        db.session.commit()
        
        return device_schema.jsonify(new_device), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all devices
@app.route('/devices', methods=['GET'])
def get_devices():
    """Get a list of all IoT devices."""
    devices = Device.query.all()
    return devices_schema.jsonify(devices)

# Get a device by ID
@app.route('/devices/<int:id>', methods=['GET'])
def get_device(id):
    """Get a specific IoT device by ID."""
    device = Device.query.get(id)
    if not device:
        raise NotFound(f'Device with ID {id} not found.')
    return device_schema.jsonify(device)

# Update a device
@app.route('/devices/<int:id>', methods=['PUT'])
def update_device(id):
    """Update an existing IoT device."""
    device = Device.query.get(id)
    if not device:
        raise NotFound(f'Device with ID {id} not found.')

    try:
        if 'name' in request.json:
            device.name = request.json['name']
        if 'type' in request.json:
            device.type = request.json['type']
        if 'status' in request.json:
            device.status = request.json['status']
        
        db.session.commit()
        return device_schema.jsonify(device)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Delete a device
@app.route('/devices/<int:id>', methods=['DELETE'])
def delete_device(id):
    """Delete an IoT device by ID."""
    device = Device.query.get(id)
    if not device:
        raise NotFound(f'Device with ID {id} not found.')
    
    db.session.delete(device)
    db.session.commit()
    return jsonify({"message": "Device deleted successfully"}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": "Bad request, please check your input."}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
