"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: "Design an app development architecture for a client in the healthcare industry, incorporating features such as secure data storage, user authentication, and push notifications, using iOS, Android, or Windows Phone."
Generated: DETERMINISTIC_861eab83042f49c5
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Healthcare Mobile App Architecture
# This code outlines a backend service for a healthcare mobile app
# Includes secure data storage, user authentication, and push notifications

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///healthcare.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Firebase for push notifications
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # patient, doctor, admin
    fcm_token = db.Column(db.String(255))  # For push notifications

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    record_data = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Decorator for token verification
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

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        role=data['role']
    )
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({
        'token': token,
        'user_id': user.id,
        'role': user.role
    }), 200

@app.route('/records', methods=['GET'])
@token_required
def get_records(current_user):
    if current_user.role == 'patient':
        records = PatientRecord.query.filter_by(patient_id=current_user.id).all()
    elif current_user.role == 'doctor':
        records = PatientRecord.query.filter_by(doctor_id=current_user.id).all()
    else:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    output = []
    for record in records:
        record_data = {
            'id': record.id,
            'record_data': record.record_data,
            'created_at': record.created_at,
            'updated_at': record.updated_at
        }
        output.append(record_data)
    
    return jsonify({'records': output}), 200

@app.route('/records', methods=['POST'])
@token_required
def create_record(current_user):
    if current_user.role != 'doctor':
        return jsonify({'message': 'Only doctors can create records'}), 403
    
    data = request.get_json()
    new_record = PatientRecord(
        patient_id=data['patient_id'],
        doctor_id=current_user.id,
        record_data=data['record_data']
    )
    
    db.session.add(new_record)
    db.session.commit()
    
    # Send push notification to patient
    patient = User.query.get(data['patient_id'])
    if patient and patient.fcm_token:
        message = messaging.Message(
            notification=messaging.Notification(
                title='New Health Record',
                body='Your doctor has added a new health record'
            ),
            token=patient.fcm_token
        )
        try:
            messaging.send(message)
        except Exception as e:
            app.logger.error(f"Failed to send notification: {str(e)}")
    
    return jsonify({'message': 'Record created successfully'}), 201

@app.route('/fcm_token', methods=['POST'])
@token_required
def update_fcm_token(current_user):
    data = request.get_json()
    current_user.fcm_token = data['fcm_token']
    db.session.commit()
    return jsonify({'message': 'FCM token updated successfully'}), 200

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
