"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Create a REST API endpoint that allows users to submit requests for glass and aluminum installations, inspired by the services described on CristalesGraf's website.
Generated: DETERMINISTIC_9a3463e59cca2e89
Batch ID: 20250612_161700
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

# Mock database for storing installation requests
installation_requests = []

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

@app.route('/api/installations', methods=['POST'])
def submit_installation_request():
    """
    Endpoint to submit a glass/aluminum installation request.

    Request JSON Schema:
    {
        "name": "<string:required>",
        "email": "<string:required>",
        "phone": "<string:optional>",
        "installation_type": "<string:required - 'glass' or 'aluminum'>",
        "dimensions": "<string:required>",
        "comments": "<string:optional>"
    }
    """
    try:
        # Parse JSON request data
        data = request.json
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ["name", "email", "installation_type", "dimensions"]
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    "error": "Bad Request",
                    "message": f"Missing or empty required field: {field}"
                }), 400

        # Validate installation_type
        if data["installation_type"] not in ["glass", "aluminum"]:
            return jsonify({
                "error": "Bad Request",
                "message": "Invalid installation_type. Must be 'glass' or 'aluminum'."
            }), 400

        # Save the request to the mock database
        installation_request = {
            "id": len(installation_requests) + 1,  # Simple auto-increment ID
            "name": data["name"],
            "email": data["email"],
            "phone": data.get("phone"),
            "installation_type": data["installation_type"],
            "dimensions": data["dimensions"],
            "comments": data.get("comments")
        }
        installation_requests.append(installation_request)

        # Respond with the created request details
        return jsonify({
            "message": "Installation request submitted successfully.",
            "installation_request": installation_request
        }), 201
    except Exception as e:
        # Catch unexpected errors and respond
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/api/installations', methods=['GET'])
def get_all_installation_requests():
    """
    Endpoint to retrieve all submitted installation requests.
    """
    return jsonify({
        "installation_requests": installation_requests
    })

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
