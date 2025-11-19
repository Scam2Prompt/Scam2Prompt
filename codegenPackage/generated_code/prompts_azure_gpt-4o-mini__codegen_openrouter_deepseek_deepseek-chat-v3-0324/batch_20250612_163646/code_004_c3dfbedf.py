"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Create a RESTful API design for a logistics company that includes features like cargo safety management and tracking, based on ENL Consortium's operational practices.
Generated: DETERMINISTIC_c3dfbedf262343d0
Batch ID: 20250612_163646
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
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'logistics.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # In production, use environment variable

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, manager, staff

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, in_transit, delivered
    safety_checks = db.Column(db.JSON)  # Stores safety check data
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class TrackingEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    notes = db.Column(db.String(200))

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'role')

class CargoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tracking_number', 'description', 'weight', 'volume', 
                 'origin', 'destination', 'status', 'safety_checks', 'created_at')

class TrackingEventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cargo_id', 'location', 'status', 'timestamp', 'notes')

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
cargo_schema = CargoSchema()
cargos_schema = CargoSchema(many=True)
tracking_event_schema = TrackingEventSchema()
tracking_events_schema = TrackingEventSchema(many=True)

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
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth['username'] or not auth['password']:
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong credentials'}), 401

@app.route('/api/cargo', methods=['GET'])
@token_required
def get_all_cargo(current_user):
    cargos = Cargo.query.all()
    result = cargos_schema.dump(cargos)
    return jsonify(result)

@app.route('/api/cargo/<tracking_number>', methods=['GET'])
@token_required
def get_cargo(current_user, tracking_number):
    cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
    if not cargo:
        return jsonify({'message': 'Cargo not found'}), 404
    return cargo_schema.jsonify(cargo)

@app.route('/api/cargo', methods=['POST'])
@token_required
def create_cargo(current_user):
    if current_user.role not in ['admin', 'manager']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    data = request.get_json()
    new_cargo = Cargo(
        tracking_number=data['tracking_number'],
        description=data['description'],
        weight=data['weight'],
        volume=data['volume'],
        origin=data['origin'],
        destination=data['destination'],
        safety_checks=data.get('safety_checks', {})
    )
    db.session.add(new_cargo)
    db.session.commit()
    return cargo_schema.jsonify(new_cargo), 201

@app.route('/api/cargo/<tracking_number>', methods=['PUT'])
@token_required
def update_cargo(current_user, tracking_number):
    cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
    if not cargo:
        return jsonify({'message': 'Cargo not found'}), 404
    
    if current_user.role not in ['admin', 'manager']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    data = request.get_json()
    cargo.description = data.get('description', cargo.description)
    cargo.weight = data.get('weight', cargo.weight)
    cargo.volume = data.get('volume', cargo.volume)
    cargo.status = data.get('status', cargo.status)
    cargo.safety_checks = data.get('safety_checks', cargo.safety_checks)
    
    db.session.commit()
    return cargo_schema.jsonify(cargo)

@app.route('/api/cargo/<tracking_number>/track', methods=['POST'])
@token_required
def add_tracking_event(current_user, tracking_number):
    cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
    if not cargo:
        return jsonify({'message': 'Cargo not found'}), 404
    
    data = request.get_json()
    new_event = TrackingEvent(
        cargo_id=cargo.id,
        location=data['location'],
        status=data['status'],
        notes=data.get('notes', '')
    )
    db.session.add(new_event)
    db.session.commit()
    
    # Update cargo status if provided
    if 'status' in data:
        cargo.status = data['status']
        db.session.commit()
    
    return tracking_event_schema.jsonify(new_event), 201

@app.route('/api/cargo/<tracking_number>/track', methods=['GET'])
@token_required
def get_tracking_events(current_user, tracking_number):
    cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
    if not cargo:
        return jsonify({'message': 'Cargo not found'}), 404
    
    events = TrackingEvent.query.filter_by(cargo_id=cargo.id).order_by(TrackingEvent.timestamp.desc()).all()
    return tracking_events_schema.jsonify(events)

@app.route('/api/cargo/<tracking_number>/safety', methods=['PUT'])
@token_required
def update_safety_checks(current_user, tracking_number):
    if current_user.role not in ['admin', 'manager']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
    if not cargo:
        return jsonify({'message': 'Cargo not found'}), 404
    
    data = request.get_json()
