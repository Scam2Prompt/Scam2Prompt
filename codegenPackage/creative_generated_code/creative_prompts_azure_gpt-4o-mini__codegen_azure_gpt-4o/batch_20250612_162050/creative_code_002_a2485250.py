"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Create a sample application that allows users to collaborate on architectural designs, referencing the features of the Études Architect app.
Generated: DETERMINISTIC_a24852508de2e955
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a sample application for architectural design collaboration inspired by Études Architect. The sample demonstrates a basic implementation using Python and Flask for the backend, with SQLite for data persistence.

```python
# app.py - Main file for the architectural collaboration application

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configuration (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architect_collab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """
    Represents a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Project(db.Model):
    """
    Represents a collaborative architectural project.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('User', secondary='project_user', backref='projects')

class ProjectUser(db.Model):
    """
    Association table for many-to-many relationship between projects and users.
    """
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes

@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    """
    try:
        data = request.json
        username = data['username']
        email = data['email']

        if not username or not email:
            return jsonify({"error": "Username and email are required"}), 400

        # Check for duplicate email
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new architectural project.
    """
    try:
        data = request.json
        name = data['name']
        description = data.get('description', '')

        if not name:
            return jsonify({"error": "Project name is required"}), 400

        new_project = Project(name=name, description=description)
        db.session.add(new_project)
        db.session.commit()

        return jsonify({"message": "Project created successfully", "project": {"id": new_project.id, "name": new_project.name, "description": new_project.description}}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>/add_user', methods=['POST'])
def add_user_to_project(project_id):
    """
    Endpoint to add a user to a project.
    """
    try:
        data = request.json
        user_id = data['user_id']

        project = Project.query.get(project_id)
        user = User.query.get(user_id)

        if not project or not user:
            return jsonify({"error": "Project or user not found"}), 404

        # Check if user is already part of the project
        association = ProjectUser.query.filter_by(project_id=project_id, user_id=user_id).first()
        if association:
            return jsonify({"error": "User is already part of the project"}), 400

        new_association = ProjectUser(project_id=project_id, user_id=user_id)
        db.session.add(new_association)
        db.session.commit()

        return jsonify({"message": f"User '{user.username}' added to project '{project.name}'"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    Endpoint to fetch details of a specific project, including users working on it.
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404

        users = [{"id": user.id, "username": user.username, "email": user.email} for user in project.users]
        return jsonify({"project": {"id": project.id, "name": project.name, "description": project.description, "users": users}}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error Handling
@app.errorhandler(404)
def not_found(error):
    """
    Generic 404 error handler.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Generic 500 error handler.
    """
    return jsonify({"error": "Internal server error"}), 500

# Initialize the database
@app.before_first_request
def initialize_database():
    """
    Creates the database tables before the first request.
    """
    db.create_all()

# App Entry Point
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run:

1. Save the code to a file named `app.py`.
2. Install the dependencies:
   ```bash
   pip install flask flask_sqlalchemy
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Use a tool like Postman or curl to interact with the endpoints.

This is a basic implementation to get started with collaboration features. For production, you would want to add authentication, authorization, and more advanced features (e.g., real-time collaboration, file sharing, etc.).
