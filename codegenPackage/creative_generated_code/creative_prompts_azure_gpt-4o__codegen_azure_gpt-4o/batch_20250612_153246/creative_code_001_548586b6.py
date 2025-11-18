"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Generate an API design for managing surgical instrument inventory, referencing specific product categories such as "Cone Knives," "Tongue Depressors," and "Needle Holders" mentioned on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_548586b6e11dff26
Batch ID: 20250612_153246
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

# Sample data to represent the inventory (In production, use a proper database).
inventory = {
    "Cone Knives": [
        {"id": 1, "name": "Cone Knife A", "quantity": 10, "price": 99.99},
        {"id": 2, "name": "Cone Knife B", "quantity": 5, "price": 149.99},
    ],
    "Tongue Depressors": [
        {"id": 1, "name": "Tongue Depressor A", "quantity": 20, "price": 5.99},
    ],
    "Needle Holders": [
        {"id": 1, "name": "Needle Holder A", "quantity": 8, "price": 49.99},
    ],
}


@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Endpoint to retrieve the entire inventory.
    """
    return jsonify({"inventory": inventory}), 200


@app.route('/inventory/<category>', methods=['GET'])
def get_category_inventory(category):
    """
    Endpoint to retrieve inventory for a specific category.
    """
    if category in inventory:
        return jsonify({category: inventory[category]}), 200
    return jsonify({"error": f"Category '{category}' not found"}), 404


@app.route('/inventory/<category>', methods=['POST'])
def add_item_to_category(category):
    """
    Endpoint to add an item to a specific category.
    Request Body:
    {
        "id": int,
        "name": str,
        "quantity": int,
        "price": float
    }
    """
    if category not in inventory:
        return jsonify({"error": f"Category '{category}' not found"}), 404
    
    try:
        item = request.get_json()
        # Validate required fields
        if not all(key in item for key in ("id", "name", "quantity", "price")):
            return jsonify({"error": "Missing required fields"}), 400
        inventory[category].append(item)
        return jsonify({"message": "Item added successfully", "item": item}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/inventory/<category>/<int:item_id>', methods=['PUT'])
def update_item_in_category(category, item_id):
    """
    Endpoint to update an item in a specific category.
    Request Body:
    {
        "name": str (optional),
        "quantity": int (optional),
        "price": float (optional)
    }
    """
    if category not in inventory:
        return jsonify({"error": f"Category '{category}' not found"}), 404
    
    try:
        item_data = request.get_json()
        for item in inventory[category]:
            if item["id"] == item_id:
                item.update({key: value for key, value in item_data.items() if key in item})
                return jsonify({"message": "Item updated successfully", "item": item}), 200
        return jsonify({"error": f"Item with id '{item_id}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/inventory/<category>/<int:item_id>', methods=['DELETE'])
def delete_item_from_category(category, item_id):
    """
    Endpoint to delete an item from a specific category.
    """
    if category not in inventory:
        return jsonify({"error": f"Category '{category}' not found"}), 404
    
    try:
        for item in inventory[category]:
            if item["id"] == item_id:
                inventory[category].remove(item)
                return jsonify({"message": f"Item with id '{item_id}' deleted successfully"}), 200
        return jsonify({"error": f"Item with id '{item_id}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the application (In production, use a proper WSGI server like Gunicorn).
    app.run(debug=True)
```
