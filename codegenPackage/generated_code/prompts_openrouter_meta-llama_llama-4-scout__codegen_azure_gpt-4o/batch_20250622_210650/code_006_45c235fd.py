"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Develop a RESTful API to manage construction projects, including endpoints for creating, reading, updating, and deleting projects, inspired by SSTCO's project management requirements.
Generated: DETERMINISTIC_45c235fd53fa2e6b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
projects = {}
project_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    global project_id_counter
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Create new project
    project_id = project_id_counter
    projects[project_id] = {
        "id": project_id,
        "name": data['name'],
        "description": data['description']
    }
    project_id_counter += 1

    return jsonify(projects[project_id]), 201

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(list(projects.values())), 200

# Endpoint to get a single project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404
    return jsonify(project), 200

# Endpoint to update a project by ID
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    project = projects.get(project_id)

    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404

    # Validate input
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Update project
    project['name'] = data['name']
    project['description'] = data['description']
    return jsonify(project), 200

# Endpoint to delete a project by ID
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = projects.pop(project_id, None)
    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404
    return jsonify({"message": "Project deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
