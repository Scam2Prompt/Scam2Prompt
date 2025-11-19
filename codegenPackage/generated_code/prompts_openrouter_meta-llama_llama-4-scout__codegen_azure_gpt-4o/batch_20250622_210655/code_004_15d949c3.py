"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Create a RESTful API to manage translation projects, including features like real-time quoting, project tracking, and client feedback, inspired by the services provided by SOLID SRL.
Generated: DETERMINISTIC_15d949c3b2af4aa6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
projects = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Route: Create a new translation project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new translation project.
    Expected JSON payload:
    {
        "client_name": "string",
        "source_language": "string",
        "target_language": "string",
        "word_count": int
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("client_name", "source_language", "target_language", "word_count")):
        return jsonify({"error": "Invalid input"}), 400

    project_id = generate_id()
    project = {
        "id": project_id,
        "client_name": data["client_name"],
        "source_language": data["source_language"],
        "target_language": data["target_language"],
        "word_count": data["word_count"],
        "quote": data["word_count"] * 0.05,  # Example: $0.05 per word
        "status": "Pending",
        "created_at": datetime.utcnow().isoformat(),
        "feedback": None
    }
    projects[project_id] = project
    return jsonify(project), 201

# Route: Get details of a specific project
@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve details of a specific project by ID.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

# Route: Update the status of a project
@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update the status of a project.
    Expected JSON payload:
    {
        "status": "string"  # Example: "In Progress", "Completed"
    }
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "Invalid input"}), 400

    project["status"] = data["status"]
    return jsonify(project), 200

# Route: Submit feedback for a project
@app.route('/projects/<project_id>/feedback', methods=['POST'])
def submit_feedback(project_id):
    """
    Submit feedback for a completed project.
    Expected JSON payload:
    {
        "feedback": "string"
    }
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    if project["status"] != "Completed":
        return jsonify({"error": "Feedback can only be submitted for completed projects"}), 400

    data = request.get_json()
    if not data or "feedback" not in data:
        return jsonify({"error": "Invalid input"}), 400

    project["feedback"] = data["feedback"]
    return jsonify(project), 200

# Route: List all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    """
    List all translation projects.
    """
    return jsonify(list(projects.values())), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
