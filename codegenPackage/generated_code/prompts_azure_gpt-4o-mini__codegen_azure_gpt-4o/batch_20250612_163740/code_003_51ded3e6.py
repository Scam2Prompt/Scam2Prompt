"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve information about Karnataka Aromas' specialty products and their applications in the fragrance industry.
Generated: DETERMINISTIC_51ded3e620f8abb7
Batch ID: 20250612_163740
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

# Sample data representing Karnataka Aromas' specialty products
products = [
    {
        "id": 1,
        "name": "Sandalwood Oil",
        "description": "Premium quality sandalwood oil used in high-end perfumes.",
        "applications": ["Perfumery", "Aromatherapy", "Cosmetics"]
    },
    {
        "id": 2,
        "name": "Jasmine Absolute",
        "description": "Highly concentrated jasmine extract for luxury fragrances.",
        "applications": ["Perfumery", "Skincare", "Haircare"]
    },
    {
        "id": 3,
        "name": "Patchouli Essential Oil",
        "description": "Earthy and musky essential oil for base notes in perfumes.",
        "applications": ["Perfumery", "Aromatherapy"]
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all specialty products and their applications.
    Returns:
        JSON response containing the list of products.
    """
    try:
        # Return the list of products as a JSON response
        return jsonify({"status": "success", "data": products}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a specific product by its ID.
    Args:
        product_id (int): ID of the product to retrieve.
    Returns:
        JSON response containing the product details or an error message.
    """
    try:
        # Find the product with the given ID
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify({"status": "success", "data": product}), 200
        else:
            # Return a 404 error if the product is not found
            return jsonify({"status": "error", "message": "Product not found"}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"status": "error", "message": "Endpoint not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with a 500 error message.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
