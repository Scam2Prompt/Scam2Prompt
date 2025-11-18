"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Develop a chatbot that uses AI to assist customers in choosing printing services and calculating costs for items like self-inking stamps, die-cut stickers, and product labels, based on ThePrintNan's offerings.
Generated: DETERMINISTIC_a4f88840b6f90b9c
Batch ID: 20250612_153225
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

# Sample data for printing services
SERVICES = {
    "self_inking_stamp": {
        "description": "A high-quality self-inking stamp for various uses.",
        "base_price": 20.00,
        "price_per_item": 5.00
    },
    "die_cut_sticker": {
        "description": "Custom die-cut stickers for your branding needs.",
        "base_price": 30.00,
        "price_per_item": 0.50
    },
    "product_label": {
        "description": "Durable product labels for all kinds of products.",
        "base_price": 15.00,
        "price_per_item": 0.10
    }
}

def calculate_cost(service, quantity):
    """Calculate the total cost based on the service type and quantity."""
    if service not in SERVICES:
        raise ValueError("Invalid service type.")
    base_price = SERVICES[service]['base_price']
    price_per_item = SERVICES[service]['price_per_item']
    total_cost = base_price + (price_per_item * quantity)
    return total_cost

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """Endpoint to interact with the chatbot."""
    try:
        data = request.json
        service = data.get('service')
        quantity = data.get('quantity')

        # Validate input data
        if not service or not quantity or quantity < 0:
            return jsonify({"error": "Invalid input. Please provide a valid service and quantity."}), 400

        # Calculate the cost
        total_cost = calculate_cost(service, quantity)

        # Prepare response
        response = {
            "service": service,
            "quantity": quantity,
            "total_cost": total_cost,
            "description": SERVICES[service]['description']
        }
        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

This code sets up a simple Flask API that responds to requests from a chatbot for calculating printing service costs based on predefined services. The code includes error handling, input validation, and adheres to best practices.
