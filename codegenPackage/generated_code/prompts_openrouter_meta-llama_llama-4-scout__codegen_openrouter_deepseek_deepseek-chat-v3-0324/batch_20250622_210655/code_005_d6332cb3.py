"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Create a RESTful API to manage construction project documentation, including client information, project plans, and progress reports, for a company like ILMAM Construction."
Generated: DETERMINISTIC_d6332cb3031d5ce4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RESTful API for Construction Project Documentation Management
"""

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_docs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, manager, worker

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20))  # planning, in_progress, completed, delayed
    budget = db.Column(db.Float)
    client = db.relationship('Client', backref=db.backref('projects', lazy=True))

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # plan, report, contract, etc.
    upload_date = db.Column(db.Date)
    file_path = db.Column(db.String(200), nullable=False)
    project = db.relationship('Project', backref=db.backref('documents', lazy=True))

class ProgressReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    report_date = db.Column(db.Date, nullable=False)
    progress_percentage = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)
    project = db.relationship('Project', backref=db.backref('progress_reports', lazy=True))

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
        if current_user.role != 'admin':
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Authentication Routes
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('username') or not auth.get('password'):
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
    
    return jsonify({'message': 'Wrong password'}), 403

# Client Routes
@app.route('/clients', methods=['GET'])
@token_required
def get_clients(current_user):
    clients = Client.query.all()
    output = []
    for client in clients:
        client_data = {
            'id': client.id,
            'name': client.name,
            'contact_person': client.contact_person,
            'email': client.email,
            'phone': client.phone,
            'address': client.address
        }
        output.append(client_data)
    return jsonify({'clients': output})

@app.route('/clients/<int:client_id>', methods=['GET'])
@token_required
def get_client(current_user, client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify({
        'id': client.id,
        'name': client.name,
        'contact_person': client.contact_person,
        'email': client.email,
        'phone': client.phone,
        'address': client.address
    })

@app.route('/clients', methods=['POST'])
@token_required
@admin_required
def create_client(current_user):
    data = request.json
    if not data or not data.get('name'):
        abort(400, description="Client name is required")
    
    client = Client(
        name=data['name'],
        contact_person=data.get('contact_person'),
        email=data.get('email'),
        phone=data.get('phone'),
        address=data.get('address')
    )
    db.session.add(client)
    db.session.commit()
    return jsonify({'message': 'Client created successfully'}), 201

@app.route('/clients/<int:client_id>', methods=['PUT'])
@token_required
@admin_required
def update_client(current_user, client_id):
    client = Client.query.get_or_404(client_id)
    data = request.json
    
    client.name = data.get('name', client.name)
    client.contact_person = data.get('contact_person', client.contact_person)
    client.email = data.get('email', client.email)
    client.phone = data.get('phone', client.phone)
    client.address = data.get('address', client.address)
    
    db.session.commit()
    return jsonify({'message': 'Client updated successfully'})

@app.route('/clients/<int:client_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_client(current_user, client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted successfully'})

# Project Routes
@app.route('/projects', methods=['GET'])
@token_required
def get_projects(current_user):
    projects = Project.query.all()
    output = []
    for project in projects:
        project_data = {
            'id': project.id,
            'name': project.name,
            'client_id': project.client_id,
            'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
            'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
            'status': project.status,
            'budget': project.budget
        }
        output.append(project_data)
    return jsonify({'projects': output})

@app.route('/projects/<int:project_id>', methods=['GET'])
@token_required
def get_project(current_user, project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        'id': project.id,
        'name': project.name,
        'client_id': project.client_id,
        'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
        'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
        'status': project.status,
        'budget': project.budget
    })

@app.route('/projects', methods=['POST'])
@token_required
def create_project(current_user):
    data = request.json
    if not data or not data.get('name') or not data.get('client_id'):
        abort(400, description="Project name and client ID are required")
    
    project = Project(
        name=data['name'],
        client_id=data['client_id'],
        start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date() if data.get('start_date') else None,
        end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data.get('end_date') else None,
        status=data.get('status'),
        budget=data.get('budget')
