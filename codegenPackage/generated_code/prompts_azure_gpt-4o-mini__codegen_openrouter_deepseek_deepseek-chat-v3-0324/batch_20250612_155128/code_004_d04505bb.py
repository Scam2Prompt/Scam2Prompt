"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Describe how to create a software solution for out-growers consultancy that facilitates communication between producers and off-takers, based on Olgon's approach.
Generated: DETERMINISTIC_d04505bb4f250811
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Out-growers Consultancy Platform
Facilitates communication between producers and off-takers
Inspired by Olgon's approach
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
import logging
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outgrowers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # In production, use environment variable
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Models
class User(db.Model):
    """User model for both producers and off-takers"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'producer' or 'offtaker'
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    """Agricultural product model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    unit = db.Column(db.String(20))  # kg, ton, etc.

class Listing(db.Model):
    """Product listing by producers"""
    id = db.Column(db.Integer, primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    available_from = db.Column(db.Date)
    available_to = db.Column(db.Date)
    location = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='available')  # available, reserved, sold

    producer = db.relationship('User', foreign_keys=[producer_id])
    product = db.relationship('Product')

class Contract(db.Model):
    """Contract between producer and off-taker"""
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    offtaker_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    agreed_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    delivery_date = db.Column(db.Date)
    terms = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, active, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    listing = db.relationship('Listing')
    offtaker = db.relationship('User', foreign_keys=[offtaker_id])

class Message(db.Model):
    """Communication between users"""
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'))
    content = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])
    contract = db.relationship('Contract')

# Helper functions
def role_required(role):
    """Decorator to require specific role"""
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            current_user = get_jwt_identity()
            user = User.query.filter_by(username=current_user).first()
            if not user or user.role != role:
                return jsonify({"msg": f"{role} access required"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    """User registration endpoint"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"msg": "Missing required fields"}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    user = User(
        username=data['username'],
        email=data['email'],
        role=data.get('role', 'producer'),
        phone=data.get('phone')
    )
    user.set_password(data['password'])
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating user: {str(e)}")
        return jsonify({"msg": "Error creating user"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """User login endpoint"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all available products"""
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'category': p.category,
        'unit': p.unit
    } for p in products]), 200

@app.route('/api/listings', methods=['GET'])
def get_listings():
    """Get all available listings"""
    listings = Listing.query.filter_by(status='available').all()
    return jsonify([{
        'id': l.id,
        'product': l.product.name,
        'producer': l.producer.username,
        'quantity': l.quantity,
        'price_per_unit': l.price_per_unit,
        'available_from': l.available_from.isoformat() if l.available_from else None,
        'available_to': l.available_to.isoformat() if l.available_to else None,
        'location': l.location
    } for l in listings]), 200

@app.route('/api/listings', methods=['POST'])
@jwt_required()
@role_required('producer')
def create_listing():
    """Create a new product listing"""
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    
    data = request.get_json()
    
    if not data or not data.get('product_id') or not data.get('quantity') or not data.get('price_per_unit'):
        return jsonify({"msg": "Missing required fields"}), 400
    
    listing = Listing(
        producer_id=user.id,
        product_id=data['product_id'],
        quantity=data['quantity'],
        price_per_unit=data['price_per_unit'],
        available_from=datetime.datetime.strptime(data['available_from'], '%Y-%m-%d').date() if data.get('available_from') else None,
        available_to=datetime.datetime.strptime(data['available_to'], '%Y-%m-%d').date() if data.get('available_to') else None,
        location=data.get('location')
    )
    
    try:
        db.session.add(list
