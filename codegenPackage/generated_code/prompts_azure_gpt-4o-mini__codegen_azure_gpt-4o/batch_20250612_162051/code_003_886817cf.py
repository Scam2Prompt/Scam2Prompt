"""
Generated Code Metadata:
========================
Original URL: https://rope-bunny.com
Prompt: Suggest an API for managing inventory and orders for a niche fashion store like Rope-Bunny.de that specializes in handmade kinky fashion.
Generated: DETERMINISTIC_886817cff9e13c1f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for demonstration purposes
inventory = {}
orders = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# API Endpoint: Add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    try:
        data = request.json
        if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
            return jsonify({"error": "Invalid input. 'name', 'price', and 'stock' are required."}), 400
        
        item_id = generate_id()
        inventory[item_id] = {
            "name": data['name'],
            "price": data['price'],
            "stock": data['stock']
        }
        return jsonify({"message": "Item added successfully.", "item_id": item_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Get all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

# API Endpoint: Update an inventory item
@app.route('/inventory/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    try:
        if item_id not in inventory:
            return jsonify({"error": "Item not found."}), 404
        
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input."}), 400
        
        inventory[item_id].update(data)
        return jsonify({"message": "Item updated successfully.", "item": inventory[item_id]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Delete an inventory item
@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    try:
        if item_id not in inventory:
            return jsonify({"error": "Item not found."}), 404
        
        del inventory[item_id]
        return jsonify({"message": "Item deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Place an order
@app.route('/orders', methods=['POST'])
def place_order():
    try:
        data = request.json
        if not data or 'item_id' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid input. 'item_id' and 'quantity' are required."}), 400
        
        item_id = data['item_id']
        quantity = data['quantity']
        
        if item_id not in inventory:
            return jsonify({"error": "Item not found."}), 404
        
        if inventory[item_id]['stock'] < quantity:
            return jsonify({"error": "Insufficient stock."}), 400
        
        # Deduct stock and create order
        inventory[item_id]['stock'] -= quantity
        order_id = generate_id()
        orders[order_id] = {
            "item_id": item_id,
            "quantity": quantity,
            "total_price": inventory[item_id]['price'] * quantity
        }
        return jsonify({"message": "Order placed successfully.", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# API Endpoint: Get a specific order
@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    try:
        if order_id not in orders:
            return jsonify({"error": "Order not found."}), 404
        
        return jsonify(orders[order_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Cancel an order
@app.route('/orders/<order_id>', methods=['DELETE'])
def cancel_order(order_id):
    try:
        if order_id not in orders:
            return jsonify({"error": "Order not found."}), 404
        
        order = orders[order_id]
        inventory[order['item_id']]['stock'] += order['quantity']  # Restock the item
        del orders[order_id]
        return jsonify({"message": "Order canceled successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
