"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Create a REST API endpoint for managing service requests related to garden and pool maintenance, inspired by the domestic services provided by Alphamor.
Generated: DETERMINISTIC_07dfc2ed75e6a4ff
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for service requests
service_requests = []
request_id_counter = 1

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

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new service request
@app.route('/service-requests', methods=['POST'])
def create_service_request():
    """
    Create a new service request for garden or pool maintenance.
    Expected JSON payload:
    {
        "type": "garden" or "pool",
        "description": "Details about the service request"
    }
    """
    global request_id_counter

    # Validate input
    data = request.get_json()
    if not data or 'type' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    if data['type'] not in ['garden', 'pool']:
        return jsonify({"error": "Bad Request", "message": "Invalid type. Must be 'garden' or 'pool'"}), 400

    # Create the service request
    new_request = {
        "id": request_id_counter,
        "type": data['type'],
        "description": data['description'],
        "status": "pending"  # Default status
    }
    service_requests.append(new_request)
    request_id_counter += 1

    return jsonify(new_request), 201

# Endpoint to retrieve all service requests
@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """
    Retrieve all service requests.
    """
    return jsonify(service_requests), 200

# Endpoint to retrieve a specific service request by ID
@app.route('/service-requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """
    Retrieve a specific service request by ID.
    """
    request_item = next((req for req in service_requests if req['id'] == request_id), None)
    if not request_item:
        return jsonify({"error": "Not Found", "message": "Service request not found"}), 404

    return jsonify(request_item), 200

# Endpoint to update the status of a service request
@app.route('/service-requests/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    """
    Update the status of a service request.
    Expected JSON payload:
    {
        "status": "pending", "in-progress", or "completed"
    }
    """
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    if data['status'] not in ['pending', 'in-progress', 'completed']:
        return jsonify({"error": "Bad Request", "message": "Invalid status. Must be 'pending', 'in-progress', or 'completed'"}), 400

    request_item = next((req for req in service_requests if req['id'] == request_id), None)
    if not request_item:
        return jsonify({"error": "Not Found", "message": "Service request not found"}), 404

    request_item['status'] = data['status']
    return jsonify(request_item), 200

# Endpoint to delete a service request
@app.route('/service-requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """
    Delete a specific service request by ID.
    """
    global service_requests
    request_item = next((req for req in service_requests if req['id'] == request_id), None)
    if not request_item:
        return jsonify({"error": "Not Found", "message": "Service request not found"}), 404

    service_requests = [req for req in service_requests if req['id'] != request_id]
    return jsonify({"message": "Service request deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
