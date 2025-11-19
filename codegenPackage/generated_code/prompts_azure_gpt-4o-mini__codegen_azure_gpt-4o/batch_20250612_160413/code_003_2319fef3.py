"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Develop a RESTful API endpoint for a mentorship program that connects teen moms with resources and legal counsel, based on the services offered by My Flow Foundation.
Generated: DETERMINISTIC_2319fef39eb41a68
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for demonstration purposes
resources = [
    {"id": 1, "name": "Parenting Classes", "description": "Learn essential parenting skills."},
    {"id": 2, "name": "Legal Counsel", "description": "Get legal advice and support."},
    {"id": 3, "name": "Financial Assistance", "description": "Access financial aid programs."},
]

mentorship_programs = [
    {"id": 1, "name": "Teen Mom Mentorship", "description": "Connect with experienced mentors."},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    }), 500

# Endpoint to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    GET /api/resources
    Returns a list of all available resources.
    """
    return jsonify({"resources": resources}), 200

# Endpoint to get all mentorship programs
@app.route('/api/mentorship-programs', methods=['GET'])
def get_mentorship_programs():
    """
    GET /api/mentorship-programs
    Returns a list of all available mentorship programs.
    """
    return jsonify({"mentorship_programs": mentorship_programs}), 200

# Endpoint to get a specific resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    """
    GET /api/resources/<resource_id>
    Returns a specific resource by its ID.
    """
    resource = next((r for r in resources if r["id"] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify(resource), 200

# Endpoint to get a specific mentorship program by ID
@app.route('/api/mentorship-programs/<int:program_id>', methods=['GET'])
def get_mentorship_program_by_id(program_id):
    """
    GET /api/mentorship-programs/<program_id>
    Returns a specific mentorship program by its ID.
    """
    program = next((p for p in mentorship_programs if p["id"] == program_id), None)
    if program is None:
        return jsonify({"error": "Mentorship program not found"}), 404
    return jsonify(program), 200

# Endpoint to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    POST /api/resources
    Adds a new resource to the database.
    """
    data = request.get_json()
    if not data or "name" not in data or "description" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_resource = {
        "id": len(resources) + 1,
        "name": data["name"],
        "description": data["description"]
    }
    resources.append(new_resource)
    return jsonify(new_resource), 201

# Endpoint to add a new mentorship program
@app.route('/api/mentorship-programs', methods=['POST'])
def add_mentorship_program():
    """
    POST /api/mentorship-programs
    Adds a new mentorship program to the database.
    """
    data = request.get_json()
    if not data or "name" not in data or "description" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_program = {
        "id": len(mentorship_programs) + 1,
        "name": data["name"],
        "description": data["description"]
    }
    mentorship_programs.append(new_program)
    return jsonify(new_program), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
