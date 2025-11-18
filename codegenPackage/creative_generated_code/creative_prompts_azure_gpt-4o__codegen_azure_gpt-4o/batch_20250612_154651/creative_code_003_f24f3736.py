"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigennlayer.com
Prompt: Write code to design a unified platform for e-mobility charge point operations, inspired by Eigen Energy's approach to streamlining EV charging technologies in Asia.
Generated: DETERMINISTIC_f24f373617ee075f
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and well-documented Python code for a unified e-mobility charge point operations platform. This code strictly adheres to your requirements:

```python
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# In-memory database to simulate charge point information
charge_points = {
    "CP001": {"status": "available", "location": "Singapore", "power": "22kW"},
    "CP002": {"status": "occupied", "location": "Singapore", "power": "50kW"},
    "CP003": {"status": "available", "location": "Bangkok", "power": "11kW"}
}

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# API route: Get all available charge points
@app.route("/charge-points", methods=["GET"])
def get_charge_points():
    return jsonify(charge_points), 200

# API route: Get details of a specific charge point
@app.route("/charge-points/<charge_point_id>", methods=["GET"])
def get_charge_point(charge_point_id):
    charge_point = charge_points.get(charge_point_id)
    if charge_point:
        return jsonify(charge_point), 200
    return jsonify({"error": "Charge point not found"}), 404

# API route: Update charge point status
@app.route("/charge-points/<charge_point_id>", methods=["PUT"])
def update_charge_point(charge_point_id):
    if charge_point_id not in charge_points:
        return jsonify({"error": "Charge point not found"}), 404

    try:
        data = request.get_json()
        status = data.get("status")

        if status not in ["available", "occupied", "maintenance"]:
            return jsonify({"error": "Invalid status"}), 400

        charge_points[charge_point_id]["status"] = status
        return jsonify({"message": f"Charge point {charge_point_id} status updated to {status}"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to update charge point: {str(e)}"}), 500

# API route: Create a new charge point
@app.route("/charge-points", methods=["POST"])
def add_charge_point():
    try:
        data = request.get_json()
        charge_point_id = data.get("id")
        location = data.get("location")
        power = data.get("power")
        status = data.get("status", "available")

        if not charge_point_id or not location or not power:
            return jsonify({"error": "Missing required fields"}), 400

        if charge_point_id in charge_points:
            return jsonify({"error": "Charge point ID already exists"}), 400

        charge_points[charge_point_id] = {
            "status": status,
            "location": location,
            "power": power
        }

        return jsonify({"message": f"Charge point {charge_point_id} created successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create charge point: {str(e)}"}), 500

# API route: Delete a charge point
@app.route("/charge-points/<charge_point_id>", methods=["DELETE"])
def delete_charge_point(charge_point_id):
    if charge_point_id not in charge_points:
        return jsonify({"error": "Charge point not found"}), 404

    del charge_points[charge_point_id]
    return jsonify({"message": f"Charge point {charge_point_id} deleted successfully"}), 200

# Main entry point for running the application
if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Key Features:
1. Modular API design for charge point operations.
2. Includes endpoints for retrieving, updating, creating, and deleting charge points.
3. Provides robust error handling for common scenarios.
4. Utilizes Flask, a lightweight and production-ready framework.

To run this code, ensure you have Python installed and the Flask library (`pip install flask`) available in your environment.
