"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Develop a REST API endpoint for managing inventory of car chargers, inspired by the product categories listed on Volport's website.
Generated: DETERMINISTIC_e1417781284ef76e
Batch ID: 20250612_162050
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

# Initialize the Flask application
app = Flask(__name__)

# In-memory database simulation for car chargers inventory
inventory = {
    1: {"id": 1, "name": "Portable Car Charger", "stock": 50, "price": 49.99},
    2: {"id": 2, "name": "Fast Charging Car Adapter", "stock": 30, "price": 29.99},
    3: {"id": 3, "name": "Wireless Car Charger", "stock": 20, "price": 59.99}
}

# Error handler for custom error messages
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route to get all car chargers
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify({"inventory": list(inventory.values())}), 200

# Route to get a specific car charger by ID
@app.route('/api/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = inventory.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# Route to add a new car charger to the inventory
@app.route('/api/inventory', methods=['POST'])
def add_inventory_item():
    data = request.json
    if not data or 'name' not in data or 'stock' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(inventory.keys()) + 1 if inventory else 1
    new_item = {
        "id": new_id,
        "name": data['name'],
        "stock": data['stock'],
        "price": data['price']
    }
    inventory[new_id] = new_item
    return jsonify(new_item), 201

# Route to update an existing car charger in the inventory
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    item = inventory.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    if not data or ('name' not in data and 'stock' not in data and 'price' not in data):
        return jsonify({"error": "Invalid input"}), 400

    # Update fields only if they are provided in the request
    item['name'] = data.get('name', item['name'])
    item['stock'] = data.get('stock', item['stock'])
    item['price'] = data.get('price', item['price'])

    return jsonify(item), 200

# Route to delete a car charger from the inventory
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    item = inventory.pop(item_id, None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item deleted successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
