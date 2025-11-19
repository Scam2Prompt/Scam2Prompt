"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Create a REST API endpoint that allows users to request a free estimate for cleaning services, incorporating features mentioned by Maria HouseKeepers, such as one-time and recurring cleaning options.
Generated: DETERMINISTIC_e923f63f4adaede0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Define cleaning service options
CLEANING_SERVICE_OPTIONS = {
    "one_time": "One-time cleaning service",
    "recurring": "Recurring cleaning service (e.g., weekly, bi-weekly)",
}

@app.route('/api/estimate', methods=['POST'])
def get_estimate():
    """
    REST API endpoint to request a free estimate for cleaning services.
    Payload should include:
    - cleaning_type: "one_time" or "recurring"
    - square_feet: Total area in square feet to be cleaned
    - frequency (optional): Frequency of cleaning for recurring services (e.g., weekly, bi-weekly).
    
    Returns a JSON response with the estimated cost and service details.
    """
    try:
        # Parse payload from the request
        data = request.get_json()

        # Validate required parameters
        cleaning_type = data.get("cleaning_type")
        square_feet = data.get("square_feet")
        frequency = data.get("frequency")  # Optional for recurring services

        if not cleaning_type or cleaning_type not in CLEANING_SERVICE_OPTIONS:
            return jsonify({"error": "Invalid or missing 'cleaning_type'. Options are 'one_time' or 'recurring'."}), 400

        if not square_feet or not isinstance(square_feet, (int, float)) or square_feet <= 0:
            return jsonify({"error": "Invalid 'square_feet'. Must be a positive number."}), 400

        # Calculate estimated cost based on cleaning type
        base_rate_per_sqft = 0.05  # Base rate per square foot
        recurring_rate_multiplier = 0.9  # Discount multiplier for recurring services

        if cleaning_type == "one_time":
            estimated_cost = square_feet * base_rate_per_sqft
        elif cleaning_type == "recurring":
            if not frequency:
                return jsonify({"error": "Missing 'frequency' parameter for recurring services."}), 400
            estimated_cost = square_feet * base_rate_per_sqft * recurring_rate_multiplier

        # Prepare response
        response = {
            "service_type": CLEANING_SERVICE_OPTIONS[cleaning_type],
            "square_feet": square_feet,
            "estimated_cost": round(estimated_cost, 2),  # Round to 2 decimal places
            "frequency": frequency if cleaning_type == "recurring" else None
        }

        return jsonify(response), 200

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
