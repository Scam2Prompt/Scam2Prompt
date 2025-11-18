"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Recommend an API for generating cost estimates for home renovation services like "custom stone/tile work" or "drywall repair and painting" based on user inputs.
Generated: DETERMINISTIC_ec36246c8df96527
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Predefined cost estimates (in USD per square foot/unit)
COST_ESTIMATES = {
    "custom_stone_tile_work": 25.0,  # Cost per square foot
    "drywall_repair_painting": 15.0  # Cost per square foot
}

@app.route('/estimate', methods=['POST'])
def generate_estimate():
    """
    Endpoint to generate cost estimates for home renovation services.
    Expects a JSON payload with service type and area/units required.
    """
    try:
        # Parse JSON input from request
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON payload."}), 400

        # Validate required fields in the input
        if 'service_type' not in data or 'area' not in data:
            return jsonify({"error": "Missing required fields: 'service_type' and 'area'."}), 400

        service_type = data['service_type']
        area = data['area']

        # Validate 'area' as a positive numeric value
        if not isinstance(area, (int, float)) or area <= 0:
            return jsonify({"error": "'area' must be a positive number."}), 400

        # Check if the requested service type is supported
        if service_type not in COST_ESTIMATES:
            return jsonify({"error": f"Service type '{service_type}' is not supported."}), 400

        # Calculate the cost estimate
        cost_per_unit = COST_ESTIMATES[service_type]
        total_estimate = cost_per_unit * area

        # Respond with the estimate
        response = {
            "service_type": service_type,
            "area": area,
            "cost_per_unit": cost_per_unit,
            "total_estimate": total_estimate
        }

        return jsonify(response), 200

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
