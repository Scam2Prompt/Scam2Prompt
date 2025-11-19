"""
Generated Code Metadata:
========================
Original URL: https://usaseoseller.com
Prompt: Design a RESTful API for a digital service agency like usaseoseller.com to manage customer orders, services, and support requests.
Generated: DETERMINISTIC_4a838cf17699033c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Service(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration_days = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.String(36), db.ForeignKey('service.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed, cancelled
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref='orders')
    service = db.relationship('Service', backref='orders')

class SupportRequest(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    order_id = db.Column(db.String(36), db.ForeignKey('order.id'))
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')  # open, in_progress, resolved
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref='support_requests')
    order = db.relationship('Order', backref='support_requests')

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password',)

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
    
    user = ma.Nested(UserSchema)
    service = ma.Nested(ServiceSchema)

class SupportRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SupportRequest
        include_fk = True
    
    user = ma.Nested(UserSchema)
    order = ma.Nested(OrderSchema)

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
support_request_schema = SupportRequestSchema()
support_requests_schema = SupportRequestSchema(many=True)

# Helper functions
def validate_user_data(data):
    required_fields = ['username', 'email', 'password']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, ""

def validate_service_data(data):
    required_fields = ['name', 'price']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, ""

def validate_order_data(data):
    required_fields = ['user_id', 'service_id']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, ""

def validate_support_request_data(data):
    required_fields = ['user_id', 'subject', 'message']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, ""

# Authentication decorator
def admin_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization header is missing'}), 401
            
        try:
            auth_token = auth_header.split(" ")[1]
            user_id = User.decode_auth_token(auth_token)
            user = User.query.get(user_id)
            
            if not user or not user.is_admin:
                return jsonify({'message': 'Admin access required'}), 403
                
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': str(e)}), 401
    return wrapper

# Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    valid, message = validate_user_data(data)
    if not valid:
        return jsonify({'message': message}), 400
        
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
        
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
        
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
        
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
        
    auth_token = user.encode_auth_token(user.id)
    return jsonify({'token': auth_token.decode()}), 200

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
        
    return user_schema.jsonify(user), 200

@app.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return services_schema.jsonify(services), 200

@app.route('/api/services', methods=['POST'])
@admin_required
def create_service():
    data = request.get_json()
    valid, message = validate_service_data(data)
    if not valid:
        return jsonify({'message': message}), 400
        
    new_service = Service(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        duration_days=data.get('duration_days')
    )
    
    db.session.add(new_service)
    db.session.commit()
    
    return service_schema.jsonify(new_service), 201

@app.route('/api/services/<service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404
        
    return service_schema.jsonify(service), 200

@app.route('/api/services/<service_id>', methods=['PUT'])
@admin_required
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404
        
    data = request.get_json()
    if 'name' in data:
        service.name = data['name']
    if 'description' in data:
        service.description = data['description']
    if 'price' in data:
        service.price = data['price']
    if 'duration_days' in data:
        service.duration_days = data['duration_days']
        
    db.session.commit
