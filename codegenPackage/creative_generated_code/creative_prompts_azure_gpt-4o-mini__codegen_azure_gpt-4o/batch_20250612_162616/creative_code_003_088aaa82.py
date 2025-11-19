"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zellerscanada.ca
Prompt: Develop a REST API endpoint for managing product collections in an online store, inspired by the Zellers catalog structure.
Generated: DETERMINISTIC_088aaa820a10c8e1
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

# Initialize Flask app
app = Flask(__name__)

# In-memory data store for product collections
collections = {}

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 - Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint to create a new product collection
@app.route('/collections', methods=['POST'])
def create_collection():
    """
    Create a new product collection.
    Expected JSON payload:
    {
        "name": "Collection Name",
        "description": "Description of the collection",
        "products": ["product1", "product2", "product3"]
    }
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Generate a unique ID for the new collection
        collection_id = str(uuid.uuid4())
        collections[collection_id] = {
            "id": collection_id,
            "name": data['name'],
            "description": data.get('description', ""),
            "products": data.get('products', [])
        }

        return jsonify(collections[collection_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all collections
@app.route('/collections', methods=['GET'])
def get_collections():
    """
    Retrieve all product collections.
    Response: List of collections.
    """
    return jsonify(list(collections.values())), 200

# Endpoint to retrieve a single product collection by ID
@app.route('/collections/<collection_id>', methods=['GET'])
def get_collection(collection_id):
    """
    Retrieve a single product collection by its ID.
    """
    collection = collections.get(collection_id)
    if not collection:
        return jsonify({"error": "Collection not found"}), 404
    return jsonify(collection), 200

# Endpoint to update a product collection
@app.route('/collections/<collection_id>', methods=['PUT'])
def update_collection(collection_id):
    """
    Update an existing product collection.
    Expected JSON payload:
    {
        "name": "Updated Collection Name",
        "description": "Updated description",
        "products": ["updated_product1", "updated_product2"]
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        collection = collections.get(collection_id)
        if not collection:
            return jsonify({"error": "Collection not found"}), 404

        # Update the collection details
        collection['name'] = data.get('name', collection['name'])
        collection['description'] = data.get('description', collection['description'])
        collection['products'] = data.get('products', collection['products'])

        return jsonify(collection), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a product collection
@app.route('/collections/<collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """
    Delete a product collection by its ID.
    """
    collection = collections.pop(collection_id, None)
    if not collection:
        return jsonify({"error": "Collection not found"}), 404
    return jsonify({"message": "Collection deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
