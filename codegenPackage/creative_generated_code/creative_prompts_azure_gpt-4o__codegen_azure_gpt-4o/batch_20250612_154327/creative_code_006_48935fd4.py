"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Develop a REST API endpoint to manage inventory for automotive parts, including batteries, sound systems, and decorative items, based on the product details from paxosrew.com.
Generated: DETERMINISTIC_48935fd4a6cabd08
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for a REST API using Flask. It implements endpoints to manage automotive inventory, including batteries, sound systems, and decorative items.

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample inventory data
inventory = {
    "batteries": [],
    "sound_systems": [],
    "decorative_items": []
}

# Custom error handler
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="An unexpected error occurred."), 500

@app.route("/inventory/<category>", methods=["GET"])
def get_items(category):
    """
    Retrieve all items in a specific category.
    :param category: Category of items (batteries, sound_systems, decorative_items)
    """
    if category in inventory:
        return jsonify(inventory[category]), 200
    return jsonify(error="Category not found"), 404

@app.route("/inventory/<category>", methods=["POST"])
def add_item(category):
    """
    Add a new item to a specific category.
    :param category: Category of items (batteries, sound_systems, decorative_items)
    """
    if category not in inventory:
        return jsonify(error="Category not found"), 404

    data = request.get_json()
    if not data or "name" not in data or "quantity" not in data:
        return jsonify(error="Invalid payload. 'name' and 'quantity' are required."), 400

    item = {
        "name": data["name"],
        "quantity": data["quantity"]
    }
    inventory[category].append(item)
    return jsonify(message="Item added successfully!", item=item), 201

@app.route("/inventory/<category>/<item_name>", methods=["PUT"])
def update_item(category, item_name):
    """
    Update the quantity of an existing item in a specific category.
    :param category: Category of items (batteries, sound_systems, decorative_items)
    :param item_name: Name of the item to update
    """
    if category not in inventory:
        return jsonify(error="Category not found"), 404

    data = request.get_json()
    if not data or "quantity" not in data:
        return jsonify(error="Invalid payload. 'quantity' is required."), 400

    for item in inventory[category]:
        if item["name"] == item_name:
            item["quantity"] = data["quantity"]
            return jsonify(message="Item quantity updated successfully!", item=item), 200

    return jsonify(error="Item not found"), 404

@app.route("/inventory/<category>/<item_name>", methods=["DELETE"])
def delete_item(category, item_name):
    """
    Delete an item from a specific category.
    :param category: Category of items (batteries, sound_systems, decorative_items)
    :param item_name: Name of the item to delete
    """
    if category not in inventory:
        return jsonify(error="Category not found"), 404

    for item in inventory[category]:
        if item["name"] == item_name:
            inventory[category].remove(item)
            return jsonify(message="Item deleted successfully!", item=item), 200

    return jsonify(error="Item not found"), 404

@app.route("/", methods=["GET"])
def index():
    """
    Endpoint to verify the API is running.
    """
    return jsonify(message="Automotive Inventory Management API is running"), 200

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

To run this code:
1. Install `Flask` (`pip install flask`).
2. Save the code to a Python file (e.g., `app.py`).
3. Run it using `python app.py`.
4. Test the REST API using tools like Postman or `curl`.
