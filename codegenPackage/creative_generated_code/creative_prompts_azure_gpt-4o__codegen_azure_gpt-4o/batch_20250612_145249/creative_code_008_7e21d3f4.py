"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Design a REST API for managing heritage building restoration projects, including endpoints for tracking tuckpointing progress and material usage.
Generated: DETERMINISTIC_7e21d3f40b744f13
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data store for simplicity (replace with a database in production)
projects = {}

# Error handler to return JSON responses for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response

# Helper functions
def validate_project_data(data):
    required_fields = ["name", "location", "tuckpointing_progress", "materials_used"]
    for field in required_fields:
        if field not in data:
            return f"Field '{field}' is required."
    if not isinstance(data["tuckpointing_progress"], int) or not (0 <= data["tuckpointing_progress"] <= 100):
        return "'tuckpointing_progress' must be an integer between 0 and 100."
    if not isinstance(data["materials_used"], list):
        return "'materials_used' must be a list."
    return None

# Routes

@app.route("/projects", methods=["POST"])
def create_project():
    """
    Create a new heritage building restoration project.
    """
    data = request.json
    validation_error = validate_project_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    project_id = len(projects) + 1
    projects[project_id] = data
    return jsonify({"id": project_id, "message": "Project created successfully"}), 201


@app.route("/projects", methods=["GET"])
def list_projects():
    """
    List all heritage building restoration projects.
    """
    return jsonify({"projects": projects}), 200


@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    """
    Retrieve details of a specific project by ID.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"id": project_id, "project": project}), 200


@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    """
    Update an existing heritage building restoration project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    validation_error = validate_project_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    projects[project_id] = data
    return jsonify({"id": project_id, "message": "Project updated successfully"}), 200


@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    """
    Delete a heritage building restoration project by ID.
    """
    if project_id not in projects:
        return jsonify({"error": "Project not found"}), 404

    del projects[project_id]
    return jsonify({"id": project_id, "message": "Project deleted successfully"}), 200


@app.route("/projects/<int:project_id>/tuckpointing", methods=["PATCH"])
def update_tuckpointing_progress(project_id):
    """
    Update the tuckpointing progress for a specific project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    if "tuckpointing_progress" not in data:
        return jsonify({"error": "Field 'tuckpointing_progress' is required."}), 400
    if not isinstance(data["tuckpointing_progress"], int) or not (0 <= data["tuckpointing_progress"] <= 100):
        return jsonify({"error": "'tuckpointing_progress' must be an integer between 0 and 100."}), 400

    project["tuckpointing_progress"] = data["tuckpointing_progress"]
    return jsonify({"id": project_id, "message": "Tuckpointing progress updated successfully"}), 200


@app.route("/projects/<int:project_id>/materials", methods=["PATCH"])
def update_materials_used(project_id):
    """
    Update the materials used for a specific project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    if "materials_used" not in data:
        return jsonify({"error": "Field 'materials_used' is required."}), 400
    if not isinstance(data["materials_used"], list):
        return jsonify({"error": "'materials_used' must be a list."}), 400

    project["materials_used"] = data["materials_used"]
    return jsonify({"id": project_id, "message": "Materials used updated successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
```
