"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Design a RESTful API for integrating safety and health coordination services with other construction management systems, following AFCO's guidelines and French regulations.
Generated: DETERMINISTIC_c4d53ecb0c7dd4da
Batch ID: 20250622_205412
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

# Mock database for demonstration purposes
projects = [
    {
        "id": 1,
        "name": "Project A",
        "location": "Paris, France",
        "safety_coordinator": "John Doe",
        "health_guidelines": ["Wear helmets", "Use safety harnesses"]
    },
    {
        "id": 2,
        "name": "Project B",
        "location": "Lyon, France",
        "safety_coordinator": "Jane Smith",
        "health_guidelines": ["Regular health checks", "Provide first aid kits"]
    }
]

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

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API status.
    """
    return jsonify({"status": "API is running"}), 200

# Get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Retrieve all construction projects with safety and health coordination details.
    """
    return jsonify(projects), 200

# Get a specific project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve a specific project by its ID.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

# Create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    """
    Create a new construction project with safety and health coordination details.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "location", "safety_coordinator", "health_guidelines")):
        return jsonify({"error": "Invalid input"}), 400

    new_project = {
        "id": len(projects) + 1,
        "name": data["name"],
        "location": data["location"],
        "safety_coordinator": data["safety_coordinator"],
        "health_guidelines": data["health_guidelines"]
    }
    projects.append(new_project)
    return jsonify(new_project), 201

# Update an existing project
@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing construction project by its ID.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    project.update({
        "name": data.get("name", project["name"]),
        "location": data.get("location", project["location"]),
        "safety_coordinator": data.get("safety_coordinator", project["safety_coordinator"]),
        "health_guidelines": data.get("health_guidelines", project["health_guidelines"])
    })
    return jsonify(project), 200

# Delete a project
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a construction project by its ID.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    projects.remove(project)
    return jsonify({"message": "Project deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
