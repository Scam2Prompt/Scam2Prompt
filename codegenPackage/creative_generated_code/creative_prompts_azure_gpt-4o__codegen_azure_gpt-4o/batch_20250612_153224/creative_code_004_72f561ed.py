"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Suggest an API for managing green infrastructure projects, including plant selection and maintenance, as mentioned in the Ilmam Construction zelenih površin services.
Generated: DETERMINISTIC_72f561ed096dbe2c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: green_infrastructure_api.py

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data storage for projects
projects = []
project_id_counter = 1

# Error handler for API
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to create a new green infrastructure project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new green infrastructure project.
    Expected JSON format:
    {
        "name": "Project Name",
        "location": "Project Location",
        "plants": ["Plant1", "Plant2"],
        "maintenance_schedule": "Weekly"
    }
    """
    global project_id_counter
    try:
        data = request.json
        if not data or 'name' not in data or 'location' not in data or 'plants' not in data or 'maintenance_schedule' not in data:
            return jsonify({"error": "Invalid input data"}), 400

        project = {
            "id": project_id_counter,
            "name": data["name"],
            "location": data["location"],
            "plants": data["plants"],
            "maintenance_schedule": data["maintenance_schedule"]
        }
        projects.append(project)
        project_id_counter += 1
        return jsonify({"message": "Project created successfully", "project": project}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Retrieve all green infrastructure projects.
    """
    return jsonify(projects), 200

# Endpoint to get a single project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    """
    Retrieve a specific project by its ID.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return jsonify(project), 200
    return jsonify({"error": "Project not found"}), 404

# Endpoint to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing project.
    Expected JSON format:
    {
        "name": "Updated Project Name",
        "location": "Updated Project Location",
        "plants": ["Updated Plant1", "Updated Plant2"],
        "maintenance_schedule": "Updated Schedule"
    }
    """
    try:
        project = next((p for p in projects if p["id"] == project_id), None)
        if not project:
            return jsonify({"error": "Project not found"}), 404

        data = request.json
        if not data or 'name' not in data or 'location' not in data or 'plants' not in data or 'maintenance_schedule' not in data:
            return jsonify({"error": "Invalid input data"}), 400

        project.update({
            "name": data["name"],
            "location": data["location"],
            "plants": data["plants"],
            "maintenance_schedule": data["maintenance_schedule"]
        })
        return jsonify({"message": "Project updated successfully", "project": project}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a green infrastructure project by ID.
    """
    global projects
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    projects = [p for p in projects if p["id"] != project_id]
    return jsonify({"message": "Project deleted successfully"}), 200

# Run the Flask app (typically used in development only)
if __name__ == '__main__':
    app.run(debug=True)
```
