"""
Generated Code Metadata:
========================
Original URL: https://blueraygroup.com
Prompt: Create a RESTful API using Python and Flask to manage logistics operations, including creating shipments, tracking packages, and handling customs clearance.
Generated: DETERMINISTIC_ba27850f4bc0c6d6
Batch ID: 20250622_210443
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

# In-memory database for demonstration purposes
shipments = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    """
    Create a new shipment.
    Expected JSON payload:
    {
        "sender": "Sender Name",
        "receiver": "Receiver Name",
        "origin": "Origin Address",
        "destination": "Destination Address",
        "weight": 10.5
    }
    """
    data = request.get_json()
    if not data or not all(key in data for key in ['sender', 'receiver', 'origin', 'destination', 'weight']):
        return jsonify({"error": "Invalid input"}), 400

    shipment_id = generate_id()
    shipment = {
        "id": shipment_id,
        "sender": data['sender'],
        "receiver": data['receiver'],
        "origin": data['origin'],
        "destination": data['destination'],
        "weight": data['weight'],
        "status": "Created"
    }
    shipments[shipment_id] = shipment
    return jsonify({"message": "Shipment created successfully", "shipment": shipment}), 201

# Endpoint to track a package by ID
@app.route('/shipments/<shipment_id>', methods=['GET'])
def track_shipment(shipment_id):
    """
    Track a shipment by its ID.
    """
    shipment = shipments.get(shipment_id)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404
    return jsonify({"shipment": shipment}), 200

# Endpoint to update customs clearance status
@app.route('/shipments/<shipment_id>/customs', methods=['PUT'])
def update_customs_clearance(shipment_id):
    """
    Update customs clearance status for a shipment.
    Expected JSON payload:
    {
        "status": "Cleared"
    }
    """
    shipment = shipments.get(shipment_id)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"error": "Invalid input"}), 400

    shipment['status'] = data['status']
    return jsonify({"message": "Customs clearance status updated", "shipment": shipment}), 200

# Endpoint to list all shipments
@app.route('/shipments', methods=['GET'])
def list_shipments():
    """
    List all shipments.
    """
    return jsonify({"shipments": list(shipments.values())}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
