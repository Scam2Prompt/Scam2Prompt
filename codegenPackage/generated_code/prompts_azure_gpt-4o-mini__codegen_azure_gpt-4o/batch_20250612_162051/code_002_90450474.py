"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Create a REST API endpoint that allows users to submit their carpentry project details, inspired by the services provided by Aluivars in Altea.
Generated: DETERMINISTIC_9045047439b2d3ea
Batch ID: 20250612_162051
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

# In-memory storage for carpentry projects (for demonstration purposes)
carpentry_projects = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).data
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

@app.route('/api/carpentry-projects', methods=['POST'])
def submit_carpentry_project():
    """
    Endpoint to submit carpentry project details.
    Expects a JSON payload with the following fields:
    - project_name (string): Name of the project
    - client_name (string): Name of the client
    - description (string): Description of the project
    - deadline (string): Deadline for the project in ISO 8601 format (e.g., "2023-12-31")
    - budget (float): Budget for the project

    Returns:
    - 201 Created: If the project is successfully submitted
    - 400 Bad Request: If the input data is invalid
    """
    try:
        # Parse JSON payload
        data = request.get_json()

        # Validate required fields
        required_fields = ['project_name', 'client_name', 'description', 'deadline', 'budget']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": "Bad Request",
                    "description": f"Missing required field: {field}"
                }), 400

        # Validate data types
        if not isinstance(data['project_name'], str) or not data['project_name'].strip():
            return jsonify({
                "error": "Bad Request",
                "description": "Invalid project_name. It must be a non-empty string."
            }), 400
        if not isinstance(data['client_name'], str) or not data['client_name'].strip():
            return jsonify({
                "error": "Bad Request",
                "description": "Invalid client_name. It must be a non-empty string."
            }), 400
        if not isinstance(data['description'], str) or not data['description'].strip():
            return jsonify({
                "error": "Bad Request",
                "description": "Invalid description. It must be a non-empty string."
            }), 400
        if not isinstance(data['deadline'], str):  # Additional date format validation can be added
            return jsonify({
                "error": "Bad Request",
                "description": "Invalid deadline. It must be a string in ISO 8601 format."
            }), 400
        if not isinstance(data['budget'], (int, float)) or data['budget'] <= 0:
            return jsonify({
                "error": "Bad Request",
                "description": "Invalid budget. It must be a positive number."
            }), 400

        # Add project to in-memory storage
        project_id = len(carpentry_projects) + 1
        project = {
            "id": project_id,
            "project_name": data['project_name'],
            "client_name": data['client_name'],
            "description": data['description'],
            "deadline": data['deadline'],
            "budget": data['budget']
        }
        carpentry_projects.append(project)

        # Return success response
        return jsonify({
            "message": "Carpentry project submitted successfully.",
            "project": project
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "Internal Server Error",
            "description": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
