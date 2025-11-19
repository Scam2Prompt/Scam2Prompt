"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: How can I implement a project management API to streamline communication and collaboration in a construction project, similar to the services offered by Bismillah Traders?
Generated: DETERMINISTIC_912da78a7ab0bc28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean and well-documented implementation of a project management API using Python and Flask. It includes basic functionality such as managing projects, tasks, and team members. For production readiness, it includes error handling, input validation, and follows Python best practices.

```python
from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

# In-memory database simulation
projects = {}  # Structure: {project_id: {"name": str, "description": str, "tasks": [], "team_members": []}}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid4())

# Error handling: Custom error response
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify({"projects": list(projects.values())}), 200

# Route: Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        if not data or "name" not in data or "description" not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        project_id = generate_id()
        projects[project_id] = {
            "id": project_id,
            "name": data["name"],
            "description": data["description"],
            "tasks": [],
            "team_members": []
        }
        return jsonify({"message": "Project created", "project": projects[project_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get a single project by ID
@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"project": project}), 200

# Route: Add a task to a project
@app.route('/projects/<project_id>/tasks', methods=['POST'])
def add_task_to_project(project_id):
    try:
        project = projects.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        data = request.json
        if not data or "title" not in data or "description" not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        task_id = generate_id()
        task = {
            "id": task_id,
            "title": data["title"],
            "description": data["description"],
            "completed": False
        }
        project["tasks"].append(task)
        return jsonify({"message": "Task added", "task": task}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update a task in a project
@app.route('/projects/<project_id>/tasks/<task_id>', methods=['PUT'])
def update_task_in_project(project_id, task_id):
    try:
        project = projects.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        task = next((t for t in project["tasks"] if t["id"] == task_id), None)
        if not task:
            return jsonify({"error": "Task not found"}), 404

        data = request.json
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        task["title"] = data.get("title", task["title"])
        task["description"] = data.get("description", task["description"])
        task["completed"] = data.get("completed", task["completed"])
        return jsonify({"message": "Task updated", "task": task}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a team member to a project
@app.route('/projects/<project_id>/team', methods=['POST'])
def add_team_member_to_project(project_id):
    try:
        project = projects.get(project_id)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        data = request.json
        if not data or "name" not in data or "role" not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        team_member_id = generate_id()
        team_member = {
            "id": team_member_id,
            "name": data["name"],
            "role": data["role"]
        }
        project["team_members"].append(team_member)
        return jsonify({"message": "Team member added", "team_member": team_member}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a project
@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = projects.pop(project_id, None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"message": "Project deleted"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

This code is a solid foundation for a project management API tailored to construction project workflows. It can be extended further with authentication, integration with external services, and deployment-ready configurations.
