"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: How can I implement a project oversight feature in a task management application that tracks progress and manages team roles, similar to the Zapper platform?
Generated: DETERMINISTIC_e943c03c4219b056
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready implementation of a project oversight feature in a task management application. It is written in Python using Flask as a web framework and SQLAlchemy for database management.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    """Model for team members."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Roles: 'Manager', 'Developer', 'Tester', etc.

class Project(db.Model):
    """Model for projects."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    progress = db.Column(db.Float, nullable=False, default=0.0)  # Progress in percentage

class Task(db.Model):
    """Model for tasks within a project."""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')  # Status: 'Pending', 'In Progress', 'Completed'

# Error Handling
@app.errorhandler(404)
def resource_not_found(e):
    """Handle 404 errors."""
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle server errors."""
    return jsonify(error="Internal server error"), 500

# Routes
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    try:
        data = request.json
        new_project = Project(name=data['name'], description=data.get('description', ''))
        db.session.add(new_project)
        db.session.commit()
        return jsonify(message="Project created successfully", project_id=new_project.id), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error="Failed to create project", details=str(e)), 400

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve details of a specific project."""
    project = Project.query.get(project_id)
    if not project:
        return jsonify(error="Project not found"), 404
    tasks = Task.query.filter_by(project_id=project_id).all()
    task_details = [{
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "assigned_to": User.query.get(task.assigned_to).name
    } for task in tasks]
    return jsonify(
        id=project.id,
        name=project.name,
        description=project.description,
        progress=project.progress,
        tasks=task_details
    ), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task within a project."""
    try:
        data = request.json
        assigned_user = User.query.get(data['assigned_to'])
        project = Project.query.get(data['project_id'])
        if not assigned_user or not project:
            return jsonify(error="Invalid user or project ID"), 400
        new_task = Task(
            project_id=data['project_id'],
            assigned_to=data['assigned_to'],
            description=data['description']
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(message="Task created successfully", task_id=new_task.id), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error="Failed to create task", details=str(e)), 400

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update the status or description of a task."""
    task = Task.query.get(task_id)
    if not task:
        return jsonify(error="Task not found"), 404
    try:
        data = request.json
        if 'status' in data:
            task.status = data['status']
        if 'description' in data:
            task.description = data['description']
        db.session.commit()
        return jsonify(message="Task updated successfully"), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error="Failed to update task", details=str(e)), 400

@app.route('/projects/<int:project_id>/progress', methods=['GET'])
def calculate_progress(project_id):
    """Calculate and return the overall progress of a project."""
    project = Project.query.get(project_id)
    if not project:
        return jsonify(error="Project not found"), 404
    tasks = Task.query.filter_by(project_id=project_id).all()
    if not tasks:
        return jsonify(progress=0.0), 200
    completed_tasks = sum(1 for task in tasks if task.status == 'Completed')
    progress = (completed_tasks / len(tasks)) * 100
    project.progress = progress
    db.session.commit()
    return jsonify(progress=progress), 200

@app.route('/users', methods=['POST'])
def create_user():
    """Add a new team member."""
    try:
        data = request.json
        new_user = User(name=data['name'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User created successfully", user_id=new_user.id), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error="Failed to create user", details=str(e)), 400

# Initialize database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

Save this code into a file (e.g., `app.py`), and run it using `python app.py`. Ensure that you have Flask and SQLAlchemy installed (`pip install flask flask-sqlalchemy`). This code provides a clean implementation of the requested feature, including error handling, database setup, and RESTful routes for managing projects, tasks, and users.
