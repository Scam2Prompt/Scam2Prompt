"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Create a freelancer platform API to connect businesses with Oracle ERP experts.
Generated: DETERMINISTIC_b7af03782b4a4161
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
from uuid import uuid4

app = Flask(__name__)

# In-memory database for demonstration purposes
freelancers = []
projects = []

# Error messages
ERRORS = {
    "not_found": "Resource not found.",
    "invalid_data": "Invalid data provided.",
    "missing_fields": "Missing required fields."
}

# Helper function to validate required fields
def validate_fields(data, required_fields):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

# Route to register a freelancer
@app.route('/freelancers', methods=['POST'])
def register_freelancer():
    """
    Register a new freelancer.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "skills": ["Oracle ERP", "SQL", "PL/SQL"]
    }
    """
    data = request.get_json()
    required_fields = ["name", "email", "skills"]
    is_valid, error_message = validate_fields(data, required_fields)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    freelancer = {
        "id": str(uuid4()),
        "name": data["name"],
        "email": data["email"],
        "skills": data["skills"]
    }
    freelancers.append(freelancer)
    return jsonify(freelancer), 201

# Route to list all freelancers
@app.route('/freelancers', methods=['GET'])
def list_freelancers():
    """
    List all registered freelancers.
    """
    return jsonify(freelancers), 200

# Route to post a project
@app.route('/projects', methods=['POST'])
def post_project():
    """
    Post a new project.
    Expected JSON payload:
    {
        "title": "Oracle ERP Implementation",
        "description": "Looking for an expert to implement Oracle ERP.",
        "required_skills": ["Oracle ERP"]
    }
    """
    data = request.get_json()
    required_fields = ["title", "description", "required_skills"]
    is_valid, error_message = validate_fields(data, required_fields)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    project = {
        "id": str(uuid4()),
        "title": data["title"],
        "description": data["description"],
        "required_skills": data["required_skills"]
    }
    projects.append(project)
    return jsonify(project), 201

# Route to list all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    """
    List all posted projects.
    """
    return jsonify(projects), 200

# Route to match freelancers to a project
@app.route('/projects/<project_id>/match', methods=['GET'])
def match_freelancers(project_id):
    """
    Match freelancers to a project based on required skills.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": ERRORS["not_found"]}), 404

    matched_freelancers = [
        freelancer for freelancer in freelancers
        if any(skill in freelancer["skills"] for skill in project["required_skills"])
    ]
    return jsonify(matched_freelancers), 200

# Error handling for unsupported routes
@app.errorhandler(404)
def resource_not_found(e):
    """
    Handle 404 errors for unsupported routes.
    """
    return jsonify({"error": ERRORS["not_found"]}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
