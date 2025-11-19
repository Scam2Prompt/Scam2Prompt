"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Create a RESTful API endpoint that allows users to submit requests for brick and stone restoration services, incorporating features like ventilation replacement and water repellant application mentioned on the Premier Pointing website.
Generated: DETERMINISTIC_068e41435907bd0f
Batch ID: 20250612_163423
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

# In-memory storage for service requests (for demonstration purposes)
service_requests = []

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the API.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/service-request', methods=['POST'])
def submit_service_request():
    """
    Endpoint to submit a service request for brick and stone restoration services.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'address', 'services']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Validate services field
        valid_services = ['brick_restoration', 'stone_restoration', 'ventilation_replacement', 'water_repellant_application']
        invalid_services = [service for service in data['services'] if service not in valid_services]
        if invalid_services:
            return jsonify({"error": f"Invalid services: {', '.join(invalid_services)}"}), 400

        # Create a new service request
        service_request = {
            "id": len(service_requests) + 1,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "address": data['address'],
            "services": data['services'],
            "comments": data.get('comments', '')  # Optional field
        }

        # Store the service request
        service_requests.append(service_request)

        # Return success response
        return jsonify({"message": "Service request submitted successfully", "request": service_request}), 201

    except Exception as e:
        # Catch any unexpected errors
        return handle_exception(e)

@app.route('/api/service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all submitted service requests.
    """
    return jsonify({"service_requests": service_requests}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code creates a RESTful API with two endpoints:
1. `/api/service-request` (POST) - Allows users to submit service requests.
2. `/api/service-requests` (GET) - Retrieves all submitted service requests.

It includes validation, error handling, and follows best practices for Flask-based APIs.
