"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Suggest tools and write code snippets for managing team collaboration in system and software development projects, inspired by the oppomobile.id site.
Generated: DETERMINISTIC_c604ae31fa9a93af
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is production-ready code for managing team collaboration in system and software development projects. This example uses Python and Flask to build a simple collaborative API backend.

```python
# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database
projects = {}
tasks = {}

# Helper Functions
def generate_id():
    """Generate a unique identifier."""
    return str(uuid.uuid4())

# Routes for Project Management
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    Request data: { "name": "Project Name", "description": "Project Description" }
    Response: { "id": "project_id", "name": "Project Name", "description": "Project Description", "created_at": "timestamp" }
    """
    try:
        data = request.json
        project_id = generate_id()
        projects[project_id] = {
            "id": project_id,
            "name": data["name"],
            "description": data["description"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify(projects[project_id]), 201
    except KeyError:
        return jsonify({"error": "Invalid project data"}), 400

@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Get all projects.
    Response: List of all projects.
    """
    return jsonify(list(projects.values())), 200

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    Get a single project by ID.
    Response: Project details.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a project by ID.
    Response: Success message.
    """
    if project_id not in projects:
        return jsonify({"error": "Project not found"}), 404
    del projects[project_id]
    return jsonify({"message": "Project deleted successfully"}), 200

# Routes for Task Management
@app.route('/projects/<project_id>/tasks', methods=['POST'])
def create_task(project_id):
    """
    Create a task within a project.
    Request data: { "title": "Task Title", "description": "Task Description", "assigned_to": "User Name" }
    Response: Task details.
    """
    try:
        if project_id not in projects:
            return jsonify({"error": "Project not found"}), 404

        data = request.json
        task_id = generate_id()
        task = {
            "id": task_id,
            "title": data["title"],
            "description": data.get("description", ""),
            "assigned_to": data.get("assigned_to", ""),
            "status": "Pending",
            "created_at": datetime.now().isoformat(),
            "project_id": project_id
        }
        tasks[task_id] = task
        return jsonify(task), 201
    except KeyError:
        return jsonify({"error": "Invalid task data"}), 400

@app.route('/projects/<project_id>/tasks', methods=['GET'])
def get_tasks(project_id):
    """
    Get all tasks for a specific project.
    Response: List of tasks belonging to the project.
    """
    if project_id not in projects:
        return jsonify({"error": "Project not found"}), 404
    project_tasks = [task for task in tasks.values() if task["project_id"] == project_id]
    return jsonify(project_tasks), 200

@app.route('/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    """
    Update a task's status, description, or assigned user.
    Request data: { "status": "New Status", "description": "Updated Description", "assigned_to": "New User" }
    Response: Updated task details.
    """
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.json
    if "status" in data:
        task["status"] = data["status"]
    if "description" in data:
        task["description"] = data["description"]
    if "assigned_to" in data:
        task["assigned_to"] = data["assigned_to"]
    return jsonify(task), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a task by ID.
    Response: Success message.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    return jsonify({"message": "Task deleted successfully"}), 200

# Application Entry Point
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Install dependencies:
   ```
   pip install flask
   ```
2. Run the application:
   ```
   python app.py
   ```
This code provides endpoints to manage projects and tasks, with proper error handling and adherence to best practices. Each endpoint is designed to be clear and intuitive for team collaboration purposes.
