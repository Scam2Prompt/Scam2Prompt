"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Create an API endpoint for a construction company that manages geodetic work, similar to the services provided by URANPRES in Slovakia.
Generated: DETERMINISTIC_6fc8fc01e66c611f
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
projects = []

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

# API endpoint to create a new geodetic project
@app.route('/api/projects', methods=['POST'])
def create_project():
    """
    Create a new geodetic project.
    Expected JSON payload:
    {
        "name": "Project Name",
        "location": "Project Location",
        "description": "Project Description"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Invalid JSON payload"}), 400

        # Validate required fields
        name = data.get('name')
        location = data.get('location')
        description = data.get('description')

        if not name or not location or not description:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        # Create a new project
        project_id = len(projects) + 1
        new_project = {
            "id": project_id,
            "name": name,
            "location": location,
            "description": description
        }
        projects.append(new_project)

        return jsonify({"message": "Project created successfully", "project": new_project}), 201
    except Exception as e:
        return handle_exception(e)

# API endpoint to retrieve all geodetic projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Retrieve all geodetic projects.
    """
    return jsonify({"projects": projects}), 200

# API endpoint to retrieve a specific geodetic project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve a specific geodetic project by ID.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404
    return jsonify({"project": project}), 200

# API endpoint to update a specific geodetic project by ID
@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update a specific geodetic project by ID.
    Expected JSON payload:
    {
        "name": "Updated Project Name",
        "location": "Updated Project Location",
        "description": "Updated Project Description"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Invalid JSON payload"}), 400

        project = next((p for p in projects if p['id'] == project_id), None)
        if not project:
            return jsonify({"error": "Not Found", "message": "Project not found"}), 404

        # Update project fields
        project['name'] = data.get('name', project['name'])
        project['location'] = data.get('location', project['location'])
        project['description'] = data.get('description', project['description'])

        return jsonify({"message": "Project updated successfully", "project": project}), 200
    except Exception as e:
        return handle_exception(e)

# API endpoint to delete a specific geodetic project by ID
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a specific geodetic project by ID.
    """
    global projects
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404

    projects = [p for p in projects if p['id'] != project_id]
    return jsonify({"message": "Project deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
