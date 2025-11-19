"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Recommend an API for managing construction projects that includes features for client communication and personalized service, similar to those offered by Fullteco Spa.
Generated: DETERMINISTIC_8a596f1953656ef2
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing Construction Projects
Features:
1. Client Communication
2. Personalized Service
"""

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database for simplicity (Use a proper DB like PostgreSQL in production)
projects = {}
clients = {}

# Error messages
ERROR_PROJECT_NOT_FOUND = "Project not found."
ERROR_CLIENT_NOT_FOUND = "Client not found."
ERROR_VALIDATION_FAILED = "Validation failed."

# Utility function for validation
def validate_request_data(required_fields, data):
    """
    Validates the incoming request data.
    :param required_fields: List of required fields.
    :param data: Incoming JSON data.
    :return: Tuple (bool, error_message)
    """
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required."
    return True, None

# Route: Create a new construction project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new construction project.
    """
    data = request.json
    required_fields = ["name", "client_id", "deadline", "details"]
    is_valid, error = validate_request_data(required_fields, data)
    if not is_valid:
        return jsonify({"error": ERROR_VALIDATION_FAILED, "details": error}), 400

    project_id = len(projects) + 1
    projects[project_id] = {
        "id": project_id,
        "name": data["name"],
        "client_id": data["client_id"],
        "deadline": data["deadline"],
        "details": data["details"]
    }
    logging.info("Created new project: %s", projects[project_id])
    return jsonify({"message": "Project created successfully.", "project": projects[project_id]}), 201

# Route: Get details of a specific project
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Get details of a specific construction project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": ERROR_PROJECT_NOT_FOUND}), 404
    return jsonify({"project": project}), 200

# Route: Update a construction project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing construction project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": ERROR_PROJECT_NOT_FOUND}), 404

    data = request.json
    project.update(data)
    logging.info("Updated project: %s", project)
    return jsonify({"message": "Project updated successfully.", "project": project}), 200

# Route: Delete a construction project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a construction project.
    """
    project = projects.pop(project_id, None)
    if not project:
        return jsonify({"error": ERROR_PROJECT_NOT_FOUND}), 404

    logging.info("Deleted project with ID: %d", project_id)
    return jsonify({"message": "Project deleted successfully."}), 200

# Route: Create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client.
    """
    data = request.json
    required_fields = ["name", "contact_info"]
    is_valid, error = validate_request_data(required_fields, data)
    if not is_valid:
        return jsonify({"error": ERROR_VALIDATION_FAILED, "details": error}), 400

    client_id = len(clients) + 1
    clients[client_id] = {
        "id": client_id,
        "name": data["name"],
        "contact_info": data["contact_info"]
    }
    logging.info("Created new client: %s", clients[client_id])
    return jsonify({"message": "Client created successfully.", "client": clients[client_id]}), 201

# Route: Send communication to a client
@app.route('/clients/<int:client_id>/send_message', methods=['POST'])
def send_message(client_id):
    """
    Send a communication/message to a specific client.
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": ERROR_CLIENT_NOT_FOUND}), 404

    data = request.json
    required_fields = ["message"]
    is_valid, error = validate_request_data(required_fields, data)
    if not is_valid:
        return jsonify({"error": ERROR_VALIDATION_FAILED, "details": error}), 400

    # Simulate sending a message (In production, integrate with an email/SMS service)
    logging.info("Sent message to client %d: %s", client_id, data["message"])
    return jsonify({"message": "Message sent successfully.", "client": client}), 200

# Route: Get all clients
@app.route('/clients', methods=['GET'])
def get_all_clients():
    """
    Get a list of all clients.
    """
    return jsonify({"clients": list(clients.values())}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
