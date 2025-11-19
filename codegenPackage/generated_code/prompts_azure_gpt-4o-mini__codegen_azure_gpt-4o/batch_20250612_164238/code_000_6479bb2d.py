"""
Generated Code Metadata:
========================
Original URL: https://lsinterior.com.my
Prompt: Generate a code snippet for a web application that allows users to request home renovation services, including features for space planning and project management.
Generated: DETERMINISTIC_6479bb2d9d9dd5c1
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for simplicity (replace with a real database in production)
renovation_requests = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route to submit a renovation request
@app.route('/submit_request', methods=['POST'])
def submit_request():
    """
    Endpoint to submit a home renovation request.
    Expects JSON payload with 'name', 'email', 'space_details', and 'project_description'.
    """
    try:
        data = request.get_json()
        # Validate input
        if not all(key in data for key in ['name', 'email', 'space_details', 'project_description']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new request object
        new_request = {
            "id": len(renovation_requests) + 1,
            "name": data['name'],
            "email": data['email'],
            "space_details": data['space_details'],
            "project_description": data['project_description'],
            "status": "Pending"
        }
        renovation_requests.append(new_request)
        return jsonify({"message": "Request submitted successfully", "request": new_request}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all renovation requests
@app.route('/requests', methods=['GET'])
def get_requests():
    """
    Endpoint to retrieve all renovation requests.
    Returns a list of all requests in JSON format.
    """
    return jsonify({"requests": renovation_requests}), 200

# Route to update the status of a renovation request
@app.route('/update_status/<int:request_id>', methods=['PUT'])
def update_status(request_id):
    """
    Endpoint to update the status of a renovation request.
    Expects JSON payload with 'status'.
    """
    try:
        data = request.get_json()
        if 'status' not in data:
            return jsonify({"error": "Missing 'status' field"}), 400
        
        # Find the request by ID
        for req in renovation_requests:
            if req['id'] == request_id:
                req['status'] = data['status']
                return jsonify({"message": "Status updated successfully", "request": req}), 200
        
        return jsonify({"error": "Request not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a renovation request
@app.route('/delete_request/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    """
    Endpoint to delete a renovation request by ID.
    """
    try:
        global renovation_requests
        renovation_requests = [req for req in renovation_requests if req['id'] != request_id]
        return jsonify({"message": "Request deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
