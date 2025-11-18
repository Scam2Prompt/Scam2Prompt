"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Generate a REST API for managing legal file financing requests, referencing Rhino Finance's "File Financing" service.
Generated: DETERMINISTIC_32a6c70188213831
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A Flask-based REST API for managing legal file financing requests.
# The API interacts with Rhino Finance's "File Financing" service.

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for demonstration purposes
financing_requests = {}

class FinancingRequest:
    def __init__(self, client_name, case_id, requested_amount):
        self.request_id = str(uuid.uuid4())  # Generate a unique ID
        self.client_name = client_name
        self.case_id = case_id
        self.requested_amount = requested_amount
        self.status = "Pending"  # Default status

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "client_name": self.client_name,
            "case_id": self.case_id,
            "requested_amount": self.requested_amount,
            "status": self.status
        }

@app.route('/financing-requests', methods=['POST'])
def create_financing_request():
    """
    Create a new legal file financing request.
    Expects a JSON payload with client_name, case_id, and requested_amount.
    """
    try:
        data = request.get_json()
        client_name = data.get("client_name")
        case_id = data.get("case_id")
        requested_amount = data.get("requested_amount")

        # Validate input
        if not client_name or not case_id or not requested_amount:
            return jsonify({"error": "Missing required fields"}), 400

        # Create and store the financing request
        financing_request = FinancingRequest(client_name, case_id, requested_amount)
        financing_requests[financing_request.request_id] = financing_request

        return jsonify(financing_request.to_dict()), 201  # Return the created request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle unexpected errors

@app.route('/financing-requests/<request_id>', methods=['GET'])
def get_financing_request(request_id):
    """
    Retrieve a specific financing request by its ID.
    """
    try:
        financing_request = financing_requests.get(request_id)
        if not financing_request:
            return jsonify({"error": "Request not found"}), 404

        return jsonify(financing_request.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/financing-requests/<request_id>', methods=['PUT'])
def update_financing_request(request_id):
    """
    Update the status of a financing request.
    Expects a JSON payload with the 'status' field.
    """
    try:
        financing_request = financing_requests.get(request_id)
        if not financing_request:
            return jsonify({"error": "Request not found"}), 404

        data = request.get_json()
        new_status = data.get("status")

        # Validate input
        if not new_status:
            return jsonify({"error": "Missing 'status' field"}), 400

        # Update the financing request's status
        financing_request.status = new_status
        return jsonify(financing_request.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/financing-requests/<request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    """
    Delete a specific financing request by its ID.
    """
    try:
        if request_id not in financing_requests:
            return jsonify({"error": "Request not found"}), 404

        # Remove the financing request
        del financing_requests[request_id]
        return jsonify({"message": "Request deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(host='0.0.0.0', port=5000)
```

Note: This code assumes Flask is installed. Before running, install Flask using `pip install flask`. For production, consider deploying using a WSGI server like Gunicorn and configuring appropriate security measures (e.g., input validation, authentication).
