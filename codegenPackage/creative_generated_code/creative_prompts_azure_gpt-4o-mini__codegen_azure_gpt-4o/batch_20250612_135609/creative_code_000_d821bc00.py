"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehemacare.com
Prompt: Generate a code snippet for a web application that allows users to request personalized healthcare services like Attendant Care and Habilitation from Rehema Care LLC.
Generated: DETERMINISTIC_d821bc003915cd0c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for storing service requests
# In production, this would be replaced with a proper database
service_requests = []

# Define available healthcare services
AVAILABLE_SERVICES = ["Attendant Care", "Habilitation"]

@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint for users to request personalized healthcare services.

    Request JSON should include:
    - "name": Name of the user (string)
    - "email": User's email address (string)
    - "service": Requested service (string, must be in AVAILABLE_SERVICES)
    - "details": Additional details about the request (string, optional)
    """

    try:
        # Parse the incoming request JSON
        data = request.get_json()

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        service = data.get('service')
        details = data.get('details', '')

        if not name or not email or not service:
            return jsonify({"error": "Missing required fields: name, email, and service"}), 400

        if service not in AVAILABLE_SERVICES:
            return jsonify({"error": f"Invalid service. Available services are: {AVAILABLE_SERVICES}"}), 400

        # Create a new service request
        service_request = {
            "id": len(service_requests) + 1,  # Auto-increment ID
            "name": name,
            "email": email,
            "service": service,
            "details": details
        }

        # Store the request in the in-memory database
        service_requests.append(service_request)

        # Return success response
        return jsonify({"message": "Service request submitted successfully", "request": service_request}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/services', methods=['GET'])
def get_available_services():
    """
    Endpoint to retrieve the list of available healthcare services.
    """
    return jsonify({"services": AVAILABLE_SERVICES}), 200

@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all submitted service requests.
    """
    return jsonify({"service_requests": service_requests}), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
