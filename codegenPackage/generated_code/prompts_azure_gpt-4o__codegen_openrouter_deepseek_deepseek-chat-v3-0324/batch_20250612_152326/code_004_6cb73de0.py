"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Write code using Flask or Django to create a backend system for managing vendor applications for a festival, including booth assignments and application statuses.
Generated: DETERMINISTIC_6cb73de013a9a7a7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask backend for festival vendor management

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
import uuid
import datetime
from functools import wraps
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///festival.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Vendor(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    business_name = db.Column(db.String(100))
    business_description = db.Column(db.Text)
    products = db.Column(db.Text)
    tax_id = db.Column(db.String(50))
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    booth_id = db.Column(db.Integer, db.ForeignKey('booth.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    booth = db.relationship('Booth', backref='vendor')

class Booth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    size = db.Column(db.String(20))  # small, medium, large
    location = db.Column(db.String(100))
    price = db.Column(db.Float)
    amenities = db.Column(db.Text)
    is_occupied = db.Column(db.Boolean, default=False)

class Admin(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Schemas
class VendorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'business_name', 
                 'business_description', 'products', 'tax_id', 'status', 
                 'booth_id', 'created_at')

class BoothSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number', 'size', 'location', 'price', 
                 'amenities', 'is_occupied')

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
booth_schema = BoothSchema()
booths_schema = BoothSchema(many=True)

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_admin = Admin.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_admin, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/api/vendors/register', methods=['POST'])
def register_vendor():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    if Vendor.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Vendor already exists'}), 409
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_vendor = Vendor(
        name=data.get('name'),
        email=data['email'],
        password=hashed_password,
        phone=data.get('phone'),
        business_name=data.get('business_name'),
        business_description=data.get('business_description'),
        products=data.get('products'),
        tax_id=data.get('tax_id')
    )
    
    db.session.add(new_vendor)
    db.session.commit()
    
    return jsonify({'message': 'Vendor registered successfully'}), 201

@app.route('/api/vendors/login', methods=['POST'])
def login_vendor():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    vendor = Vendor.query.filter_by(email=data['email']).first()
    
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404
    
    if check_password_hash(vendor.password, data['password']):
        token = jwt.encode({
            'id': vendor.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'vendor': vendor_schema.dump(vendor)
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/admin/login', methods=['POST'])
def login_admin():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required'}), 400
    
    admin = Admin.query.filter_by(username=data['username']).first()
    
    if not admin:
        return jsonify({'message': 'Admin not found'}), 404
    
    if check_password_hash(admin.password, data['password']):
        token = jwt.encode({
            'id': admin.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'admin': {'id': admin.id, 'username': admin.username}
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/vendors', methods=['GET'])
@token_required
def get_all_vendors(current_admin):
    vendors = Vendor.query.all()
    result = vendors_schema.dump(vendors)
    return jsonify(result), 200

@app.route('/api/vendors/<vendor_id>', methods=['GET'])
@token_required
def get_vendor(current_admin, vendor_id):
    vendor = Vendor.query.get(vendor_id)
    
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404
    
    return jsonify(vendor_schema.dump(vendor)), 200

@app.route('/api/vendors/<vendor_id>/status', methods=['PUT'])
@token_required
def update_vendor_status(current_admin, vendor_id):
    data = request.get_json()
    vendor = Vendor.query.get(vendor_id)
    
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404
    
    if 'status' not in data:
        return jsonify({'message': 'Status is required'}), 400
    
    vendor.status = data['status']
    db.session.commit()
    
    return jsonify({'message': 'Vendor status updated successfully'}), 200

@app.route('/api/vendors/<vendor_id>/booth', methods=['PUT'])
@token_required
def assign_booth(current_admin, vendor_id):
    data = request.get_json()
    vendor = Vendor.query.get(vendor_id)
    
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404
    
    if 'booth_id' not in data:
        return jsonify({'message': 'Booth ID is required'}), 400
    
    booth = Booth.query.get(data['booth_id'])
    
    if not booth:
        return jsonify({'message': 'Booth not found'}), 404
    
    if booth.is_occupied:
        return jsonify({'message': 'Booth is already occupied'}), 400
    
    # Clear previous booth assignment if any
    if vendor.booth_id:
        prev_booth = Booth.query.get(vendor.booth_id)
        prev_booth.is_occupied = False
    
    vendor.booth_id = booth.id
    booth.is_occupied = True
    db.session.commit()
    
    return jsonify({'message': 'Booth assigned successfully'}), 200

@app.route('/api/booths', methods=['GET'])
@token_required
def get_all_booths(current_admin):
    booths = Booth.query.all()
    result = booths_schema.dump(booths)
    return jsonify(result), 200

@app.route('/api/booths', methods=['POST'])
@token_required
def create_booth(current_admin):
