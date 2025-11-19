"""
Generated Code Metadata:
========================
Original URL: https://cmjsr.com
Prompt: Generate a RESTful API for a self-service platform that provides TikTok services, including endpoints for ordering, payment, and order status updates.
Generated: DETERMINISTIC_2c074622473e4427
Batch ID: 20250622_210020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
import uuid
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tiktok_services.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True)
    admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    user = db.relationship('User', backref='orders')
    service = db.relationship('Service', backref='orders')

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    order = db.relationship('Order', backref='payments')

# Helper functions
def validate_service_data(data):
    required_fields = ['name', 'price', 'duration_days']
    for field in required_fields:
        if field not in data:
            return False
    return True

def validate_order_data(data):
    required_fields = ['service_id', 'quantity']
    for field in required_fields:
        if field not in data:
            return False
    return True

def validate_payment_data(data):
    required_fields = ['order_id', 'amount', 'payment_method']
    for field in required_fields:
        if field not in data:
            return False
    return True

# Routes
@app.route('/')
def index():
    return jsonify({'message': 'TikTok Services API'})

# Auth Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        email=data['email'],
        admin=data.get('admin', False)
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'public_id': user.public_id, 'admin': user.admin})
    return jsonify({'access_token': access_token}), 200

# Service Routes
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{
        'id': service.id,
        'name': service.name,
        'description': service.description,
        'price': service.price,
        'duration_days': service.duration_days
    } for service in services]), 200

@app.route('/services', methods=['POST'])
@jwt_required()
def create_service():
    current_user = get_jwt_identity()
    if not current_user['admin']:
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    if not validate_service_data(data):
        return jsonify({'message': 'Invalid service data'}), 400

    service = Service(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        duration_days=data['duration_days']
    )
    db.session.add(service)
    db.session.commit()

    return jsonify({'message': 'Service created successfully', 'id': service.id}), 201

# Order Routes
@app.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    if not validate_order_data(data):
        return jsonify({'message': 'Invalid order data'}), 400

    service = Service.query.get(data['service_id'])
    if not service:
        return jsonify({'message': 'Service not found'}), 404

    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user['public_id']).first()

    order = Order(
        user_id=user.id,
        service_id=service.id,
        quantity=data['quantity'],
        total_price=service.price * data['quantity']
    )
    db.session.add(order)
    db.session.commit()

    return jsonify({
        'message': 'Order created successfully',
        'order_id': order.public_id,
        'total_price': order.total_price
    }), 201

@app.route('/orders/<order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    order = Order.query.filter_by(public_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user['public_id']).first()

    if order.user_id != user.id and not current_user['admin']:
        return jsonify({'message': 'Unauthorized access'}), 403

    return jsonify({
        'id': order.public_id,
        'service': order.service.name,
        'quantity': order.quantity,
        'total_price': order.total_price,
        'status': order.status,
        'created_at': order.created_at.isoformat()
    }), 200

@app.route('/orders/<order_id>/status', methods=['PUT'])
@jwt_required()
def update_order_status(order_id):
    current_user = get_jwt_identity()
    if not current_user['admin']:
        return jsonify({'message': 'Admin access required'}), 403

    order = Order.query.filter_by(public_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    data = request.get_json()
    if 'status' not in data:
        return jsonify({'message': 'Status is required'}), 400

    order.status = data['status']
    db.session.commit()

    return jsonify({'message': 'Order status updated successfully'}), 200

# Payment Routes
@app.route('/payments', methods=['POST'])
@jwt_required()
def
