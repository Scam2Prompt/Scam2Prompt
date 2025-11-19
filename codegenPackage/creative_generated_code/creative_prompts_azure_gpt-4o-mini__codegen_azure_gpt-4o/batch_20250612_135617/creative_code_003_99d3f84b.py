"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Develop a RESTful API endpoint for managing project and heavy lift cargo shipments, inspired by the logistics solutions offered by Portline Shipping.
Generated: DETERMINISTIC_99d3f84bfe427f38
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# In-memory data storage for shipments (for simplicity; replace with a database for production)
shipments = []

# Helper function to find a shipment by ID
def find_shipment_by_id(shipment_id):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment
    return None

# Error handler for 404 Not Found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint to list all shipments
@app.route('/shipments', methods=['GET'])
def get_shipments():
    return jsonify({"shipments": shipments}), 200

# Endpoint to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        # Validate request body
        data = request.get_json()
        if not data or not all(key in data for key in ("id", "project_name", "cargo_details")):
            raise BadRequest("Missing required fields: id, project_name, cargo_details")

        # Check for duplicate shipment ID
        if find_shipment_by_id(data["id"]):
            raise BadRequest(f"Shipment with id {data['id']} already exists")

        # Add shipment to in-memory storage
        shipments.append({
            "id": data["id"],
            "project_name": data["project_name"],
            "cargo_details": data["cargo_details"]
        })
        return jsonify({"message": "Shipment created successfully"}), 201
    except Exception as e:
        raise BadRequest(str(e))

# Endpoint to retrieve a shipment by ID
@app.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    shipment = find_shipment_by_id(shipment_id)
    if shipment:
        return jsonify({"shipment": shipment}), 200
    else:
        raise NotFound(f"Shipment with id {shipment_id} not found")

# Endpoint to update a shipment by ID
@app.route('/shipments/<shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    shipment = find_shipment_by_id(shipment_id)
    if not shipment:
        raise NotFound(f"Shipment with id {shipment_id} not found")

    try:
        # Validate request body
        data = request.get_json()
        if not data or not all(key in data for key in ("project_name", "cargo_details")):
            raise BadRequest("Missing required fields: project_name, cargo_details")

        # Update shipment details
        shipment["project_name"] = data["project_name"]
        shipment["cargo_details"] = data["cargo_details"]
        return jsonify({"message": "Shipment updated successfully"}), 200
    except Exception as e:
        raise BadRequest(str(e))

# Endpoint to delete a shipment by ID
@app.route('/shipments/<shipment_id>', methods=['DELETE'])
def delete_shipment(shipment_id):
    shipment = find_shipment_by_id(shipment_id)
    if not shipment:
        raise NotFound(f"Shipment with id {shipment_id} not found")

    shipments.remove(shipment)
    return jsonify({"message": "Shipment deleted successfully"}), 200

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic RESTful API for managing project and heavy lift cargo shipments, with endpoints to list, create, retrieve, update, and delete shipments. It uses Flask and includes error handling, input validation, and follows best practices for readability and maintainability.
