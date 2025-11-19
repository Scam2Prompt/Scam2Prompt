"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Generate a code snippet for a web application that tracks the progress of public sector projects, inspired by Licitare's project management methodologies.
Generated: DETERMINISTIC_46364e99e97002c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store project data
projects = {}

# Helper function to validate project data
def validate_project_data(data):
    required_fields = ['name', 'description', 'start_date', 'end_date', 'status']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.strptime(data['start_date'], '%Y-%m-%d')
        datetime.strptime(data['end_date'], '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."
    return True, None

@app.route('/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new project.
    Expects JSON payload with: name, description, start_date, end_date, status.
    """
    data = request.json
    is_valid, error_msg = validate_project_data(data)
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    project_id = str(uuid.uuid4())
    projects[project_id] = {
        "id": project_id,
        "name": data['name'],
        "description": data['description'],
        "start_date": data['start_date'],
        "end_date": data['end_date'],
        "status": data['status'],
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    return jsonify(projects[project_id]), 201

@app.route('/projects', methods=['GET'])
def list_projects():
    """
    Endpoint to list all projects.
    Returns a JSON array of all stored projects.
    """
    return jsonify(list(projects.values())), 200

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    Endpoint to retrieve a single project by its ID.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Endpoint to update an existing project.
    Expects JSON payload with: name, description, start_date, end_date, status.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    is_valid, error_msg = validate_project_data(data)
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    project.update({
        "name": data['name'],
        "description": data['description'],
        "start_date": data['start_date'],
        "end_date": data['end_date'],
        "status": data['status'],
        "updated_at": datetime.utcnow().isoformat()
    })

    return jsonify(project), 200

@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Endpoint to delete a project by its ID.
    """
    project = projects.pop(project_id, None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"message": "Project deleted successfully"}), 200

# Error handler for JSON parsing errors
@app.errorhandler(400)
def bad_request_error(error):
    """
    Handles JSON parsing errors or invalid request payloads.
    """
    return jsonify({"error": "Bad request. Please check your input."}), 400

# Error handler for unexpected internal server errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles unexpected server errors.
    """
    return jsonify({"error": "Internal server error. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
