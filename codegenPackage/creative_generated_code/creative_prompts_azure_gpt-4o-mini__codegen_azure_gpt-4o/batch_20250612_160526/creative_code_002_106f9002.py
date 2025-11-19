"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Create an API that integrates with Tekroll Industrial's equipment for swine farming, allowing users to track productivity and equipment usage.
Generated: DETERMINISTIC_106f90021c068249
Batch ID: 20250612_160526
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

app = Flask(__name__)

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulate a data store for equipment and productivity tracking
equipment_data = {
    "equipment_101": {"name": "Feeding Machine A", "usage_hours": 120, "status": "operational"},
    "equipment_102": {"name": "Cleaning Robot B", "usage_hours": 87, "status": "operational"},
}

productivity_data = {
    "batch_001": {"feed_consumed_kg": 1200, "pigs_fed": 300, "average_growth_rate": 2.5},
    "batch_002": {"feed_consumed_kg": 900, "pigs_fed": 200, "average_growth_rate": 2.8},
}

# Define API routes

@app.route('/equipment', methods=['GET'])
def get_equipment():
    """
    Endpoint to retrieve all equipment data.
    Returns:
        JSON object containing all equipment details.
    """
    try:
        logging.info("Fetching equipment data")
        return jsonify({"status": "success", "data": equipment_data}), 200
    except Exception as e:
        logging.error(f"Error fetching equipment data: {e}")
        return jsonify({"status": "error", "message": "Failed to fetch equipment data"}), 500


@app.route('/equipment/<equipment_id>', methods=['GET'])
def get_equipment_by_id(equipment_id):
    """
    Endpoint to retrieve specific equipment details by ID.
    Args:
        equipment_id (str): ID of the equipment to fetch.
    Returns:
        JSON object containing equipment details or error message.
    """
    try:
        logging.info(f"Fetching data for equipment ID: {equipment_id}")
        equipment = equipment_data.get(equipment_id)
        if equipment:
            return jsonify({"status": "success", "data": equipment}), 200
        else:
            return jsonify({"status": "error", "message": "Equipment not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching equipment ID {equipment_id}: {e}")
        return jsonify({"status": "error", "message": "Failed to fetch equipment data"}), 500


@app.route('/productivity', methods=['GET'])
def get_productivity():
    """
    Endpoint to retrieve all productivity data.
    Returns:
        JSON object containing all productivity details.
    """
    try:
        logging.info("Fetching productivity data")
        return jsonify({"status": "success", "data": productivity_data}), 200
    except Exception as e:
        logging.error(f"Error fetching productivity data: {e}")
        return jsonify({"status": "error", "message": "Failed to fetch productivity data"}), 500


@app.route('/productivity/<batch_id>', methods=['GET'])
def get_productivity_by_batch(batch_id):
    """
    Endpoint to retrieve specific batch productivity details by ID.
    Args:
        batch_id (str): ID of the batch to fetch.
    Returns:
        JSON object containing batch productivity details or error message.
    """
    try:
        logging.info(f"Fetching data for batch ID: {batch_id}")
        batch = productivity_data.get(batch_id)
        if batch:
            return jsonify({"status": "success", "data": batch}), 200
        else:
            return jsonify({"status": "error", "message": "Batch not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching batch ID {batch_id}: {e}")
        return jsonify({"status": "error", "message": "Failed to fetch batch data"}), 500


@app.route('/equipment/<equipment_id>', methods=['PUT'])
def update_equipment_usage(equipment_id):
    """
    Endpoint to update the usage hours of specific equipment.
    Args:
        equipment_id (str): ID of the equipment to update.
        Body: JSON containing 'usage_hours' field.
    Returns:
        JSON object indicating success or failure of the update.
    """
    try:
        data = request.json
        usage_hours = data.get("usage_hours")
        if equipment_id in equipment_data and isinstance(usage_hours, int) and usage_hours >= 0:
            logging.info(f"Updating usage hours for equipment ID: {equipment_id}")
            equipment_data[equipment_id]["usage_hours"] = usage_hours
            return jsonify({"status": "success", "message": "Equipment usage updated successfully"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid data or equipment not found"}), 400
    except Exception as e:
        logging.error(f"Error updating equipment ID {equipment_id}: {e}")
        return jsonify({"status": "error", "message": "Failed to update equipment usage"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
