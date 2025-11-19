"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Develop a RESTful API endpoint for managing project and heavy lift cargo shipments, inspired by the logistics solutions offered by Portline Shipping.
Generated: DETERMINISTIC_99d3f84bfe427f38
Batch ID: 20250612_135617
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Shipment
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    cargo_type = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    destination = db.Column(db.String(100), nullable=False)

# Schema for validating input data
class ShipmentSchema(Schema):
    project_name = fields.Str(required=True)
    cargo_type = fields.Str(required=True)
    weight = fields.Float(required=True)
    destination = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        # Validate and deserialize input data
        shipment_data = ShipmentSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new shipment record
    new_shipment = Shipment(**shipment_data)
    db.session.add(new_shipment)
    db.session.commit()
    
    return jsonify({"id": new_shipment.id}), 201

# API endpoint to retrieve all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    shipments = Shipment.query.all()
    shipment_schema = ShipmentSchema(many=True)
    return jsonify(shipment_schema.dump(shipments)), 200

# API endpoint to retrieve a shipment by ID
@app.route('/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    shipment_schema = ShipmentSchema()
    return jsonify(shipment_schema.dump(shipment)), 200

# API endpoint to update a shipment
@app.route('/shipments/<int:shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    
    try:
        # Validate and deserialize input data
        shipment_data = ShipmentSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update shipment record
    for key, value in shipment_data.items():
        setattr(shipment, key, value)
    
    db.session.commit()
    return jsonify({"message": "Shipment updated successfully"}), 200

# API endpoint to delete a shipment
@app.route('/shipments/<int:shipment_id>', methods=['DELETE'])
def delete_shipment(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    db.session.delete(shipment)
    db.session.commit()
    return jsonify({"message": "Shipment deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
