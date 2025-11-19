"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API design for a construction company that includes endpoints for project tracking, based on the services offered by Sadad Engineering.
Generated: DETERMINISTIC_83c3a80688dc126f
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready RESTful API implementation written in Python using Flask:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation for projects
projects = []

# Error handling for 404 - Resource Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404


# Error handling for 400 - Bad Request
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400


# API Endpoint: Get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Retrieve the list of all projects.
    """
    return jsonify({"projects": projects}), 200


# API Endpoint: Create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    """
    Create a new project. Expects JSON input with 'name', 'description', and 'status'.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'status' not in data:
            raise ValueError("Invalid input data")
        
        project = {
            "id": len(projects) + 1,
            "name": data['name'],
            "description": data['description'],
            "status": data['status']  # e.g., 'ongoing', 'completed', etc.
        }
        projects.append(project)
        return jsonify({"message": "Project created successfully", "project": project}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400


# API Endpoint: Get a single project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve the details of a single project by ID.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return jsonify({"project": project}), 200
    else:
        return jsonify({"error": "Project not found"}), 404


# API Endpoint: Update a project by ID
@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update the details of a project by ID. Expects JSON input with 'name', 'description', and/or 'status'.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        try:
            data = request.get_json()
            if not data:
                raise ValueError("Invalid input data")
            
            project['name'] = data.get('name', project['name'])
            project['description'] = data.get('description', project['description'])
            project['status'] = data.get('status', project['status'])
            return jsonify({"message": "Project updated successfully", "project": project}), 200
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
    else:
        return jsonify({"error": "Project not found"}), 404


# API Endpoint: Delete a project by ID
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a project by ID.
    """
    global projects
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        projects = [p for p in projects if p['id'] != project_id]
        return jsonify({"message": "Project deleted successfully"}), 200
    else:
        return jsonify({"error": "Project not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Save this code to a file, e.g., `app.py`.
2. Install Flask using `pip install flask`.
3. Run the application using `python app.py`.
4. Test the API using tools like Postman or `curl`.
