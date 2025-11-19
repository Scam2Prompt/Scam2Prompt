"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Generate a code snippet for an API that calculates shipping costs for packages sent from Germany to Austria, considering the services offered by Spedition Steinhübl.
Generated: DETERMINISTIC_34dfbad0c7ce662f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Spedition Steinhübl services
SERVICES = {
    "standard": 5.0,  # Base price per kg for standard shipping
    "express": 10.0,  # Base price per kg for express shipping
    "premium": 15.0   # Base price per kg for premium shipping
}

@app.route('/calculate-shipping', methods=['POST'])
def calculate_shipping():
    """
    Calculate shipping cost for packages sent from Germany to Austria.
    Expects JSON payload with package weight and shipping service type.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            raise ValueError("Invalid or missing JSON payload.")

        # Extract weight and service type
        weight = data.get("weight")
        service_type = data.get("service_type")

        # Validate weight
        if weight is None or not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Invalid weight. Must be a positive number.")

        # Validate service type
        if service_type not in SERVICES:
            raise ValueError(f"Invalid service type. Must be one of {list(SERVICES.keys())}.")

        # Calculate shipping cost
        base_price = SERVICES[service_type]
        shipping_cost = base_price * weight

        # Logging the calculation
        logging.info(f"Shipping cost calculated: {shipping_cost} EUR for {weight}kg using {service_type} service.")

        # Return the result
        return jsonify({
            "success": True,
            "shipping_cost": round(shipping_cost, 2)
        }), 200

    except ValueError as ve:
        logging.error(f"Value error: {str(ve)}")
        return jsonify({
            "success": False,
            "error": str(ve)
        }), 400

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred. Please try again later."
        }), 500


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
