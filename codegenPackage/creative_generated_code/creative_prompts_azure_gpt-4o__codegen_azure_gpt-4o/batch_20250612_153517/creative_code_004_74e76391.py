"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Create a REST API design for an NGO like Child Nepal to manage their projects, beneficiaries, and partnerships. Include endpoints for tracking project milestones and reporting impact metrics.
Generated: DETERMINISTIC_74e76391c761d58f
Batch ID: 20250612_153517
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

# In-memory data store for demonstration purposes
projects = {}
beneficiaries = {}
partnerships = {}

# Error handling
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request"}), 400

# Endpoints

# Projects
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    """
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    project_id = len(projects) + 1
    projects[project_id] = {
        "id": project_id,
        "name": data["name"],
        "description": data["description"],
        "milestones": [],
        "impact_metrics": []
    }
    return jsonify({"message": "Project created", "project": projects[project_id]}), 201

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Get details of a specific project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify({"project": project}), 200

@app.route('/projects/<int:project_id>/milestones', methods=['POST'])
def add_milestone(project_id):
    """
    Add a milestone to a project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    
    data = request.json
    if not data or 'milestone' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    milestone = data["milestone"]
    project["milestones"].append(milestone)
    return jsonify({"message": "Milestone added", "project": project}), 200

@app.route('/projects/<int:project_id>/impact', methods=['POST'])
def add_impact_metric(project_id):
    """
    Add an impact metric to a project.
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    
    data = request.json
    if not data or 'metric' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    metric = data["metric"]
    project["impact_metrics"].append(metric)
    return jsonify({"message": "Impact metric added", "project": project}), 200

# Beneficiaries
@app.route('/beneficiaries', methods=['POST'])
def create_beneficiary():
    """
    Add a new beneficiary.
    """
    data = request.json
    if not data or 'name' not in data or 'details' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    beneficiary_id = len(beneficiaries) + 1
    beneficiaries[beneficiary_id] = {
        "id": beneficiary_id,
        "name": data["name"],
        "details": data["details"]
    }
    return jsonify({"message": "Beneficiary created", "beneficiary": beneficiaries[beneficiary_id]}), 201

@app.route('/beneficiaries/<int:beneficiary_id>', methods=['GET'])
def get_beneficiary(beneficiary_id):
    """
    Get details of a specific beneficiary.
    """
    beneficiary = beneficiaries.get(beneficiary_id)
    if not beneficiary:
        return jsonify({"error": "Beneficiary not found"}), 404
    return jsonify({"beneficiary": beneficiary}), 200

# Partnerships
@app.route('/partnerships', methods=['POST'])
def create_partnership():
    """
    Create a new partnership.
    """
    data = request.json
    if not data or 'organization' not in data or 'details' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    partnership_id = len(partnerships) + 1
    partnerships[partnership_id] = {
        "id": partnership_id,
        "organization": data["organization"],
        "details": data["details"]
    }
    return jsonify({"message": "Partnership created", "partnership": partnerships[partnership_id]}), 201

@app.route('/partnerships/<int:partnership_id>', methods=['GET'])
def get_partnership(partnership_id):
    """
    Get details of a specific partnership.
    """
    partnership = partnerships.get(partnership_id)
    if not partnership:
        return jsonify({"error": "Partnership not found"}), 404
    return jsonify({"partnership": partnership}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
