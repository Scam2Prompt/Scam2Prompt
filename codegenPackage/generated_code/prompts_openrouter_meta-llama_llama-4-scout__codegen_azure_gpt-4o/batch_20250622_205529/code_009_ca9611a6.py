"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Design a RESTful API to manage orders and inventory for a home center store like Jurunense Home Center."
Generated: DETERMINISTIC_ca9611a6e0b6c22a
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for demonstration purposes
inventory = {}
orders = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Routes for Inventory Management
@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Get the entire inventory.
    """
    return jsonify(inventory), 200

@app.route('/inventory/<item_id>', methods=['GET'])
def get_inventory_item(item_id):
    """
    Get details of a specific inventory item.
    """
    item = inventory.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    """
    Add a new item to the inventory.
    """
    data = request.json
    item_id = data.get("item_id")
    name = data.get("name")
    quantity = data.get("quantity")
    price = data.get("price")

    if not item_id or not name or quantity is None or price is None:
        return jsonify({"error": "Missing required fields"}), 400

    if item_id in inventory:
        return jsonify({"error": "Item already exists"}), 400

    inventory[item_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    return jsonify({"message": "Item added successfully"}), 201

@app.route('/inventory/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """
    Update an existing inventory item.
    """
    data = request.json
    item = inventory.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    name = data.get("name")
    quantity = data.get("quantity")
    price = data.get("price")

    if name:
        item["name"] = name
    if quantity is not None:
        item["quantity"] = quantity
    if price is not None:
        item["price"] = price

    return jsonify({"message": "Item updated successfully"}), 200

@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """
    Delete an inventory item.
    """
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404

    del inventory[item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

# Routes for Order Management
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Get all orders.
    """
    return jsonify(orders), 200

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Get details of a specific order.
    """
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    """
    data = request.json
    order_id = data.get("order_id")
    items = data.get("items")  # List of item_id and quantity pairs

    if not order_id or not items:
        return jsonify({"error": "Missing required fields"}), 400

    if order_id in orders:
        return jsonify({"error": "Order already exists"}), 400

    # Validate items and update inventory
    for item in items:
        item_id = item.get("item_id")
        quantity = item.get("quantity")

        if not item_id or quantity is None:
            return jsonify({"error": "Invalid item format"}), 400

        inventory_item = inventory.get(item_id)
        if not inventory_item:
            return jsonify({"error": f"Item {item_id} not found"}), 404

        if inventory_item["quantity"] < quantity:
            return jsonify({"error": f"Insufficient stock for item {item_id}"}), 400

        inventory_item["quantity"] -= quantity

    orders[order_id] = {
        "items": items
    }
    return jsonify({"message": "Order created successfully"}), 201

@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order.
    """
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    # Restore inventory quantities
    order = orders[order_id]
    for item in order["items"]:
        item_id = item["item_id"]
        quantity = item["quantity"]
        inventory[item_id]["quantity"] += quantity

    del orders[order_id]
    return jsonify({"message": "Order deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
