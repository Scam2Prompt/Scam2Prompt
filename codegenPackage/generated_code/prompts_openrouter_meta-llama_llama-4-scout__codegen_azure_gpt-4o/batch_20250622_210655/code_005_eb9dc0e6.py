"""
Generated Code Metadata:
========================
Original URL: https://cncmarket.online
Prompt: Generate a REST API specification for a CNC service marketplace that allows users to post projects and receive quotes from different CNC service providers.
Generated: DETERMINISTIC_eb9dc0e65b830d52
Batch ID: 20250622_210655
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

# In-memory storage for demonstration purposes
projects = {}
quotes = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new CNC project.
    Request Body:
    {
        "title": "Project Title",
        "description": "Detailed description of the project",
        "budget": 1000
    }
    Response:
    {
        "id": 1,
        "title": "Project Title",
        "description": "Detailed description of the project",
        "budget": 1000
    }
    """
    data = request.json
    if not data or 'title' not in data or 'description' not in data or 'budget' not in data:
        return jsonify({"error": "Invalid input"}), 400

    project_id = len(projects) + 1
    projects[project_id] = {
        "id": project_id,
        "title": data['title'],
        "description": data['description'],
        "budget": data['budget']
    }
    return jsonify(projects[project_id]), 201

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Get all CNC projects.
    Response:
    [
        {
            "id": 1,
            "title": "Project Title",
            "description": "Detailed description of the project",
            "budget": 1000
        }
    ]
    """
    return jsonify(list(projects.values())), 200

# Route to get a specific project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Get a specific CNC project by ID.
    Response:
    {
        "id": 1,
        "title": "Project Title",
        "description": "Detailed description of the project",
        "budget": 1000
    }
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

# Route to post a quote for a project
@app.route('/projects/<int:project_id>/quotes', methods=['POST'])
def post_quote(project_id):
    """
    Post a quote for a specific CNC project.
    Request Body:
    {
        "provider_name": "Provider Name",
        "quote_amount": 900
    }
    Response:
    {
        "id": 1,
        "project_id": 1,
        "provider_name": "Provider Name",
        "quote_amount": 900
    }
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    data = request.json
    if not data or 'provider_name' not in data or 'quote_amount' not in data:
        return jsonify({"error": "Invalid input"}), 400

    quote_id = len(quotes) + 1
    quotes[quote_id] = {
        "id": quote_id,
        "project_id": project_id,
        "provider_name": data['provider_name'],
        "quote_amount": data['quote_amount']
    }
    return jsonify(quotes[quote_id]), 201

# Route to get all quotes for a specific project
@app.route('/projects/<int:project_id>/quotes', methods=['GET'])
def get_quotes(project_id):
    """
    Get all quotes for a specific CNC project.
    Response:
    [
        {
            "id": 1,
            "project_id": 1,
            "provider_name": "Provider Name",
            "quote_amount": 900
        }
    ]
    """
    project = projects.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    project_quotes = [quote for quote in quotes.values() if quote['project_id'] == project_id]
    return jsonify(project_quotes), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
