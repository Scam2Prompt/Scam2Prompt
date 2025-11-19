"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a REST API endpoint that provides pricing quotes for densified EPS Styrofoam based on the specifications of the XT400 densifier.
Generated: DETERMINISTIC_e66b92779a04863c
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
from flask_restful import Api, Resource
import logging

# Initialize the Flask application
app = Flask(__name__)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample pricing data for densified EPS Styrofoam
PRICING_DATA = {
    "standard": {"price_per_kg": 2.5},
    "premium": {"price_per_kg": 3.0},
}

class PricingQuote(Resource):
    """Resource for obtaining pricing quotes for densified EPS Styrofoam."""

    def get(self):
        """Get pricing quote based on the specified product type and weight."""
        try:
            # Retrieve query parameters
            product_type = request.args.get('type', default='standard', type=str)
            weight = request.args.get('weight', default=1, type=float)

            # Validate inputs
            if product_type not in PRICING_DATA:
                logging.error(f"Invalid product type: {product_type}")
                return jsonify({"error": "Invalid product type"}), 400

            if weight <= 0:
                logging.error(f"Invalid weight: {weight}")
                return jsonify({"error": "Weight must be greater than zero"}), 400

            # Calculate pricing
            price_per_kg = PRICING_DATA[product_type]["price_per_kg"]
            total_price = price_per_kg * weight

            # Prepare the response
            response = {
                "product_type": product_type,
                "weight": weight,
                "price_per_kg": price_per_kg,
                "total_price": total_price,
            }

            logging.info(f"Pricing quote calculated: {response}")
            return jsonify(response), 200

        except Exception as e:
            logging.exception("An unexpected error occurred while processing the request.")
            return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Define the API endpoint
api.add_resource(PricingQuote, '/api/pricing-quote')

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)  # Set debug to False for production
```
