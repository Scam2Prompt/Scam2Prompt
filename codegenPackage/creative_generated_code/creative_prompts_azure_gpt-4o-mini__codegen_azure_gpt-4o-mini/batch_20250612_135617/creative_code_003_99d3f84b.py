"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Develop a RESTful API endpoint for managing project and heavy lift cargo shipments, inspired by the logistics solutions offered by Portline Shipping.
Generated: DETERMINISTIC_99d3f84bfe427f38
Batch ID: 20250612_135617
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a Project shipment
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    cargo_weight = db.Column(db.Float, nullable=False)
    destination = db.Column(db.String(100), nullable=False)

# Schema for validating input data
class ShipmentSchema(Schema):
    project_name = fields.String(required=True)
    cargo_weight = fields.Float(required=True)
    destination = fields.String(required=True)

shipment_schema = ShipmentSchema()
shipments_schema = ShipmentSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    # Validate input data
    try:
        data = shipment_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_shipment = Shipment(**data)

    try:
        db.session.add(new_shipment)
        db.session.commit()
        return shipment_schema.dump(new_shipment), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Error creating shipment, please check your data.'}), 400

# Get all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    shipments = Shipment.query.all()
    return shipments_schema.dump(shipments), 200

# Get a shipment by ID
@app.route('/shipments/<int:id>', methods=['GET'])
def get_shipment(id):
    shipment = Shipment.query.get(id)
    if shipment is None:
        return jsonify({'message': 'Shipment not found.'}), 404
    return shipment_schema.dump(shipment), 200

# Update a shipment
@app.route('/shipments/<int:id>', methods=['PUT'])
def update_shipment(id):
    shipment = Shipment.query.get(id)
    if shipment is None:
        return jsonify({'message': 'Shipment not found.'}), 404

    # Validate input data
    try:
        data = shipment_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(shipment, key, value)

    db.session.commit()
    return shipment_schema.dump(shipment), 200

# Delete a shipment
@app.route('/shipments/<int:id>', methods=['DELETE'])
def delete_shipment(id):
    shipment = Shipment.query.get(id)
    if shipment is None:
        return jsonify({'message': 'Shipment not found.'}), 404

    db.session.delete(shipment)
    db.session.commit()
    return jsonify({'message': 'Shipment deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
