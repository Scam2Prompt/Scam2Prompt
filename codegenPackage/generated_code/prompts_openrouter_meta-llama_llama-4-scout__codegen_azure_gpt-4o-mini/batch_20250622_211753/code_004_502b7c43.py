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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ozone_generators.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the OzoneGenerator model
class OzoneGenerator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='inactive')  # active or inactive
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the OzoneGenerator object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/devices', methods=['POST'])
def register_device():
    """Register a new ozone generator device."""
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Device name is required.")

    new_device = OzoneGenerator(name=data['name'])
    db.session.add(new_device)
    db.session.commit()
    return jsonify(new_device.to_dict()), 201

@app.route('/devices/<int:device_id>/activate', methods=['POST'])
def activate_device(device_id):
    """Activate an ozone generator device."""
    device = OzoneGenerator.query.get_or_404(device_id)
    device.status = 'active'
    db.session.commit()
    return jsonify(device.to_dict()), 200

@app.route('/devices/<int:device_id>/deactivate', methods=['POST'])
def deactivate_device(device_id):
    """Deactivate an ozone generator device."""
    device = OzoneGenerator.query.get_or_404(device_id)
    device.status = 'inactive'
    db.session.commit()
    return jsonify(device.to_dict()), 200

@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device_status(device_id):
    """Get the status of an ozone generator device."""
    device = OzoneGenerator.query.get_or_404(device_id)
    return jsonify(device.to_dict()), 200

@app.route('/devices', methods=['GET'])
def list_devices():
    """List all registered ozone generator devices."""
    devices = OzoneGenerator.query.all()
    return jsonify([device.to_dict() for device in devices]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
