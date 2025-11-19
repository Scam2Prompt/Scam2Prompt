"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Create a RESTful API endpoint for a construction management system that handles data related to mining and road construction projects.
Generated: DETERMINISTIC_6676918e0818a1f1
Batch ID: 20250612_155223
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

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Retrieve all projects.
    """
    return jsonify(projects), 200

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['name', 'type', 'start_date', 'end_date']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Bad Request", "message": f"Missing required field: {field}"}), 400

        # Validate project type
        if data['type'] not in ['mining', 'road_construction']:
            return jsonify({"error": "Bad Request", "message": "Invalid project type. Must be 'mining' or 'road_construction'"}), 400

        # Create project object
        project = {
            "id": len(projects) + 1,
            "name": data['name'],
            "type": data['type'],
            "start_date": data['start_date'],
            "end_date": data['end_date'],
            "description": data.get('description', '')  # Optional field
        }

        # Add project to the database
        projects.append(project)
        return jsonify(project), 201

    except Exception as e:
        return handle_general_exception(e)

# Endpoint to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve a specific project by ID.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Not Found", "message": "Project not found"}), 404
    return jsonify(project), 200

# Endpoint to update a specific project by ID
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update a specific project by ID.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        project = next((p for p in projects if p['id'] == project_id), None)
        if not project:
            return jsonify({"error": "Not Found", "message": "Project not found"}), 404

        # Update project fields
        project['name'] = data.get('name', project['name'])
        project['type'] = data.get('type', project['type'])
        project['start_date'] = data.get('start_date', project['start_date'])
        project['end_date'] = data.get('end_date', project['end_date'])
        project['description'] = data.get('description', project['description'])

        return jsonify(project), 200

    except Exception as e:
        return handle_general_exception(e)

# Endpoint to delete a specific project by ID
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a specific project by ID.
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
