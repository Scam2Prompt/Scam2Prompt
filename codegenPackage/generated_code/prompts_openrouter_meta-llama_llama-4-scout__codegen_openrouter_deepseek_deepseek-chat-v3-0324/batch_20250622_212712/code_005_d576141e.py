"""
Generated Code Metadata:
========================
Original URL: https://mustmenfashion.gr
Prompt: Design a RESTful API to manage orders and inventory for Must Men Fashion, including endpoints for creating, reading, updating, and deleting orders and products.
Generated: DETERMINISTIC_d576141e8655b743
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'must_men_fashion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Product {self.name}>'

# Order Model
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20))
    shipping_address = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    order_items = db.relationship('OrderItem', backref='order', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Order {self.id}>'

# OrderItem Model (Join table between Order and Product)
class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    product = db.relationship('Product')

    def __repr__(self):
        return f'<OrderItem {self.id}>'

# Product Schema for serialization/deserialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)
    category = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Order Schema
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    customer_email = fields.Str(required=True)
    customer_phone = fields.Str()
    shipping_address = fields.Str(required=True)
    total_amount = fields.Float(required=True)
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    order_items = fields.Nested('OrderItemSchema', many=True)

# OrderItem Schema
class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    product = fields.Nested('ProductSchema', only=('id', 'name', 'price'))

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = {
        "error": e.name,
        "message": e.description
    }
    return jsonify(response), e.code

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": "ValidationError", "messages": e.messages}), 400

# Product Endpoints
@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify(products_schema.dump(products))

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a single product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product_schema.dump(product))

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify(product_schema.dump(product)), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product"""
    product = Product.query.get_or_404(product_id)
    try:
        data = product_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(product, key, value)
    
    db.session.commit()
    return jsonify(product_schema.dump(product))

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

# Order Endpoints
@app.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders))

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get a single order by ID"""
    order = Order.query.get_or_404(order_id)
    return jsonify(order_schema.dump(order))

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    try:
        data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Validate product quantities
    for item in data['order_items']:
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({"error": f"Product with ID {item['product_id']} not found"}), 404
        if product.quantity < item['quantity']:
            return jsonify({"error": f"Insufficient quantity for product {product.name}"}), 400

    # Create order
    order = Order(
        customer_name=data['customer_name'],
        customer_email=data['customer_email'],
        customer_phone=data.get('customer_phone'),
        shipping_address=data['shipping_address'],
        total_amount=data['total_amount'],
        status=data.get('status', 'pending')
    )
    db.session.add(order)
    db.session.commit()

    # Create order items and update product quantities
    for item in data['order_items']:
        product = Product.query.get(item['product_id'])
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price']
        )
        db.session.add(order_item)
        product.quantity -= item['quantity']
    
    db.session.commit()
    return jsonify(order_schema.dump(order)), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an order (primarily status updates)"""
    order = Order.query.get_or_404(order_id)
    try:
        data = order_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Only allow status updates for simplicity
    if 'status' in data:
        order.status = data['status']
    
    db.session.commit()
    return jsonify(order_schema.dump(order))

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order"""
    order = Order.query.get_or_404(order_id)
    
    # Restore
