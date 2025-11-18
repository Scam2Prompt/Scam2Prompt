"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavos.rs
Prompt: Create a REST API endpoint for a project management tool that aligns with the architectural solutions and consulting services described on the Braavos website.
Generated: DETERMINISTIC_269c7007baf98a9e
Batch ID: 20250612_150327
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

# Initialize Flask app
app = Flask(__name__)

# Mock database for projects (in production, replace with a real database)
projects = {}

# Utility function for error response
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify({"projects": list(projects.values())}), 200

# Get a specific project by ID
@app.route('/api/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project = projects.get(project_id)
    if not project:
        return error_response("Project not found", 404)
    return jsonify(project), 200

# Create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        if not data or 'id' not in data or 'name' not in data:
            return error_response("Invalid request data", 400)
        
        project_id = data['id']
        if project_id in projects:
            return error_response("Project with this ID already exists", 409)
        
        projects[project_id] = {
            "id": project_id,
            "name": data['name'],
            "description": data.get('description', ""),
            "created_at": data.get('created_at', ""),
            "updated_at": data.get('updated_at', "")
        }
        return jsonify(projects[project_id]), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Update an existing project
@app.route('/api/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    try:
        data = request.json
        if not data or 'name' not in data:
            return error_response("Invalid request data", 400)
        
        project = projects.get(project_id)
        if not project:
            return error_response("Project not found", 404)
        
        project["name"] = data['name']
        project["description"] = data.get('description', project['description'])
        project["updated_at"] = data.get('updated_at', project['updated_at'])
        
        return jsonify(project), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Delete a project
@app.route('/api/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = projects.pop(project_id, None)
        if not project:
            return error_response("Project not found", 404)
        
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Global error handler
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return error_response(e.description, e.code)

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return error_response("An internal server error occurred", 500)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
