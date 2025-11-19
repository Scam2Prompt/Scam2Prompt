"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Create an API endpoint for a car repair service that allows users to request services such as engine repair, AC repair, and body shop services, inspired by the features of Mechanics.ae.
Generated: DETERMINISTIC_49e548d88882bbbc
Batch ID: 20250612_160804
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

# In-memory storage to simulate a database for service requests
service_requests = []

# Available services
AVAILABLE_SERVICES = ["engine repair", "AC repair", "body shop"]

@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to request a car repair service.
    Expected JSON format:
    {
        "customer_name": "John Doe",
        "contact_number": "1234567890",
        "service_type": "engine repair",
        "car_model": "Toyota Corolla",
        "additional_details": "Check engine light is on"
    }
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Validate required fields
        required_fields = ["customer_name", "contact_number", "service_type", "car_model"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Validate service type
        service_type = data.get("service_type")
        if service_type not in AVAILABLE_SERVICES:
            return jsonify({
                "error": f"Invalid service_type. Available options are: {', '.join(AVAILABLE_SERVICES)}"
            }), 400

        # Create service request entry
        service_request = {
            "id": len(service_requests) + 1,  # Auto-increment ID
            "customer_name": data["customer_name"],
            "contact_number": data["contact_number"],
            "service_type": service_type,
            "car_model": data["car_model"],
            "additional_details": data.get("additional_details", ""),  # Optional field
            "status": "Pending"  # Default status
        }
        service_requests.append(service_request)

        # Respond with the created service request
        return jsonify({"message": "Service request created successfully", "service_request": service_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/get-service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all service requests.
    """
    return jsonify({"service_requests": service_requests}), 200


@app.route('/update-service-status/<int:request_id>', methods=['PATCH'])
def update_service_status(request_id):
    """
    Endpoint to update the status of a service request.
    Expected JSON format:
    {
        "status": "Completed"  # Valid statuses: Pending, In Progress, Completed
    }
    """
    try:
        data = request.get_json()
        
        if not data or "status" not in data:
            return jsonify({"error": "Invalid JSON format or missing 'status' field"}), 400
        
        valid_statuses = ["Pending", "In Progress", "Completed"]
        new_status = data["status"]

        if new_status not in valid_statuses:
            return jsonify({"error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"}), 400

        # Find the service request by ID
        for service_request in service_requests:
            if service_request["id"] == request_id:
                service_request["status"] = new_status
                return jsonify({"message": "Service request status updated successfully", "service_request": service_request}), 200

        return jsonify({"error": "Service request not found"}), 404

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
