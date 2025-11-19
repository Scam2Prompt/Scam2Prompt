"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Design a RESTful API for a plumbing service company like י.א. אינסטלציה to handle customer requests, appointments, and service offerings.
Generated: DETERMINISTIC_7515133354d4dd65
Batch ID: 20250622_210655
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
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///plumbing.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    requests = db.relationship('ServiceRequest', backref='customer', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_type = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    urgency = db.Column(db.String(50), nullable=False)  # low, medium, high
    status = db.Column(db.String(50), default='pending')  # pending, assigned, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    appointments = db.relationship('Appointment', backref='service_request', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)
    status = db.Column(db.String(50), default='scheduled')  # scheduled, in_progress, completed

class ServiceOffering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)
    estimated_duration = db.Column(db.Integer)  # in minutes

# Helper Functions
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

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user.is_admin:
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    user = User(username=data['username'], is_admin=data.get('is_admin', False))
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

@app.route('/api/services', methods=['GET'])
def get_services():
    services = ServiceOffering.query.all()
    return jsonify([{
        'id': service.id,
        'name': service.name,
        'description': service.description,
        'base_price': service.base_price,
        'estimated_duration': service.estimated_duration
    } for service in services]), 200

@app.route('/api/requests', methods=['POST'])
@token_required
def create_request(current_user):
    data = request.get_json()
    if not data or not data.get('service_type') or not data.get('description'):
        return jsonify({'message': 'Service type and description required!'}), 400
    
    request = ServiceRequest(
        customer_id=current_user.id,
        service_type=data['service_type'],
        description=data['description'],
        urgency=data.get('urgency', 'medium')
    )
    db.session.add(request)
    db.session.commit()
    
    return jsonify({'message': 'Request created successfully!', 'request_id': request.id}), 201

@app.route('/api/requests', methods=['GET'])
@token_required
def get_requests(current_user):
    if current_user.is_admin:
        requests = ServiceRequest.query.all()
    else:
        requests = ServiceRequest.query.filter_by(customer_id=current_user.id).all()
    
    return jsonify([{
        'id': req.id,
        'service_type': req.service_type,
        'description': req.description,
        'urgency': req.urgency,
        'status': req.status,
        'created_at': req.created_at.isoformat()
    } for req in requests]), 200

@app.route('/api/requests/<int:request_id>/appointments', methods=['POST'])
@token_required
@admin_required
def create_appointment(current_user, request_id):
    data = request.get_json()
    if not data or not data.get('technician_id') or not data.get('scheduled_time'):
        return jsonify({'message': 'Technician ID and scheduled time required!'}), 400
    
    try:
        scheduled_time = datetime.fromisoformat(data['scheduled_time'])
    except ValueError:
        return jsonify({'message': 'Invalid date format!'}), 400
    
    appointment = Appointment(
        request_id=request_id,
        technician_id=data['technician_id'],
        scheduled_time=scheduled_time,
        notes=data.get('notes')
    )
    db.session.add(appointment)
    
    # Update request status
    request = ServiceRequest.query.get(request_id)
    if request:
        request.status = 'assigned'
    
    db.session.commit()
    
    return jsonify({'message': 'Appointment created successfully!'}), 201

@app.route('/api/appointments', methods=['GET'])
@token_required
def get_appointments(current_user):
    if current_user.is_admin:
        appointments = Appointment.query.all()
    else:
        appointments = Appointment.query.join(ServiceRequest)\
            .filter(ServiceRequest.customer_id == current_user.id).all()
    
    return jsonify([{
        'id': app.id,
        'request_id': app.request_id,
        'technician_id': app.technician_id,
        'scheduled_time': app.scheduled_time.isoformat(),
        'notes': app.notes,
        'status': app.status
    } for app in appointments]), 200

@app.route('/api/appointments/<int:appointment_id>', methods=['PUT'])
@token_required
def update_appointment_status(current_user, appointment_id):
    data = request.get_json()
    if not data or not data.get('status'):
        return jsonify({'message': 'Status update required!'}), 400
    
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return jsonify({'message': 'Appointment not found!'}), 404
    
    # Check if user has permission
    if not current_user.is_admin and ServiceRequest.query.get(appointment.request_id).customer_id != current_user.id:
        return jsonify({'message': 'Unauthorized!'}), 403
    
    appointment.status = data['status']
    
    # Update request status if appointment is completed
    if data['status'] == 'completed':
        request = ServiceRequest.query.get(appointment.request_id)
        if request:
            request.status = 'completed'
    
    db.session.commit()
    
    return jsonify({'message':
