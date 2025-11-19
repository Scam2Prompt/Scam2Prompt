"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Create an API documentation for retrieving information about Emanuelson Reels' products, including their specifications, prices, and related accessories like leather cases."
Generated: DETERMINISTIC_09c12ce28349b1a5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for Emanuelson Reels' products
products = [
    {
        "id": 1,
        "name": "Emanuelson Reel Model X",
        "specifications": {
            "material": "Aluminum",
            "weight": "250g",
            "gear_ratio": "5.2:1"
        },
        "price": 120.99,
        "accessories": [
            {"name": "Leather Case", "price": 25.99},
            {"name": "Spare Spool", "price": 15.99}
        ]
    },
    {
        "id": 2,
        "name": "Emanuelson Reel Model Y",
        "specifications": {
            "material": "Carbon Fiber",
            "weight": "200g",
            "gear_ratio": "6.0:1"
        },
        "price": 150.49,
        "accessories": [
            {"name": "Leather Case", "price": 30.99},
            {"name": "Maintenance Kit", "price": 20.99}
        ]
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all products.
    Returns:
        JSON response containing a list of all products.
    """
    return jsonify({"products": products}), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a specific product by its ID.
    Args:
        product_id (int): ID of the product to retrieve.
    Returns:
        JSON response containing the product details if found, or a 404 error if not found.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/<int:product_id>/accessories', methods=['GET'])
def get_product_accessories(product_id):
    """
    Endpoint to retrieve accessories for a specific product by its ID.
    Args:
        product_id (int): ID of the product whose accessories are to be retrieved.
    Returns:
        JSON response containing the accessories if the product is found, or a 404 error if not found.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"accessories": product["accessories"]}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Returns:
        JSON response with a 500 error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
