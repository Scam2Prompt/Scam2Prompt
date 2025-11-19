"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clarkconstructionllc.net
Prompt: Create a RESTful API endpoint that captures customer details for custom deck and patio designs, inspired by the services provided by Clark Construction LLC.
Generated: DETERMINISTIC_09fdfccb028e4552
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# In-memory storage (for demonstration purposes)
# In production, replace with a database (e.g., PostgreSQL, MySQL, MongoDB)
customer_requests = []

# Utility function for custom error handling
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return structured error responses."""
    if isinstance(e, HTTPException):
        response = {
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }
    else:
        response = {
            "error": "Internal Server Error",
            "message": str(e),
            "status_code": 500
        }
    return jsonify(response), response["status_code"]

# Route to capture customer details
@app.route('/api/custom-deck-patio', methods=['POST'])
def capture_customer_details():
    """
    Endpoint to capture customer details for custom deck and patio designs.
    Expected input: JSON payload with customer details.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'design_preference', 'budget']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": "Validation Error",
                    "message": f"The field '{field}' is required."
                }), 400

        # Validate email format (basic validation)
        if '@' not in data['email']:
            return jsonify({
                "error": "Validation Error",
                "message": "Invalid email format."
            }), 400

        # Add new customer request to in-memory storage
        customer_requests.append(data)

        # Return success response
        return jsonify({
            "message": "Customer details captured successfully.",
            "data": data
        }), 201

    except Exception as e:
        # Handle unexpected errors
        raise e

# Route to retrieve all customer requests (for admin purposes)
@app.route('/api/custom-deck-patio/requests', methods=['GET'])
def get_customer_requests():
    """
    Endpoint to retrieve all customer requests.
    Admin-only functionality for production use.
    """
    try:
        return jsonify({
            "message": "Customer requests retrieved successfully.",
            "data": customer_requests
        }), 200

    except Exception as e:
        # Handle unexpected errors
        raise e

# Main entry point to run the Flask app
if __name__ == '__main__':
    # Start the Flask application
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=True, host='0.0.0.0', port=5000)
```
