"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Suggest an API for tracking shipments of CM-Canada's construction materials across North America, ensuring rapid and efficient logistics.
Generated: DETERMINISTIC_882df6aa1e124a01
Batch ID: 20250612_155048
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipments.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for shipments
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(255), nullable=False)

# Schema for validating shipment data
class ShipmentSchema(Schema):
    tracking_number = fields.Str(required=True)
    status = fields.Str(required=True)
    destination = fields.Str(required=True)

# Initialize the schema
shipment_schema = ShipmentSchema()
shipments_schema = ShipmentSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new shipment
@app.route('/shipments', methods=['POST'])
def add_shipment():
    json_data = request.get_json()
    try:
        data = shipment_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_shipment = Shipment(**data)
    db.session.add(new_shipment)
    db.session.commit()
    return shipment_schema.dump(new_shipment), 201

# Endpoint to get shipment by tracking number
@app.route('/shipments/<string:tracking_number>', methods=['GET'])
def get_shipment(tracking_number):
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    if shipment is None:
        return jsonify({"message": "Shipment not found"}), 404
    return shipment_schema.dump(shipment)

# Endpoint to update shipment status
@app.route('/shipments/<string:tracking_number>', methods=['PUT'])
def update_shipment(tracking_number):
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    if shipment is None:
        return jsonify({"message": "Shipment not found"}), 404

    json_data = request.get_json()
    try:
        data = shipment_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    shipment.status = data['status']
    shipment.destination = data['destination']
    db.session.commit()
    return shipment_schema.dump(shipment)

# Endpoint to delete a shipment
@app.route('/shipments/<string:tracking_number>', methods=['DELETE'])
def delete_shipment(tracking_number):
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    if shipment is None:
        return jsonify({"message": "Shipment not found"}), 404

    db.session.delete(shipment)
    db.session.commit()
    return jsonify({"message": "Shipment deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
