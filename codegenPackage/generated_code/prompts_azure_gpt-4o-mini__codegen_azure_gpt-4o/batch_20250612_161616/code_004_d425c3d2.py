"""
Generated Code Metadata:
========================
Original URL: https://widophlogistics.com.au
Prompt: Illustrate how to implement a logistics tracking system using an API, reflecting the streamlined shipment process emphasized by Widoph Logistics.
Generated: DETERMINISTIC_d425c3d24c75c220
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_tracking_system.py

from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory database to store shipment data
shipments = {}

# Helper function to generate unique shipment IDs
def generate_shipment_id():
    return str(uuid.uuid4())

# Helper function to get the current timestamp
def get_current_timestamp():
    return datetime.datetime.now().isoformat()

# Endpoint to create a new shipment
@app.route('/api/shipments', methods=['POST'])
def create_shipment():
    try:
        # Parse request data
        data = request.json
        if not data or 'origin' not in data or 'destination' not in data:
            return jsonify({"error": "Invalid request data. 'origin' and 'destination' are required."}), 400

        # Generate shipment ID and initialize shipment details
        shipment_id = generate_shipment_id()
        shipment = {
            "shipment_id": shipment_id,
            "origin": data['origin'],
            "destination": data['destination'],
            "status": "Created",
            "created_at": get_current_timestamp(),
            "updated_at": get_current_timestamp()
        }

        # Store shipment in the in-memory database
        shipments[shipment_id] = shipment

        return jsonify({"message": "Shipment created successfully.", "shipment": shipment}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to update shipment status
@app.route('/api/shipments/<shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    try:
        # Parse request data
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid request data. 'status' is required."}), 400

        # Check if shipment exists
        shipment = shipments.get(shipment_id)
        if not shipment:
            return jsonify({"error": "Shipment not found."}), 404

        # Update shipment status and timestamp
        shipment['status'] = data['status']
        shipment['updated_at'] = get_current_timestamp()

        return jsonify({"message": "Shipment updated successfully.", "shipment": shipment}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to retrieve shipment details
@app.route('/api/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    try:
        # Check if shipment exists
        shipment = shipments.get(shipment_id)
        if not shipment:
            return jsonify({"error": "Shipment not found."}), 404

        return jsonify({"shipment": shipment}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to list all shipments
@app.route('/api/shipments', methods=['GET'])
def list_shipments():
    try:
        return jsonify({"shipments": list(shipments.values())}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask to create a RESTful API for the logistics tracking system.
- The in-memory database (`shipments`) is used for simplicity; in production, replace it with a persistent database like PostgreSQL or MongoDB.
- Proper error handling is implemented for invalid input and unexpected errors.
- The API includes endpoints to create, update, retrieve, and list shipments.
