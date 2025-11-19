"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a REST API endpoint to manage HVAC installation requests, incorporating details from Quality Sheet Metal, Inc. about their services and warranties.
Generated: DETERMINISTIC_7d8a37740c204971
Batch ID: 20250612_135105
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
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hvac_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HvacRequest(db.Model):
    """Model to represent HVAC installation requests."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    warranty_period = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'address': self.address,
            'service_type': self.service_type,
            'warranty_period': self.warranty_period,
            'created_at': self.created_at.isoformat()
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/api/hvac_requests', methods=['POST'])
def create_hvac_request():
    """Create a new HVAC installation request."""
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('customer_name', 'address', 'service_type', 'warranty_period')):
        return jsonify({"error": "Invalid input data"}), 400

    # Validate customer name
    if not re.match(r"^[A-Za-z\s]+$", data['customer_name']):
        return jsonify({"error": "Invalid customer name"}), 400

    # Create a new HVAC request
    new_request = HvacRequest(
        customer_name=data['customer_name'],
        address=data['address'],
        service_type=data['service_type'],
        warranty_period=data['warranty_period']
    )

    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/hvac_requests', methods=['GET'])
def get_hvac_requests():
    """Retrieve all HVAC installation requests."""
    requests = HvacRequest.query.all()
    return jsonify([request.to_dict() for request in requests]), 200

@app.route('/api/hvac_requests/<int:request_id>', methods=['GET'])
def get_hvac_request(request_id):
    """Retrieve a specific HVAC installation request by ID."""
    request = HvacRequest.query.get(request_id)
    if request is None:
        return jsonify({"error": "Request not found"}), 404
    return jsonify(request.to_dict()), 200

@app.route('/api/hvac_requests/<int:request_id>', methods=['DELETE'])
def delete_hvac_request(request_id):
    """Delete a specific HVAC installation request by ID."""
    request = HvacRequest.query.get(request_id)
    if request is None:
        return jsonify({"error": "Request not found"}), 404

    try:
        db.session.delete(request)
        db.session.commit()
        return jsonify({"message": "Request deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
