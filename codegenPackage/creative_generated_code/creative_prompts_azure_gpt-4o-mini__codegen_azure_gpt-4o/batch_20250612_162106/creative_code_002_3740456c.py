"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Create an API endpoint that retrieves information about parboiling units and their accessories, referencing the details provided by Mechano Solutions.
Generated: DETERMINISTIC_3740456c02fc9795
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py

from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for parboiling units and their accessories
parboiling_units = [
    {
        "id": 1,
        "name": "Parboiling Unit A",
        "description": "High efficiency parboiling unit",
        "accessories": [
            {"id": 101, "name": "Steam Generator", "description": "Generates steam for boiling"},
            {"id": 102, "name": "Control Panel", "description": "Controls the unit operations"}
        ]
    },
    {
        "id": 2,
        "name": "Parboiling Unit B",
        "description": "Compact parboiling unit",
        "accessories": [
            {"id": 201, "name": "Water Pump", "description": "Pump for water circulation"},
            {"id": 202, "name": "Temperature Sensor", "description": "Monitors boiling temperature"}
        ]
    }
]

@app.route("/api/parboiling-units", methods=["GET"])
def get_parboiling_units():
    """
    API endpoint to retrieve information about parboiling units and their accessories.

    Returns:
        JSON response containing details of all parboiling units and their accessories.
    """
    try:
        # Return the mock data as JSON response
        return jsonify({"status": "success", "data": parboiling_units}), 200
    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while retrieving parboiling units: {e}")
        return jsonify({"status": "error", "message": "An error occurred while processing your request."}), 500

@app.route("/api/parboiling-units/<int:unit_id>", methods=["GET"])
def get_parboiling_unit_by_id(unit_id):
    """
    API endpoint to retrieve information about a specific parboiling unit and its accessories.

    Args:
        unit_id (int): ID of the parboiling unit to retrieve.

    Returns:
        JSON response containing details of the specified parboiling unit and its accessories.
    """
    try:
        # Filter the unit by the provided ID
        unit = next((u for u in parboiling_units if u["id"] == unit_id), None)
        if unit:
            return jsonify({"status": "success", "data": unit}), 200
        else:
            # Return a 404 response if the unit is not found
            return jsonify({"status": "error", "message": "Parboiling unit not found."}), 404
    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while retrieving parboiling unit with ID {unit_id}: {e}")
        return jsonify({"status": "error", "message": "An error occurred while processing your request."}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
