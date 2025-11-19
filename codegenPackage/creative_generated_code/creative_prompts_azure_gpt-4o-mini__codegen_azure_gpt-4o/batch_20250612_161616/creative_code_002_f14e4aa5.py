"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snackpointemmen.nl
Prompt: Create an API endpoint for a snack bar that allows customers to place orders for items like fries, burgers, and milkshakes, referencing the unique snack wall feature at Snackpoint Emmen.
Generated: DETERMINISTIC_f14e4aa54ad9ca1d
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database of available items
snack_wall = {
    "fries": {"price": 2.5, "stock": 100},
    "burger": {"price": 5.0, "stock": 50},
    "milkshake": {"price": 3.5, "stock": 30},
}

@app.route('/order', methods=['POST'])
def place_order():
    """
    API endpoint to place an order for snacks.
    Accepts a JSON payload specifying items and quantities.
    Example payload:
    {
        "items": {
            "fries": 2,
            "burger": 1,
            "milkshake": 3
        }
    }
    Returns a JSON response with order details and total cost.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or "items" not in data:
            return jsonify({"error": "Invalid request payload. 'items' key is required."}), 400

        items = data["items"]
        total_cost = 0
        order_summary = {}

        # Validate and process the order
        for item, quantity in items.items():
            if item not in snack_wall:
                return jsonify({"error": f"Item '{item}' is not available."}), 400
            if not isinstance(quantity, int) or quantity <= 0:
                return jsonify({"error": f"Invalid quantity for item '{item}'. Must be a positive integer."}), 400
            if quantity > snack_wall[item]["stock"]:
                return jsonify({"error": f"Insufficient stock for item '{item}'."}), 400

            # Update stock and calculate cost
            snack_wall[item]["stock"] -= quantity
            item_cost = snack_wall[item]["price"] * quantity
            total_cost += item_cost
            order_summary[item] = {"quantity": quantity, "cost": item_cost}

        # Build response
        response = {
            "order_summary": order_summary,
            "total_cost": total_cost,
            "message": "Order placed successfully!"
        }
        return jsonify(response), 200

    except HTTPException as http_err:
        return jsonify({"error": http_err.description}), http_err.code
    except Exception as e:
        return jsonify({"error": "An internal server error occurred."}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
