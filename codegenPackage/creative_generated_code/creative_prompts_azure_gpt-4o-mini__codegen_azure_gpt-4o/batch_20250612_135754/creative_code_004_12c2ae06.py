"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://limited-drop.com
Prompt: Outline a RESTful API design for managing inventory of limited edition clothing items at Limited Drop, including endpoints for adding and removing items.
Generated: DETERMINISTIC_12c2ae061113cc66
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, well-documented RESTful API design in Python using the Flask framework:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for inventory
inventory = {}

# ================================
# Endpoints for managing inventory
# ================================

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Endpoint to retrieve all items in the inventory.
    Returns:
        JSON response containing all inventory items.
    """
    return jsonify({"inventory": inventory}), 200


@app.route('/inventory', methods=['POST'])
def add_item():
    """
    Endpoint to add a new item to the inventory.
    Request JSON Body:
        {
            "item_id": (str) Unique identifier for the item,
            "name": (str) Name of the clothing item,
            "quantity": (int) Number of items available,
            "price": (float) Price of the item
        }
    Returns:
        JSON response confirming the addition or detailing errors.
    """
    data = request.get_json()

    # Validate request data
    if not data or 'item_id' not in data or 'name' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Invalid request. Please provide item_id, name, quantity, and price."}), 400

    item_id = data['item_id']

    if item_id in inventory:
        return jsonify({"error": f"Item with ID {item_id} already exists."}), 400

    # Add item to inventory
    inventory[item_id] = {
        "name": data['name'],
        "quantity": data['quantity'],
        "price": data['price']
    }
    return jsonify({"message": f"Item with ID {item_id} added successfully.", "item": inventory[item_id]}), 201


@app.route('/inventory/<string:item_id>', methods=['DELETE'])
def remove_item(item_id):
    """
    Endpoint to remove an item from the inventory by item_id.
    Path Parameters:
        item_id: (str) Unique identifier for the item.
    Returns:
        JSON response confirming the removal or detailing errors.
    """
    if item_id not in inventory:
        return jsonify({"error": f"Item with ID {item_id} does not exist."}), 404

    removed_item = inventory.pop(item_id)
    return jsonify({"message": f"Item with ID {item_id} removed successfully.", "item": removed_item}), 200


# ==========================
# Error Handling Middleware
# ==========================

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 Not Found errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return jsonify({"error": "Internal server error"}), 500


# =================
# Application Entry
# =================

if __name__ == '__main__':
    # Run the Flask app in debug mode for development purposes
    app.run(debug=True)
```

This Flask application provides endpoints for managing inventory with robust error handling, adhering to RESTful API conventions.
