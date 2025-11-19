"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://albatrosspa.cl
Prompt: Create a RESTful API design for a construction company that highlights architectural design and project planning, reflecting the services offered by Albatros SPA.
Generated: DETERMINISTIC_4d91b006d5d6836f
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data to simulate a database
services = [
    {"id": 1, "name": "Architectural Design", "description": "High-quality architectural planning and visualization."},
    {"id": 2, "name": "Project Planning", "description": "Comprehensive project planning and execution strategies."}
]

projects = [
    {"id": 1, "name": "Skyscraper X", "status": "In Progress", "service_id": 1},
    {"id": 2, "name": "Residential Complex Y", "status": "Completed", "service_id": 2}
]

# Error handler for routes not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Root route for API status
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to Albatros SPA Construction API", "status": "Running"})

# Endpoint to retrieve all services
@app.route("/services", methods=["GET"])
def get_services():
    return jsonify({"services": services})

# Endpoint to retrieve a specific service by ID
@app.route("/services/<int:service_id>", methods=["GET"])
def get_service_by_id(service_id):
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return jsonify({"service": service})

# Endpoint to retrieve all projects
@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify({"projects": projects})

# Endpoint to retrieve a specific project by ID
@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project_by_id(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"project": project})

# Endpoint to create a new project
@app.route("/projects", methods=["POST"])
def create_project():
    try:
        data = request.get_json()
        if not all(key in data for key in ("name", "status", "service_id")):
            return jsonify({"error": "Invalid input"}), 400

        # Ensure the service_id exists
        if not any(s for s in services if s["id"] == data["service_id"]):
            return jsonify({"error": "Service ID not found"}), 404
        
        # Generate a new project ID
        new_id = max(project["id"] for project in projects) + 1
        new_project = {
            "id": new_id,
            "name": data["name"],
            "status": data["status"],
            "service_id": data["service_id"]
        }
        projects.append(new_project)
        return jsonify({"message": "Project created successfully", "project": new_project}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Endpoint to update a project by ID
@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    try:
        data = request.get_json()
        project = next((p for p in projects if p["id"] == project_id), None)
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        # Update project fields if they exist in the request data
        project["name"] = data.get("name", project["name"])
        project["status"] = data.get("status", project["status"])
        project["service_id"] = data.get("service_id", project["service_id"])
        
        return jsonify({"message": "Project updated successfully", "project": project})
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Endpoint to delete a project by ID
@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    global projects
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    projects = [p for p in projects if p["id"] != project_id]
    return jsonify({"message": "Project deleted successfully"})

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
