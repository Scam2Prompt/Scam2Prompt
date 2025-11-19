"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Provide an API recommendation for managing agricultural machinery inventory, similar to the tractor attachments offered by JECO.
Generated: DETERMINISTIC_10986a5db2e759b0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for the inventory
inventory = {
    "1": {"name": "Plow", "type": "Attachment", "quantity": 10, "description": "Used for soil preparation"},
    "2": {"name": "Harvester", "type": "Machine", "quantity": 5, "description": "Used for harvesting crops"},
}

# Error handling utility functions
def item_not_found(item_id):
    return jsonify({"error": f"Item with ID {item_id} not found"}), 404

def bad_request(message):
    return jsonify({"error": message}), 400

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Retrieve the full inventory.

    Returns:
        JSON object containing all inventory items.
    """
    return jsonify(inventory)

@app.route('/inventory/<item_id>', methods=['GET'])
def get_item(item_id):
    """
    Retrieve a specific inventory item by ID.

    Args:
        item_id (str): The ID of the item to retrieve.

    Returns:
        JSON object containing the item details if found, or an error message if not.
    """
    item = inventory.get(item_id)
    if not item:
        return item_not_found(item_id)
    return jsonify({item_id: item})

@app.route('/inventory', methods=['POST'])
def add_item():
    """
    Add a new item to the inventory.

    Request body:
        - name (str): Name of the item.
        - type (str): Type of the item, e.g., "Attachment" or "Machine".
        - quantity (int): Quantity of the item in stock.
        - description (str): Description of the item.

    Returns:
        Success message or error details.
    """
    data = request.json
    if not data:
        return bad_request("Request body must be JSON formatted")
    
    name = data.get("name")
    item_type = data.get("type")
    quantity = data.get("quantity")
    description = data.get("description")

    if not all([name, item_type, quantity, description]):
        return bad_request("All fields (name, type, quantity, description) are required")

    try:
        quantity = int(quantity)
        if quantity < 0:
            return bad_request("Quantity must be a non-negative integer")
    except ValueError:
        return bad_request("Quantity must be an integer")

    new_id = str(len(inventory) + 1)
    inventory[new_id] = {
        "name": name,
        "type": item_type,
        "quantity": quantity,
        "description": description
    }
    return jsonify({"message": "Item added successfully", "item_id": new_id}), 201

@app.route('/inventory/<item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Update an existing inventory item.

    Args:
        item_id (str): The ID of the item to update.

    Request body:
        Fields to update (partial or complete):
            - name (str)
            - type (str)
            - quantity (int)
            - description (str)

    Returns:
        Success message or error details.
    """
    item = inventory.get(item_id)
    if not item:
        return item_not_found(item_id)
    
    data = request.json
    if not data:
        return bad_request("Request body must be JSON formatted")
    
    name = data.get("name", item["name"])
    item_type = data.get("type", item["type"])
    quantity = data.get("quantity", item["quantity"])
    description = data.get("description", item["description"])

    try:
        quantity = int(quantity)
        if quantity < 0:
            return bad_request("Quantity must be a non-negative integer")
    except ValueError:
        return bad_request("Quantity must be an integer")
    
    inventory[item_id] = {
        "name": name,
        "type": item_type,
        "quantity": quantity,
        "description": description
    }
    return jsonify({"message": "Item updated successfully", "item_id": item_id}), 200

@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Delete an inventory item by ID.

    Args:
        item_id (str): The ID of the item to delete.

    Returns:
        Success message or error details.
    """
    item = inventory.pop(item_id, None)
    if not item:
        return item_not_found(item_id)
    return jsonify({"message": "Item deleted successfully", "item_id": item_id}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
