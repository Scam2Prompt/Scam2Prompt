"""
Generated Code Metadata:
========================
Original URL: https://biamtechintl.com
Prompt: "Develop a RESTful API to manage orders for surgical kits, including laparotomy sets, vaginal sets, and bone surgery instruments."
Generated: DETERMINISTIC_67b312bc7fee8f07
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for orders
orders = []
order_id_counter = 1

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Helper function to find an order by ID
def find_order(order_id):
    return next((order for order in orders if order["id"] == order_id), None)

# Route: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    """
    return jsonify(orders), 200

# Route: Get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve a specific order by ID.
    """
    order = find_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

# Route: Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    """
    global order_id_counter
    data = request.get_json()

    # Validate input
    if not data or "type" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Create the order
    new_order = {
        "id": order_id_counter,
        "type": data["type"],
        "quantity": data["quantity"]
    }
    orders.append(new_order)
    order_id_counter += 1

    return jsonify(new_order), 201

# Route: Update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order.
    """
    order = find_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()

    # Validate input
    if not data or "type" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Update the order
    order["type"] = data["type"]
    order["quantity"] = data["quantity"]

    return jsonify(order), 200

# Route: Delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by ID.
    """
    order = find_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    orders.remove(order)
    return jsonify({"message": "Order deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
