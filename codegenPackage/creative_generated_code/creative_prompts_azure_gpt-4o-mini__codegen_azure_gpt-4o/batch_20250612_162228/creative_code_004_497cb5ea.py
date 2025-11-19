"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Illustrate how to implement a RESTful API to manage inventory for various additives and pigments, referencing the product categories from M J Pigment & Additives.
Generated: DETERMINISTIC_497cb5eaab3548c1
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for simplicity
inventory = {
    "additives": [],
    "pigments": [],
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).data
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": str(e)}), 500

# Route to get all items in a category
@app.route("/api/inventory/<category>", methods=["GET"])
def get_inventory(category):
    if category not in inventory:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(inventory[category])

# Route to add a new item to a category
@app.route("/api/inventory/<category>", methods=["POST"])
def add_to_inventory(category):
    if category not in inventory:
        return jsonify({"error": "Category not found"}), 404
    
    item = request.json
    if not item or "name" not in item or "quantity" not in item:
        return jsonify({"error": "Invalid item data"}), 400

    inventory[category].append(item)
    return jsonify({"message": "Item added successfully"}), 201

# Route to update an item's quantity in a category
@app.route("/api/inventory/<category>/<item_name>", methods=["PUT"])
def update_inventory(category, item_name):
    if category not in inventory:
        return jsonify({"error": "Category not found"}), 404

    item = next((i for i in inventory[category] if i["name"] == item_name), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    update_data = request.json
    if not update_data or "quantity" not in update_data:
        return jsonify({"error": "Invalid update data"}), 400
    
    item["quantity"] = update_data["quantity"]
    return jsonify({"message": "Item updated successfully"}), 200

# Route to delete an item from a category
@app.route("/api/inventory/<category>/<item_name>", methods=["DELETE"])
def delete_from_inventory(category, item_name):
    if category not in inventory:
        return jsonify({"error": "Category not found"}), 404

    item = next((i for i in inventory[category] if i["name"] == item_name), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory[category].remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200

# Route to list all categories
@app.route("/api/inventory/categories", methods=["GET"])
def get_categories():
    return jsonify(list(inventory.keys()))

# Run the app
if __name__ == "__main__":
    # For production usage, use a WSGI server like Gunicorn
    app.run(debug=False, host="0.0.0.0", port=5000)
```
