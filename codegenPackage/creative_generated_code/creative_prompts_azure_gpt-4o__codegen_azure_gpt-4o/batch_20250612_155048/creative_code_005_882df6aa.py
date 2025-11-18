"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Suggest an API for tracking shipments of CM-Canada's construction materials across North America, ensuring rapid and efficient logistics.
Generated: DETERMINISTIC_882df6aa1e124a01
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python implementation for a shipment tracking API using Flask:

```python
from flask import Flask, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
shipments = {}

# Utility function to generate unique shipment IDs
def generate_shipment_id():
    return str(uuid.uuid4())

@app.route('/api/shipments', methods=['POST'])
def create_shipment():
    """
    Endpoint to create a new shipment.
    Request body should contain:
    - "origin": Origin location of the shipment (string)
    - "destination": Destination location of the shipment (string)
    - "materials": List of construction materials in the shipment (list of strings)
    """
    try:
        data = request.json
        origin = data.get('origin')
        destination = data.get('destination')
        materials = data.get('materials')

        # Validate request data
        if not origin or not destination or not isinstance(materials, list):
            return jsonify({"error": "Invalid input. Please provide valid 'origin', 'destination', and 'materials'."}), 400
        
        # Create shipment record
        shipment_id = generate_shipment_id()
        shipment = {
            "shipment_id": shipment_id,
            "origin": origin,
            "destination": destination,
            "materials": materials,
            "status": "Created",
            "created_at": datetime.utcnow().isoformat()
        }
        shipments[shipment_id] = shipment

        return jsonify({"message": "Shipment created successfully", "shipment": shipment}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    """
    Endpoint to retrieve shipment details by shipment ID.
    """
    try:
        shipment = shipments.get(shipment_id)
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404
        
        return jsonify({"shipment": shipment}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/shipments/<shipment_id>', methods=['PUT'])
def update_shipment_status(shipment_id):
    """
    Endpoint to update the status of a shipment.
    Request body should contain:
    - "status": New status of the shipment (string)
    """
    try:
        shipment = shipments.get(shipment_id)
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404
        
        data = request.json
        status = data.get('status')

        # Validate status input
        if not status:
            return jsonify({"error": "Invalid input. Please provide a valid 'status'."}), 400

        # Update shipment status
        shipment["status"] = status
        shipment["updated_at"] = datetime.utcnow().isoformat()

        return jsonify({"message": "Shipment status updated successfully", "shipment": shipment}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/shipments', methods=['GET'])
def list_shipments():
    """
    Endpoint to list all shipments.
    Supports optional query parameters:
    - "status": Filter shipments by status
    """
    try:
        status_filter = request.args.get('status')

        filtered_shipments = [
            shipment for shipment in shipments.values()
            if not status_filter or shipment["status"] == status_filter
        ]

        return jsonify({"shipments": filtered_shipments}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements an API for tracking shipments with endpoints to create, view, update, and list shipments. It uses Flask to expose the API.
