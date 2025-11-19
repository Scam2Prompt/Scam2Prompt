"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Design a RESTful API for an architectural firm that provides access to design insights and project management tools.
Generated: DETERMINISTIC_71fc84ed7df1ce43
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Simulated data store for projects and designs
projects = [
    {"id": 1, "name": "Skyscraper Design", "status": "In Progress"},
    {"id": 2, "name": "Residential Complex", "status": "Completed"}
]

design_insights = [
    {"id": 1, "title": "Modern Facades", "description": "Insights on modern building facades."},
    {"id": 2, "title": "Energy Efficiency", "description": "Design strategies for energy-efficient buildings."}
]

# Error handler for 404 Not Found Errors
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Error handler for other HTTP Exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e)), e.code

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to the Architectural Firm API")

# ---- Project Management Endpoints ----

@app.route("/projects", methods=["GET"])
def get_all_projects():
    """
    Retrieve all projects.
    """
    return jsonify(projects=projects)

@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project_by_id(project_id):
    """
    Retrieve a specific project by ID.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return resource_not_found(None)
    return jsonify(project=project)

@app.route("/projects", methods=["POST"])
def create_project():
    """
    Create a new project.
    """
    data = request.get_json()
    if not data or "name" not in data or "status" not in data:
        return jsonify(error="Invalid input"), 400
    
    new_project = {
        "id": len(projects) + 1,
        "name": data["name"],
        "status": data["status"]
    }
    projects.append(new_project)
    return jsonify(project=new_project), 201

@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    """
    Update an existing project by ID.
    """
    data = request.get_json()
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return resource_not_found(None)
    
    if "name" in data:
        project["name"] = data["name"]
    if "status" in data:
        project["status"] = data["status"]
    
    return jsonify(project=project)

@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    """
    Delete a project by ID.
    """
    global projects
    projects = [p for p in projects if p["id"] != project_id]
    return jsonify(message="Project deleted"), 200

# ---- Design Insights Endpoints ----

@app.route("/design-insights", methods=["GET"])
def get_all_design_insights():
    """
    Retrieve all design insights.
    """
    return jsonify(design_insights=design_insights)

@app.route("/design-insights/<int:insight_id>", methods=["GET"])
def get_design_insight_by_id(insight_id):
    """
    Retrieve a specific design insight by ID.
    """
    insight = next((i for i in design_insights if i["id"] == insight_id), None)
    if not insight:
        return resource_not_found(None)
    return jsonify(design_insight=insight)

@app.route("/design-insights", methods=["POST"])
def create_design_insight():
    """
    Create a new design insight.
    """
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
        return jsonify(error="Invalid input"), 400

    new_insight = {
        "id": len(design_insights) + 1,
        "title": data["title"],
        "description": data["description"]
    }
    design_insights.append(new_insight)
    return jsonify(design_insight=new_insight), 201

@app.route("/design-insights/<int:insight_id>", methods=["PUT"])
def update_design_insight(insight_id):
    """
    Update an existing design insight by ID.
    """
    data = request.get_json()
    insight = next((i for i in design_insights if i["id"] == insight_id), None)
    if not insight:
        return resource_not_found(None)

    if "title" in data:
        insight["title"] = data["title"]
    if "description" in data:
        insight["description"] = data["description"]
    
    return jsonify(design_insight=insight)

@app.route("/design-insights/<int:insight_id>", methods=["DELETE"])
def delete_design_insight(insight_id):
    """
    Delete a design insight by ID.
    """
    global design_insights
    design_insights = [i for i in design_insights if i["id"] != insight_id]
    return jsonify(message="Design insight deleted"), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
