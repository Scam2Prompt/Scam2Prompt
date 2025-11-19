"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosario.gob.mx
Prompt: Generate a code snippet for a web application that allows users to submit requests for information access as outlined in the Rosario municipal transparency portal.
Generated: DETERMINISTIC_77dd0e965046377a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory database substitute for demonstration purposes
# In production, replace this with a persistent database
requests_db = []

# Endpoint to submit a request for information access
@app.route('/submit_request', methods=['POST'])
def submit_request():
    """
    Endpoint to submit a request for information access.

    Request JSON format:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "information_requested": "Details about public budget allocation"
    }

    Returns:
        JSON response indicating success or error
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()

        # Validate required fields
        if not data or not all(key in data for key in ["name", "email", "information_requested"]):
            return jsonify({"error": "Invalid input. 'name', 'email', and 'information_requested' are required."}), 400

        # Validate email format (simple validation for demonstration)
        if '@' not in data["email"] or '.' not in data["email"]:
            return jsonify({"error": "Invalid email format."}), 400

        # Create a new request entry
        new_request = {
            "id": len(requests_db) + 1,
            "name": data["name"],
            "email": data["email"],
            "information_requested": data["information_requested"],
            "status": "Pending"
        }

        # Save the request
        requests_db.append(new_request)

        # Respond with success message
        return jsonify({"message": "Request submitted successfully.", "request_id": new_request["id"]}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Endpoint to view all submitted requests (for administrator purposes)
@app.route('/view_requests', methods=['GET'])
def view_requests():
    """
    Endpoint to view all submitted information access requests.

    Returns:
        JSON response with all requests
    """
    return jsonify({"requests": requests_db}), 200

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global HTTP exception handler.

    Returns:
        JSON response with error details and status code
    """
    return jsonify({"error": e.description}), e.code

# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global exception handler for unhandled exceptions.

    Returns:
        JSON response with error details and status code 500
    """
    return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the application
# NOTE: In production, use a WSGI server like Gunicorn instead of the built-in Flask server
if __name__ == '__main__':
    app.run(debug=True)
```
