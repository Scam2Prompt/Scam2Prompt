"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Write a Python script using the Flask framework to create an e-commerce product catalog API that includes endpoints for listing products, filtering by category (e.g., electronics, beauty, fashion), and retrieving product details like price and availability.
Generated: DETERMINISTIC_f621b5ec5b9475ed
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Example Product Data
PRODUCTS = [
    {'id': 1, 'name': 'Smartphone', 'category': 'electronics', 'price': 699.99, 'availability': True},
    {'id': 2, 'name': 'Laptop', 'category': 'electronics', 'price': 999.99, 'availability': True},
    {'id': 3, 'name': 'Lipstick', 'category': 'beauty', 'price': 19.99, 'availability': True},
    {'id': 4, 'name': 'T-shirt', 'category': 'fashion', 'price': 14.99, 'availability': False},
    {'id': 5, 'name': 'Headphones', 'category': 'electronics', 'price': 49.99, 'availability': True},
    {'id': 6, 'name': 'Foundation', 'category': 'beauty', 'price': 29.99, 'availability': False},
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    """
    List all products in the catalog.
    Query Params:
        category (optional): Filter products by category (e.g., electronics, beauty, fashion).
    """
    category = request.args.get('category', None)
    
    # If category is provided, filter products by category
    if category:
        filtered_products = [product for product in PRODUCTS if product['category'].lower() == category.lower()]
        return jsonify(filtered_products), 200

    # If no category filter is applied, return all products
    return jsonify(PRODUCTS), 200

# Endpoint to retrieve product details by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    Retrieve details of a product by ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    """
    # Find the product by ID
    product = next((product for product in PRODUCTS if product['id'] == product_id), None)
    
    if not product:
        abort(404)  # Return 404 if product not found
    
    return jsonify(product), 200

# Main entry point for running the Flask app
if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    # Note: Debug mode should be disabled in production
    app.run(debug=True)
```
