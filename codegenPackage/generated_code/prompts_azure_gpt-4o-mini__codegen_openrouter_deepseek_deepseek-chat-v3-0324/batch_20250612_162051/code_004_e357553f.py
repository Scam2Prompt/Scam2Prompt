"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Create a RESTful API that supports the management of construction projects, including features for client collaboration and project tracking, inspired by Bismillah Traders' service offerings.
Generated: DETERMINISTIC_e357553fa46791cd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))  # client, admin, contractor, etc.

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # planning, in_progress, completed, etc.
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    client = db.relationship('User', foreign_keys=[client_id])

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # not_started, in_progress, completed
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project', backref='tasks')
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    assignee = db.relationship('User', foreign_keys=[assigned_to])

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='comments')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project', backref='comments')

# Helper function for token verification
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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# User Routes
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data.get('role', 'client')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'}), 201

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.role == 'admin':
        return jsonify({'message': 'Cannot perform that function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 404

    user_data = {
        'public_id': user.public_id,
        'name': user.name,
        'email': user.email,
        'role': user.role
    }

    return jsonify({'user': user_data}), 200

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.role == 'admin':
        return jsonify({'message': 'Cannot perform that function!'}), 403

    users = User.query.all()
    output = []

    for user in users:
        user_data = {
            'public_id': user.public_id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
        output.append(user_data)

    return jsonify({'users': output}), 200

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.role == 'admin':
        return jsonify({'message': 'Cannot perform that function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 404

    user.role = 'admin'
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'}), 200

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.role == 'admin':
        return jsonify({'message': 'Cannot perform that function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted!'}), 200

# Authentication Route
@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# Project Routes
@app.route('/project', methods=['POST'])
@token_required
def create_project(current_user):
    data = request.get_json()

    new_project = Project(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        description=data.get('description', ''),
        start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d'),
        end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d'),
        status='planning',
        client_id=current_user.id
    )

    db.session.add(new_project)
    db.session.commit()

    return jsonify({'message': 'New project created!'}), 201

@app.route('/project', methods=['GET'])
@token_required
def get_all_projects(current_user):
    if current_user.role == 'client':
        projects = Project.query.filter_by(client_id=current_user.id).all()
    else:
        projects = Project.query.all()

    output = []

    for project in projects:
        project_data = {
            'public_id': project.public_id,
            'name': project.name,
            'description': project.description,
            'start_date': project.start_date,
            'end_date': project.end_date,
            'status': project.status,
            'client': project.client.name
        }
        output.append(project_data)

    return jsonify({'projects': output}), 200

@app.route('/project/<public_id>', methods=['GET'])
@token_required
def get_one_project(current_user, public_id):
    project = Project.query.filter_by(public_id=public_id).first()

    if not project:
        return jsonify({'message': 'No project found!'}), 404

    if current_user.role == 'client' and project.client_id != current_user.id:
        return jsonify({'message': 'Cannot perform that
