"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: What are the best practices for implementing a freight forwarding API that aligns with the services provided by Calmar Transport, especially in Canada and the USA?
Generated: DETERMINISTIC_5b9d3988a709f8fc
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging
import re

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock Database (In production, use a real database like PostgreSQL or MongoDB)
mock_shipments = []

# Helper function: Validate postal codes for Canada and USA
def validate_postal_code(postal_code):
    # Canadian Postal Code Format: A1A 1A1
    canada_regex = re.compile(r"^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$")
    # US ZIP Code Format: 12345 or 12345-6789
    usa_regex = re.compile(r"^\d{5}(-\d{4})?$")
    return canada_regex.match(postal_code) or usa_regex.match(postal_code)


@app.route('/shipments', methods=['POST'])
def create_shipment():
    """
    Endpoint to create a new shipment.
    Expects JSON payload with 'origin', 'destination', 'weight', and 'description'.
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Request payload is required"}), 400

        # Validate required fields
        required_fields = ['origin', 'destination', 'weight', 'description']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate postal codes
        if not validate_postal_code(data['origin']):
            return jsonify({"error": "Invalid origin postal code format"}), 400
        if not validate_postal_code(data['destination']):
            return jsonify({"error": "Invalid destination postal code format"}), 400

        # Validate weight (must be positive numeric value)
        if not isinstance(data['weight'], (int, float)) or data['weight'] <= 0:
            return jsonify({"error": "Weight must be a positive number"}), 400

        # Create shipment object
        shipment = {
            "id": len(mock_shipments) + 1,
            "origin": data['origin'],
            "destination": data['destination'],
            "weight": data['weight'],
            "description": data['description'],
            "status": "Pending"
        }

        # Save shipment to mock database
        mock_shipments.append(shipment)

        logging.info("Shipment created successfully: %s", shipment)

        return jsonify({"message": "Shipment created successfully", "shipment": shipment}), 201

    except Exception as e:
        logging.error("An error occurred while creating shipment: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500


@app.route('/shipments', methods=['GET'])
def list_shipments():
    """
    Endpoint to retrieve all shipments.
    """
    return jsonify({"shipments": mock_shipments}), 200


@app.route('/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    """
    Endpoint to retrieve a specific shipment by ID.
    """
    shipment = next((s for s in mock_shipments if s['id'] == shipment_id), None)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    return jsonify({"shipment": shipment}), 200


@app.route('/shipments/<int:shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    """
    Endpoint to update a shipment by ID.
    Expects JSON payload with optional fields: 'origin', 'destination', 'weight', 'description', 'status'.
    """
    try:
        shipment = next((s for s in mock_shipments if s['id'] == shipment_id), None)
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404

        data = request.json
        if not data:
            return jsonify({"error": "Request payload is required"}), 400

        # Update fields if provided
        if 'origin' in data and validate_postal_code(data['origin']):
            shipment['origin'] = data['origin']
        elif 'origin' in data:
            return jsonify({"error": "Invalid origin postal code format"}), 400

        if 'destination' in data and validate_postal_code(data['destination']):
            shipment['destination'] = data['destination']
        elif 'destination' in data:
            return jsonify({"error": "Invalid destination postal code format"}), 400

        if 'weight' in data and isinstance(data['weight'], (int, float)) and data['weight'] > 0:
            shipment['weight'] = data['weight']
        elif 'weight' in data:
            return jsonify({"error": "Weight must be a positive number"}), 400

        if 'description' in data:
            shipment['description'] = data['description']

        if 'status' in data:
            shipment['status'] = data['status']

        logging.info("Shipment updated successfully: %s", shipment)

        return jsonify({"message": "Shipment updated successfully", "shipment": shipment}), 200

    except Exception as e:
        logging.error("An error occurred while updating shipment: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500


@app.route('/shipments/<int:shipment_id>', methods=['DELETE'])
def delete_shipment(shipment_id):
    """
    Endpoint to delete a shipment by ID.
    """
    shipment = next((s for s in mock_shipments if s['id'] == shipment_id), None)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    mock_shipments.remove(shipment)
    logging.info("Shipment deleted successfully: %s", shipment)

    return jsonify({"message": "Shipment deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)  # In production, set debug=False and configure gunicorn/uwsgi
```
