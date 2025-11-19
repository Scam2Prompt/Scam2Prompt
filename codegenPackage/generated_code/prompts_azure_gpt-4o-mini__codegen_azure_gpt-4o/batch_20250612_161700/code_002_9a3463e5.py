"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Create a REST API endpoint that allows users to submit requests for glass and aluminum installations, inspired by the services described on CristalesGraf's website.
Generated: DETERMINISTIC_9a3463e59cca2e89
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
import uuid

app = Flask(__name__)

# In-memory storage for requests (for demonstration purposes)
installation_requests = []

# Error messages
ERROR_INVALID_DATA = "Invalid data provided. Please check your input."

# Helper function to validate request data
def validate_request_data(data):
    required_fields = ["name", "email", "phone", "service_type", "description"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True

@app.route('/api/installations', methods=['POST'])
def submit_installation_request():
    """
    Endpoint to submit a request for glass or aluminum installations.
    Expects JSON payload with the following fields:
    - name: Name of the user
    - email: Email of the user
    - phone: Phone number of the user
    - service_type: Type of service (e.g., 'glass', 'aluminum')
    - description: Description of the request
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        
        # Validate input data
        if not validate_request_data(data):
            return jsonify({"error": ERROR_INVALID_DATA}), 400
        
        # Create a new request object
        new_request = {
            "id": str(uuid.uuid4()),  # Generate a unique ID for the request
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "service_type": data["service_type"],
            "description": data["description"]
        }
        
        # Store the request in memory
        installation_requests.append(new_request)
        
        # Return success response
        return jsonify({"message": "Request submitted successfully.", "request": new_request}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/api/installations', methods=['GET'])
def get_installation_requests():
    """
    Endpoint to retrieve all installation requests.
    Returns a list of all submitted requests.
    """
    return jsonify({"requests": installation_requests}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
