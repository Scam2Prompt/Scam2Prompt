"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Design a RESTful API for managing orders and inventory of off-road vehicle accessories, including endpoints for retrieving product information and processing payments."
Generated: DETERMINISTIC_aa940104e97fd8f0
Batch ID: 20250622_210316
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Product Schema for serialization
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Order Schema for serialization
class OrderSchema(Schema):
    id = fields.Int()
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.dump(products), 200

# Endpoint to retrieve a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return product_schema.dump(product), 200

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_product = Product(**product_data)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.dump(new_product), 201

# Endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in product_data.items():
        setattr(product, key, value)
    db.session.commit()
    return product_schema.dump(product), 200

# Endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 204

# Endpoint to create an order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product = Product.query.get(order_data['product_id'])
    if product is None or product.stock < order_data['quantity']:
        abort(400, description="Insufficient stock or product not found")

    new_order = Order(**order_data)
    product.stock -= order_data['quantity']  # Update stock
    db.session.add(new_order)
    db.session.commit()
    return order_schema.dump(new_order), 201

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.dump(orders), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
