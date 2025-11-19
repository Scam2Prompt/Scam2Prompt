"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Write a Python API for an automotive parts marketplace that allows customers to get quotes for vehicle parts and accessories from multiple suppliers.
Generated: DETERMINISTIC_218c6d43397c067e
Batch ID: 20250622_212702
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

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for suppliers
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parts = db.relationship('Part', backref='supplier', lazy=True)

# Database model for parts
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

# Schema for input validation
class PartSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get quotes for a specific part
@app.route('/get_quotes', methods=['POST'])
def get_quotes():
    try:
        # Validate input data
        part_schema = PartSchema()
        data = part_schema.load(request.json)

        # Query suppliers for the requested part
        quotes = Part.query.filter_by(name=data['name']).all()

        # Prepare response
        if not quotes:
            return jsonify({"message": "No quotes found for the requested part."}), 404

        response = [{"supplier": quote.supplier.name, "price": quote.price} for quote in quotes]
        return jsonify(response), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"message": "An error occurred while processing your request."}), 500

# Route to add a new supplier
@app.route('/add_supplier', methods=['POST'])
def add_supplier():
    try:
        name = request.json.get('name')
        if not name:
            return jsonify({"message": "Supplier name is required."}), 400

        new_supplier = Supplier(name=name)
        db.session.add(new_supplier)
        db.session.commit()

        return jsonify({"message": "Supplier added successfully."}), 201

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"message": "An error occurred while adding the supplier."}), 500

# Route to add a new part
@app.route('/add_part', methods=['POST'])
def add_part():
    try:
        name = request.json.get('name')
        price = request.json.get('price')
        supplier_id = request.json.get('supplier_id')

        if not name or price is None or not supplier_id:
            return jsonify({"message": "Part name, price, and supplier ID are required."}), 400

        new_part = Part(name=name, price=price, supplier_id=supplier_id)
        db.session.add(new_part)
        db.session.commit()

        return jsonify({"message": "Part added successfully."}), 201

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"message": "An error occurred while adding the part."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
