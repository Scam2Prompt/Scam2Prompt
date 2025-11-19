"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Create a RESTful API to manage orders and inventory for an e-commerce site selling products like car mobile holders and posture corrector belts.
Generated: DETERMINISTIC_ab5409da986d5711
Batch ID: 20250622_205553
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import os

# Initialize Flask app
app = Flask(__name__)
auth = HTTPBasicAuth()

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schemas for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    stock_quantity = fields.Int(required=True)
    category = fields.Str()

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    total_amount = fields.Float(required=True)
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    is_admin = fields.Bool()

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)
user_schema = UserSchema()

# Authentication
@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

@auth.error_handler
def auth_error(status):
    return jsonify({'error': 'Access denied'}), status

# Helper functions
def validate_product_data(data):
    try:
        product_schema.load(data)
        return True, None
    except ValidationError as err:
        return False, err.messages

def validate_order_data(data):
    try:
        order_schema.load(data)
        return True, None
    except ValidationError as err:
        return False, err.messages

def validate_order_item_data(data):
    try:
        order_item_schema.load(data)
        return True, None
    except ValidationError as err:
        return False, err.messages

# Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products_schema.dump(products))

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product_schema.dump(product))

@app.route('/api/products', methods=['POST'])
@auth.login_required
def add_product():
    if not auth.current_user().is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    data = request.get_json()
    valid, errors = validate_product_data(data)
    if not valid:
        return jsonify(errors), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock_quantity=data['stock_quantity'],
        category=data.get('category')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product_schema.dump(product)), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
@auth.login_required
def update_product(product_id):
    if not auth.current_user().is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    valid, errors = validate_product_data(data)
    if not valid:
        return jsonify(errors), 400
    
    product.name = data['name']
    product.description = data.get('description')
    product.price = data['price']
    product.stock_quantity = data['stock_quantity']
    product.category = data.get('category')
    
    db.session.commit()
    return jsonify(product_schema.dump(product))

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@auth.login_required
def delete_product(product_id):
    if not auth.current_user().is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/api/orders', methods=['GET'])
@auth.login_required
def get_orders():
    if auth.current_user().is_admin:
        orders = Order.query.all()
    else:
        orders = Order.query.filter_by(user_id=auth.current_user().id).all()
    return jsonify(orders_schema.dump(orders))

@app.route('/api/orders/<int:order_id>', methods=['GET'])
@auth.login_required
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    if not auth.current_user().is_admin and order.user_id != auth.current_user().id:
        return jsonify({'error': 'Access denied'}), 403
    return jsonify(order_schema.dump(order))

@app.route('/api/orders', methods=['POST'])
@auth.login_required
def create_order():
    data = request.get_json()
    valid, errors = validate_order_data(data)
    if not valid:
        return jsonify(errors), 400
    
    order = Order(
        user_id=auth.current_user().id,
        total_amount=data['total_amount'],
        status=data.get('status', 'pending')
    )
    db.session.add(order)
    db.session.commit()
    
    # Add order items
    for item in data.get('items', []):
        product = Product.query.get(item['product_id'])
        if not product:
            continue
        
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=product.price
        )
        db.session.add(order_item)
        
        # Update product stock
        product.stock_quantity -= item['quantity']
    
    db.session.commit()
    return jsonify(order_schema.dump(order)), 201

@app.route('/api/orders/<int:order_id>', methods=['PUT'])
@auth.login_required
def update_order_status(order_id):
    if not auth.current_user().is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    
    if 'status' not in data:
        return jsonify({'error': 'Status is required'}), 400
    
    order.status = data['status']
    db.session.commit()
    return jsonify(order_schema.dump(order))

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request
