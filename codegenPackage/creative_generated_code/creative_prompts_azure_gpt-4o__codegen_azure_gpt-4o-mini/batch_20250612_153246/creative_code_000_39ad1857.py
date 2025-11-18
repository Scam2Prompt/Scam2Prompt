"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write Python code to create an e-commerce API for listing cannabis products such as CBG, CBD, and CB9 flowers, using product details like weight, dimensions, and stock availability from Marine Kiosk's catalog.
Generated: DETERMINISTIC_39ad185757495b95
Batch ID: 20250612_153246
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity, can be changed to any production-ready database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cannabis_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., CBG, CBD, CB9
    weight = db.Column(db.Float, nullable=False)      # in grams
    dimensions = db.Column(db.String(50), nullable=True)  # e.g., "10x5x3 cm"
    stock = db.Column(db.Integer, nullable=False)     # available stock

# Create a schema for serialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    weight = fields.Float(required=True)
    dimensions = fields.Str(required=False)
    stock = fields.Int(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
