"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Create a logistics API integration for importing and exporting goods to and from Africa, America, Asia, and Europe, inspired by Olgadorks Shipping Company Limited's global reach.
Generated: DETERMINISTIC_193966c19b8b5640
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity, can be changed to any other DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Shipment model
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    goods_description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)

# Create a schema for input validation
class ShipmentSchema(Schema):
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)
    goods_description = fields.Str(required=True)
    weight = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        # Validate and deserialize input
        shipment_schema = ShipmentSchema()
        shipment_data = shipment_schema.load(request.json)

        # Create a new shipment record
        new_shipment = Shipment(**shipment_data)
        db.session.add(new_shipment)
        db.session.commit()

        logging.info(f"Shipment created: {new_shipment.id}")
        return jsonify({"id": new_shipment.id}), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating shipment: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Endpoint to get all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    try:
        shipments = Shipment.query.all()
        shipment_schema = ShipmentSchema(many=True)
        return jsonify(shipment_schema.dump(shipments)), 200
    except Exception as e:
        logging.error(f"Error fetching shipments: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Endpoint to get a shipment by ID
@app.route('/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    try:
        shipment = Shipment.query.get_or_404(shipment_id)
        shipment_schema = ShipmentSchema()
        return jsonify(shipment_schema.dump(shipment)), 200
    except Exception as e:
        logging.error(f"Error fetching shipment {shipment_id}: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
