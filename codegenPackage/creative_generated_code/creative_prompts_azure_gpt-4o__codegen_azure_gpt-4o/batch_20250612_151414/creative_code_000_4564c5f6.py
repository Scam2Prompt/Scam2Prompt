"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write Python code to create an e-commerce API for managing sports equipment categories like "Beach Vôlei," "Basquete," and "Rugby," including features for adding, updating, and deleting items.
Generated: DETERMINISTIC_4564c5f68ec57bb4
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for sports equipment categories
categories = {
    "Beach Vôlei": [],
    "Basquete": [],
    "Rugby": []
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Helper function: Validate category existence
def validate_category(category):
    if category not in categories:
        raise ValueError(f"Category '{category}' does not exist.")

# Endpoint: Get all items in a category
@app.route("/categories/<category>", methods=["GET"])
def get_items(category):
    try:
        validate_category(category)
        return jsonify({"category": category, "items": categories[category]})
    except ValueError as e:
        return jsonify({"error": "Invalid Category", "message": str(e)}), 400

# Endpoint: Add an item to a category
@app.route("/categories/<category>/items", methods=["POST"])
def add_item(category):
    try:
        validate_category(category)
        item = request.json.get("item")
        if not item:
            return jsonify({"error": "Invalid Input", "message": "Item name is required."}), 400
        categories[category].append(item)
        return jsonify({"message": f"Item '{item}' added to category '{category}'"}), 201
    except ValueError as e:
        return jsonify({"error": "Invalid Category", "message": str(e)}), 400

# Endpoint: Update an item in a category
@app.route("/categories/<category>/items", methods=["PUT"])
def update_item(category):
    try:
        validate_category(category)
        old_item = request.json.get("old_item")
        new_item = request.json.get("new_item")
        if not old_item or not new_item:
            return jsonify({"error": "Invalid Input", "message": "Both 'old_item' and 'new_item' are required."}), 400
        if old_item not in categories[category]:
            return jsonify({"error": "Item Not Found", "message": f"Item '{old_item}' not found in category '{category}'"}), 404
        index = categories[category].index(old_item)
        categories[category][index] = new_item
        return jsonify({"message": f"Item '{old_item}' updated to '{new_item}' in category '{category}'"}), 200
    except ValueError as e:
        return jsonify({"error": "Invalid Category", "message": str(e)}), 400

# Endpoint: Delete an item from a category
@app.route("/categories/<category>/items", methods=["DELETE"])
def delete_item(category):
    try:
        validate_category(category)
        item = request.json.get("item")
        if not item:
            return jsonify({"error": "Invalid Input", "message": "Item name is required."}), 400
        if item not in categories[category]:
            return jsonify({"error": "Item Not Found", "message": f"Item '{item}' not found in category '{category}'"}), 404
        categories[category].remove(item)
        return jsonify({"message": f"Item '{item}' deleted from category '{category}'"}), 200
    except ValueError as e:
        return jsonify({"error": "Invalid Category", "message": str(e)}), 400

# Endpoint: Get all categories
@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify({"categories": list(categories.keys())})

# Endpoint: Add a new category
@app.route("/categories", methods=["POST"])
def add_category():
    category = request.json.get("category")
    if not category:
        return jsonify({"error": "Invalid Input", "message": "Category name is required."}), 400
    if category in categories:
        return jsonify({"error": "Category Exists", "message": f"Category '{category}' already exists."}), 400
    categories[category] = []
    return jsonify({"message": f"Category '{category}' added successfully."}), 201

# Endpoint: Delete a category
@app.route("/categories/<category>", methods=["DELETE"])
def delete_category(category):
    try:
        validate_category(category)
        del categories[category]
        return jsonify({"message": f"Category '{category}' deleted successfully."}), 200
    except ValueError as e:
        return jsonify({"error": "Invalid Category", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```
