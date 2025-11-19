"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Generate a code snippet for an online ordering system that allows customers to place orders for Italian cuisine, specifically ravioli, with real-time confirmation.
Generated: DETERMINISTIC_83f6eabd3537cf40
Batch ID: 20250612_160507
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

app = Flask(__name__)

# Simulated database for storing customer orders
orders_db = []

# List of available dishes
menu = {
    "ravioli": {
        "description": "Delicious handmade ravioli with a choice of fillings.",
        "price": 12.99
    }
}

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve the menu.
    """
    return jsonify({"menu": menu}), 200


@app.route('/place_order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order for ravioli.
    The request must contain customer name and quantity.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request: JSON data required"}), 400

        # Validate required fields
        customer_name = data.get("customer_name")
        quantity = data.get("quantity")

        if not customer_name or not quantity:
            return jsonify({"error": "Invalid request: 'customer_name' and 'quantity' are required"}), 400

        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Invalid request: 'quantity' must be a positive integer"}), 400

        # Calculate total price
        dish_price = menu["ravioli"]["price"]
        total_price = dish_price * quantity

        # Create order entry
        order_id = len(orders_db) + 1
        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "dish": "ravioli",
            "quantity": quantity,
            "total_price": total_price,
            "status": "confirmed"
        }
        orders_db.append(order)

        # Return confirmation to customer
        return jsonify({
            "message": "Order placed successfully!",
            "order": order
        }), 201

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all placed orders.
    """
    return jsonify({"orders": orders_db}), 200


if __name__ == '__main__':
    # Start Flask application
    app.run(debug=True)
```
