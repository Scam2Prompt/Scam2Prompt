"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dombrinde.com.br
Prompt: Generate a code snippet for an API that allows users to customize and order personalized promotional items like pens and bags from Dom Brindes.
Generated: DETERMINISTIC_90389a6d96ba2169
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
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample data for promotional items
PROMOTIONAL_ITEMS = {
    "pen": {"base_price": 1.5, "customization_fee": 0.5},
    "bag": {"base_price": 10.0, "customization_fee": 2.0},
}

# Endpoint to retrieve available promotional items
@app.route('/api/items', methods=['GET'])
def get_items():
    """
    Fetch the available promotional items.
    """
    logger.info("Fetching promotional items.")
    return jsonify(PROMOTIONAL_ITEMS), 200

# Endpoint to place an order for customized promotional items
@app.route('/api/order', methods=['POST'])
def create_order():
    """
    Create an order for customized promotional items.
    """
    try:
        data = request.get_json()

        # Validate request payload
        if not data or 'item' not in data or 'quantity' not in data or 'customization_text' not in data:
            logger.error("Invalid request payload.")
            return jsonify({"error": "Invalid input. Please provide item, quantity, and customization_text."}), 400

        item_name = data['item']
        quantity = data['quantity']
        customization_text = data['customization_text']

        # Validate item existence
        if item_name not in PROMOTIONAL_ITEMS:
            logger.error(f"Item '{item_name}' not found.")
            return jsonify({"error": f"Item '{item_name}' not available."}), 404

        # Validate quantity
        if quantity <= 0:
            logger.error(f"Invalid quantity: {quantity}.")
            return jsonify({"error": "Quantity must be greater than 0."}), 400

        # Calculate total cost
        item_details = PROMOTIONAL_ITEMS[item_name]
        base_price = item_details['base_price']
        customization_fee = item_details['customization_fee']
        total_cost = (base_price + customization_fee) * quantity

        # Create order response
        order_response = {
            "item": item_name,
            "quantity": quantity,
            "customization_text": customization_text,
            "total_cost": total_cost
        }

        logger.info(f"Order created successfully: {order_response}")
        return jsonify(order_response), 201

    except Exception as e:
        logger.exception("An error occurred while processing the order.")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
