"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Recommend APIs or libraries for creating a construction project management tool, considering factors like scalability, user interface, and integration with other tools, similar to SSTCO's project management needs.
Generated: DETERMINISTIC_090e1c0a0e46d3ec
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize the database and marshmallow instances
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    projects = db.relationship('Project', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __init__(self, name, description, project_id):
        self.name = name
        self.description = description
        self.project_id = project_id

# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Define the Project schema
class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

# Define the Task schema
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        user = User(data['username'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Login a user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        token = request.headers['Authorization'].split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        data = request.json
        project = Project(data['name'], data['description'], user.id)
        db.session.add(project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get all projects for a user
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        token = request.headers['Authorization'].split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        projects = Project.query.filter_by(user_id=user.id).all()
        project_schema = ProjectSchema(many=True)
        return jsonify(project_schema.dump(projects)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        token = request.headers['Authorization'].split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        data = request.json
        project = Project.query.get(data['project_id'])
        if project and project.user_id == user.id:
            task = Task(data['name'], data['description'], project.id)
            db.session.add(task)
            db.session.commit()
            return jsonify({'message': 'Task created successfully'}), 201
        else:
            return jsonify({'message': 'Project not found or not authorized'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
