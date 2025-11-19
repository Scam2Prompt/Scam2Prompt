"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Create an API recommendation for managing project timelines and inspections in luxury property development, highlighting features that ensure stringent quality control.
Generated: DETERMINISTIC_8381f36f5a44c15e
Batch ID: 20250612_135848
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
inspections = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Helper function to validate date format
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    Request JSON format:
    {
        "name": "Project Name",
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD"
    }
    """
    data = request.get_json()
    name = data.get('name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Validate input
    if not name or not start_date or not end_date:
        return jsonify({"error": "Missing required fields"}), 400
    if not validate_date(start_date) or not validate_date(end_date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    if datetime.strptime(start_date, '%Y-%m-%d') >= datetime.strptime(end_date, '%Y-%m-%d'):
        return jsonify({"error": "Start date must be before end date"}), 400

    # Create project
    project_id = generate_id()
    projects[project_id] = {
        "id": project_id,
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "created_at": datetime.now().isoformat()
    }
    return jsonify(projects[project_id]), 201

# Endpoint to list all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    """
    List all projects.
    """
    return jsonify(list(projects.values())), 200

# Endpoint to create an inspection for a project
@app.route('/projects/<project_id>/inspections', methods=['POST'])
def create_inspection(project_id):
    """
    Create a new inspection for a project.
    Request JSON format:
    {
        "inspection_date": "YYYY-MM-DD",
        "inspector_name": "Inspector Name",
        "notes": "Inspection Notes"
    }
    """
    if project_id not in projects:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json()
    inspection_date = data.get('inspection_date')
    inspector_name = data.get('inspector_name')
    notes = data.get('notes')

    # Validate input
    if not inspection_date or not inspector_name:
        return jsonify({"error": "Missing required fields"}), 400
    if not validate_date(inspection_date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Create inspection
    inspection_id = generate_id()
    inspections[inspection_id] = {
        "id": inspection_id,
        "project_id": project_id,
        "inspection_date": inspection_date,
        "inspector_name": inspector_name,
        "notes": notes,
        "created_at": datetime.now().isoformat()
    }
    return jsonify(inspections[inspection_id]), 201

# Endpoint to list all inspections for a project
@app.route('/projects/<project_id>/inspections', methods=['GET'])
def list_inspections(project_id):
    """
    List all inspections for a specific project.
    """
    if project_id not in projects:
        return jsonify({"error": "Project not found"}), 404

    project_inspections = [
        inspection for inspection in inspections.values()
        if inspection['project_id'] == project_id
    ]
    return jsonify(project_inspections), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
