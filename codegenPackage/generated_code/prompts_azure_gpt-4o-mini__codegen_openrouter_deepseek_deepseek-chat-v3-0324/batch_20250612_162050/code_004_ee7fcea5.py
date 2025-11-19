"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Illustrate how to implement a web development project that includes features for medical billing and coding, based on the healthcare services provided by Vital Corporate Solutions.
Generated: DETERMINISTIC_ee7fcea527bcb5e7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from datetime import timedelta
from flask_cors import CORS
import logging

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_billing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key in production

# Initialize database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'billing_staff', 'provider'

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    insurance_id = db.Column(db.String(50), nullable=False)
    policy_number = db.Column(db.String(50), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)  # CPT/HCPCS code
    description = db.Column(db.String(200), nullable=False)
    fee = db.Column(db.Float, nullable=False)

class BillingRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date_of_service = db.Column(db.Date, nullable=False)
    diagnosis_code = db.Column(db.String(20), nullable=False)  # ICD-10 code
    status = db.Column(db.String(20), nullable=False)  # 'pending', 'billed', 'paid', 'denied'
    amount = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)

    patient = db.relationship('Patient', backref='billing_records')
    provider = db.relationship('User', backref='billing_records')
    service = db.relationship('Service', backref='billing_records')

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
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        password=hashed_password,
        role=data['role']
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error registering user: {str(e)}")
        return jsonify({'message': 'Error registering user'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'role': user.role
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/patients', methods=['POST'])
@token_required
def create_patient(current_user):
    if current_user.role not in ['admin', 'billing_staff']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('dob') or not data.get('insurance_id') or not data.get('policy_number'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    try:
        new_patient = Patient(
            name=data['name'],
            dob=datetime.datetime.strptime(data['dob'], '%Y-%m-%d').date(),
            insurance_id=data['insurance_id'],
            policy_number=data['policy_number']
        )
        
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({'message': 'Patient created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating patient: {str(e)}")
        return jsonify({'message': 'Error creating patient'}), 500

@app.route('/api/patients', methods=['GET'])
@token_required
def get_patients(current_user):
    if current_user.role not in ['admin', 'billing_staff', 'provider']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    patients = Patient.query.all()
    output = []
    
    for patient in patients:
        patient_data = {
            'id': patient.id,
            'name': patient.name,
            'dob': patient.dob.strftime('%Y-%m-%d'),
            'insurance_id': patient.insurance_id,
            'policy_number': patient.policy_number
        }
        output.append(patient_data)
    
    return jsonify({'patients': output}), 200

@app.route('/api/services', methods=['POST'])
@token_required
def create_service(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized access'}), 403
    
    data = request.get_json()
    
    if not data or not data.get('code') or not data.get('description') or not data.get('fee'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if Service.query.filter_by(code=data['code']).first():
        return jsonify({'message': 'Service code already exists'}), 400
    
    try:
        new_service = Service(
            code=data['code'],
            description=data['description'],
            fee=data['fee']
        )
        
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'message': 'Service created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating service: {str(e)}")
        return jsonify({'message': 'Error creating service'}), 500

@app.route('/api/services', methods=['GET'])
@token_required
def get_services(current_user):
    services = Service.query.all()
    output = []
    
    for service in services:
        service_data = {
            'id': service.id,
            'code': service.code,
            'description': service.description,
            'fee': service.fee
        }
        output.append(service_data)
    
    return jsonify({'services': output}), 200

@app.route('/api/billing', methods=['POST'])
@token_required
def create_billing_record(current_user):
    if current_user.role not in ['admin', 'provider']:
        return jsonify({'message': 'Unauthorized access'}), 403
    
    data = request.get_json()
    
    required_fields = ['patient_id', 'service_id', 'date_of_service', 'diagnosis_code']
    if not data or any(field not
