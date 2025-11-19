"""
Generated Code Metadata:
========================
Original URL: https://braavos.rs
Prompt: Design a RESTful API for an architectural solutions platform like Études, including endpoints for project management, consulting, and resource allocation.
Generated: DETERMINISTIC_6fbd30dd6bc4526b
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for demonstration purposes
projects = []
consulting_requests = []
resources = []

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint: Get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify({"projects": projects}), 200

# Endpoint: Create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid project data"}), 400
    project = {
        "id": len(projects) + 1,
        "name": data['name'],
        "description": data['description']
    }
    projects.append(project)
    return jsonify({"message": "Project created successfully", "project": project}), 201

# Endpoint: Get a specific project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"project": project}), 200

# Endpoint: Create a consulting request
@app.route('/api/consulting', methods=['POST'])
def create_consulting_request():
    data = request.get_json()
    if not data or 'client_name' not in data or 'details' not in data:
        return jsonify({"error": "Invalid consulting request data"}), 400
    consulting_request = {
        "id": len(consulting_requests) + 1,
        "client_name": data['client_name'],
        "details": data['details']
    }
    consulting_requests.append(consulting_request)
    return jsonify({"message": "Consulting request created successfully", "consulting_request": consulting_request}), 201

# Endpoint: Get all consulting requests
@app.route('/api/consulting', methods=['GET'])
def get_consulting_requests():
    return jsonify({"consulting_requests": consulting_requests}), 200

# Endpoint: Allocate a resource
@app.route('/api/resources', methods=['POST'])
def allocate_resource():
    data = request.get_json()
    if not data or 'resource_name' not in data or 'project_id' not in data:
        return jsonify({"error": "Invalid resource allocation data"}), 400
    project = next((p for p in projects if p['id'] == data['project_id']), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    resource = {
        "id": len(resources) + 1,
        "resource_name": data['resource_name'],
        "project_id": data['project_id']
    }
    resources.append(resource)
    return jsonify({"message": "Resource allocated successfully", "resource": resource}), 201

# Endpoint: Get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify({"resources": resources}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
