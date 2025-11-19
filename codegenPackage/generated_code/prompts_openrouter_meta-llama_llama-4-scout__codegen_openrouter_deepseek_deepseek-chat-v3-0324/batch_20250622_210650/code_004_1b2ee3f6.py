"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Develop a RESTful API to manage and track investigation projects, including features for task assignment, report generation, and client communication."
Generated: DETERMINISTIC_1b2ee3f6a7ed292c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investigation_project_api.py
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'investigation.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))
    projects = db.relationship('Project', backref='user', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tasks = db.relationship('Task', backref='project', lazy=True)
    reports = db.relationship('Report', backref='project', lazy=True)
    communications = db.relationship('Communication', backref='project', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    due_date = db.Column(db.DateTime)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

class Communication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    message = db.Column(db.Text)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'username', 'role')

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'title', 'description', 'status', 'created_at', 'user_id')

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'title', 'description', 'status', 'assigned_to', 'project_id', 'due_date')

class ReportSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'title', 'content', 'created_at', 'project_id')

class CommunicationSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'message', 'sender_id', 'project_id', 'created_at')

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
report_schema = ReportSchema()
reports_schema = ReportSchema(many=True)
communication_schema = CommunicationSchema()
communications_schema = CommunicationSchema(many=True)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password,
        role=data.get('role', 'investigator')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth['username']).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth['password']):
        token = create_access_token(identity={'public_id': user.public_id, 'role': user.role})
        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# Project routes
@app.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user['public_id']).first()
    projects = Project.query.filter_by(user_id=user.id).all()
    return jsonify(projects_schema.dump(projects))

@app.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user['public_id']).first()
    
    new_project = Project(
        public_id=str(uuid.uuid4()),
        title=data['title'],
        description=data.get('description', ''),
        status='active',
        user_id=user.id
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(project_schema.dump(new_project)), 201

@app.route('/projects/<project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    project = Project.query.filter_by(public_id=project_id).first()
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    return jsonify(project_schema.dump(project))

@app.route('/projects/<project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    project = Project.query.filter_by(public_id=project_id).first()
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    
    data = request.get_json()
    project.title = data.get('title', project.title)
    project.description = data.get('description', project.description)
    project.status = data.get('status', project.status)
    
    db.session.commit()
    return jsonify(project_schema.dump(project))

@app.route('/projects/<project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    project = Project.query.filter_by(public_id=project_id).first()
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted'}), 200

# Task routes
@app.route('/projects/<project_id>/tasks', methods=['GET'])
@jwt_required()
def get_tasks(project_id):
    project = Project.query.filter_by(public_id=project_id).first()
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    
    tasks = Task.query.filter_by(project_id=project.id).all()
    return jsonify(tasks_schema.dump(tasks))

@app.route('/projects/<project_id>/tasks', methods=['POST'])
@jwt_required()
def create_task(project_id):
    project = Project.query.filter_by(public_id=project_id).first()
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    
    data = request.get_json()
    new_task = Task(
        public_id=str(uuid.uuid4()),
        title=data['title'],
        description=data.get('description', ''),
        status='pending',
        assigned_to=data.get('assigned_to'),
        project_id=project.id,
        due_date=data
