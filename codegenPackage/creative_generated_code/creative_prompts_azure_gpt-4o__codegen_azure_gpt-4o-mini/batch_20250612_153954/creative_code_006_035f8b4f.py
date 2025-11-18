"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Suggest an API for tracking international shipments across Uniair Cargo’s global network of 67 countries.
Generated: DETERMINISTIC_035f8b4f22a4d3a4
Batch ID: 20250612_153954
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
from datetime import datetime
import requests

app = Flask(__name__)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Shipment model
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {
            'id': self.id,
            'tracking_number': self.tracking_number,
            'status': self.status,
            'origin': self.origin,
            'destination': self.destination,
            'updated_at': self.updated_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new shipment
@app.route('/api/shipments', methods=['POST'])
def add_shipment():
    data = request.get_json()
    try:
        new_shipment = Shipment(
            tracking_number=data['tracking_number'],
            status=data['status'],
            origin=data['origin'],
            destination=data['destination']
        )
        db.session.add(new_shipment)
        db.session.commit()
        return jsonify(new_shipment.as_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to track a shipment
@app.route('/api/shipments/<tracking_number>', methods=['GET'])
def track_shipment(tracking_number):
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    if shipment:
        return jsonify(shipment.as_dict()), 200
    return jsonify({"error": "Shipment not found"}), 404

# Endpoint to update shipment status
@app.route('/api/shipments/<tracking_number>', methods=['PUT'])
def update_shipment(tracking_number):
    data = request.get_json()
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    try:
        shipment.status = data.get('status', shipment.status)
        shipment.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify(shipment.as_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
