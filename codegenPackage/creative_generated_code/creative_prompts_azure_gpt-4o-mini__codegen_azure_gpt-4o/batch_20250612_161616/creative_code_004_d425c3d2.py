"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://widophlogistics.com.au
Prompt: Illustrate how to implement a logistics tracking system using an API, reflecting the streamlined shipment process emphasized by Widoph Logistics.
Generated: DETERMINISTIC_d425c3d24c75c220
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Logistics Tracking System using a RESTful API for Widoph Logistics.
This implementation covers streamlined shipment tracking functionality.

Requirements:
- Python 3.8+
- Flask (for API implementation)
- SQLite (or any DB for simplicity)

Install dependencies before running:
    pip install flask sqlalchemy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///widoph_logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Shipment model
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(50), unique=True, nullable=False)
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "tracking_number": self.tracking_number,
            "sender": self.sender,
            "recipient": self.recipient,
            "origin": self.origin,
            "destination": self.destination,
            "status": self.status,
        }

# Create database tables (run once)
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        # Extract shipment data from request
        data = request.json
        tracking_number = data.get('tracking_number')
        sender = data.get('sender')
        recipient = data.get('recipient')
        origin = data.get('origin')
        destination = data.get('destination')

        # Validate required fields
        if not all([tracking_number, sender, recipient, origin, destination]):
            return jsonify({"error": "Missing required fields"}), 400

        # Create new shipment instance
        shipment = Shipment(
            tracking_number=tracking_number,
            sender=sender,
            recipient=recipient,
            origin=origin,
            destination=destination,
            status="Pending"
        )
        db.session.add(shipment)
        db.session.commit()
        return jsonify({"message": "Shipment created successfully", "shipment": shipment.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update shipment status
@app.route('/shipments/<tracking_number>/status', methods=['PUT'])
def update_status(tracking_number):
    try:
        # Find shipment by tracking number
        shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404

        # Update status
        data = request.json
        new_status = data.get('status')
        if not new_status:
            return jsonify({"error": "Missing 'status' field"}), 400

        shipment.status = new_status
        db.session.commit()
        return jsonify({"message": "Shipment status updated", "shipment": shipment.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve details of a shipment
@app.route('/shipments/<tracking_number>', methods=['GET'])
def get_shipment(tracking_number):
    try:
        # Find shipment by tracking number
        shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404

        return jsonify({"shipment": shipment.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to list all shipments
@app.route('/shipments', methods=['GET'])
def list_shipments():
    try:
        # Retrieve all shipments
        shipments = Shipment.query.all()
        return jsonify({"shipments": [shipment.to_dict() for shipment in shipments]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
