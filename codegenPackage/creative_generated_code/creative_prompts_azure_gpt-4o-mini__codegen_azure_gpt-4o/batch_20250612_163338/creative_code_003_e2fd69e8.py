"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Develop a RESTful API endpoint that retrieves service details related to sustainable architecture and historical building preservation from Inaka Revive Solutions.
Generated: DETERMINISTIC_e2fd69e8e6d4994d
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Python code using Flask to create a RESTful API endpoint. It includes proper error handling, best practices, and detailed comments.

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Simulated database for service details
SERVICE_DETAILS = {
    "sustainable_architecture": {
        "id": 1,
        "name": "Sustainable Architecture",
        "description": "Design and implementation of energy-efficient and environmentally friendly structures.",
        "contact_email": "info@inakarevive.com"
    },
    "historical_building_preservation": {
        "id": 2,
        "name": "Historical Building Preservation",
        "description": "Restoration and preservation of culturally significant historical buildings.",
        "contact_email": "preservation@inakarevive.com"
    }
}

@app.route('/api/service-details/<service_name>', methods=['GET'])
def get_service_details(service_name):
    """
    RESTful API endpoint to retrieve service details.

    Args:
        service_name (str): The name of the service to retrieve details for.

    Returns:
        JSON response with service details or an error message.
    """
    try:
        # Validate input
        if not service_name:
            return jsonify({"error": "Service name is required"}), 400

        # Retrieve service details
        service = SERVICE_DETAILS.get(service_name.lower())
        if service:
            return jsonify(service), 200
        else:
            return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        # Return a generic error message for unexpected exceptions
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(exception):
    """
    Global HTTP exception handler.

    Args:
        exception (HTTPException): The exception instance.

    Returns:
        JSON response with error details and status code.
    """
    return jsonify({"error": exception.description}), exception.code

@app.errorhandler(Exception)
def handle_generic_exception(exception):
    """
    Global exception handler for uncaught errors.

    Args:
        exception (Exception): The exception instance.

    Returns:
        JSON response with error details and 500 status code.
    """
    return jsonify({"error": "Internal Server Error", "details": str(exception)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Features:
- **GET Endpoint**: `/api/service-details/<service_name>` retrieves service details based on the provided service name.
- **Error Handling**: Handles missing parameters, unknown services, HTTP exceptions, and uncaught errors.
- **Production-ready**: Includes detailed comments and adheres to Flask best practices.
