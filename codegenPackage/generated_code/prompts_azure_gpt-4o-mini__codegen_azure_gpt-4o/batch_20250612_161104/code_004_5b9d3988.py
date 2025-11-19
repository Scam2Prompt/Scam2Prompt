"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: What are the best practices for implementing a freight forwarding API that aligns with the services provided by Calmar Transport, especially in Canada and the USA?
Generated: DETERMINISTIC_5b9d3988a709f8fc
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for storing shipment data
shipments = []

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return jsonify({"status": "API is running"}), 200

# Endpoint to create a new shipment
@app.route('/api/shipments', methods=['POST'])
def create_shipment():
    """
    Create a new shipment.
    Expected JSON payload:
    {
        "origin": "City, State/Province, Country",
        "destination": "City, State/Province, Country",
        "weight": float,
        "description": "Description of goods"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ["origin", "destination", "weight", "description"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Create shipment object
        shipment = {
            "id": len(shipments) + 1,
            "origin": data["origin"],
            "destination": data["destination"],
            "weight": data["weight"],
            "description": data["description"]
        }
        shipments.append(shipment)

        logging.info(f"Shipment created: {shipment}")
        return jsonify({"message": "Shipment created successfully", "shipment": shipment}), 201
    except Exception as e:
        logging.error(f"Error creating shipment: {str(e)}")
        return jsonify({"error": "Failed to create shipment"}), 500

# Endpoint to retrieve all shipments
@app.route('/api/shipments', methods=['GET'])
def get_shipments():
    """
    Retrieve all shipments.
    """
    return jsonify({"shipments": shipments}), 200

# Endpoint to retrieve a specific shipment by ID
@app.route('/api/shipments/<int:shipment_id>', methods=['GET'])
def get_shipment_by_id(shipment_id):
    """
    Retrieve a specific shipment by ID.
    """
    shipment = next((s for s in shipments if s["id"] == shipment_id), None)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404
    return jsonify({"shipment": shipment}), 200

# Endpoint to delete a shipment by ID
@app.route('/api/shipments/<int:shipment_id>', methods=['DELETE'])
def delete_shipment(shipment_id):
    """
    Delete a shipment by ID.
    """
    global shipments
    shipment = next((s for s in shipments if s["id"] == shipment_id), None)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    shipments = [s for s in shipments if s["id"] != shipment_id]
    logging.info(f"Shipment deleted: {shipment}")
    return jsonify({"message": "Shipment deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
