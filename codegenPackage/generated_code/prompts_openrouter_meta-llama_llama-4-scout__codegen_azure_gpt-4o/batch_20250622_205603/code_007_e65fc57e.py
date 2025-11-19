"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Design a RESTful API to manage renovation services, including endpoints for creating service requests, estimating costs, and tracking project progress, inspired by the functionalities implied on the ПАНАМ website."
Generated: DETERMINISTIC_e65fc57ea372a120
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for demonstration purposes
service_requests = {}

# Helper function to calculate cost estimation
def calculate_cost_estimation(service_type, area_size):
    base_cost = {
        "painting": 10,  # cost per square meter
        "flooring": 20,
        "plumbing": 30,
    }
    return base_cost.get(service_type, 0) * area_size

# Endpoint: Create a new service request
@app.route('/service-requests', methods=['POST'])
def create_service_request():
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ("customer_name", "service_type", "area_size")):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Generate a unique ID for the service request
        request_id = str(uuid4())
        service_requests[request_id] = {
            "customer_name": data["customer_name"],
            "service_type": data["service_type"],
            "area_size": data["area_size"],
            "cost_estimation": calculate_cost_estimation(data["service_type"], data["area_size"]),
            "status": "Pending",
        }
        return jsonify({"message": "Service request created", "request_id": request_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get cost estimation for a service request
@app.route('/service-requests/<request_id>/cost-estimation', methods=['GET'])
def get_cost_estimation(request_id):
    try:
        service_request = service_requests.get(request_id)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404
        
        return jsonify({"cost_estimation": service_request["cost_estimation"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Update project progress
@app.route('/service-requests/<request_id>/progress', methods=['PATCH'])
def update_project_progress(request_id):
    try:
        data = request.json
        service_request = service_requests.get(request_id)
        if not service_request:
            return jsonify({"error": "Service request not found"}), 404
        
        # Validate input
        if "status" not in data:
            return jsonify({"error": "Missing required field: status"}), 400
        
        # Update the status of the service request
        service_request["status"] = data["status"]
        return jsonify({"message": "Project progress updated", "status": service_request["status"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get all service requests
@app.route('/service-requests', methods=['GET'])
def get_all_service_requests():
    try:
        return jsonify(service_requests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
