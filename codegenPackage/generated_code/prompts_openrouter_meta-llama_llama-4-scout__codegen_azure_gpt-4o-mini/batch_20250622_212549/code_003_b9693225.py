"""
Generated Code Metadata:
========================
Original URL: https://www.lattechocolate.com.ar
Prompt: Design a simple API for managing products, orders, and shipping information for an e-commerce platform like Latte Chocolate, including endpoints for product categories and shipping calculations.
Generated: DETERMINISTIC_b969322538c70514
Batch ID: 20250622_212549
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ShippingInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    shipping_cost = db.Column(db.Float, nullable=False)

# Schemas for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class ShippingInfoSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    address = fields.Str(required=True)
    shipping_cost = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoints

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_schema = ProductSchema()
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Get a specific product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product)), 200

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_schema = OrderSchema()
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Calculate shipping cost
@app.route('/shipping/calculate', methods=['POST'])
def calculate_shipping():
    data = request.json
    if 'weight' not in data or 'distance' not in data:
        return jsonify({"error": "Weight and distance are required."}), 400
    
    weight = data['weight']
    distance = data['distance']
    
    # Simple shipping cost calculation
    shipping_cost = weight * 0.5 + distance * 0.2
    return jsonify({"shipping_cost": shipping_cost}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
