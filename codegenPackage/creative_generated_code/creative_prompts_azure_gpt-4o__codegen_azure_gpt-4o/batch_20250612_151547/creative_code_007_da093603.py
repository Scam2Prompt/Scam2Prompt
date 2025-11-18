"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Develop a REST API for managing product categories like "Combination Machines" and "Overlock and Coverstitch Machines" on an e-commerce site similar to Brother NZ.
Generated: DETERMINISTIC_da093603c8313270
Batch ID: 20250612_151547
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

# In-memory data store for product categories
categories = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "description": str(e)}), 500

# Helper function to validate category data
def validate_category_data(data):
    if not data.get("name"):
        return "Category name is required."
    if not isinstance(data.get("name"), str):
        return "Category name must be a string."
    return None

# Route: Get all categories
@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(list(categories.values())), 200

# Route: Get a category by ID
@app.route("/categories/<int:category_id>", methods=["GET"])
def get_category_by_id(category_id):
    category = categories.get(category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200

# Route: Create a new category
@app.route("/categories", methods=["POST"])
def create_category():
    data = request.json
    error = validate_category_data(data)
    if error:
        return jsonify({"error": error}), 400

    new_id = max(categories.keys(), default=0) + 1
    category = {"id": new_id, "name": data["name"]}
    categories[new_id] = category
    return jsonify(category), 201

# Route: Update an existing category
@app.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    category = categories.get(category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404

    data = request.json
    error = validate_category_data(data)
    if error:
        return jsonify({"error": error}), 400

    category["name"] = data["name"]
    return jsonify(category), 200

# Route: Delete a category by ID
@app.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    if category_id not in categories:
        return jsonify({"error": "Category not found"}), 404

    del categories[category_id]
    return jsonify({"message": "Category deleted successfully"}), 200

# Application entry point
if __name__ == "__main__":
    app.run(debug=True)
```

This code provides a REST API for managing product categories using Flask, a lightweight web framework for Python. It includes endpoints for CRUD operations and has proper error handling and validation.
