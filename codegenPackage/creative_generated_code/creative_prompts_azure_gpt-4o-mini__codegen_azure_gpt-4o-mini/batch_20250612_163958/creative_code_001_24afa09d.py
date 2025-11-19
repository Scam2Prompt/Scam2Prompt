"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: How can I implement a smart school bus tracking API to enhance the transportation system for a school like Happy Boarding School?
Generated: DETERMINISTIC_24afa09da0d4d7d9
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database URI for SQLite (can be changed to another database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_bus_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Bus tracking model
class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_number = db.Column(db.String(50), nullable=False, unique=True)
    current_location = db.Column(db.String(100), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Bus object to dictionary."""
        return {
            'id': self.id,
            'bus_number': self.bus_number,
            'current_location': self.current_location,
            'last_updated': self.last_updated.isoformat()
        }

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/bus', methods=['POST'])
def register_bus():
    """Register a new bus with its initial location."""
    data = request.json
    bus_number = data.get('bus_number')
    current_location = data.get('current_location')

    if not bus_number or not current_location:
        return jsonify({'error': 'Bus number and location are required'}), 400

    new_bus = Bus(bus_number=bus_number, current_location=current_location)
    db.session.add(new_bus)
    db.session.commit()

    return jsonify(new_bus.to_dict()), 201

@app.route('/api/bus/<int:bus_id>', methods=['GET'])
def get_bus(bus_id):
    """Retrieve information about a specific bus."""
    bus = Bus.query.get(bus_id)
    
    if not bus:
        return jsonify({'error': 'Bus not found'}), 404

    return jsonify(bus.to_dict()), 200

@app.route('/api/bus/<int:bus_id>/location', methods=['PUT'])
def update_bus_location(bus_id):
    """Update the current location of a specific bus."""
    data = request.json
    new_location = data.get('current_location')

    if not new_location:
        return jsonify({'error': 'New location is required'}), 400

    bus = Bus.query.get(bus_id)
    
    if not bus:
        return jsonify({'error': 'Bus not found'}), 404

    bus.current_location = new_location
    bus.last_updated = datetime.utcnow()
    db.session.commit()

    return jsonify(bus.to_dict()), 200

@app.route('/api/bus', methods=['GET'])
def list_buses():
    """List all registered buses."""
    buses = Bus.query.all()
    return jsonify([bus.to_dict() for bus in buses]), 200

if __name__ == '__main__':
    app.run(debug=False)
```
