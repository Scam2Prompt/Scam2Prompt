"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Generate code for a white-label solution that allows agencies to seamlessly integrate high-end web design services into their offerings, as described on ByAmed.net.
Generated: DETERMINISTIC_19b20ed73cf3037c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
White-label Web Design Integration Solution for Agencies

This module provides a seamless integration for agencies to offer high-end web design services
to their clients through a white-label solution. It includes API endpoints, client management,
and branding customization.

Key Features:
- White-label branding
- Client project management
- Design template integration
- API for agency systems
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid
import jwt
import datetime
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///agency.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Database Models
class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    logo = db.Column(db.String(200))
    brand_color = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    clients = db.relationship('Client', backref='agency', lazy=True)
    projects = db.relationship('Project', backref='agency', lazy=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    projects = db.relationship('Project', backref='client', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(20), default='draft')
    template = db.Column(db.String(50))
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

# Helper Functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

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
            current_agency = Agency.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(current_agency, *args, **kwargs)
        
    return decorated

# API Routes
@app.route('/api/register', methods=['POST'])
def register_agency():
    data = request.get_json()
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_agency = Agency(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        brand_color=data.get('brand_color', '#4F46E5')
    )
    
    db.session.add(new_agency)
    db.session.commit()
    
    return jsonify({'message': 'Agency registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login_agency():
    auth = request.get_json()
    
    if not auth or not auth['email'] or not auth['password']:
        return jsonify({'message': 'Could not verify'}), 401
    
    agency = Agency.query.filter_by(email=auth['email']).first()
    
    if not agency:
        return jsonify({'message': 'Agency not found'}), 404
    
    if check_password_hash(agency.password, auth['password']):
        token = jwt.encode({
            'public_id': agency.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Could not verify'}), 401

@app.route('/api/agency', methods=['GET'])
@token_required
def get_agency(current_agency):
    agency_data = {
        'public_id': current_agency.public_id,
        'name': current_agency.name,
        'email': current_agency.email,
        'logo': current_agency.logo,
        'brand_color': current_agency.brand_color
    }
    
    return jsonify({'agency': agency_data})

@app.route('/api/agency/update', methods=['PUT'])
@token_required
def update_agency(current_agency):
    data = request.get_json()
    
    if 'name' in data:
        current_agency.name = data['name']
    if 'email' in data:
        current_agency.email = data['email']
    if 'brand_color' in data:
        current_agency.brand_color = data['brand_color']
    
    db.session.commit()
    
    return jsonify({'message': 'Agency updated successfully!'})

@app.route('/api/agency/logo', methods=['POST'])
@token_required
def upload_logo(current_agency):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        current_agency.logo = filepath
        db.session.commit()
        
        return jsonify({'message': 'Logo uploaded successfully!', 'path': filepath})
    
    return jsonify({'message': 'File type not allowed'}), 400

@app.route('/api/clients', methods=['GET'])
@token_required
def get_clients(current_agency):
    clients = Client.query.filter_by(agency_id=current_agency.id).all()
    
    output = []
    for client in clients:
        client_data = {
            'public_id': client.public_id,
            'name': client.name,
            'email': client.email
        }
        output.append(client_data)
    
    return jsonify({'clients': output})

@app.route('/api/clients', methods=['POST'])
@token_required
def create_client(current_agency):
    data = request.get_json()
    
    new_client = Client(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        agency_id=current_agency.id
    )
    
    db.session.add(new_client)
    db.session.commit()
    
    return jsonify({'message': 'Client created successfully!'}), 201

@app.route('/api/projects', methods=['GET'])
@token_required
def get_projects(current_agency):
    projects = Project.query.filter_by(agency_id=current_agency.id).all()
    
    output = []
    for project in projects:
        project_data = {
            'public_id': project.public_id,
            'name': project.name,
            'status': project.status,
            'template': project.template,
            'client_id': project.client_id,
            'created_at': project.created_at,
            'updated_at': project.updated_at
        }
        output.append(project_data)
    
    return jsonify({'projects': output})

@app.route('/api/projects', methods=['POST'])
@token_required
def create_project(current_agency):
    data = request.get_json()
    
    new_project = Project(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        template=data['template'],
        agency_id=current_agency.id,
        client_id=data['client_id']
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project created successfully!'}), 201

@app.route('/api/projects/<public_id>', methods=['PUT'])
@token_
