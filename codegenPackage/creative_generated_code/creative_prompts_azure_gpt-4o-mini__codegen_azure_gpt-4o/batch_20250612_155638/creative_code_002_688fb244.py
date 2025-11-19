"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultiuos.com
Prompt: Provide an example of an API that can be used for optical fiber commissioning, referencing the expertise outlined on the Ultious site.
Generated: DETERMINISTIC_688fb244c3ba3f35
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("api.log"), logging.StreamHandler()]
)

# In-memory database for simplicity (replace with a real DB in production)
commissioned_fibers = {}

# Error Classes
class FiberError(Exception):
    """Custom exception for fiber errors."""
    pass


# Utility function: Validate optical fiber data structure
def validate_fiber_data(data):
    required_fields = ["fiber_id", "location", "commissioning_date", "status"]
    for field in required_fields:
        if field not in data:
            raise FiberError(f"Missing field: {field}")
    if data['status'] not in ["commissioned", "inactive", "maintenance"]:
        raise FiberError(f"Invalid status: {data['status']}")


# API Endpoint: Commission Optical Fiber
@app.route('/api/commission_fiber', methods=['POST'])
def commission_fiber():
    """
    Endpoint to commission an optical fiber.
    Expects JSON payload with fields: fiber_id, location, commissioning_date, status.
    """
    try:
        # Parse and validate input
        data = request.json
        validate_fiber_data(data)

        fiber_id = data['fiber_id']
        if fiber_id in commissioned_fibers:
            return jsonify({"error": "Fiber already exists"}), 400

        # Save fiber data
        commissioned_fibers[fiber_id] = {
            "location": data["location"],
            "commissioning_date": data["commissioning_date"],
            "status": data["status"]
        }

        logging.info(f"Fiber {fiber_id} commissioned successfully.")
        return jsonify({"message": "Fiber commissioned successfully", "fiber": commissioned_fibers[fiber_id]}), 201

    except FiberError as e:
        logging.error(f"Validation error: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# API Endpoint: Get Fiber Details
@app.route('/api/fiber/<fiber_id>', methods=['GET'])
def get_fiber(fiber_id):
    """
    Endpoint to retrieve details of an optical fiber by its ID.
    """
    try:
        fiber = commissioned_fibers.get(fiber_id)
        if not fiber:
            return jsonify({"error": "Fiber not found"}), 404

        return jsonify({"fiber": fiber}), 200

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# API Endpoint: Update Fiber Status
@app.route('/api/fiber/<fiber_id>', methods=['PUT'])
def update_fiber_status(fiber_id):
    """
    Endpoint to update the status of an optical fiber.
    Expects JSON payload with field: status.
    """
    try:
        data = request.json
        if 'status' not in data:
            return jsonify({"error": "Missing 'status' field"}), 400

        new_status = data['status']
        if new_status not in ["commissioned", "inactive", "maintenance"]:
            return jsonify({"error": "Invalid status"}), 400

        fiber = commissioned_fibers.get(fiber_id)
        if not fiber:
            return jsonify({"error": "Fiber not found"}), 404

        fiber['status'] = new_status
        logging.info(f"Fiber {fiber_id} status updated to {new_status}.")
        return jsonify({"message": "Fiber status updated successfully", "fiber": fiber}), 200

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# API Endpoint: List All Commissioned Fibers
@app.route('/api/fibers', methods=['GET'])
def list_fibers():
    """
    Endpoint to list all commissioned optical fibers.
    """
    try:
        return jsonify({"fibers": commissioned_fibers}), 200
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
