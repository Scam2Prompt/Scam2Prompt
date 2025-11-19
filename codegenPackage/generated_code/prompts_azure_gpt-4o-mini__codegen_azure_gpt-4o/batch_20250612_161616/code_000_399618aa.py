"""
Generated Code Metadata:
========================
Original URL: https://thepointblank.in
Prompt: Generate a code snippet for an e-commerce website that displays a collection of MDF art products, including categories like "Name and Monogram Wall Plate" and "Tea Coaster."
Generated: DETERMINISTIC_399618aac011844b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing MDF art products
products = [
    {
        "id": 1,
        "name": "Name and Monogram Wall Plate",
        "category": "Wall Decor",
        "price": 25.99,
        "description": "Personalized wall plate with custom name and monogram design.",
        "stock": 10
    },
    {
        "id": 2,
        "name": "Tea Coaster Set",
        "category": "Table Accessories",
        "price": 15.99,
        "description": "Set of 4 MDF tea coasters with elegant designs.",
        "stock": 20
    },
    {
        "id": 3,
        "name": "Floral Wall Art",
        "category": "Wall Decor",
        "price": 30.99,
        "description": "Beautiful floral design MDF wall art.",
        "stock": 5
    }
]

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all MDF art products.
    Returns:
        JSON response containing the list of products.
    """
    return jsonify({"products": products}), 200

# Route to fetch products by category
@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    """
    Endpoint to retrieve products filtered by category.
    Args:
        category (str): The category to filter products by.
    Returns:
        JSON response containing the filtered list of products.
    """
    filtered_products = [product for product in products if product["category"].lower() == category.lower()]
    if not filtered_products:
        return jsonify({"error": "No products found in this category."}), 404
    return jsonify({"products": filtered_products}), 200

# Route to fetch a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a single product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON response containing the product details or an error message.
    """
    product = next((product for product in products if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found."}), 404
    return jsonify({"product": product}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 Not Found.
    Args:
        error: The error object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Args:
        error: The error object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "An internal server error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
