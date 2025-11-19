"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: What are the best practices for setting up a service request API for air conditioning repairs and installations?
Generated: DETERMINISTIC_5498660ec8cac111
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data storage for service requests (replace with a database in production)
service_requests = []

# Status options for service requests
STATUS_OPTIONS = {"pending", "in_progress", "completed", "cancelled"}

# Helper function to validate service request data
def validate_request_data(data):
    required_fields = ["name", "contact", "address", "service_type", "description"]
    for field in required_fields:
        if field not in data or not data[field]:
            return f"Missing or invalid field: {field}"
    if data["service_type"] not in {"repair", "installation"}:
        return "Invalid service type. Must be 'repair' or 'installation'."
    return None

@app.route("/api/service-request", methods=["POST"])
def create_service_request():
    """
    Create a new service request for air conditioning repair or installation.
    """
    try:
        # Parse JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON data expected"}), 400

        # Validate the input data
        validation_error = validate_request_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Generate a unique ID for the service request
        request_id = str(uuid.uuid4())

        # Create a new service request object
        new_request = {
            "id": request_id,
            "name": data["name"],
            "contact": data["contact"],
            "address": data["address"],
            "service_type": data["service_type"],
            "description": data["description"],
            "status": "pending",
            "created_at": datetime.utcnow().isoformat(),
        }

        # Add the new service request to the storage
        service_requests.append(new_request)

        return jsonify({"message": "Service request created successfully", "request": new_request}), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/api/service-request/<string:request_id>", methods=["GET"])
def get_service_request(request_id):
    """
    Retrieve the details of a specific service request by ID.
    """
    try:
        # Find the service request by ID
        service_request = next((req for req in service_requests if req["id"] == request_id), None)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        return jsonify({"request": service_request}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/api/service-request/<string:request_id>", methods=["PUT"])
def update_service_request(request_id):
    """
    Update the status or details of a specific service request by ID.
    """
    try:
        # Parse JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON data expected"}), 400

        # Find the service request by ID
        service_request = next((req for req in service_requests if req["id"] == request_id), None)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        # Update fields if provided
        if "status" in data:
            if data["status"] not in STATUS_OPTIONS:
                return jsonify({"error": f"Invalid status. Must be one of {STATUS_OPTIONS}"}), 400
            service_request["status"] = data["status"]
        if "description" in data:
            service_request["description"] = data["description"]

        return jsonify({"message": "Service request updated successfully", "request": service_request}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/api/service-request/<string:request_id>", methods=["DELETE"])
def delete_service_request(request_id):
    """
    Delete a specific service request by ID.
    """
    try:
        # Find the service request by ID
        service_request = next((req for req in service_requests if req["id"] == request_id), None)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        # Remove the service request from storage
        service_requests.remove(service_request)

        return jsonify({"message": "Service request deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask application
    # In production, use a proper WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```
