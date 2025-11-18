"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Provide an example of a REST API design for managing construction projects, with endpoints for adding new projects, updating milestones, and retrieving statistics like apartments built and hours worked, as described by INARO S.A.S.
Generated: DETERMINISTIC_6ddb61bb09ec781b
Batch ID: 20250612_153401
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

# In-memory database simulation
projects = {}
project_id_counter = 1

# Error handler for invalid API usage
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).data
    response.content_type = "application/json"
    return response

# Endpoint: Add a new construction project
@app.route('/projects', methods=['POST'])
def add_project():
    """
    Add a new construction project.

    Expected JSON Payload:
    {
        "name": "Project Name",
        "start_date": "2023-01-01",
        "end_date": "2023-12-31"
    }
    """
    global project_id_counter
    
    # Validate payload
    data = request.get_json()
    if not data or 'name' not in data or 'start_date' not in data or 'end_date' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    # Create a new project entry
    project_id = project_id_counter
    projects[project_id] = {
        "id": project_id,
        "name": data['name'],
        "start_date": data['start_date'],
        "end_date": data['end_date'],
        "milestones": [],
        "stats": {
            "apartments_built": 0,
            "hours_worked": 0
        }
    }
    
    project_id_counter += 1
    return jsonify({"message": "Project created successfully", "project_id": project_id}), 201

# Endpoint: Update project milestones
@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def update_milestones(project_id):
    """
    Update milestones for a specific project.

    Expected JSON Payload:
    {
        "milestone": "Foundation Completed",
        "date": "2023-03-15"
    }
    """
    # Validate project existence
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Validate payload
    data = request.get_json()
    if not data or 'milestone' not in data or 'date' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    # Update milestones
    project['milestones'].append({
        "milestone": data['milestone'],
        "date": data['date']
    })
    return jsonify({"message": "Milestone updated successfully"}), 200

# Endpoint: Retrieve project statistics
@app.route('/projects/<int:project_id>/statistics', methods=['GET'])
def get_statistics(project_id):
    """
    Get statistics for a specific project.

    Response Example:
    {
        "apartments_built": 20,
        "hours_worked": 1500
    }
    """
    # Validate project existence
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Return statistics
    return jsonify(project['stats']), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
