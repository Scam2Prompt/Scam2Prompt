"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Design a simple guard tour system using IoT devices and a cloud-based management platform."
Generated: DETERMINISTIC_9f32045f190f2848
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# IoT Guard Tour System
# Cloud-based management platform with IoT device integration

import json
import time
from datetime import datetime
import uuid
import paho.mqtt.client as mqtt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps

# Configuration
CONFIG = {
    "MQTT_BROKER": "mqtt.example.com",
    "MQTT_PORT": 1883,
    "MQTT_TOPIC": "guard_tour/checkpoints",
    "DB_URI": "sqlite:///guard_tour.db",
    "SECRET_KEY": "your-secret-key-here",
    "TOKEN_EXPIRATION": 3600  # 1 hour
}

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['DB_URI']
app.config['SECRET_KEY'] = CONFIG['SECRET_KEY']
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # admin, supervisor, guard

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Checkpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.String(36), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    checkpoints = db.relationship('Checkpoint', secondary='tour_checkpoints')

class TourCheckpoints(db.Model):
    __tablename__ = 'tour_checkpoints'
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), primary_key=True)
    checkpoint_id = db.Column(db.Integer, db.ForeignKey('checkpoint.id'), primary_key=True)
    order = db.Column(db.Integer)

class Patrol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'))
    guard_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # ongoing, completed, missed

class CheckpointLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patrol_id = db.Column(db.Integer, db.ForeignKey('patrol.id'))
    checkpoint_id = db.Column(db.Integer, db.ForeignKey('checkpoint.id'))
    scan_time = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # on_time, late, missed

# MQTT Client for IoT Device Communication
mqtt_client = mqtt.Client(client_id="guard_tour_server")
mqtt_client.username_pw_set(username="server", password="server_pass")

def on_mqtt_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(CONFIG['MQTT_TOPIC'])
    else:
        print(f"Failed to connect, return code {rc}")

def on_mqtt_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        handle_checkpoint_scan(payload)
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

mqtt_client.on_connect = on_mqtt_connect
mqtt_client.on_message = on_mqtt_message

def handle_checkpoint_scan(data):
    """Process checkpoint scan from IoT device"""
    try:
        device_id = data.get('device_id')
        guard_id = data.get('guard_id')
        timestamp = datetime.fromtimestamp(data.get('timestamp'))
        
        checkpoint = Checkpoint.query.filter_by(device_id=device_id).first()
        if not checkpoint:
            print(f"Unknown device ID: {device_id}")
            return
        
        # Find active patrol for this guard
        patrol = Patrol.query.filter_by(
            guard_id=guard_id,
            status='ongoing'
        ).first()
        
        if not patrol:
            print(f"No active patrol found for guard {guard_id}")
            return
        
        # Create checkpoint log entry
        log = CheckpointLog(
            patrol_id=patrol.id,
            checkpoint_id=checkpoint.id,
            scan_time=timestamp,
            status='on_time'  # Simplified - would need actual logic
        )
        db.session.add(log)
        db.session.commit()
        
        print(f"Checkpoint scan recorded: {checkpoint.name} by guard {guard_id}")
    except Exception as e:
        print(f"Error handling checkpoint scan: {e}")

# Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# API Routes
@app.route('/api/login', methods=['POST'])
def login():
    auth = request.json
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if user.check_password(auth['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow().timestamp() + CONFIG['TOKEN_EXPIRATION']
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong password'}), 401

@app.route('/api/checkpoints', methods=['GET'])
@token_required
def get_checkpoints(current_user):
    checkpoints = Checkpoint.query.all()
    output = []
    
    for checkpoint in checkpoints:
        checkpoint_data = {
            'id': checkpoint.id,
            'name': checkpoint.name,
            'location': checkpoint.location,
            'device_id': checkpoint.device_id,
            'is_active': checkpoint.is_active
        }
        output.append(checkpoint_data)
    
    return jsonify({'checkpoints': output})

@app.route('/api/patrols/start', methods=['POST'])
@token_required
def start_patrol(current_user):
    if current_user.role != 'guard':
        return jsonify({'message': 'Only guards can start patrols'}), 403
    
    data = request.json
    tour_id = data.get('tour_id')
    
    if not tour_id:
        return jsonify({'message': 'Tour ID is required'}), 400
    
    tour = Tour.query.get(tour_id)
    if not tour:
        return jsonify({'message': 'Tour not found'}), 404
    
    # Check if guard already has an active patrol
    active_patrol = Patrol.query.filter_by(
        guard_id=current_user.id,
        status='ongoing'
    ).first()
    
    if active_patrol:
        return jsonify({'message': 'You already have an active patrol'}), 400
    
    patrol = Patrol(
        tour_id=tour_id,
        guard_id=current_user.id,
        start_time=datetime.utcnow(),
        status='ongoing'
    )
    db.session.add(patrol)
    db.session.commit()
    
    return jsonify({
        'message': 'Patrol started successfully',
        'patrol_id': patrol.id
    }), 201

@app.route('/api/patrols/<int:patrol_id>/end', methods=['POST'])
@token_required
def end_patrol(current_user, patrol_id):
    patrol = Patrol.query.get(patrol_id)
    
    if not patrol:
        return jsonify({'message': 'Patrol not found'}), 404
    
    if patrol.guard_id != current_user.id and current_user.role != 'admin':
        return jsonify({'message': 'Not authorized'}), 403
    
    patrol.end_time = datetime.utcnow()
    patrol.status = 'completed'
    db.session.commit()
    
    return jsonify({'message': 'Patrol ended successfully
