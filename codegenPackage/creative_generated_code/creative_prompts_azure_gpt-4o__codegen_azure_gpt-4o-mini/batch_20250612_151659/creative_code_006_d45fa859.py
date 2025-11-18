"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptoslive.com
Prompt: Develop a cloud-native POS system with Aptos ONE that supports mobile-first design and enterprise-grade capabilities.
Generated: DETERMINISTIC_d45fa859405e1fa1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pos_system.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Product(db.Model):
    """Model representing a product in the POS system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Transaction(db.Model):
    """Model representing a transaction in the POS system."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Schemas
class ProductSchema(Schema):
    """Schema for serializing and deserializing Product objects."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class TransactionSchema(Schema):
    """Schema for serializing and deserializing Transaction objects."""
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize DB
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Routes
@app.route('/products', methods=['POST'])
def add_product():
    """Endpoint to add a new product."""
    json_data = request.get_json()
    product_schema = ProductSchema()

    try:
        # Validate and deserialize input
        product_data = product_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new Product instance
    new_product = Product(name=product_data['name'], price=product_data['price'])
    
    # Add to the database
    db.session.add(new_product)
    db.session.commit()

    return product_schema.dump(new_product), 201

@app.route('/products', methods=['GET'])
def get_products():
    """Endpoint to retrieve all products."""
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return product_schema.dump(products)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    """Endpoint to add a new transaction."""
    json_data = request.get_json()
    transaction_schema = TransactionSchema()

    try:
        # Validate and deserialize input
        transaction_data = transaction_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new Transaction instance
    new_transaction = Transaction(product_id=transaction_data['product_id'], quantity=transaction_data['quantity'])
    
    # Add to the database
    db.session.add(new_transaction)
    db.session.commit()

    return transaction_schema.dump(new_transaction), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
    """Endpoint to retrieve all transactions."""
    transactions = Transaction.query.all()
    transaction_schema = TransactionSchema(many=True)
    return transaction_schema.dump(transactions)

# Main entry point
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False').lower() in ['true', '1'])
```
