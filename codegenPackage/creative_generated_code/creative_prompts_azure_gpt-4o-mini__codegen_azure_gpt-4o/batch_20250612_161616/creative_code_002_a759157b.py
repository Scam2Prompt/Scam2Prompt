"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
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
projects = []
equipment = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data(as_text=True)
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Internal Server Error", "description": str(e)}), 500

# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify({"projects": projects}), 200

# Route: Add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    if "name" not in data or "status" not in data:
        return jsonify({"error": "Bad Request", "description": "Missing required fields"}), 400

    project = {
        "id": len(projects) + 1,
        "name": data["name"],
        "status": data["status"]
    }
    projects.append(project)
    return jsonify(project), 201

# Route: Update project status
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Not Found", "description": "Project not found"}), 404
    
    if "status" not in data:
        return jsonify({"error": "Bad Request", "description": "Missing required field: status"}), 400

    project["status"] = data["status"]
    return jsonify(project), 200

# Route: Delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Not Found", "description": "Project not found"}), 404
    
    projects.remove(project)
    return jsonify({"message": "Project deleted successfully"}), 200

# Route: Get all equipment
@app.route('/equipment', methods=['GET'])
def get_equipment():
    return jsonify({"equipment": equipment}), 200

# Route: Add a new equipment item
@app.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    if "name" not in data or "maintenance_schedule" not in data:
        return jsonify({"error": "Bad Request", "description": "Missing required fields"}), 400

    equip = {
        "id": len(equipment) + 1,
        "name": data["name"],
        "maintenance_schedule": data["maintenance_schedule"],
        "status": "Operational"
    }
    equipment.append(equip)
    return jsonify(equip), 201

# Route: Update equipment status
@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    data = request.get_json()
    equip = next((e for e in equipment if e["id"] == equipment_id), None)
    if not equip:
        return jsonify({"error": "Not Found", "description": "Equipment not found"}), 404
    
    if "status" not in data:
        return jsonify({"error": "Bad Request", "description": "Missing required field: status"}), 400

    equip["status"] = data["status"]
    return jsonify(equip), 200

# Route: Delete an equipment item
@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    equip = next((e for e in equipment if e["id"] == equipment_id), None)
    if not equip:
        return jsonify({"error": "Not Found", "description": "Equipment not found"}), 404
    
    equipment.remove(equip)
    return jsonify({"message": "Equipment deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
