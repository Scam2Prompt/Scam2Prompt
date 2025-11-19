"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Generate a RESTful API documentation for a server that manages orders and inventory of fiberglass products, including endpoints for creating, reading, updating, and deleting (CRUD) product information."
Generated: DETERMINISTIC_eac9ac64e55e6cc1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RESTful API Documentation for Fiberglass Products Management

This API allows users to manage orders and inventory of fiberglass products.
It provides endpoints for CRUD operations on product information.

Base URL: /api/v1/products

Endpoints:
1. GET /api/v1/products - Retrieve a list of all products.
2. GET /api/v1/products/<product_id> - Retrieve details of a specific product.
3. POST /api/v1/products - Create a new product.
4. PUT /api/v1/products/<product_id> - Update an existing product.
5. DELETE /api/v1/products/<product_id> - Delete a product.

Error Handling:
- Returns appropriate HTTP status codes (e.g., 200, 201, 400, 404, 500).
- Provides meaningful error messages in JSON format.

"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration purposes
products = {}

# Helper function to generate unique product IDs
def generate_product_id():
    return str(len(products) + 1)

# GET /api/v1/products - Retrieve a list of all products
@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify({"products": list(products.values())}), 200

# GET /api/v1/products/<product_id> - Retrieve details of a specific product
@app.route('/api/v1/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# POST /api/v1/products - Create a new product
@app.route('/api/v1/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid product data"}), 400

        product_id = generate_product_id()
        product = {
            "id": product_id,
            "name": data['name'],
            "price": data['price'],
            "quantity": data['quantity']
        }
        products[product_id] = product
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT /api/v1/products/<product_id> - Update an existing product
@app.route('/api/v1/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = products.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid product data"}), 400

        product['name'] = data.get('name', product['name'])
        product['price'] = data.get('price', product['price'])
        product['quantity'] = data.get('quantity', product['quantity'])
        products[product_id] = product
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE /api/v1/products/<product_id> - Delete a product
@app.route('/api/v1/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = products.pop(product_id, None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
