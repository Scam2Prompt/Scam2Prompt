"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Create a REST API that allows users to request services related to hospital equipment installation, referencing AKNAN's expertise in flame retardant and antibacterial curtains.
Generated: DETERMINISTIC_cf6dadc6e604e59b
Batch ID: 20250612_163442
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

# In-memory database to store service requests
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

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to create a new service request
@app.route('/api/service-request', methods=['POST'])
def create_service_request():
    """
    Endpoint to create a new service request.
    Expects JSON payload with 'name', 'email', 'phone', and 'details'.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'details']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Bad Request", "message": f"Missing field: {field}"}), 400

        # Create a new service request
        service_request = {
            "id": len(service_requests) + 1,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "details": data['details'],
            "status": "Pending"
        }
        service_requests.append(service_request)

        return jsonify({"message": "Service request created successfully", "service_request": service_request}), 201
    except Exception as e:
        return handle_exception(e)

# Route to retrieve all service requests
@app.route('/api/service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all service requests.
    """
    return jsonify({"service_requests": service_requests}), 200

# Route to retrieve a specific service request by ID
@app.route('/api/service-request/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """
    Endpoint to retrieve a specific service request by ID.
    """
    service_request = next((req for req in service_requests if req['id'] == request_id), None)
    if not service_request:
        return jsonify({"error": "Not Found", "message": "Service request not found"}), 404
    return jsonify({"service_request": service_request}), 200

# Route to update the status of a service request
@app.route('/api/service-request/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    """
    Endpoint to update the status of a service request.
    Expects JSON payload with 'status'.
    """
    try:
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": "Bad Request", "message": "Request body must contain 'status'"}), 400

        service_request = next((req for req in service_requests if req['id'] == request_id), None)
        if not service_request:
            return jsonify({"error": "Not Found", "message": "Service request not found"}), 404

        # Update the status of the service request
        service_request['status'] = data['status']
        return jsonify({"message": "Service request updated successfully", "service_request": service_request}), 200
    except Exception as e:
        return handle_exception(e)

# Route to delete a service request
@app.route('/api/service-request/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """
    Endpoint to delete a service request by ID.
    """
    global service_requests
    service_request = next((req for req in service_requests if req['id'] == request_id), None)
    if not service_request:
        return jsonify({"error": "Not Found", "message": "Service request not found"}), 404

    service_requests = [req for req in service_requests if req['id'] != request_id]
    return jsonify({"message": "Service request deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
