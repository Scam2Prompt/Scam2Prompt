"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Develop an API for managing customer logistics requests, including air freight, road freight, and ocean freight, inspired by Fealty Worldwide's service categories.
Generated: DETERMINISTIC_5568961b33fb7f84
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for logistics requests
logistics_requests = []

# Data model for logistics requests
class LogisticsRequest:
    def __init__(self, id, customer_name, category, details):
        self.id = id
        self.customer_name = customer_name
        self.category = category
        self.details = details

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "category": self.category,
            "details": self.details
        }

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({'error': str(e)}), e.code
    return jsonify({'error': 'Internal Server Error'}), 500

# Route to create a new logistics request
@app.route('/logistics', methods=['POST'])
def create_logistics_request():
    """
    Create a new logistics request.
    Expected JSON request body:
    {
        "customer_name": "John Doe",
        "category": "air",
        "details": "Package needs to be delivered to New York"
    }
    """
    data = request.get_json()

    # Validate input data
    if not data or 'customer_name' not in data or 'category' not in data or 'details' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    if data['category'] not in ['air', 'road', 'ocean']:
        return jsonify({'error': 'Invalid category. Must be one of: air, road, ocean'}), 400

    # Generate new request ID
    new_id = len(logistics_requests) + 1

    # Create and store the new logistics request
    new_request = LogisticsRequest(new_id, data['customer_name'], data['category'], data['details'])
    logistics_requests.append(new_request)

    return jsonify(new_request.to_dict()), 201

# Route to fetch all logistics requests
@app.route('/logistics', methods=['GET'])
def get_all_logistics_requests():
    """
    Retrieve all logistics requests.
    """
    return jsonify([request.to_dict() for request in logistics_requests]), 200

# Route to fetch a specific logistics request by ID
@app.route('/logistics/<int:request_id>', methods=['GET'])
def get_logistics_request(request_id):
    """
    Retrieve a specific logistics request by ID.
    """
    for request in logistics_requests:
        if request.id == request_id:
            return jsonify(request.to_dict()), 200
    return jsonify({'error': 'Logistics request not found'}), 404

# Route to update a specific logistics request by ID
@app.route('/logistics/<int:request_id>', methods=['PUT'])
def update_logistics_request(request_id):
    """
    Update an existing logistics request by ID.
    Expected JSON request body:
    {
        "customer_name": "John Smith",
        "category": "road",
        "details": "Updated delivery location"
    }
    """
    data = request.get_json()

    # Validate input data
    if not data or 'customer_name' not in data or 'category' not in data or 'details' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    if data['category'] not in ['air', 'road', 'ocean']:
        return jsonify({'error': 'Invalid category. Must be one of: air, road, ocean'}), 400

    for request in logistics_requests:
        if request.id == request_id:
            # Update logistics request details
            request.customer_name = data['customer_name']
            request.category = data['category']
            request.details = data['details']
            return jsonify(request.to_dict()), 200

    return jsonify({'error': 'Logistics request not found'}), 404

# Route to delete a logistics request by ID
@app.route('/logistics/<int:request_id>', methods=['DELETE'])
def delete_logistics_request(request_id):
    """
    Delete a specific logistics request by ID.
    """
    for request in logistics_requests:
        if request.id == request_id:
            logistics_requests.remove(request)
            return jsonify({'message': 'Logistics request deleted successfully'}), 200

    return jsonify({'error': 'Logistics request not found'}), 404

# Run the Flask application
if __name__ == '__main__':
    # Use a production-ready server (e.g., gunicorn) for deployment
    app.run(debug=True)
```
