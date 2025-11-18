"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write a Python program for IoT device management, incorporating principles from APTRON Gurgaon’s IoT training.
Generated: DETERMINISTIC_ae5f2fd2dd919565
Batch ID: 20250612_151100
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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Device model
class Device(db.Model):
    __tablename__ = 'devices'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Device(name={self.name}, status={self.status})>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/devices', methods=['POST'])
def add_device():
    """Endpoint to add a new IoT device."""
    data = request.get_json()
    if not data or 'name' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_device = Device(name=data['name'], status=data['status'])
    try:
        db.session.add(new_device)
        db.session.commit()
        return jsonify({'message': 'Device added successfully', 'device': new_device.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Device with this name already exists'}), 409

@app.route('/devices', methods=['GET'])
def get_devices():
    """Endpoint to retrieve all IoT devices."""
    devices = Device.query.all()
    return jsonify([{'id': device.id, 'name': device.name, 'status': device.status} for device in devices]), 200

@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    """Endpoint to update the status of a device."""
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    device = Device.query.get(device_id)
    if not device:
        return jsonify({'error': 'Device not found'}), 404
    
    device.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Device status updated', 'device': {'id': device.id, 'name': device.name, 'status': device.status}}), 200

@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    """Endpoint to delete a device."""
    device = Device.query.get(device_id)
    if not device:
        return jsonify({'error': 'Device not found'}), 404
    
    db.session.delete(device)
    db.session.commit()
    return jsonify({'message': 'Device deleted successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
