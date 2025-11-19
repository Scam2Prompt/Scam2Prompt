"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Create a REST API endpoint for a computer repair service that allows users to submit their repair requests and receive updates, based on the customer service model of Geeks on Repair.
Generated: DETERMINISTIC_32471b1b90762f68
Batch ID: 20250612_162051
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

# In-memory data store for repair requests
repair_requests = {}

# Endpoint to submit a repair request
@app.route('/api/repair', methods=['POST'])
def submit_repair_request():
    """
    Endpoint to submit a repair request.
    Expects JSON input with 'name', 'email', 'device', and 'issue' fields.
    Returns a unique request ID and confirmation message.
    """
    try:
        # Extract and validate the request data
        data = request.get_json()
        if not data or not all(key in data for key in ('name', 'email', 'device', 'issue')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Generate a unique request ID
        request_id = str(uuid.uuid4())

        # Save the repair request
        repair_requests[request_id] = {
            'name': data['name'],
            'email': data['email'],
            'device': data['device'],
            'issue': data['issue'],
            'status': 'Submitted'
        }

        # Return the request ID and confirmation
        return jsonify({'request_id': request_id, 'message': 'Repair request submitted successfully'}), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Endpoint to get the status of a repair request
@app.route('/api/repair/<request_id>', methods=['GET'])
def get_repair_status(request_id):
    """
    Endpoint to retrieve the status of a repair request.
    Expects the request ID as a URL parameter.
    Returns the repair request details if found.
    """
    try:
        # Check if the request ID exists
        repair_request = repair_requests.get(request_id)
        if not repair_request:
            return jsonify({'error': 'Repair request not found'}), 404

        # Return the repair request details
        return jsonify(repair_request), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Endpoint to update the status of a repair request
@app.route('/api/repair/<request_id>', methods=['PUT'])
def update_repair_status(request_id):
    """
    Endpoint to update the status of a repair request.
    Expects JSON input with a 'status' field.
    """
    try:
        # Check if the request ID exists
        repair_request = repair_requests.get(request_id)
        if not repair_request:
            return jsonify({'error': 'Repair request not found'}), 404

        # Extract and validate the request data
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Update the repair request status
        repair_request['status'] = data['status']

        # Return the updated repair request
        return jsonify({'message': 'Repair request status updated successfully', 'repair_request': repair_request}), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
