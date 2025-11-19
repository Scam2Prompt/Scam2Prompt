"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve information about Karnataka Aromas' specialty products and their applications in the fragrance industry.
Generated: DETERMINISTIC_51ded3e620f8abb7
Batch ID: 20250612_163740
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

# Sample data representing Karnataka Aromas' specialty products
products = [
    {
        "id": 1,
        "name": "Mysore Sandalwood Oil",
        "description": "Premium sandalwood essential oil sourced from Karnataka.",
        "applications": [
            "Perfume base",
            "Aromatherapy",
            "Cosmetic formulations"
        ]
    },
    {
        "id": 2,
        "name": "Jasmine Extract",
        "description": "High-quality jasmine extract for fragrance and flavor industries.",
        "applications": [
            "Fragrance creation",
            "Skincare products",
            "Food flavoring"
        ]
    },
    {
        "id": 3,
        "name": "Vetiver Essential Oil",
        "description": "Earthy and woody essential oil used as a fixative in perfumes.",
        "applications": [
            "Perfume fixative",
            "Aromatherapy blends",
            "Luxury soaps"
        ]
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve information about Karnataka Aromas' specialty products.

    Returns:
        JSON response containing product details.
    """
    try:
        # Return all products as a JSON response
        return jsonify({"success": True, "data": products}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve information about a specific product by ID.

    Args:
        product_id (int): ID of the product to retrieve.

    Returns:
        JSON response containing product details or an error message.
    """
    try:
        # Find the product with the given ID
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify({"success": True, "data": product}), 200
        else:
            return jsonify({"success": False, "message": "Product not found"}), 404
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500


# Error handling for 404 - Resource not found
@app.errorhandler(404)
def resource_not_found(error):
    """
    Handle 404 errors for resources not found.

    Returns:
        JSON response indicating resource not found.
    """
    return jsonify({"success": False, "message": "Resource not found"}), 404


# Error handling for 500 - Internal server error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for internal server issues.

    Returns:
        JSON response indicating internal server error.
    """
    return jsonify({"success": False, "message": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
