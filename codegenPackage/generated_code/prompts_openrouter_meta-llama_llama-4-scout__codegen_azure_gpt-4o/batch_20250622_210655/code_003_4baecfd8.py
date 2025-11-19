"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Develop a plan for a mobile app to engage volunteers in environmental conservation projects, such as the ones undertaken by Čuvari Šare, and suggest features like project catalogs, volunteer registration, and impact tracking.
Generated: DETERMINISTIC_4baecfd83a45f05c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code snippet for a backend API in Python using Flask to support the requested mobile app features. This code includes endpoints for project catalogs, volunteer registration, and impact tracking.

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
projects = []
volunteers = []
impact_records = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Fetch the list of all environmental conservation projects.
    """
    return jsonify({"projects": projects}), 200

# Endpoint: Add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    """
    Add a new project to the catalog.
    Request JSON format:
    {
        "name": "Project Name",
        "description": "Project Description",
        "location": "Project Location"
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "description", "location")):
        return jsonify({"error": "Invalid input"}), 400

    project = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "description": data["description"],
        "location": data["location"]
    }
    projects.append(project)
    return jsonify({"message": "Project added successfully", "project": project}), 201

# Endpoint: Register a volunteer
@app.route('/volunteers', methods=['POST'])
def register_volunteer():
    """
    Register a new volunteer.
    Request JSON format:
    {
        "name": "Volunteer Name",
        "email": "Volunteer Email"
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "email")):
        return jsonify({"error": "Invalid input"}), 400

    volunteer = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "email": data["email"]
    }
    volunteers.append(volunteer)
    return jsonify({"message": "Volunteer registered successfully", "volunteer": volunteer}), 201

# Endpoint: Track impact
@app.route('/impact', methods=['POST'])
def track_impact():
    """
    Record the impact of a volunteer's contribution to a project.
    Request JSON format:
    {
        "volunteer_id": "Volunteer ID",
        "project_id": "Project ID",
        "impact_description": "Description of the impact"
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("volunteer_id", "project_id", "impact_description")):
        return jsonify({"error": "Invalid input"}), 400

    # Validate volunteer and project IDs
    volunteer = next((v for v in volunteers if v["id"] == data["volunteer_id"]), None)
    project = next((p for p in projects if p["id"] == data["project_id"]), None)
    if not volunteer or not project:
        return jsonify({"error": "Invalid volunteer or project ID"}), 404

    impact_record = {
        "id": str(uuid.uuid4()),
        "volunteer_id": data["volunteer_id"],
        "project_id": data["project_id"],
        "impact_description": data["impact_description"]
    }
    impact_records.append(impact_record)
    return jsonify({"message": "Impact recorded successfully", "impact_record": impact_record}), 201

# Endpoint: Get impact records
@app.route('/impact', methods=['GET'])
def get_impact_records():
    """
    Fetch all impact records.
    """
    return jsonify({"impact_records": impact_records}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic backend API for the requested features. It uses Flask, includes error handling, and follows best practices for clean and maintainable code.
