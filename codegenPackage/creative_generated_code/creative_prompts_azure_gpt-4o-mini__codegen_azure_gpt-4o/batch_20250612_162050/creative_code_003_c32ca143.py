"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Provide an example of a RESTful API for tracking customer orders at a King of Ice Cream snow cone truck.
Generated: DETERMINISTIC_c32ca143e0ad1306
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database to store orders
orders = []
order_id_counter = 1

# Routes for the RESTful API

@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    Returns:
        JSON object containing a list of all orders.
    """
    return jsonify({"orders": orders}), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve a single order by ID.
    Args:
        order_id (int): ID of the order to retrieve.
    Returns:
        JSON object containing the order details or a 404 error if not found.
    """
    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request Body:
        JSON object containing the customer name and items.
    Returns:
        JSON object confirming the creation of the new order.
    """
    global order_id_counter
    data = request.get_json()
    if not data or not data.get("customer_name") or not data.get("items"):
        return jsonify({"error": "Invalid data provided"}), 400

    new_order = {
        "id": order_id_counter,
        "customer_name": data["customer_name"],
        "items": data["items"],  # List of items ordered
        "status": "Pending"  # Default status
    }
    orders.append(new_order)
    order_id_counter += 1
    return jsonify(new_order), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order by ID.
    Args:
        order_id (int): ID of the order to update.
    Request Body:
        JSON object containing the fields to update (customer_name, items, status).
    Returns:
        JSON object confirming the update or a 404 error if not found.
    """
    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data provided"}), 400

    # Update fields if they exist in the request body
    if "customer_name" in data:
        order["customer_name"] = data["customer_name"]
    if "items" in data:
        order["items"] = data["items"]
    if "status" in data:
        order["status"] = data["status"]

    return jsonify(order), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by ID.
    Args:
        order_id (int): ID of the order to delete.
    Returns:
        JSON object confirming the deletion or a 404 error if not found.
    """
    global orders
    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    orders = [order for order in orders if order["id"] != order_id]
    return jsonify({"message": f"Order {order_id} deleted"}), 200

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for unsupported routes.
    Returns:
        JSON object with an error message.
    """
    return jsonify({"error": "Not found"}), 404

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```
