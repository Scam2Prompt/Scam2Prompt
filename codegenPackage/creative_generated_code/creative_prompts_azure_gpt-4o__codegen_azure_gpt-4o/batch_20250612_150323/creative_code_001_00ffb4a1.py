"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Generate an API recommendation for managing inventory of diving gear, including items like "регуляторы и октопусы" and "компенсаторы плавучести," based on the catalog structure from https://opensea.ru.
Generated: DETERMINISTIC_00ffb4a1bdc1097a
Batch ID: 20250612_150323
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

# Sample inventory data structure
inventory = [
    {"id": 1, "name": "Регулятор", "category": "регуляторы и октопусы", "quantity": 10, "price": 25000},
    {"id": 2, "name": "Октопус", "category": "регуляторы и октопусы", "quantity": 5, "price": 12000},
    {"id": 3, "name": "Компенсатор плавучести", "category": "компенсаторы плавучести", "quantity": 7, "price": 35000},
]

# Error messages for consistent API responses
ERROR_ITEM_NOT_FOUND = {"error": "Item not found"}
ERROR_INVALID_DATA = {"error": "Invalid data provided"}

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Endpoint to retrieve the entire inventory.
    Returns:
        JSON object containing the list of all items in inventory.
    """
    return jsonify(inventory), 200

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Endpoint to retrieve a specific inventory item by id.
    Args:
        item_id (int): ID of the item to retrieve.
    Returns:
        JSON object containing the item's details or an error if not found.
    """
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify(ERROR_ITEM_NOT_FOUND), 404

@app.route('/inventory', methods=['POST'])
def add_item():
    """
    Endpoint to add a new inventory item.
    Expects JSON payload with 'name', 'category', 'quantity', and 'price'.
    Returns:
        JSON object containing the newly created item or an error if data is invalid.
    """
    try:
        data = request.get_json()
        if not all(k in data for k in ('name', 'category', 'quantity', 'price')):
            return jsonify(ERROR_INVALID_DATA), 400

        new_item = {
            "id": inventory[-1]['id'] + 1 if inventory else 1,  # Generate a new ID
            "name": data['name'],
            "category": data['category'],
            "quantity": int(data['quantity']),
            "price": float(data['price']),
        }
        inventory.append(new_item)
        return jsonify(new_item), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Endpoint to update an existing inventory item.
    Expects JSON payload with optional 'name', 'category', 'quantity', or 'price'.
    Returns:
        JSON object containing the updated item or an error if not found.
    """
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify(ERROR_ITEM_NOT_FOUND), 404

    try:
        data = request.get_json()
        if 'name' in data:
            item['name'] = data['name']
        if 'category' in data:
            item['category'] = data['category']
        if 'quantity' in data:
            item['quantity'] = int(data['quantity'])
        if 'price' in data:
            item['price'] = float(data['price'])
        return jsonify(item), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Endpoint to delete an inventory item by id.
    Args:
        item_id (int): ID of the item to delete.
    Returns:
        Success message or error if not found.
    """
    global inventory
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify(ERROR_ITEM_NOT_FOUND), 404

    inventory = [i for i in inventory if i['id'] != item_id]
    return jsonify({"message": f"Item with ID {item_id} deleted"}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
