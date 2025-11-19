"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Create a REST API endpoint that handles plumbing service requests, including validation for residential and commercial plumbing needs.
Generated: DETERMINISTIC_2e6feab0acaef3c0
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

# Sample data structure to store service requests
service_requests = []

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

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Validation function for service requests
def validate_request(data):
    required_fields = ["name", "email", "phone", "address", "service_type", "description"]
    if not all(field in data for field in required_fields):
        return False, f"Missing required fields: {', '.join([field for field in required_fields if field not in data])}"
    
    if data["service_type"] not in ["residential", "commercial"]:
        return False, "Invalid service_type. Must be 'residential' or 'commercial'."
    
    return True, None

# REST API endpoint to handle plumbing service requests
@app.route('/api/plumbing-service', methods=['POST'])
def create_service_request():
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400
        
        # Validate request data
        is_valid, error_message = validate_request(data)
        if not is_valid:
            return jsonify({"error": "Bad Request", "message": error_message}), 400
        
        # Create a new service request
        service_request = {
            "id": len(service_requests) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "address": data["address"],
            "service_type": data["service_type"],
            "description": data["description"]
        }
        service_requests.append(service_request)
        
        # Return success response
        return jsonify({"message": "Service request created successfully", "data": service_request}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
