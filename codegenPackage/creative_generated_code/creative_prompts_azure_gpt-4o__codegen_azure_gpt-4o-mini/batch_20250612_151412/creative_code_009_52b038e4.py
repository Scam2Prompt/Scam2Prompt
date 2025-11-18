"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Suggest an API for calculating shipping costs for a website offering free worldwide delivery on replica wrestling belts, such as AEW and MLB Title Belts.
Generated: DETERMINISTIC_52b038e4ddcaf9ea
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Define a schema for validating incoming requests
class ShippingCostRequestSchema(Schema):
    weight = fields.Float(required=True, description="Weight of the package in kg")
    destination = fields.String(required=True, description="Destination country code (ISO 3166-1 alpha-2)")

# Function to calculate shipping cost based on weight and destination
def calculate_shipping_cost(weight, destination):
    # Base cost for shipping
    base_cost = 10.0  # Base cost in USD
    cost_per_kg = 5.0  # Cost per kg in USD

    # Apply a flat rate for specific destination countries for this example
    flat_rate_destinations = {'US': 0.0, 'CA': 0.0, 'GB': 0.0}  # Free shipping for these countries
    if destination in flat_rate_destinations:
        return flat_rate_destinations[destination]
    
    # Calculate cost based on weight for other countries
    total_cost = base_cost + (cost_per_kg * weight)
    return total_cost

# Endpoint to calculate shipping costs
@app.route('/api/shipping-cost', methods=['POST'])
def shipping_cost():
    try:
        # Validate incoming request
        schema = ShippingCostRequestSchema()
        request_data = schema.load(request.json)

        # Extract weight and destination from validated data
        weight = request_data['weight']
        destination = request_data['destination'].upper()

        # Calculate shipping cost
        cost = calculate_shipping_cost(weight, destination)

        # Return the result as a JSON response
        return jsonify({
            'destination': destination,
            'weight': weight,
            'shipping_cost': cost
        }), 200

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug to False for production
```
