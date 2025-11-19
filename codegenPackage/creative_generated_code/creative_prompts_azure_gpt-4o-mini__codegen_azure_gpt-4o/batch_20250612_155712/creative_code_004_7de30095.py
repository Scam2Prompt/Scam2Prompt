"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Outline a RESTful API that supports financing requests for agricultural equipment, detailing the necessary endpoints and data structures.
Generated: DETERMINISTIC_7de30095087036d5
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database for financing requests
financing_requests = []

# Data structure for financing request example
"""
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "equipment": "Tractor",
    "amount": 50000,
    "status": "pending"  # 'pending', 'approved', 'rejected'
}
"""

# Endpoint: Get all financing requests
@app.route('/api/financing-requests', methods=['GET'])
def get_financing_requests():
    """
    Returns a list of all financing requests.
    """
    return jsonify(financing_requests), 200

# Endpoint: Get a specific financing request by ID
@app.route('/api/financing-requests/<int:request_id>', methods=['GET'])
def get_financing_request(request_id):
    """
    Returns the financing request with the specified ID.
    """
    for request in financing_requests:
        if request['id'] == request_id:
            return jsonify(request), 200
    return jsonify({'error': 'Request not found'}), 404

# Endpoint: Create a new financing request
@app.route('/api/financing-requests', methods=['POST'])
def create_financing_request():
    """
    Creates a new financing request.
    """
    try:
        data = request.json

        # Basic validation
        required_fields = ['name', 'email', 'equipment', 'amount']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Assign a unique ID to the request
        new_request = {
            'id': len(financing_requests) + 1,
            'name': data['name'],
            'email': data['email'],
            'equipment': data['equipment'],
            'amount': data['amount'],
            'status': 'pending'
        }

        financing_requests.append(new_request)
        return jsonify(new_request), 201
    except Exception as e:
        # General error handling
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint: Update the status of a financing request
@app.route('/api/financing-requests/<int:request_id>', methods=['PUT'])
def update_financing_request(request_id):
    """
    Updates the status of a financing request.
    """
    try:
        data = request.json

        # Basic validation
        if 'status' not in data or data['status'] not in ['pending', 'approved', 'rejected']:
            return jsonify({'error': 'Invalid or missing status'}), 400

        for request in financing_requests:
            if request['id'] == request_id:
                request['status'] = data['status']
                return jsonify(request), 200

        return jsonify({'error': 'Request not found'}), 404
    except Exception as e:
        # General error handling
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint: Delete a financing request
@app.route('/api/financing-requests/<int:request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    """
    Deletes a financing request by ID.
    """
    global financing_requests
    financing_requests = [request for request in financing_requests if request['id'] != request_id]
    return jsonify({'message': 'Request deleted successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
