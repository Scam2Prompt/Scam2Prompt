"""
Generated Code Metadata:
========================
Original URL: https://parrotrans.com
Prompt: Create a RESTful API for managing translation projects, including endpoints for client registration, project submission, and translator assignment, inspired by Parrotrans' B2B service model.
Generated: DETERMINISTIC_f545e5499427cb6b
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
from uuid import uuid4

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
clients = {}
projects = {}
translators = {}

# Error messages
CLIENT_NOT_FOUND = "Client not found."
PROJECT_NOT_FOUND = "Project not found."
TRANSLATOR_NOT_FOUND = "Translator not found."

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# Endpoint: Register a new client
@app.route('/clients', methods=['POST'])
def register_client():
    try:
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid client data."}), 400
        
        client_id = generate_id()
        clients[client_id] = {
            "id": client_id,
            "name": data['name'],
            "email": data['email']
        }
        return jsonify(clients[client_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Submit a new translation project
@app.route('/projects', methods=['POST'])
def submit_project():
    try:
        data = request.json
        if not data or 'client_id' not in data or 'title' not in data or 'description' not in data:
            return jsonify({"error": "Invalid project data."}), 400
        
        client_id = data['client_id']
        if client_id not in clients:
            return jsonify({"error": CLIENT_NOT_FOUND}), 404
        
        project_id = generate_id()
        projects[project_id] = {
            "id": project_id,
            "client_id": client_id,
            "title": data['title'],
            "description": data['description'],
            "translator_id": None,
            "status": "Pending"
        }
        return jsonify(projects[project_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Assign a translator to a project
@app.route('/projects/<project_id>/assign', methods=['POST'])
def assign_translator(project_id):
    try:
        data = request.json
        if not data or 'translator_id' not in data:
            return jsonify({"error": "Invalid assignment data."}), 400
        
        if project_id not in projects:
            return jsonify({"error": PROJECT_NOT_FOUND}), 404
        
        translator_id = data['translator_id']
        if translator_id not in translators:
            return jsonify({"error": TRANSLATOR_NOT_FOUND}), 404
        
        projects[project_id]['translator_id'] = translator_id
        projects[project_id]['status'] = "Assigned"
        return jsonify(projects[project_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Register a new translator
@app.route('/translators', methods=['POST'])
def register_translator():
    try:
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid translator data."}), 400
        
        translator_id = generate_id()
        translators[translator_id] = {
            "id": translator_id,
            "name": data['name'],
            "email": data['email']
        }
        return jsonify(translators[translator_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(list(clients.values())), 200

# Endpoint: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(list(projects.values())), 200

# Endpoint: Get all translators
@app.route('/translators', methods=['GET'])
def get_translators():
    return jsonify(list(translators.values())), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
