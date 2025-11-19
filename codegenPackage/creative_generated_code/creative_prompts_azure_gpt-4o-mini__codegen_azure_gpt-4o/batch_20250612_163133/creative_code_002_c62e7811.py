"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radical-wear.cz
Prompt: Create an API endpoint for managing user accounts and orders, referencing the user account features found on Radical Wear's site.
Generated: DETERMINISTIC_c62e7811c239f896
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready Python code example using Flask to create an API endpoint for managing user accounts and orders:

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for users and orders
users = {}
orders = {}

# Error messages
USER_NOT_FOUND_ERROR = {"error": "User not found"}
ORDER_NOT_FOUND_ERROR = {"error": "Order not found"}

# Utility functions
def generate_id():
    """Generate a unique identifier."""
    return str(uuid.uuid4())

# Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user account.
    Body JSON: {"name": "User Name", "email": "user@example.com"}
    """
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = generate_id()
    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
    }
    
    return jsonify({"message": "User created", "user": users[user_id]}), 201


@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve user details.
    Path parameter: user_id (string)
    """
    user = users.get(user_id)
    if not user:
        return jsonify(USER_NOT_FOUND_ERROR), 404
    
    return jsonify(user), 200


@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Create a new order for a user.
    Body JSON: {"user_id": "user_id", "items": ["item1", "item2"]}
    """
    data = request.json
    if not data or 'user_id' not in data or 'items' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = data['user_id']
    if user_id not in users:
        return jsonify(USER_NOT_FOUND_ERROR), 404

    order_id = generate_id()
    orders[order_id] = {
        "id": order_id,
        "user_id": user_id,
        "items": data['items'],
    }
    
    return jsonify({"message": "Order created", "order": orders[order_id]}), 201


@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve order details.
    Path parameter: order_id (string)
    """
    order = orders.get(order_id)
    if not order:
        return jsonify(ORDER_NOT_FOUND_ERROR), 404

    return jsonify(order), 200


@app.route('/api/users/<user_id>/orders', methods=['GET'])
def get_user_orders(user_id):
    """
    Retrieve all orders for a specific user.
    Path parameter: user_id (string)
    """
    if user_id not in users:
        return jsonify(USER_NOT_FOUND_ERROR), 404

    user_orders = [order for order in orders.values() if order['user_id'] == user_id]
    return jsonify(user_orders), 200


@app.route('/api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order.
    Path parameter: order_id (string)
    """
    if order_id not in orders:
        return jsonify(ORDER_NOT_FOUND_ERROR), 404

    del orders[order_id]
    return jsonify({"message": "Order deleted"}), 200


@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user account and their orders.
    Path parameter: user_id (string)
    """
    if user_id not in users:
        return jsonify(USER_NOT_FOUND_ERROR), 404

    # Remove user's orders
    user_orders = [order_id for order_id, order in orders.items() if order['user_id'] == user_id]
    for order_id in user_orders:
        del orders[order_id]

    # Remove user
    del users[user_id]
    return jsonify({"message": "User and their orders deleted"}), 200


# Error handling
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


# Main entry point to run the server
if __name__ == '__main__':
    app.run(debug=True)
```
