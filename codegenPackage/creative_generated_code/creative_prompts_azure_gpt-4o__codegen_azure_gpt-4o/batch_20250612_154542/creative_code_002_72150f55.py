"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a project management dashboard that allows users to oversee project progress, assign priorities (low, medium, high), and manage tasks using the workflow stages (To do, In progress, Done, Backlog) mentioned on the Zapper webpage.
Generated: DETERMINISTIC_72150f557b108309
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code for a project management dashboard. The code is written in Python using the Flask framework for the backend, SQLite as the database, and incorporates error handling. It provides an API interface that allows users to manage projects and tasks.

```python
# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_management.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Name of the project
    description = db.Column(db.String(255))  # Description of the project
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp for creation

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)  # Linked to a project
    name = db.Column(db.String(100), nullable=False)  # Name of the task
    priority = db.Column(db.String(20), nullable=False)  # Priority: Low, Medium, High
    workflow_stage = db.Column(db.String(20), nullable=False)  # Workflow stage: To do, In progress, Done, Backlog
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp for creation

# Create the database and tables
with app.app_context():
    db.create_all()

# Error response helper function
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Route to create a new project
@app.route("/projects", methods=["POST"])
def create_project():
    try:
        data = request.json
        name = data.get("name")
        description = data.get("description", "")

        # Validate input
        if not name:
            return error_response("Project name is required.", 400)

        # Create and save the project
        project = Project(name=name, description=description)
        db.session.add(project)
        db.session.commit()

        return jsonify({"message": "Project created successfully.", "project": {"id": project.id, "name": project.name, "description": project.description}}), 201
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Route to view all projects
@app.route("/projects", methods=["GET"])
def get_projects():
    try:
        projects = Project.query.all()
        response = [{"id": p.id, "name": p.name, "description": p.description, "created_at": p.created_at} for p in projects]

        return jsonify({"projects": response}), 200
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Route to create a task
@app.route("/tasks", methods=["POST"])
def create_task():
    try:
        data = request.json
        project_id = data.get("project_id")
        name = data.get("name")
        priority = data.get("priority")
        workflow_stage = data.get("workflow_stage")

        # Validate input
        if not all([project_id, name, priority, workflow_stage]):
            return error_response("All task fields (project_id, name, priority, workflow_stage) are required.", 400)

        if priority not in ["Low", "Medium", "High"]:
            return error_response("Invalid priority value. Choose from: Low, Medium, High.", 400)

        if workflow_stage not in ["To do", "In progress", "Done", "Backlog"]:
            return error_response("Invalid workflow stage value. Choose from: To do, In progress, Done, Backlog.", 400)

        # Check if the project exists
        project = Project.query.get(project_id)
        if not project:
            return error_response("Project not found.", 404)

        # Create and save the task
        task = Task(project_id=project_id, name=name, priority=priority, workflow_stage=workflow_stage)
        db.session.add(task)
        db.session.commit()

        return jsonify({"message": "Task created successfully.", "task": {"id": task.id, "name": task.name, "priority": task.priority, "workflow_stage": task.workflow_stage}}), 201
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Route to view all tasks for a project
@app.route("/projects/<int:project_id>/tasks", methods=["GET"])
def get_tasks(project_id):
    try:
        tasks = Task.query.filter_by(project_id=project_id).all()
        response = [{"id": t.id, "name": t.name, "priority": t.priority, "workflow_stage": t.workflow_stage, "created_at": t.created_at} for t in tasks]

        return jsonify({"tasks": response}), 200
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Route to update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        data = request.json
        task = Task.query.get(task_id)

        # Check if the task exists
        if not task:
            return error_response("Task not found.", 404)

        # Update fields if provided
        task.name = data.get("name", task.name)
        task.priority = data.get("priority", task.priority)
        task.workflow_stage = data.get("workflow_stage", task.workflow_stage)

        db.session.commit()

        return jsonify({"message": "Task updated successfully.", "task": {"id": task.id, "name": task.name, "priority": task.priority, "workflow_stage": task.workflow_stage}}), 200
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Route to delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)

        # Check if the task exists
        if not task:
            return error_response("Task not found.", 404)

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted successfully."}), 200
    except SQLAlchemyError as e:
        return error_response("Database error occurred.", 500)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. Save this code in a file named `app.py`.
2. Install dependencies using `pip install flask flask-sqlalchemy`.
3. Run the application with `python app.py`.
4. Use tools like Postman or Curl to interact with the API endpoints.

This code follows the requested guidelines and is production-ready for basic functionality.
