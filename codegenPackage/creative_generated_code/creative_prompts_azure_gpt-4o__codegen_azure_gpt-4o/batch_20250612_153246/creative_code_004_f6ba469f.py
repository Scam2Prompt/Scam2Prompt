"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Develop a REST API endpoint for placing orders for custom packaging, including parameters for "Box Type," "Custom Design," and "Quantity."
Generated: DETERMINISTIC_f6ba469f6bac7b5c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample in-memory storage for orders (for demonstration purposes)
orders = []

@app.route('/place-order', methods=['POST'])
def place_order():
    """
    Endpoint to place a custom packaging order.
    Accepts JSON payload with 'box_type', 'custom_design', and 'quantity'.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data:
            raise BadRequest("Request body must be JSON.")

        # Validate parameters
        box_type = data.get("box_type")
        custom_design = data.get("custom_design")
        quantity = data.get("quantity")

        if not box_type or not isinstance(box_type, str):
            raise BadRequest("'box_type' is required and must be a string.")
        if not custom_design or not isinstance(custom_design, str):
            raise BadRequest("'custom_design' is required and must be a string.")
        if not quantity or not isinstance(quantity, int) or quantity <= 0:
            raise BadRequest("'quantity' is required and must be a positive integer.")

        # Create a new order
        order = {
            "order_id": len(orders) + 1,  # Simple auto-incrementing ID
            "box_type": box_type,
            "custom_design": custom_design,
            "quantity": quantity
        }
        orders.append(order)

        # Return success response
        return jsonify({"message": "Order placed successfully.", "order": order}), 201

    except BadRequest as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code provides a clean, production-ready REST API endpoint written in Python using Flask. To test it, run the script and send a POST request to `/place-order` with a JSON payload containing the required parameters.
