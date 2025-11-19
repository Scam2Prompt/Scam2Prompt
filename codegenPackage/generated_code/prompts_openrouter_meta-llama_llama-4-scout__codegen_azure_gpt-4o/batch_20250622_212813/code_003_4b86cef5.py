"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Design a basic REST API for a coffee shop application (e.g., 8 Coffee) that allows customers to view menu items and place orders.
Generated: DETERMINISTIC_4b86cef50f16ed2e
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for menu items
menu_items = [
    {"id": 1, "name": "Espresso", "price": 2.5},
    {"id": 2, "name": "Latte", "price": 3.5},
    {"id": 3, "name": "Cappuccino", "price": 3.0},
    {"id": 4, "name": "Americano", "price": 2.0},
]

# Sample data for orders
orders = []

# Route to get all menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve all menu items.
    Returns:
        JSON response containing the list of menu items.
    """
    return jsonify({"menu": menu_items}), 200

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Expects a JSON payload with 'item_id' and 'quantity'.
    Returns:
        JSON response with order confirmation or error message.
    """
    try:
        # Parse the request data
        data = request.get_json()
        item_id = data.get('item_id')
        quantity = data.get('quantity')

        # Validate input
        if not item_id or not quantity:
            return jsonify({"error": "Invalid input. 'item_id' and 'quantity' are required."}), 400

        # Find the menu item
        item = next((item for item in menu_items if item['id'] == item_id), None)
        if not item:
            return jsonify({"error": "Menu item not found."}), 404

        # Create the order
        order = {
            "order_id": len(orders) + 1,
            "item": item,
            "quantity": quantity,
            "total_price": item['price'] * quantity
        }
        orders.append(order)

        return jsonify({"message": "Order placed successfully.", "order": order}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while placing the order.", "details": str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders.
    Returns:
        JSON response containing the list of orders.
    """
    return jsonify({"orders": orders}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
