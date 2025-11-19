"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Generate code for a task tracker system that includes features for project management, user account creation, and role assignment as described on the Zapper webpage.
Generated: DETERMINISTIC_70c900edd3107f86
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Task Tracker System with Project Management, User Account Creation, and Role Assignment.

Framework: Flask (Python)
Database: SQLite (SQLAlchemy ORM)
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and configure database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'admin', 'member'

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the password matches the hash."""
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    tasks = db.relationship("Task", backref="project", lazy=True)

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'in_progress', 'completed'
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)

# Routes
@app.route("/register", methods=["POST"])
def register_user():
    """
    Endpoint for user registration.
    Expects a JSON payload: { "username": "string", "password": "string", "role": "string" }
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    # Input validation
    if not username or not password or not role:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    # Register new user
    new_user = User(username=username, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/projects", methods=["POST"])
def create_project():
    """
    Endpoint for creating a new project.
    Expects a JSON payload: { "name": "string", "description": "string" }
    """
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    # Input validation
    if not name:
        return jsonify({"error": "Project name is required"}), 400

    # Check if project name already exists
    if Project.query.filter_by(name=name).first():
        return jsonify({"error": "Project with this name already exists"}), 400

    # Create new project
    new_project = Project(name=name, description=description)
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Project created successfully"}), 201

@app.route("/projects/<int:project_id>/tasks", methods=["POST"])
def create_task(project_id):
    """
    Endpoint for creating a task within a project.
    Expects a JSON payload: { "name": "string", "status": "string" }
    """
    data = request.get_json()
    name = data.get("name")
    status = data.get("status")

    # Input validation
    if not name or not status:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if project exists
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Create new task
    new_task = Task(name=name, status=status, project_id=project_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201

@app.route("/projects/<int:project_id>/tasks", methods=["GET"])
def list_tasks(project_id):
    """
    Endpoint for retrieving all tasks within a project.
    """
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    tasks = Task.query.filter_by(project_id=project_id).all()
    tasks_data = [
        {"id": task.id, "name": task.name, "status": task.status} for task in tasks
    ]
    return jsonify({"tasks": tasks_data}), 200

@app.route("/users", methods=["GET"])
def list_users():
    """
    Endpoint for retrieving all users.
    """
    users = User.query.all()
    users_data = [{"id": user.id, "username": user.username, "role": user.role} for user in users]
    return jsonify({"users": users_data}), 200

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    """Handles 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handles 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == "__main__":
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```
