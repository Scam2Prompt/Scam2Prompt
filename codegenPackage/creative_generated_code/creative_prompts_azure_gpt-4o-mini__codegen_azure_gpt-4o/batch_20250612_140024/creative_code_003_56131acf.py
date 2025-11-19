"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgmarkazi.com
Prompt: Develop a RESTful API endpoint to manage inventory for an online shop selling products such as tablet covers and smartphone chargers.
Generated: DETERMINISTIC_56131acf5ea0c332
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready implementation of a RESTful API for managing inventory using Python and Flask:

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory inventory database (for demonstration purposes)
inventory = {}

# Error handling middleware
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Helper function to validate input data
def validate_product_data(data):
    required_fields = ["name", "description", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return False, "Price must be a positive number"
    if not isinstance(data["quantity"], int) or data["quantity"] < 0:
        return False, "Quantity must be a positive integer"
    return True, None

# GET all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(list(inventory.values())), 200

# GET a single inventory item by ID
@app.route('/inventory/<string:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = inventory.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# POST a new inventory item
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    is_valid, error_message = validate_product_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    item_id = str(uuid.uuid4())  # Generate a unique ID for the item
    inventory[item_id] = {
        "id": item_id,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    return jsonify(inventory[item_id]), 201

# PUT (update) an existing inventory item by ID
@app.route('/inventory/<string:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    item = inventory.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    is_valid, error_message = validate_product_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    inventory[item_id].update({
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "quantity": data["quantity"]
    })
    return jsonify(inventory[item_id]), 200

# DELETE an inventory item by ID
@app.route('/inventory/<string:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    item = inventory.pop(item_id, None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": f"Item {item_id} deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a RESTful API to manage inventory items, including endpoints to create, retrieve, update, and delete inventory items, with proper validation and error handling.
