"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: How can I implement an API to handle user project selection and urgency status in a telephony service application?
Generated: DETERMINISTIC_a92f811fba23b133
Batch ID: 20250612_163945
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

# In-memory storage for user projects and urgency status
user_projects = {}

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

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/api/projects', methods=['POST'])
def add_project():
    """
    Endpoint to add or update a user's project and urgency status.
    Expects JSON payload with 'user_id', 'project_name', and 'urgency_status'.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Invalid JSON payload"}), 400

        user_id = data.get('user_id')
        project_name = data.get('project_name')
        urgency_status = data.get('urgency_status')

        if not user_id or not project_name or not urgency_status:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        # Update or add the user's project and urgency status
        user_projects[user_id] = {
            "project_name": project_name,
            "urgency_status": urgency_status
        }

        return jsonify({"message": "Project added/updated successfully", "data": user_projects[user_id]}), 200
    except Exception as e:
        return handle_exception(e)

@app.route('/api/projects/<user_id>', methods=['GET'])
def get_project(user_id):
    """
    Endpoint to retrieve a user's project and urgency status by user_id.
    """
    try:
        if user_id not in user_projects:
            return jsonify({"error": "Not Found", "message": "User project not found"}), 404

        return jsonify({"data": user_projects[user_id]}), 200
    except Exception as e:
        return handle_exception(e)

@app.route('/api/projects/<user_id>', methods=['DELETE'])
def delete_project(user_id):
    """
    Endpoint to delete a user's project and urgency status by user_id.
    """
    try:
        if user_id not in user_projects:
            return jsonify({"error": "Not Found", "message": "User project not found"}), 404

        deleted_project = user_projects.pop(user_id)
        return jsonify({"message": "Project deleted successfully", "data": deleted_project}), 200
    except Exception as e:
        return handle_exception(e)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
