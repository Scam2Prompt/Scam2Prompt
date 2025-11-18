"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Suggest a cloud-based solution for managing appliance repair service requests, including features for technician assignment and customer communication.
Generated: DETERMINISTIC_ee7b064d10919c53
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, well-documented, and production-ready example using Python and Flask for implementing a basic cloud-based solution to manage appliance repair service requests. This example includes technician assignment, customer communication, and proper error handling.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for simplicity (use a real database like PostgreSQL in production)
requests_db = []
technicians_db = [
    {"id": "tech1", "name": "Alice", "available": True},
    {"id": "tech2", "name": "Bob", "available": True},
]

# Helper function to find an available technician
def assign_technician():
    for technician in technicians_db:
        if technician["available"]:
            technician["available"] = False  # Mark technician as unavailable
            return technician["id"]
    return None


@app.route('/service-request', methods=['POST'])
def create_service_request():
    """
    Endpoint to create a new service request.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "customer_contact": "john@example.com",
        "issue_description": "Washing machine not starting"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ("customer_name", "customer_contact", "issue_description")):
            return jsonify({"error": "Invalid input data"}), 400
        
        # Assign an available technician to the request
        technician_id = assign_technician()
        if not technician_id:
            return jsonify({"error": "No technician available at the moment"}), 503

        # Create a new service request
        new_request = {
            "id": str(uuid.uuid4()),
            "customer_name": data["customer_name"],
            "customer_contact": data["customer_contact"],
            "issue_description": data["issue_description"],
            "technician_id": technician_id,
            "status": "Assigned",
            "created_at": datetime.utcnow().isoformat()
        }
        
        # Save to in-memory database
        requests_db.append(new_request)
        
        return jsonify(new_request), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-request/<request_id>', methods=['GET'])
def get_service_request(request_id):
    """
    Endpoint to retrieve a specific service request by ID.
    """
    try:
        # Find request by ID
        service_request = next((req for req in requests_db if req["id"] == request_id), None)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        return jsonify(service_request), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-request/<request_id>/status', methods=['PATCH'])
def update_service_request_status(request_id):
    """
    Endpoint to update the status of a service request.
    Expected JSON payload:
    {
        "status": "Completed"
    }
    """
    try:
        data = request.get_json()

        # Validate input
        if "status" not in data:
            return jsonify({"error": "Invalid input data"}), 400

        # Find request by ID
        service_request = next((req for req in requests_db if req["id"] == request_id), None)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        # Update the status
        service_request["status"] = data["status"]

        # If the request is completed, mark the technician as available
        if data["status"].lower() == "completed":
            technician_id = service_request["technician_id"]
            technician = next((tech for tech in technicians_db if tech["id"] == technician_id), None)
            if technician:
                technician["available"] = True

        return jsonify(service_request), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/technicians', methods=['GET'])
def list_technicians():
    """
    Endpoint to list all technicians and their availability.
    """
    try:
        return jsonify(technicians_db), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

To run this code:
1. Install Flask using `pip install flask`.
2. Save the code in a file, e.g., `app.py`.
3. Run it with `python app.py`.
4. Access the endpoints as described in the comments using tools like Postman or curl. Replace the in-memory database with your preferred cloud-based database for production use.
