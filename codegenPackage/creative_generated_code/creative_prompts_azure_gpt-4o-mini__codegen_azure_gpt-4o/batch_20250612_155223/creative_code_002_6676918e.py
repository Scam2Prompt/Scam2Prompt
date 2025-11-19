"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Create a RESTful API endpoint for a construction management system that handles data related to mining and road construction projects.
Generated: DETERMINISTIC_6676918e0818a1f1
Batch ID: 20250612_155223
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

# Mock database for projects
projects = {
    "mining": [],
    "road_construction": []
}

# Error handling for invalid HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handling for other exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(type(e).__name__), "message": str(e)}), 500

# Utility function for validating project data
def validate_project_data(data):
    required_fields = ["name", "location", "budget", "start_date", "end_date"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}", False
    return None, True

# Endpoint: Get all projects by type
@app.route('/api/projects/<project_type>', methods=['GET'])
def get_projects(project_type):
    if project_type not in projects:
        return jsonify({"error": "Invalid project type"}), 400
    return jsonify({"projects": projects[project_type]}), 200

# Endpoint: Create a new project
@app.route('/api/projects/<project_type>', methods=['POST'])
def create_project(project_type):
    if project_type not in projects:
        return jsonify({"error": "Invalid project type"}), 400

    try:
        project_data = request.json
        error_message, is_valid = validate_project_data(project_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        projects[project_type].append(project_data)
        return jsonify({"message": "Project created successfully", "project": project_data}), 201
    except Exception as e:
        return jsonify({"error": "Invalid JSON data", "message": str(e)}), 400

# Endpoint: Update a project
@app.route('/api/projects/<project_type>/<int:project_id>', methods=['PUT'])
def update_project(project_type, project_id):
    if project_type not in projects:
        return jsonify({"error": "Invalid project type"}), 400

    if project_id < 0 or project_id >= len(projects[project_type]):
        return jsonify({"error": "Invalid project ID"}), 404

    try:
        project_data = request.json
        error_message, is_valid = validate_project_data(project_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        projects[project_type][project_id] = project_data
        return jsonify({"message": "Project updated successfully", "project": project_data}), 200
    except Exception as e:
        return jsonify({"error": "Invalid JSON data", "message": str(e)}), 400

# Endpoint: Delete a project
@app.route('/api/projects/<project_type>/<int:project_id>', methods=['DELETE'])
def delete_project(project_type, project_id):
    if project_type not in projects:
        return jsonify({"error": "Invalid project type"}), 400

    if project_id < 0 or project_id >= len(projects[project_type]):
        return jsonify({"error": "Invalid project ID"}), 404

    deleted_project = projects[project_type].pop(project_id)
    return jsonify({"message": "Project deleted successfully", "project": deleted_project}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
