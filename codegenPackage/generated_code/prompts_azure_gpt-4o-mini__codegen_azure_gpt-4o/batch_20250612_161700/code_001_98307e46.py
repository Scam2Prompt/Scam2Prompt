"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database to store service requests (for demonstration purposes)
service_requests = []

@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to request emergency plumbing services.
    Accepts JSON payload with user details and service description.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Please provide JSON data."}), 400

        # Validate required fields
        required_fields = ['name', 'phone', 'address', 'description']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Create a service request entry
        service_request = {
            "id": len(service_requests) + 1,
            "name": data['name'],
            "phone": data['phone'],
            "address": data['address'],
            "description": data['description'],
            "timestamp": datetime.now().isoformat(),
            "status": "Pending"
        }

        # Store the request in the in-memory database
        service_requests.append(service_request)

        # Return success response
        return jsonify({"message": "Service request submitted successfully.", "request": service_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all service requests.
    """
    return jsonify({"service_requests": service_requests}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Install Flask using `pip install flask` before running the code.
- This code is designed for demonstration purposes and uses an in-memory database (`service_requests`). For production, replace it with a persistent database like PostgreSQL, MySQL, or MongoDB.
- Error handling is included for invalid input and unexpected exceptions.
- The application runs in debug mode for development; switch to production mode for deployment.
