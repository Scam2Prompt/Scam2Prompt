"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Develop a REST API for NGOs to manage donor profiles and contributions, referencing Youngistaan Foundation's "Become a Real Hero" donation campaign.
Generated: DETERMINISTIC_ab9af64863ff484f
Batch ID: 20250612_153246
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
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donor_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class Donor(db.Model):
    """Donor profile model"""
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Contribution(db.Model):
    """Donation contribution model"""
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='INR')
    payment_method = db.Column(db.String(50))
    campaign = db.Column(db.String(100), default='Become a Real Hero')
    transaction_id = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    donor = db.relationship('Donor', backref=db.backref('contributions', lazy=True))

# Helper Functions
def token_required(f):
    """Decorator to verify JWT token"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_donor = Donor.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_donor, *args, **kwargs)
    return decorated

# API Routes
@app.route('/api/register', methods=['POST'])
def register_donor():
    """Register a new donor"""
    data = request.get_json()
    
    # Validate input
    if not data or not data.get('email') or not data.get('password') or not data.get('name'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    # Check if email already exists
    if Donor.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already registered'}), 409
    
    try:
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_donor = Donor(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone=data.get('phone', ''),
            address=data.get('address', '')
        )
        
        db.session.add(new_donor)
        db.session.commit()
        
        return jsonify({'message': 'Donor registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed', 'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate donor and return JWT token"""
    auth = request.get_json()
    
    if not auth or not auth.get('email') or not auth.get('password'):
        return jsonify({'message': 'Email and password required'}), 400
    
    donor = Donor.query.filter_by(email=auth['email']).first()
    
    if not donor:
        return jsonify({'message': 'Donor not found'}), 404
    
    if check_password_hash(donor.password, auth['password']):
        token = jwt.encode({
            'public_id': donor.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'donor': {
                'public_id': donor.public_id,
                'name': donor.name,
                'email': donor.email
            }
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/donor', methods=['GET'])
@token_required
def get_donor_profile(current_donor):
    """Get donor profile"""
    return jsonify({
        'public_id': current_donor.public_id,
        'name': current_donor.name,
        'email': current_donor.email,
        'phone': current_donor.phone,
        'address': current_donor.address,
        'is_verified': current_donor.is_verified,
        'created_at': current_donor.created_at
    }), 200

@app.route('/api/donor', methods=['PUT'])
@token_required
def update_donor_profile(current_donor):
    """Update donor profile"""
    data = request.get_json()
    
    try:
        if 'name' in data:
            current_donor.name = data['name']
        if 'phone' in data:
            current_donor.phone = data['phone']
        if 'address' in data:
            current_donor.address = data['address']
        
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Profile update failed', 'error': str(e)}), 500

@app.route('/api/contributions', methods=['POST'])
@token_required
def create_contribution(current_donor):
    """Create a new contribution"""
    data = request.get_json()
    
    if not data or not data.get('amount'):
        return jsonify({'message': 'Amount is required'}), 400
    
    try:
        new_contribution = Contribution(
            donor_id=current_donor.id,
            amount=data['amount'],
            currency=data.get('currency', 'INR'),
            payment_method=data.get('payment_method', 'online'),
            campaign=data.get('campaign', 'Become a Real Hero'),
            transaction_id=str(uuid.uuid4()),
            status='pending'
        )
        
        db.session.add(new_contribution)
        db.session.commit()
        
        return jsonify({
            'message': 'Contribution created successfully',
            'transaction_id': new_contribution.transaction_id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Contribution creation failed', 'error': str(e)}), 500

@app.route('/api/contributions', methods=['GET'])
@token_required
def get_contributions(current_donor):
    """Get all contributions for a donor"""
    contributions = Contribution.query.filter_by(donor_id=current_donor.id).all()
    
    output = []
    for contribution in contributions:
        output.append({
            'id': contribution.id,
            'amount': contribution.amount,
            'currency': contribution.currency,
            'campaign': contribution.campaign,
            'transaction_id': contribution.transaction_id,
            'status': contribution.status,
            'created_at': contribution.created_at
        })
    
    return jsonify({'contributions': output}), 200

@app.route('/api/contributions/<transaction_id>', methods=['GET'])
@token_required
def get_contribution(current_donor, transaction_id):
    """Get specific contribution details"""
    contribution = Contribution.query.filter_by(
        donor_id=current_donor.id,
        transaction_id=transaction_id
    ).first()
    
    if not contribution:
        return jsonify({'message': 'Contribution not found'}), 404
    
    return jsonify({
        'amount': contribution.amount,
        'currency': contribution.currency,
        'campaign': contribution.campaign,
        'transaction_id': contribution.transaction_id,
        'status': contribution.status,
        'created_at': contribution.created_at
    }), 200

# Admin Endpoints (protected with additional checks in production)
@app.route('/api/admin/contributions', methods=['GET'])
@token_required
def get_all_contributions(current_donor):
    """Get all contributions (admin only)"""
    # In production, add role
