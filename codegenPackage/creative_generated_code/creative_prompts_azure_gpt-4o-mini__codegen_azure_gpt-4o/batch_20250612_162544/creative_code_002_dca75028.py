"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: How can I implement an API to manage product details, including instructions for use and care for items like "Xícaras" and "Pratos"?
Generated: DETERMINISTIC_dca75028523e8188
Batch ID: 20250612_162544
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

# Sample in-memory database for products
products = {
    1: {"name": "Xícaras", "instructions": "Wash gently with warm water and soap.", "care": "Avoid using abrasive materials."},
    2: {"name": "Pratos", "instructions": "Clean with a damp cloth or dishwasher.", "care": "Store carefully to avoid chipping."}
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Route to get a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Route to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    if not request.json or 'name' not in request.json or 'instructions' not in request.json or 'care' not in request.json:
        return jsonify({"error": "Invalid input, name, instructions, and care are required"}), 400

    product_id = max(products.keys()) + 1 if products else 1
    new_product = {
        "name": request.json['name'],
        "instructions": request.json['instructions'],
        "care": request.json['care']
    }
    products[product_id] = new_product
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

# Route to update an existing product by ID
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    if not request.json:
        return jsonify({"error": "Invalid input"}), 400

    product = products[product_id]
    product['name'] = request.json.get('name', product['name'])
    product['instructions'] = request.json.get('instructions', product['instructions'])
    product['care'] = request.json.get('care', product['care'])

    products[product_id] = product
    return jsonify({"message": "Product updated successfully", "product": product}), 200

# Route to delete a product by ID
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    deleted_product = products.pop(product_id)
    return jsonify({"message": "Product deleted successfully", "product": deleted_product}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
