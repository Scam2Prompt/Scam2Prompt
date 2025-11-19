"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Illustrate how to implement a RESTful API to manage inventory for various additives and pigments, referencing the product categories from M J Pigment & Additives.
Generated: DETERMINISTIC_497cb5eaab3548c1
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database for the inventory
inventory = {
    "additives": [],
    "pigments": []
}

# Helper function to find an item by ID
def find_item(category, item_id):
    return next((item for item in inventory[category] if item['id'] == item_id), None)

# Routes for managing additives and pigments
@app.route('/api/<category>', methods=['GET'])
def get_items(category):
    """
    Get all items in a category (additives or pigments).
    """
    if category not in inventory:
        abort(404, description="Category not found")
    return jsonify(inventory[category]), 200

@app.route('/api/<category>/<int:item_id>', methods=['GET'])
def get_item(category, item_id):
    """
    Get a specific item by ID in a category.
    """
    if category not in inventory:
        abort(404, description="Category not found")
    item = find_item(category, item_id)
    if not item:
        abort(404, description="Item not found")
    return jsonify(item), 200

@app.route('/api/<category>', methods=['POST'])
def create_item(category):
    """
    Create a new item in a category.
    """
    if category not in inventory:
        abort(404, description="Category not found")
    if not request.json or 'name' not in request.json or 'quantity' not in request.json:
        abort(400, description="Invalid request payload")
    
    new_item = {
        "id": len(inventory[category]) + 1,  # Simple auto-increment ID
        "name": request.json['name'],
        "quantity": request.json['quantity']
    }
    inventory[category].append(new_item)
    return jsonify(new_item), 201

@app.route('/api/<category>/<int:item_id>', methods=['PUT'])
def update_item(category, item_id):
    """
    Update an existing item in a category.
    """
    if category not in inventory:
        abort(404, description="Category not found")
    item = find_item(category, item_id)
    if not item:
        abort(404, description="Item not found")
    if not request.json:
        abort(400, description="Invalid request payload")
    
    # Update fields if provided
    item['name'] = request.json.get('name', item['name'])
    item['quantity'] = request.json.get('quantity', item['quantity'])
    return jsonify(item), 200

@app.route('/api/<category>/<int:item_id>', methods=['DELETE'])
def delete_item(category, item_id):
    """
    Delete an item from a category.
    """
    if category not in inventory:
        abort(404, description="Category not found")
    item = find_item(category, item_id)
    if not item:
        abort(404, description="Item not found")
    inventory[category].remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 errors.
    """
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
