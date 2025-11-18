"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://royalcooler.com
Prompt: Suggest an API design for integrating "رویال کولر" product data into a third-party e-commerce platform, focusing on air conditioner listings.
Generated: DETERMINISTIC_e5b368058df93466
Batch ID: 20250612_153225
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Schema for validating and serializing product data
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# API endpoint to create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        # Validate incoming JSON data
        product_data = product_schema.load(request.json)
        
        # Create a new product instance
        new_product = Product(**product_data)
        
        # Add and commit the product to the database
        db.session.add(new_product)
        db.session.commit()
        
        return product_schema.jsonify(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating product: {e}")
        return jsonify({"error": "An error occurred while creating the product."}), 500

# API endpoint to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Exception as e:
        logging.error(f"Error fetching products: {e}")
        return jsonify({"error": "An error occurred while fetching products."}), 500

# API endpoint to retrieve a product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return product_schema.jsonify(product), 200
    except Exception as e:
        logging.error(f"Error fetching product with id {product_id}: {e}")
        return jsonify({"error": "An error occurred while fetching the product."}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug=False for production
```
