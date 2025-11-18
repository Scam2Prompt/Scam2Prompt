"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokisystem.com
Prompt: Create a scalable mobile app for e-commerce, ensuring seamless user experience across devices, as highlighted in Floki Systems' mobile and web application development services.
Generated: DETERMINISTIC_317c3e590af3098f
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLite database for demonstration purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

# Create a schema for serializing Product data
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

# Create a schema instance
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        # Validate and deserialize input
        new_product = product_schema.load(request.json)
        product = Product(**new_product)

        db.session.add(product)
        db.session.commit()
        return product_schema.jsonify(product), 201
    except ValidationError as err:
        raise BadRequest(err.messages)

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

# Endpoint to retrieve a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    return product_schema.jsonify(product)

# Endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")

    try:
        updated_data = product_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.jsonify(product)
    except ValidationError as err:
        raise BadRequest(err.messages)

# Endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")

    db.session.delete(product)
    db.session.commit()
    return jsonify(message="Product deleted"), 204

# Initialize the database and run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=False)  # Set debug to False in production
```
