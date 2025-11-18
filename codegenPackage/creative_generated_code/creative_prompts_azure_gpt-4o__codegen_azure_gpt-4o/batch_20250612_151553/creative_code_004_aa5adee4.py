"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Suggest an API for managing inventory of products like "شارژر فندکی Ldnio مدل C104" and "مبدل بلوتوث لایتنینگ به جک هدفون اپل" from the website, including stock tracking and price updates.
Generated: DETERMINISTIC_aa5adee4cc9a33b7
Batch ID: 20250612_151553
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

# In-memory database for products (Note: Replace with a real database in production)
products = {}

# Helper function for error responses
def create_error_response(message, status_code):
    return jsonify({'error': message}), status_code

@app.errorhandler(Exception)
def handle_global_exception(e):
    """Global error handler for unexpected exceptions."""
    if isinstance(e, HTTPException):
        return create_error_response(e.description, e.code)
    return create_error_response("An unexpected error occurred.", 500)

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve the list of all products.
    Returns:
        A JSON list of all products.
    """
    return jsonify(list(products.values())), 200

@app.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve details of a specific product by ID.
    Parameters:
        product_id (str): The ID of the product.
    Returns:
        A JSON object with product details or an error message.
    """
    product = products.get(product_id)
    if not product:
        return create_error_response(f"Product with ID {product_id} not found.", 404)
    return jsonify(product), 200

@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the inventory.
    Expects:
        JSON payload with 'id', 'name', 'stock', and 'price'.
    Returns:
        A success message with the created product details or an error message.
    """
    data = request.json

    # Input validation
    if not data or not all(k in data for k in ('id', 'name', 'stock', 'price')):
        return create_error_response("Missing required fields: 'id', 'name', 'stock', and 'price'.", 400)
    
    product_id = data['id']
    if product_id in products:
        return create_error_response(f"Product with ID {product_id} already exists.", 400)

    # Add product to inventory
    products[product_id] = {
        'id': product_id,
        'name': data['name'],
        'stock': data['stock'],
        'price': data['price']
    }

    return jsonify({'message': 'Product added successfully.', 'product': products[product_id]}), 201

@app.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product's stock or price.
    Parameters:
        product_id (str): The ID of the product.
    Expects:
        JSON payload with optional 'stock' and 'price' fields.
    Returns:
        A success message with the updated product details or an error message.
    """
    product = products.get(product_id)
    if not product:
        return create_error_response(f"Product with ID {product_id} not found.", 404)

    data = request.json

    # Update fields if provided
    if 'stock' in data:
        product['stock'] = data['stock']
    if 'price' in data:
        product['price'] = data['price']

    return jsonify({'message': 'Product updated successfully.', 'product': product}), 200

@app.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product from the inventory.
    Parameters:
        product_id (str): The ID of the product.
    Returns:
        A success message or an error message.
    """
    if product_id not in products:
        return create_error_response(f"Product with ID {product_id} not found.", 404)

    del products[product_id]
    return jsonify({'message': f"Product with ID {product_id} deleted successfully."}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
