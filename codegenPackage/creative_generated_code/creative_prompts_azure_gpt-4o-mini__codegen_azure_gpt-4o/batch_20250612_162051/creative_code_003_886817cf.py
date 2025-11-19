"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Suggest an API for managing inventory and orders for a niche fashion store like Rope-Bunny.de that specializes in handmade kinky fashion.
Generated: DETERMINISTIC_886817cff9e13c1f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data storage
inventory = {}
orders = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint to create a new inventory item
@app.route('/api/inventory', methods=['POST'])
def create_inventory_item():
    """
    Add a new item to the inventory.
    Request Body:
    {
        "name": "Corset",
        "quantity": 10,
        "price": 49.99
    }
    """
    data = request.json
    if not data or 'name' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    item_id = generate_id()
    inventory[item_id] = {
        "name": data['name'],
        "quantity": data['quantity'],
        "price": data['price']
    }
    return jsonify({"id": item_id, "message": "Inventory item created successfully"}), 201

# Endpoint to get all inventory items
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """Retrieve the list of all inventory items."""
    return jsonify(inventory), 200

# Endpoint to update an inventory item
@app.route('/api/inventory/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """
    Update the details of an inventory item.
    Request Body:
    {
        "name": "Updated Corset",
        "quantity": 5,
        "price": 59.99
    }
    """
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.json
    if not data or 'name' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    inventory[item_id].update({
        "name": data['name'],
        "quantity": data['quantity'],
        "price": data['price']
    })
    return jsonify({"message": "Inventory item updated successfully"}), 200

# Endpoint to delete an inventory item
@app.route('/api/inventory/<item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """Delete an inventory item."""
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404
    
    del inventory[item_id]
    return jsonify({"message": "Inventory item deleted successfully"}), 200

# Endpoint to create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request Body:
    {
        "items": [
            {"item_id": "12345", "quantity": 2},
            {"item_id": "67890", "quantity": 1}
        ]
    }
    """
    data = request.json
    if not data or 'items' not in data or not isinstance(data['items'], list):
        return jsonify({"error": "Invalid input"}), 400
    
    order_id = generate_id()
    order_items = []
    for item in data['items']:
        item_id = item.get('item_id')
        quantity = item.get('quantity')
        if item_id not in inventory or inventory[item_id]['quantity'] < quantity:
            return jsonify({"error": f"Insufficient stock for item {item_id}"}), 400
        
        # Deduct inventory quantity
        inventory[item_id]['quantity'] -= quantity
        order_items.append({
            "item_id": item_id,
            "name": inventory[item_id]['name'],
            "quantity": quantity,
            "price": inventory[item_id]['price']
        })
    
    orders[order_id] = {
        "items": order_items,
        "total_price": sum(item['price'] * item['quantity'] for item in order_items)
    }
    return jsonify({"id": order_id, "message": "Order created successfully"}), 201

# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """Retrieve the list of all orders."""
    return jsonify(orders), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
