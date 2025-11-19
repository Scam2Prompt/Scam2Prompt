"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Create a RESTful API that supports the management of construction projects, including features for client collaboration and project tracking, inspired by Bismillah Traders' service offerings.
Generated: DETERMINISTIC_e357553fa46791cd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
projects = []
clients = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Fetch all construction projects.
    """
    return jsonify({"projects": projects}), 200

# Route: Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new construction project.
    """
    data = request.json
    if not data or 'name' not in data or 'client_id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project = {
        "id": len(projects) + 1,
        "name": data['name'],
        "client_id": data['client_id'],
        "status": "Pending"
    }
    projects.append(project)
    return jsonify({"message": "Project created successfully", "project": project}), 201

# Route: Update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing construction project.
    """
    data = request.json
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    if 'name' in data:
        project['name'] = data['name']
    if 'status' in data:
        project['status'] = data['status']

    return jsonify({"message": "Project updated successfully", "project": project}), 200

# Route: Delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a construction project.
    """
    global projects
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    projects = [p for p in projects if p['id'] != project_id]
    return jsonify({"message": "Project deleted successfully"}), 200

# Route: Get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    """
    Fetch all clients.
    """
    return jsonify({"clients": clients}), 200

# Route: Create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client.
    """
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    client = {
        "id": len(clients) + 1,
        "name": data['name'],
        "email": data['email']
    }
    clients.append(client)
    return jsonify({"message": "Client created successfully", "client": client}), 201

# Route: Update a client
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """
    Update an existing client.
    """
    data = request.json
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    if 'name' in data:
        client['name'] = data['name']
    if 'email' in data:
        client['email'] = data['email']

    return jsonify({"message": "Client updated successfully", "client": client}), 200

# Route: Delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Delete a client.
    """
    global clients
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    clients = [c for c in clients if c['id'] != client_id]
    return jsonify({"message": "Client deleted successfully"}), 200

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return jsonify({"status": "API is running"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
