"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Generate a code snippet for a project management app that integrates architectural solutions and allows collaboration among architects.
Generated: DETERMINISTIC_448df0c69e840e3b
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management_app.py

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
projects = []  # List of projects
users = []  # List of users (architects)

# Helper function to find a project by ID
def find_project(project_id):
    for project in projects:
        if project["id"] == project_id:
            return project
    return None

# Helper function to find a user by ID
def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="An unexpected error occurred"), 500

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        if not data.get("name"):
            return jsonify(error="Project name is required"), 400
        new_project = {
            "id": len(projects) + 1,
            "name": data["name"],
            "description": data.get("description", ""),
            "collaborators": []  # List of user IDs
        }
        projects.append(new_project)
        return jsonify(new_project), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

# Route to add a collaborator to a project
@app.route('/projects/<int:project_id>/collaborators', methods=['POST'])
def add_collaborator(project_id):
    try:
        data = request.json
        user_id = data.get("user_id")
        if not user_id:
            return jsonify(error="User ID is required"), 400
        project = find_project(project_id)
        if not project:
            return jsonify(error="Project not found"), 404
        if user_id not in project["collaborators"]:
            user = find_user(user_id)
            if not user:
                return jsonify(error="User not found"), 404
            project["collaborators"].append(user_id)
        return jsonify(project), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

# Route to list all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    return jsonify(projects), 200

# Route to create a new user (architect)
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        if not data.get("name"):
            return jsonify(error="User name is required"), 400
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "email": data.get("email", ""),
        }
        users.append(new_user)
        return jsonify(new_user), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

# Route to list all users (architects)
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

This code snippet implements a basic project management app using the Flask web framework. It allows for creating projects, adding collaborators (architects), and managing users. Each route includes proper error handling and follows best practices for clean and maintainable code.
