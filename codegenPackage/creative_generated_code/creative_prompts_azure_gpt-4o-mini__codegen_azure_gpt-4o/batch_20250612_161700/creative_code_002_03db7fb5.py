"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Create an API endpoint for managing plumbing service requests, including features like leak detection and urgent repairs, based on the offerings of ERA Engineering.
Generated: DETERMINISTIC_03db7fb54c57ae6f
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

app = Flask(__name__)

# In-memory database to store plumbing service requests
service_requests = []


@app.route('/service-requests', methods=['POST'])
def create_service_request():
    """
    API endpoint to create a new plumbing service request.
    """
    try:
        data = request.json

        # Validate input
        if not data.get('customer_name') or not data.get('service_type'):
            return jsonify({"error": "Missing required fields: customer_name or service_type"}), 400

        # Add service request to the database
        service_request = {
            "id": len(service_requests) + 1,
            "customer_name": data['customer_name'],
            "contact_number": data.get('contact_number'),
            "service_type": data['service_type'],  # e.g., 'leak_detection', 'urgent_repair'
            "address": data.get('address'),
            "status": "Pending",  # Default status
        }
        service_requests.append(service_request)

        return jsonify(service_request), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """
    API endpoint to get details of a specific plumbing service request.
    """
    try:
        # Find the service request by ID
        service_request = next((req for req in service_requests if req["id"] == request_id), None)

        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        return jsonify(service_request), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-requests/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    """
    API endpoint to update details of a specific plumbing service request.
    """
    try:
        data = request.json

        # Find the service request by ID
        service_request = next((req for req in service_requests if req["id"] == request_id), None)

        if not service_request:
            return jsonify({"error": "Service request not found"}), 404

        # Update the service request fields
        if data.get('customer_name'):
            service_request['customer_name'] = data['customer_name']
        if data.get('contact_number'):
            service_request['contact_number'] = data['contact_number']
        if data.get('service_type'):
            service_request['service_type'] = data['service_type']
        if data.get('address'):
            service_request['address'] = data['address']
        if data.get('status'):
            service_request['status'] = data['status']

        return jsonify(service_request), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """
    API endpoint to delete a plumbing service request.
    """
    try:
        # Find the service request by ID
        global service_requests
        service_requests = [req for req in service_requests if req["id"] != request_id]

        return jsonify({"message": "Service request deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/service-requests', methods=['GET'])
def list_service_requests():
    """
    API endpoint to list all plumbing service requests.
    """
    try:
        return jsonify(service_requests), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
