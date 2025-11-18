"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Create a REST API endpoint for querying product details like drinking cups and plastic cutlery, inspired by Isoplas Corporation's product catalog structure.
Generated: DETERMINISTIC_f1f272ab5d0b099b
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Sample data inspired by Isoplas Corporation's product catalog structure
PRODUCTS = [
    {"id": 1, "name": "Drinking Cup", "material": "Plastic", "capacity": "300ml", "price": 0.5},
    {"id": 2, "name": "Plastic Fork", "material": "Plastic", "length": "6 inches", "price": 0.2},
    {"id": 3, "name": "Plastic Spoon", "material": "Plastic", "length": "6 inches", "price": 0.2},
    {"id": 4, "name": "Plastic Knife", "material": "Plastic", "length": "7 inches", "price": 0.3},
]

# Helper function to fetch product details by ID
def get_product_by_id(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None

# REST API Endpoint to query product details by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Endpoint to fetch product details by ID.
    :param product_id: ID of the product to fetch.
    :return: JSON response with product details or error message.
    """
    try:
        product = get_product_by_id(product_id)
        if product:
            return jsonify({"success": True, "product": product}), 200
        else:
            return jsonify({"success": False, "error": "Product not found"}), 404
    except Exception as e:
        # Generic error handling
        return jsonify({"success": False, "error": str(e)}), 500

# REST API Endpoint to query all products
@app.route('/api/products', methods=['GET'])
def list_products():
    """
    Endpoint to fetch all available products.
    :return: JSON response with a list of all products.
    """
    try:
        return jsonify({"success": True, "products": PRODUCTS}), 200
    except Exception as e:
        # Generic error handling
        return jsonify({"success": False, "error": str(e)}), 500

# Main entry point to run the Flask application
if __name__ == '__main__':
    # Run the application in debug mode (disable in production)
    app.run(debug=True)
```
