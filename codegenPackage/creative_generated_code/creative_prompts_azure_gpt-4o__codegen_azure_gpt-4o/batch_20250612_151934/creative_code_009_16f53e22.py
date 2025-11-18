"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Develop an API to support MIEC's empowerment initiatives for young entrepreneurs, including features for skill development and project management.
Generated: DETERMINISTIC_16f53e2289992775
Batch ID: 20250612_151934
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

# Mock database (In production, replace with an actual database such as PostgreSQL or MongoDB)
mock_db = {
    "users": [],
    "projects": []
}

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="Internal Server Error"), 500

# Endpoint to register a new user
@app.route('/api/users', methods=['POST'])
def register_user():
    """
    Register a new user.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "skills": ["marketing", "finance"]
    }
    """
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data format"}), 400
    
    # Check for duplicate email
    if any(user['email'] == data["email"] for user in mock_db["users"]):
        return jsonify({"error": "Email already exists"}), 409
    
    user = {
        "id": len(mock_db["users"]) + 1,
        "name": data["name"],
        "email": data["email"],
        "skills": data.get("skills", [])
    }
    mock_db["users"].append(user)
    return jsonify(user), 201

# Endpoint to create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    Expected JSON payload:
    {
        "title": "New Startup Idea",
        "description": "Description of the startup idea.",
        "owner_email": "johndoe@example.com"
    }
    """
    data = request.get_json()
    if not data or "title" not in data or "owner_email" not in data:
        return jsonify({"error": "Invalid data format"}), 400

    # Check if owner exists
    owner = next((user for user in mock_db["users"] if user["email"] == data["owner_email"]), None)
    if not owner:
        return jsonify({"error": "Owner not found"}), 404

    project = {
        "id": len(mock_db["projects"]) + 1,
        "title": data["title"],
        "description": data.get("description", ""),
        "owner_email": data["owner_email"]
    }
    mock_db["projects"].append(project)
    return jsonify(project), 201

# Endpoint to list all users
@app.route('/api/users', methods=['GET'])
def list_users():
    """
    Retrieve all registered users.
    """
    return jsonify(mock_db["users"]), 200

# Endpoint to list all projects
@app.route('/api/projects', methods=['GET'])
def list_projects():
    """
    Retrieve all projects.
    """
    return jsonify(mock_db["projects"]), 200

# Endpoint to retrieve user details by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve user details by ID.
    """
    user = next((user for user in mock_db["users"] if user["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Endpoint to retrieve project details by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve project details by ID.
    """
    project = next((project for project in mock_db["projects"] if project["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

if __name__ == '__main__':
    # Run the Flask server
    app.run(host='0.0.0.0', port=5000, debug=False)
```
