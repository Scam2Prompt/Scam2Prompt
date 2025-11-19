"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Create a RESTful API for a project management consultancy (PMC) service, similar to The Design Umbrella's PMC offering, with endpoints for project discovery, design, development, and delivery."
Generated: DETERMINISTIC_cd116c64a8753165
Batch ID: 20250622_210655
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

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint: Project Discovery
@app.route('/api/projects/discovery', methods=['POST'])
def project_discovery():
    """
    Handles project discovery phase.
    Expects JSON payload with 'name' and 'description'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project = {
        "id": len(projects) + 1,
        "name": data['name'],
        "description": data['description'],
        "phase": "discovery"
    }
    projects.append(project)
    return jsonify({"message": "Project discovery initiated", "project": project}), 201

# Endpoint: Project Design
@app.route('/api/projects/<int:project_id>/design', methods=['PUT'])
def project_design(project_id):
    """
    Handles project design phase.
    Expects JSON payload with 'design_details'.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    if not data or 'design_details' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project['phase'] = "design"
    project['design_details'] = data['design_details']
    return jsonify({"message": "Project design updated", "project": project}), 200

# Endpoint: Project Development
@app.route('/api/projects/<int:project_id>/development', methods=['PUT'])
def project_development(project_id):
    """
    Handles project development phase.
    Expects JSON payload with 'development_details'.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    if not data or 'development_details' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project['phase'] = "development"
    project['development_details'] = data['development_details']
    return jsonify({"message": "Project development updated", "project": project}), 200

# Endpoint: Project Delivery
@app.route('/api/projects/<int:project_id>/delivery', methods=['PUT'])
def project_delivery(project_id):
    """
    Handles project delivery phase.
    Expects JSON payload with 'delivery_details'.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    if not data or 'delivery_details' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project['phase'] = "delivery"
    project['delivery_details'] = data['delivery_details']
    return jsonify({"message": "Project delivery completed", "project": project}), 200

# Endpoint: Get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Retrieves all projects.
    """
    return jsonify({"projects": projects}), 200

# Endpoint: Get a specific project
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieves a specific project by ID.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    return jsonify({"project": project}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
