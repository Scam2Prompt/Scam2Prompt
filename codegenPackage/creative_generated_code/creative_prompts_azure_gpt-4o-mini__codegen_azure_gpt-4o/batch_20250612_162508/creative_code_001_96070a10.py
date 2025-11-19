"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Recommend an API for managing architectural designs and project supervision that aligns with the innovative solutions offered by Remas Engineering Consultants.
Generated: DETERMINISTIC_96070a1078d1229e
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based API for managing architectural designs and project supervision
# This API aligns with innovative solutions and provides endpoints for:
# - Managing architectural designs (CRUD operations)
# - Assigning supervisors to projects
# - Viewing project details

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
# Replace with a proper database in production
architectural_designs = {}
project_supervisors = {}

# Error handling for invalid requests
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors."""
    response = e.get_response()
    response.data = jsonify({"error": e.description})
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle unexpected errors."""
    return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to create a new architectural design
@app.route('/designs', methods=['POST'])
def create_design():
    """
    Create a new architectural design.
    Request JSON format:
    {
        "design_id": "unique_id",
        "name": "Design Name",
        "description": "Design Description"
    }
    """
    data = request.get_json()
    design_id = data.get("design_id")
    
    if not design_id or design_id in architectural_designs:
        return jsonify({"error": "Invalid or duplicate design ID"}), 400
    
    architectural_designs[design_id] = {
        "name": data.get("name"),
        "description": data.get("description")
    }
    
    return jsonify({"message": "Design created successfully", "design": architectural_designs[design_id]}), 201

# Endpoint to retrieve architectural designs
@app.route('/designs', methods=['GET'])
def get_designs():
    """
    Retrieve all architectural designs.
    """
    return jsonify({"designs": architectural_designs}), 200

# Endpoint to assign a supervisor to a project
@app.route('/supervisors', methods=['POST'])
def assign_supervisor():
    """
    Assign a supervisor to a project.
    Request JSON format:
    {
        "project_id": "unique_project_id",
        "supervisor_name": "Supervisor Name"
    }
    """
    data = request.get_json()
    project_id = data.get("project_id")
    supervisor_name = data.get("supervisor_name")
    
    if not project_id or not supervisor_name:
        return jsonify({"error": "Invalid input"}), 400
    
    project_supervisors[project_id] = supervisor_name
    
    return jsonify({
        "message": "Supervisor assigned successfully",
        "project_id": project_id,
        "supervisor": supervisor_name
    }), 201

# Endpoint to view details of a project
@app.route('/projects/<project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    Retrieve project details by project ID.
    Includes supervisor information if assigned.
    """
    design = architectural_designs.get(project_id)
    supervisor = project_supervisors.get(project_id)
    
    if not design:
        return jsonify({"error": "Project not found"}), 404
    
    return jsonify({
        "project_id": project_id,
        "design": design,
        "supervisor": supervisor
    }), 200

# Run the application
if __name__ == '__main__':
    # For production, use a robust WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```
