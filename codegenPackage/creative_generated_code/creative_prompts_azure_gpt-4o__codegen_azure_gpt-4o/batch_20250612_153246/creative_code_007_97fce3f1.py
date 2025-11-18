"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Create a REST API for managing a furniture catalog, with endpoints for adding new collections, retrieving product details, and filtering by material properties like "hyper lightweight" or "super resistant," inspired by Nodo Italia's offerings.
Generated: DETERMINISTIC_97fce3f12f6cfeb9
Batch ID: 20250612_153246
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

app = Flask(__name__)

# In-memory furniture catalog database (for demonstration purposes)
furniture_catalog = {}

# Error messages
ERROR_NOT_FOUND = {"error": "Item not found"}
ERROR_INVALID_INPUT = {"error": "Invalid input"}

# Endpoint: Add a new furniture collection
@app.route('/collections', methods=['POST'])
def add_collection():
    try:
        data = request.json
        if not data or 'name' not in data or 'products' not in data:
            return jsonify(ERROR_INVALID_INPUT), 400

        collection_id = str(uuid.uuid4())
        furniture_catalog[collection_id] = {
            "name": data['name'],
            "products": data.get('products', [])
        }

        return jsonify({"collection_id": collection_id, "message": "Collection added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Retrieve details of a product by ID
@app.route('/products/<product_id>', methods=['GET'])
def get_product_details(product_id):
    try:
        for collection in furniture_catalog.values():
            for product in collection['products']:
                if product['id'] == product_id:
                    return jsonify(product), 200

        return jsonify(ERROR_NOT_FOUND), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Filter products by material properties
@app.route('/products/filter', methods=['GET'])
def filter_products():
    try:
        material_property = request.args.get('material_property')
        if not material_property:
            return jsonify(ERROR_INVALID_INPUT), 400

        filtered_products = []
        for collection in furniture_catalog.values():
            for product in collection['products']:
                if material_property in product.get('material_properties', []):
                    filtered_products.append(product)

        return jsonify(filtered_products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Example structure for adding products to a collection
# {
#   "name": "Nodo Italia Collection",
#   "products": [
#       {
#           "id": "product_1",
#           "name": "Chair",
#           "material_properties": ["hyper lightweight", "super resistant"]
#       },
#       {
#           "id": "product_2",
#           "name": "Table",
#           "material_properties": ["super resistant"]
#       }
#   ]
# }

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
