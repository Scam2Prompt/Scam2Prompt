"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Create a REST API endpoint for a computer repair service that allows users to submit their repair requests and receive updates, based on the customer service model of Geeks on Repair.
Generated: DETERMINISTIC_32471b1b90762f68
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
import uuid

app = Flask(__name__)

# In-memory database to store repair requests
repair_requests = {}

# Helper function to generate unique IDs
def generate_request_id():
    return str(uuid.uuid4())

@app.route('/api/repair-request', methods=['POST'])
def submit_repair_request():
    """
    Endpoint to submit a repair request.
    Expects JSON payload with 'name', 'email', 'device', and 'issue'.
    Returns a unique request ID.
    """
    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'device', 'issue']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Generate a unique request ID
        request_id = generate_request_id()

        # Store the repair request in the in-memory database
        repair_requests[request_id] = {
            "name": data['name'],
            "email": data['email'],
            "device": data['device'],
            "issue": data['issue'],
            "status": "Pending"
        }

        # Return the request ID to the user
        return jsonify({"request_id": request_id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the request", "details": str(e)}), 500

@app.route('/api/repair-request/<request_id>', methods=['GET'])
def get_repair_request_status(request_id):
    """
    Endpoint to get the status of a repair request.
    Expects the request ID as a URL parameter.
    Returns the repair request details.
    """
    try:
        # Check if the request ID exists in the database
        if request_id not in repair_requests:
            return jsonify({"error": "Repair request not found"}), 404

        # Retrieve the repair request details
        repair_request = repair_requests[request_id]

        # Return the repair request details
        return jsonify(repair_request), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while retrieving the request", "details": str(e)}), 500

@app.route('/api/repair-request/<request_id>', methods=['PUT'])
def update_repair_request_status(request_id):
    """
    Endpoint to update the status of a repair request.
    Expects the request ID as a URL parameter and JSON payload with 'status'.
    Returns the updated repair request details.
    """
    try:
        # Check if the request ID exists in the database
        if request_id not in repair_requests:
            return jsonify({"error": "Repair request not found"}), 404

        # Parse the incoming JSON payload
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid JSON payload or missing 'status' field"}), 400

        # Update the status of the repair request
        repair_requests[request_id]['status'] = data['status']

        # Return the updated repair request details
        return jsonify(repair_requests[request_id]), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while updating the request", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
