"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Build a task tracker API that supports role-based access control (Admin, Project Manager, Developer, Submitter) and allows for project creation, task assignment, and progress tracking as specified on the Zapper platform.
Generated: DETERMINISTIC_4dad0a1d30315a90
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, jwt_optional, get_jwt_identity

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Define User roles
ROLES = ['Admin', 'Project Manager', 'Developer', 'Submitter']

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    status = db.Column(db.String(20), default='Not Started')

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'role' not in data:
        abort(400, 'Username and role are required')

    if data['role'] not in ROLES:
        abort(400, 'Invalid role')

    new_user = User(username=data['username'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': 'User created successfully'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user:
        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        return jsonify(access_token=access_token), 200
    else:
        abort(401, 'Invalid credentials')

# Project creation route
@app.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    current_user = get_jwt_identity()
    if current_user['role'] not in ['Admin', 'Project Manager']:
        abort(403, 'Permission denied')

    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, 'Project name is required')

    new_project = Project(name=data['name'])
    db.session.add(new_project)
    db.session.commit()

    return jsonify({'msg': 'Project created successfully'}), 201

# Task assignment route
@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    current_user = get_jwt_identity()
    if current_user['role'] not in ['Admin', 'Project Manager', 'Developer']:
        abort(403, 'Permission denied')

    data = request.get_json()
    if not data or 'title' not in data or 'project_id' not in data:
        abort(400, 'Title and project ID are required')

    new_task = Task(title=data['title'], description=data.get('description'), project_id=data['project_id'])
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'msg': 'Task created successfully'}), 201

# Update task status route
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
@jwt_required()
def update_task(task_id):
    current_user = get_jwt_identity()
    if current_user['role'] not in ['Admin', 'Project Manager', 'Developer']:
        abort(403, 'Permission denied')

    task = Task.query.get(task_id)
    if not task:
        abort(404, 'Task not found')

    data = request.get_json()
    if 'status' in data:
        task.status = data['status']

    db.session.commit()
    return jsonify({'msg': 'Task updated successfully'}), 200

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
```
