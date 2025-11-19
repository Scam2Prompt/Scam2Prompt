"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: "Develop a RESTful API to manage and track shipments across different modes of transportation, inspired by Fealty Worldwide's services."
Generated: DETERMINISTIC_5ca166ee9122037b
Batch ID: 20250622_205227
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

# In-memory database for shipments
shipments = {}

# Error handling helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route: Get all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    """
    Retrieve all shipments.
    """
    return jsonify(list(shipments.values())), 200

# Route: Get a specific shipment by ID
@app.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    """
    Retrieve a shipment by its ID.
    """
    shipment = shipments.get(shipment_id)
    if not shipment:
        return error_response("Shipment not found", 404)
    return jsonify(shipment), 200

# Route: Create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    """
    Create a new shipment.
    """
    data = request.json
    # Validate input
    if not data or 'mode_of_transport' not in data or 'origin' not in data or 'destination' not in data:
        return error_response("Invalid input. Required fields: mode_of_transport, origin, destination.")
    
    shipment_id = str(uuid4())  # Generate unique ID for the shipment
    shipment = {
        "id": shipment_id,
        "mode_of_transport": data['mode_of_transport'],
        "origin": data['origin'],
        "destination": data['destination'],
        "status": "Pending"  # Default status
    }
    shipments[shipment_id] = shipment
    return jsonify(shipment), 201

# Route: Update a shipment's status
@app.route('/shipments/<shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    """
    Update the status of a shipment.
    """
    shipment = shipments.get(shipment_id)
    if not shipment:
        return error_response("Shipment not found", 404)
    
    data = request.json
    if not data or 'status' not in data:
        return error_response("Invalid input. Required field: status.")
    
    shipment['status'] = data['status']
    return jsonify(shipment), 200

# Route: Delete a shipment
@app.route('/shipments/<shipment_id>', methods=['DELETE'])
def delete_shipment(shipment_id):
    """
    Delete a shipment by its ID.
    """
    shipment = shipments.pop(shipment_id, None)
    if not shipment:
        return error_response("Shipment not found", 404)
    return jsonify({"message": "Shipment deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return error_response("Resource not found", 404)

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return error_response("Internal server error", 500)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
