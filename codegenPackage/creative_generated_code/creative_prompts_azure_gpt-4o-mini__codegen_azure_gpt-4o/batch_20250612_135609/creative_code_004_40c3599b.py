"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Suggest an API for managing inventory of electrical materials, considering the diverse products listed by Miraya Electric S.A.C. such as cables, connectors, and circuit boards.
Generated: DETERMINISTIC_40c3599b9489eaba
Batch ID: 20250612_135609
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

# In-memory database for inventory
inventory = {}

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Route to list all inventory items
@app.route('/inventory', methods=['GET'])
def list_inventory():
    """
    Endpoint to retrieve all inventory items.
    """
    return jsonify(inventory), 200

# Route to add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    """
    Endpoint to add a new item to the inventory.
    Expected JSON payload:
    {
        "id": "item_id",
        "name": "item_name",
        "category": "item_category",
        "quantity": int,
        "price": float
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'category' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Check if item already exists
    item_id = data['id']
    if item_id in inventory:
        return jsonify({"error": "Item already exists"}), 400

    # Add new item to inventory
    inventory[item_id] = {
        "name": data['name'],
        "category": data['category'],
        "quantity": data['quantity'],
        "price": data['price']
    }
    return jsonify({"message": "Item added successfully"}), 201

# Route to update an existing item
@app.route('/inventory/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """
    Endpoint to update an item in the inventory.
    Expected JSON payload:
    {
        "name": "item_name",
        "category": "item_category",
        "quantity": int,
        "price": float
    }
    """
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'category' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Update item details
    inventory[item_id].update({
        "name": data['name'],
        "category": data['category'],
        "quantity": data['quantity'],
        "price": data['price']
    })
    return jsonify({"message": "Item updated successfully"}), 200

# Route to delete an item from the inventory
@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """
    Endpoint to delete an item from the inventory.
    """
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404

    del inventory[item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

# Route to get a specific item by ID
@app.route('/inventory/<item_id>', methods=['GET'])
def get_inventory_item(item_id):
    """
    Endpoint to retrieve an item by its ID.
    """
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(inventory[item_id]), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
