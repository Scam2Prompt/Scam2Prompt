"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Generate a REST API specification for a consulting service that manages architectural projects, inspired by the consulting services offered by TWM Associates.
Generated: DETERMINISTIC_ba3315165fcc5375
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
import uuid

app = Flask(__name__)

# In-memory storage (simulates a database for demonstration purposes)
projects = {}

# Helper function: Generate a unique identifier for projects
def generate_project_id():
    return str(uuid.uuid4())

# API Endpoints

@app.route('/projects', methods=['GET'])
def get_all_projects():
    """
    GET /projects
    Retrieve all architectural projects.
    """
    return jsonify(list(projects.values())), 200


@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    GET /projects/<project_id>
    Retrieve a single project by its unique ID.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(project), 200


@app.route('/projects', methods=['POST'])
def create_project():
    """
    POST /projects
    Create a new architectural project.
    Request JSON format:
    {
        "name": "Project Name",
        "description": "Project Description",
        "client_name": "Client Name"
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'name' not in data or 'description' not in data or 'client_name' not in data:
        return jsonify({'error': 'Invalid input. Name, description, and client_name are required.'}), 400

    # Create and store the new project
    project_id = generate_project_id()
    project = {
        'id': project_id,
        'name': data['name'],
        'description': data['description'],
        'client_name': data['client_name']
    }
    projects[project_id] = project

    return jsonify(project), 201


@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    """
    PUT /projects/<project_id>
    Update an existing project.
    Request JSON format:
    {
        "name": "Updated Project Name",
        "description": "Updated Project Description",
        "client_name": "Updated Client Name"
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'name' not in data or 'description' not in data or 'client_name' not in data:
        return jsonify({'error': 'Invalid input. Name, description, and client_name are required.'}), 400

    # Check if project exists
    project = projects.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404

    # Update the project
    project.update({
        'name': data['name'],
        'description': data['description'],
        'client_name': data['client_name']
    })
    return jsonify(project), 200


@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    DELETE /projects/<project_id>
    Delete a project by its unique ID.
    """
    project = projects.pop(project_id, None)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify({'message': 'Project deleted successfully'}), 200


# Error handling for unexpected server errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server Error.
    """
    return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
