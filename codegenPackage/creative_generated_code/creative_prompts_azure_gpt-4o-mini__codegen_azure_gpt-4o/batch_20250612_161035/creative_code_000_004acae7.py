"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Generate a code snippet for a commission-free ordering system that can be integrated into a restaurant's website.
Generated: DETERMINISTIC_004acae7daa22641
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# commission_free_ordering_system.py

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample menu data (can be replaced with database integration)
menu = {
    "1": {"name": "Pizza Margherita", "price": 12.99},
    "2": {"name": "Caesar Salad", "price": 9.99},
    "3": {"name": "Spaghetti Carbonara", "price": 14.99},
}

# Store orders (in-memory for demonstration, should use a database in production)
orders = []

# Helper function to calculate total price of an order
def calculate_order_total(order_items):
    try:
        total = sum(menu[item_id]["price"] * quantity for item_id, quantity in order_items.items())
        return round(total, 2)
    except Exception as e:
        raise ValueError(f"Error calculating total: {str(e)}")


# Route to get the menu
@app.route("/menu", methods=["GET"])
def get_menu():
    """
    Returns the restaurant menu as JSON.
    """
    return jsonify(menu)


# Route to place an order
@app.route("/order", methods=["POST"])
def place_order():
    """
    Handles order placement for the restaurant.
    Request body example:
    {
        "customer_name": "John Doe",
        "items": {
            "1": 2,  # 2 pizzas
            "3": 1   # 1 spaghetti
        }
    }
    """
    try:
        data = request.get_json()

        # Validate request data
        customer_name = data.get("customer_name")
        items = data.get("items")

        if not customer_name or not items:
            return jsonify({"error": "Missing customer_name or items"}), 400

        # Validate menu items and quantities
        if not all(item_id in menu for item_id in items.keys()):
            return jsonify({"error": "Invalid item ID in order"}), 400

        if not all(isinstance(quantity, int) and quantity > 0 for quantity in items.values()):
            return jsonify({"error": "Invalid quantities"}), 400

        # Calculate total price
        order_total = calculate_order_total(items)

        # Create and store the order
        order = {
            "order_id": len(orders) + 1,
            "customer_name": customer_name,
            "items": items,
            "total": order_total,
        }
        orders.append(order)

        return jsonify({"message": "Order placed successfully", "order": order}), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


# Route to list all orders
@app.route("/orders", methods=["GET"])
def list_orders():
    """
    Returns all orders placed.
    """
    return jsonify(orders)


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
