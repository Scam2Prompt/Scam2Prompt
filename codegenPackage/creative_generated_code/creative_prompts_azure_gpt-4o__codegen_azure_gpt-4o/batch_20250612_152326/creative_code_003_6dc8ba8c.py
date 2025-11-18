"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API design for a company like Sadad Engineering to manage project data, including endpoints for retrieving ongoing projects, completed projects, and affiliated companies.
Generated: DETERMINISTIC_6dc8ba8cf506326c
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration purposes
projects = [
    {"id": 1, "name": "Bridge Construction", "status": "ongoing"},
    {"id": 2, "name": "Office Renovation", "status": "completed"},
    {"id": 3, "name": "Highway Expansion", "status": "ongoing"}
]

companies = [
    {"id": 1, "name": "Sadad Engineering"},
    {"id": 2, "name": "TechBuild Co."},
    {"id": 3, "name": "InfraExperts Ltd."}
]

@app.route('/projects/ongoing', methods=['GET'])
def get_ongoing_projects():
    """
    Endpoint to retrieve a list of ongoing projects.
    """
    try:
        ongoing_projects = [project for project in projects if project['status'] == 'ongoing']
        return jsonify({"ongoing_projects": ongoing_projects})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/completed', methods=['GET'])
def get_completed_projects():
    """
    Endpoint to retrieve a list of completed projects.
    """
    try:
        completed_projects = [project for project in projects if project['status'] == 'completed']
        return jsonify({"completed_projects": completed_projects})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/companies', methods=['GET'])
def get_companies():
    """
    Endpoint to retrieve a list of affiliated companies.
    """
    try:
        return jsonify({"companies": companies})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    """
    Endpoint to retrieve a specific project by its ID.
    """
    try:
        project = next((project for project in projects if project['id'] == project_id), None)
        if project:
            return jsonify({"project": project})
        return jsonify({"error": "Project not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    """
    Endpoint to retrieve a specific company by its ID.
    """
    try:
        company = next((company for company in companies if company['id'] == company_id), None)
        if company:
            return jsonify({"company": company})
        return jsonify({"error": "Company not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 - route not found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 - internal server error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```
