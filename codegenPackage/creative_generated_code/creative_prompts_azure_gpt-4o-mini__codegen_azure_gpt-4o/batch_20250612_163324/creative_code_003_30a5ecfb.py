"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Create a RESTful API endpoint to manage product listings for construction and garden equipment, inspired by the offerings on the Gala Games app blog.
Generated: DETERMINISTIC_30a5ecfb5297e05e
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for products (simulates a database)
products = {}

# Function to validate product data
def validate_product_data(data):
    required_fields = ['name', 'category', 'price', 'description']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data.get('price'), (int, float)) or data['price'] <= 0:
        return False, "Invalid price. Must be a positive number."
    return True, None


@app.route('/products', methods=['GET'])
def get_products():
    """
    GET /products
    Returns a list of all products
    """
    return jsonify(list(products.values())), 200


@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    GET /products/<product_id>
    Returns the details of a single product
    """
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product), 200


@app.route('/products', methods=['POST'])
def create_product():
    """
    POST /products
    Creates a new product
    """
    data = request.get_json()
    # Validate product data
    is_valid, error_msg = validate_product_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    product_id = str(uuid4())
    product = {
        'id': product_id,
        'name': data['name'],
        'category': data['category'],
        'price': data['price'],
        'description': data['description']
    }
    products[product_id] = product
    return jsonify(product), 201


@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    """
    PUT /products/<product_id>
    Updates an existing product
    """
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    # Validate product data
    is_valid, error_msg = validate_product_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    product.update({
        'name': data['name'],
        'category': data['category'],
        'price': data['price'],
        'description': data['description']
    })
    return jsonify(product), 200


@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    DELETE /products/<product_id>
    Deletes an existing product
    """
    product = products.pop(product_id, None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'message': f'Product {product_id} deleted'}), 200


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
