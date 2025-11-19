"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Recommend APIs or libraries for implementing a Scrum Master project management tool, as described in PDMA's Scrum Master certification course.
Generated: DETERMINISTIC_7420010cf48389d1
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Scrum Master Project Management Tool

Below is an example implementation in Python, utilizing the Flask web framework and SQLite database.

```python
# app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'scrum.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='developer')

    def __repr__(self):
        return f"User('{self.username}', '{self.role}')"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Project(db.Model):
    """Project model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sprint_goal = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(80), nullable=False, default='backlog')

    def __repr__(self):
        return f"Project('{self.name}', '{self.state}')"


class Task(db.Model):
    """Task model"""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('tasks', lazy=True))
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(80), nullable=False, default='to-do')
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    assignee = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f"Task('{self.name}', '{self.state}')"


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        user = User(username=data['username'], role=data['role'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'Logged in successfully'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    try:
        if request.method == 'GET':
            projects = Project.query.all()
            return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'sprint_goal': p.sprint_goal, 'state': p.state} for p in projects]), 200
        elif request.method == 'POST':
            data = request.json
            project = Project(name=data['name'], description=data['description'], sprint_goal=data['sprint_goal'])
            db.session.add(project)
            db.session.commit()
            return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    try:
        if request.method == 'GET':
            tasks = Task.query.all()
            return jsonify([{'id': t.id, 'name': t.name, 'description': t.description, 'state': t.state, 'project_id': t.project_id, 'assignee_id': t.assignee_id} for t in tasks]), 200
        elif request.method == 'POST':
            data = request.json
            task = Task(name=data['name'], description=data['description'], project_id=data['project_id'])
            db.session.add(task)
            db.session.commit()
            return jsonify({'message': 'Task created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Requirements

* Python 3.8+
* Flask
* Flask-SQLAlchemy

### Installation

```bash
pip install flask flask-sqlalchemy
```

### Usage

1. Run the application: `python app.py`
2. Use a tool like `curl` or Postman to interact with the API endpoints.

### API Documentation

* `POST /register`: Create a new user
* `POST /login`: Login to the application
* `GET /projects`: Get all projects
* `POST /projects`: Create a new project
* `GET /tasks`: Get all tasks
* `POST /tasks`: Create a new task

### Notes

* This is a basic implementation and may require additional features and security measures for production use.
* This example uses a SQLite database, but you may want to consider using a more robust database solution for production.
* You should consider implementing authentication and authorization for API endpoints.
