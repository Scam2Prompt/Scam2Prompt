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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from enum import Enum

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Enum for roles
class Role(Enum):
    ADMIN = 'Admin'
    PROJECT_MANAGER = 'Project Manager'
    DEVELOPER = 'Developer'
    SUBMITTER = 'Submitter'

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)

# Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Helper function for role-based access control
def check_role(required_roles):
    def wrapper(func):
        @jwt_required()
        def decorated_function(*args, **kwargs):
            current_user = get_jwt_identity()
            user = User.query.filter_by(username=current_user).first()
            if user.role.name not in required_roles:
                return jsonify({"error": "Access forbidden"}), 403
            return func(*args, **kwargs)
        return decorated_function
    return wrapper

# Route to register users
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data['username']
        password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        role = data['role']

        if role not in [r.name for r in Role]:
            return jsonify({"error": "Invalid role"}), 400

        new_user = User(username=username, password=password, role=Role[role])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Route to login users
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Route to create a project (Admin and Project Manager only)
@app.route('/projects', methods=['POST'])
@check_role(['Admin', 'Project Manager'])
def create_project():
    data = request.json
    name = data['name']
    description = data.get('description', '')

    new_project = Project(name=name, description=description)
    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project created successfully"}), 201

# Route to assign a task (Project Manager only)
@app.route('/tasks/assign', methods=['POST'])
@check_role(['Project Manager'])
def assign_task():
    data = request.json
    title = data['title']
    assigned_to = data['assigned_to']
    project_id = data['project_id']

    user = User.query.get(assigned_to)
    project = Project.query.get(project_id)

    if not user or not project:
        return jsonify({"error": "Invalid user or project ID"}), 400

    new_task = Task(title=title, assigned_to=user.id, project_id=project.id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task assigned successfully"}), 201

# Route to update task progress (Developer only)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
@check_role(['Developer'])
def update_task(task_id):
    data = request.json
    status = data['status']

    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.status = status
    db.session.commit()

    return jsonify({"message": "Task updated successfully"}), 200

# Route to view tasks (accessible to all roles)
@app.route('/tasks', methods=['GET'])
@jwt_required()
def view_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "status": task.status,
                  "assigned_to": task.assigned_to, "project_id": task.project_id} for task in tasks]
    return jsonify(task_list), 200

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
