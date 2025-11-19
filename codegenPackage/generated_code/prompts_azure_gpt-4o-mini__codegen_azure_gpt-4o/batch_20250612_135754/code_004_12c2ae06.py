"""
Generated Code Metadata:
========================
Original URL: https://limited-drop.com
Prompt: Outline a RESTful API design for managing inventory of limited edition clothing items at Limited Drop, including endpoints for adding and removing items.
Generated: DETERMINISTIC_12c2ae061113cc66
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for inventory (for demonstration purposes)
inventory = {}

# Helper function to generate unique item IDs
def generate_item_id():
    return str(len(inventory) + 1)

# Endpoint: Get all items in inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    GET /inventory
    Returns the list of all items in the inventory.
    """
    return jsonify({"inventory": inventory}), 200

# Endpoint: Add a new item to inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    """
    POST /inventory
    Adds a new item to the inventory.
    Request Body:
    {
        "name": "Item Name",
        "description": "Item Description",
        "price": 100.00,
        "quantity": 10
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "price", "quantity")):
            return jsonify({"error": "Invalid request body"}), 400

        item_id = generate_item_id()
        inventory[item_id] = {
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "quantity": data["quantity"]
        }
        return jsonify({"message": "Item added successfully", "item_id": item_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Remove an item from inventory
@app.route('/inventory/<item_id>', methods=['DELETE'])
def remove_item(item_id):
    """
    DELETE /inventory/<item_id>
    Removes an item from the inventory by its ID.
    """
    try:
        if item_id not in inventory:
            return jsonify({"error": "Item not found"}), 404

        del inventory[item_id]
        return jsonify({"message": "Item removed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
