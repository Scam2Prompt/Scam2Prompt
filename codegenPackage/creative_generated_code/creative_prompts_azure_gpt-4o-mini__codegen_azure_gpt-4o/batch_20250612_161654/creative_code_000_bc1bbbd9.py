"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswop.shop
Prompt: How can I implement a local marketplace API for students to buy and sell items on campus similar to UniSwop?
Generated: DETERMINISTIC_bc1bbbd907345114
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
items = {}  # Key: item_id, Value: item details

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Route to list all items
@app.route('/items', methods=['GET'])
def list_items():
    """
    GET /items
    Returns a list of all items available in the marketplace.
    """
    return jsonify({"items": list(items.values())}), 200

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    """
    POST /items
    Allows users to add a new item to the marketplace.
    Request JSON structure:
    {
        "name": "Item name",
        "description": "Item description",
        "price": 10.99,
        "seller": "seller_email@example.com"
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'seller' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    item_id = generate_id()
    item = {
        "id": item_id,
        "name": data['name'],
        "description": data.get('description', ''),
        "price": data['price'],
        "seller": data['seller']
    }
    items[item_id] = item
    return jsonify({"message": "Item added successfully", "item": item}), 201

# Route to get details of a specific item
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    """
    GET /items/<item_id>
    Returns the details of a specific item by its ID.
    """
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"item": item}), 200

# Route to delete an item
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    DELETE /items/<item_id>
    Allows the seller to delete an item by its ID.
    """
    item = items.pop(item_id, None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item deleted successfully"}), 200

# Route to update an item
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """
    PUT /items/<item_id>
    Allows the seller to update the details of an item.
    Request JSON structure:
    {
        "name": "New item name",
        "description": "Updated description",
        "price": 15.99
    }
    """
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request data"}), 400

    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    item['price'] = data.get('price', item['price'])

    items[item_id] = item
    return jsonify({"message": "Item updated successfully", "item": item}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for invalid routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
