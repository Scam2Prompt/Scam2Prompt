"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Design a web application for entrepreneurs to apply for funding and investors to participate in the economic growth of Argentina, incorporating features like quote requests and project proposals.
Generated: DETERMINISTIC_e0a0f70472586ac6
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a web application using Python's Flask framework. This application allows entrepreneurs to apply for funding and investors to review and participate in projects. It includes features for quote requests and project proposals.

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for demonstration purposes
entrepreneurs = []
investors = []
projects = []

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route: Register entrepreneur
@app.route('/entrepreneurs', methods=['POST'])
def register_entrepreneur():
    """
    Register a new entrepreneur.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "business_name": "Startup Inc."
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "email", "business_name")):
        return jsonify({"error": "Invalid input"}), 400

    entrepreneur = {
        "id": len(entrepreneurs) + 1,
        "name": data["name"],
        "email": data["email"],
        "business_name": data["business_name"]
    }
    entrepreneurs.append(entrepreneur)
    return jsonify(entrepreneur), 201

# Route: Register investor
@app.route('/investors', methods=['POST'])
def register_investor():
    """
    Register a new investor.
    Request JSON format:
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "investment_focus": "Technology"
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "email", "investment_focus")):
        return jsonify({"error": "Invalid input"}), 400

    investor = {
        "id": len(investors) + 1,
        "name": data["name"],
        "email": data["email"],
        "investment_focus": data["investment_focus"]
    }
    investors.append(investor)
    return jsonify(investor), 201

# Route: Submit project proposal
@app.route('/projects', methods=['POST'])
def submit_project():
    """
    Submit a new project proposal.
    Request JSON format:
    {
        "entrepreneur_id": 1,
        "title": "Innovative Tech Solution",
        "description": "A groundbreaking technology...",
        "funding_needed": 50000
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("entrepreneur_id", "title", "description", "funding_needed")):
        return jsonify({"error": "Invalid input"}), 400

    # Validate entrepreneur ID
    entrepreneur = next((e for e in entrepreneurs if e["id"] == data["entrepreneur_id"]), None)
    if not entrepreneur:
        return jsonify({"error": "Entrepreneur not found"}), 404

    project = {
        "id": len(projects) + 1,
        "entrepreneur_id": data["entrepreneur_id"],
        "title": data["title"],
        "description": data["description"],
        "funding_needed": data["funding_needed"],
        "status": "Pending"
    }
    projects.append(project)
    return jsonify(project), 201

# Route: List all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    """
    List all project proposals.
    """
    return jsonify(projects), 200

# Route: Investors request a quote for a project
@app.route('/projects/<int:project_id>/quote', methods=['POST'])
def request_quote(project_id):
    """
    Investors request a quote for a specific project.
    Request JSON format:
    {
        "investor_id": 1,
        "message": "I am interested in funding this project."
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("investor_id", "message")):
        return jsonify({"error": "Invalid input"}), 400

    # Validate project ID
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Validate investor ID
    investor = next((i for i in investors if i["id"] == data["investor_id"]), None)
    if not investor:
        return jsonify({"error": "Investor not found"}), 404

    quote_request = {
        "project_id": project_id,
        "investor_id": data["investor_id"],
        "message": data["message"]
    }
    return jsonify(quote_request), 201

# Route: Get project details
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    Get details of a specific project.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask for simplicity and rapid development.
- Replace the in-memory storage (`entrepreneurs`, `investors`, `projects`) with a database for production use.
- Add authentication and authorization mechanisms for security in a real-world application.
- Use environment variables for sensitive configurations (e.g., database credentials).
