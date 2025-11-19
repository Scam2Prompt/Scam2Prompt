"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Create a REST API that allows users to submit and track environmental protection projects, similar to the initiatives by "Čuvari Šare" for preserving nature and rivers.
Generated: DETERMINISTIC_aa52bfa7638b8dd8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database to store projects
projects = {}

# Error messages
PROJECT_NOT_FOUND = {"error": "Project not found"}

# Helper function to validate project data
def validate_project_data(data):
    required_fields = ["name", "description", "location", "status"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new environmental protection project.
    Expects JSON payload with 'name', 'description', 'location', and 'status'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Validate project data
    is_valid, error_message = validate_project_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Create a new project
    project_id = str(uuid4())
    projects[project_id] = {
        "id": project_id,
        "name": data["name"],
        "description": data["description"],
        "location": data["location"],
        "status": data["status"]
    }

    return jsonify(projects[project_id]), 201

@app.route('/projects', methods=['GET'])
def list_projects():
    """
    Endpoint to list all environmental protection projects.
    """
    return jsonify(list(projects.values())), 200

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    Endpoint to retrieve a specific project by its ID.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify(PROJECT_NOT_FOUND), 404
    return jsonify(project), 200

@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Endpoint to update an existing project by its ID.
    Expects JSON payload with 'name', 'description', 'location', and/or 'status'.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify(PROJECT_NOT_FOUND), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Update project fields
    for key in ["name", "description", "location", "status"]:
        if key in data:
            project[key] = data[key]

    return jsonify(project), 200

@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Endpoint to delete a project by its ID.
    """
    if project_id not in projects:
        return jsonify(PROJECT_NOT_FOUND), 404

    del projects[project_id]
    return jsonify({"message": "Project deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
