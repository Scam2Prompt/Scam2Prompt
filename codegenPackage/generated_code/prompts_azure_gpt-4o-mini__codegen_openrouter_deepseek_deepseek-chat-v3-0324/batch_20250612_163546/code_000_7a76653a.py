"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Generate a code snippet for a web application that connects law firms with pre-qualified legal leads, focusing on the unique features of ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7a76653a32fc84d8
Batch ID: 20250612_163546
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
from flask_marshmallow import Marshmallow
import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'claimlink.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # In production, use environment variable

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class LawFirm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    leads = db.relationship('LegalLead', backref='law_firm', lazy=True)

class LegalLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    law_firm_id = db.Column(db.Integer, db.ForeignKey('law_firm.id'), nullable=True)

# Schemas
class LawFirmSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'specialization', 'verified')

class LegalLeadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'case_type', 'description', 'status', 'created_at', 'law_firm_id')

law_firm_schema = LawFirmSchema()
law_firms_schema = LawFirmSchema(many=True)
legal_lead_schema = LegalLeadSchema()
legal_leads_schema = LegalLeadSchema(many=True)

# Decorator for token authentication
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
            current_law_firm = LawFirm.query.get(data['law_firm_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_law_firm, *args, **kwargs)
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    # Check if law firm already exists
    if LawFirm.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Law firm already exists'}), 409
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_law_firm = LawFirm(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        specialization=data['specialization']
    )
    
    db.session.add(new_law_firm)
    db.session.commit()
    
    return jsonify({'message': 'Law firm registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    law_firm = LawFirm.query.filter_by(email=data['email']).first()
    
    if not law_firm or not check_password_hash(law_firm.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'law_firm_id': law_firm.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

@app.route('/leads', methods=['GET'])
@token_required
def get_leads(current_law_firm):
    leads = LegalLead.query.filter_by(status='pending').all()
    return jsonify(legal_leads_schema.dump(leads)), 200

@app.route('/leads/<int:lead_id>', methods=['PUT'])
@token_required
def accept_lead(current_law_firm, lead_id):
    lead = LegalLead.query.get(lead_id)
    
    if not lead:
        return jsonify({'message': 'Lead not found'}), 404
    
    if lead.status != 'pending':
        return jsonify({'message': 'Lead is not available'}), 400
    
    lead.status = 'accepted'
    lead.law_firm_id = current_law_firm.id
    db.session.commit()
    
    return jsonify({'message': 'Lead accepted successfully'}), 200

@app.route('/my-leads', methods=['GET'])
@token_required
def get_my_leads(current_law_firm):
    leads = LegalLead.query.filter_by(law_firm_id=current_law_firm.id).all()
    return jsonify(legal_leads_schema.dump(leads)), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'message': 'Internal server error'}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
