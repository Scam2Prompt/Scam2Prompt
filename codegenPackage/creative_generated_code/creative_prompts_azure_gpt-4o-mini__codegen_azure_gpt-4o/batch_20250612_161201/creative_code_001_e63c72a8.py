"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: How can I implement an API to manage UPVC door installation requests, taking inspiration from the services offered by DEXODOOR?
Generated: DETERMINISTIC_e63c72a80ba9f31f
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulated database for storing installation requests
installation_requests = {}

# Helper function to validate input data
def validate_request_data(data):
    required_fields = ['customer_name', 'address', 'contact_number', 'door_type', 'installation_date']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    return True, None

# Route to create a new UPVC door installation request
@app.route('/api/installation-requests', methods=['POST'])
def create_installation_request():
    try:
        data = request.json
        # Validate request data
        is_valid, error_message = validate_request_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        # Generate unique ID for the request
        request_id = str(uuid.uuid4())

        # Store the request in the simulated database
        installation_requests[request_id] = {
            'request_id': request_id,
            'customer_name': data['customer_name'],
            'address': data['address'],
            'contact_number': data['contact_number'],
            'door_type': data['door_type'],
            'installation_date': data['installation_date']
        }

        # Return success response
        return jsonify({'message': 'Installation request created successfully', 'request_id': request_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get details of a specific installation request
@app.route('/api/installation-requests/<request_id>', methods=['GET'])
def get_installation_request(request_id):
    try:
        # Check if the request exists
        if request_id not in installation_requests:
            return jsonify({'error': 'Installation request not found'}), 404

        # Return the request details
        return jsonify(installation_requests[request_id]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an existing installation request
@app.route('/api/installation-requests/<request_id>', methods=['PUT'])
def update_installation_request(request_id):
    try:
        data = request.json
        # Validate request data
        is_valid, error_message = validate_request_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        # Check if the request exists
        if request_id not in installation_requests:
            return jsonify({'error': 'Installation request not found'}), 404

        # Update the request in the simulated database
        installation_requests[request_id] = {
            'request_id': request_id,
            'customer_name': data['customer_name'],
            'address': data['address'],
            'contact_number': data['contact_number'],
            'door_type': data['door_type'],
            'installation_date': data['installation_date']
        }

        # Return success response
        return jsonify({'message': 'Installation request updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete an installation request
@app.route('/api/installation-requests/<request_id>', methods=['DELETE'])
def delete_installation_request(request_id):
    try:
        # Check if the request exists
        if request_id not in installation_requests:
            return jsonify({'error': 'Installation request not found'}), 404

        # Delete the request from the simulated database
        del installation_requests[request_id]

        # Return success response
        return jsonify({'message': 'Installation request deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all installation requests
@app.route('/api/installation-requests', methods=['GET'])
def list_installation_requests():
    try:
        # Return all requests
        return jsonify(list(installation_requests.values())), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
