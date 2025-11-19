"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Suggest a framework for developing a digital catalog similar to the "کاتالوگ دیجیتال" offered by Karen Fixing for their facade products.
Generated: DETERMINISTIC_c2be0e6fb9bdb8f4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code using the Flask framework for building a digital catalog. This example illustrates a basic backend API for managing product facade catalogs. It includes endpoints for fetching, adding, updating, and deleting catalog items.

```python
from flask import Flask, jsonify, request
import uuid

# Initialize the Flask app
app = Flask(__name__)

# In-memory database to store catalog items (for demonstration purposes)
# Replace this with an actual database (e.g., PostgreSQL, MongoDB) in production.
catalog_items = {}

# Error messages
ERROR_ITEM_NOT_FOUND = {"error": "Item not found"}
ERROR_INVALID_INPUT = {"error": "Invalid input data"}

# Route: Get all catalog items
@app.route('/catalog', methods=['GET'])
def get_catalog_items():
    """
    Retrieve all catalog items.
    """
    return jsonify(list(catalog_items.values())), 200

# Route: Get a specific catalog item by ID
@app.route('/catalog/<item_id>', methods=['GET'])
def get_catalog_item(item_id):
    """
    Retrieve a specific catalog item by ID.
    """
    item = catalog_items.get(item_id)
    if item:
        return jsonify(item), 200
    return jsonify(ERROR_ITEM_NOT_FOUND), 404

# Route: Add a new catalog item
@app.route('/catalog', methods=['POST'])
def add_catalog_item():
    """
    Add a new catalog item. Expects JSON input with 'name', 'description', and 'price'.
    """
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        
        # Validate input data
        if not name or not description or not isinstance(price, (int, float)) or price < 0:
            return jsonify(ERROR_INVALID_INPUT), 400

        # Generate a unique ID for the new catalog item
        item_id = str(uuid.uuid4())
        new_item = {
            "id": item_id,
            "name": name,
            "description": description,
            "price": price
        }
        catalog_items[item_id] = new_item
        return jsonify(new_item), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update an existing catalog item by ID
@app.route('/catalog/<item_id>', methods=['PUT'])
def update_catalog_item(item_id):
    """
    Update an existing catalog item by ID. Expects JSON input with 'name', 'description', and/or 'price'.
    """
    try:
        data = request.json
        item = catalog_items.get(item_id)
        if not item:
            return jsonify(ERROR_ITEM_NOT_FOUND), 404

        # Update fields if provided
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        if name:
            item['name'] = name
        if description:
            item['description'] = description
        if price is not None:
            if not isinstance(price, (int, float)) or price < 0:
                return jsonify(ERROR_INVALID_INPUT), 400
            item['price'] = price

        catalog_items[item_id] = item
        return jsonify(item), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a catalog item by ID
@app.route('/catalog/<item_id>', methods=['DELETE'])
def delete_catalog_item(item_id):
    """
    Delete a catalog item by ID.
    """
    item = catalog_items.pop(item_id, None)
    if item:
        return jsonify({"message": "Item deleted successfully"}), 200
    return jsonify(ERROR_ITEM_NOT_FOUND), 404

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors globally.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors globally.
    """
    return jsonify({"error": "Internal server error"}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code is designed to be modular, scalable, and production-ready. For actual deployment, you should integrate a real database, secure the endpoints, and use a WSGI server (e.g., Gunicorn) to serve the Flask app.
