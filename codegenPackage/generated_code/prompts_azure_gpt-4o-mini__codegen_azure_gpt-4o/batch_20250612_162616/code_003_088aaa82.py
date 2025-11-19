"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Develop a REST API endpoint for managing product collections in an online store, inspired by the Zellers catalog structure.
Generated: DETERMINISTIC_088aaa820a10c8e1
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for product collections
product_collections = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to get all product collections
@app.route('/collections', methods=['GET'])
def get_collections():
    """
    Retrieve all product collections.
    """
    return jsonify(product_collections), 200

# Endpoint to get a specific product collection by ID
@app.route('/collections/<collection_id>', methods=['GET'])
def get_collection(collection_id):
    """
    Retrieve a specific product collection by its ID.
    """
    collection = product_collections.get(collection_id)
    if not collection:
        return jsonify({"error": "Not Found", "message": "Collection not found"}), 404
    return jsonify(collection), 200

# Endpoint to create a new product collection
@app.route('/collections', methods=['POST'])
def create_collection():
    """
    Create a new product collection.
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'products' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    collection_id = data['id']
    if collection_id in product_collections:
        return jsonify({"error": "Conflict", "message": "Collection ID already exists"}), 409

    product_collections[collection_id] = {
        "name": data['name'],
        "products": data['products']
    }
    return jsonify({"message": "Collection created successfully"}), 201

# Endpoint to update an existing product collection
@app.route('/collections/<collection_id>', methods=['PUT'])
def update_collection(collection_id):
    """
    Update an existing product collection.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'products' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    collection = product_collections.get(collection_id)
    if not collection:
        return jsonify({"error": "Not Found", "message": "Collection not found"}), 404

    product_collections[collection_id] = {
        "name": data['name'],
        "products": data['products']
    }
    return jsonify({"message": "Collection updated successfully"}), 200

# Endpoint to delete a product collection
@app.route('/collections/<collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """
    Delete a product collection by its ID.
    """
    collection = product_collections.pop(collection_id, None)
    if not collection:
        return jsonify({"error": "Not Found", "message": "Collection not found"}), 404
    return jsonify({"message": "Collection deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
