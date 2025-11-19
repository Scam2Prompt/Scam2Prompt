"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Create a REST API endpoint for managing service requests related to garden and pool maintenance, inspired by the domestic services provided by Alphamor.
Generated: DETERMINISTIC_07dfc2ed75e6a4ff
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

# Mock database (in-memory storage)
service_requests = []
service_request_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Endpoint to create a new service request
@app.route('/service-requests', methods=['POST'])
def create_service_request():
    """
    Create a new service request.
    Expected JSON format:
    {
        "type": "garden" or "pool",
        "description": "short description of the service needed"
    }
    """
    global service_request_id_counter
    
    try:
        data = request.get_json()
        
        # Validate request data
        if not data or "type" not in data or "description" not in data:
            return jsonify({"error": "Invalid request data"}), 400
        
        if data["type"] not in ["garden", "pool"]:
            return jsonify({"error": "Invalid service type"}), 400
        
        # Create new service request
        new_request = {
            "id": service_request_id_counter,
            "type": data["type"],
            "description": data["description"]
        }
        service_requests.append(new_request)
        service_request_id_counter += 1
        
        return jsonify(new_request), 201
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to get all service requests
@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """
    Retrieve all service requests.
    """
    return jsonify(service_requests), 200

# Endpoint to get a specific service request by ID
@app.route('/service-requests/<int:request_id>', methods=['GET'])
def get_service_request_by_id(request_id):
    """
    Retrieve a specific service request by its ID.
    """
    try:
        for request in service_requests:
            if request["id"] == request_id:
                return jsonify(request), 200
        
        return jsonify({"error": "Service request not found"}), 404
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to delete a service request by ID
@app.route('/service-requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """
    Delete a service request by its ID.
    """
    try:
        global service_requests
        for i, request in enumerate(service_requests):
            if request["id"] == request_id:
                del service_requests[i]
                return jsonify({"message": "Service request deleted"}), 200
        
        return jsonify({"error": "Service request not found"}), 404
    except Exception as e:
        return handle_generic_exception(e)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
