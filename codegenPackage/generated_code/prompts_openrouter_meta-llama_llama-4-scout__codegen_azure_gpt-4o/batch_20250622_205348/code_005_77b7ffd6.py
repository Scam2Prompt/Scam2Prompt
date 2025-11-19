"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Create a simple API to query Groundcell product information, including sizes, prices, and availability, based on the product codes (EC100, EC150, EC200)."
Generated: DETERMINISTIC_77b7ffd611e771ea
Batch ID: 20250622_205348
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

# Mock database of Groundcell products
PRODUCTS = {
    "EC100": {"name": "Groundcell Basic", "sizes": ["S", "M", "L"], "price": 19.99, "availability": True},
    "EC150": {"name": "Groundcell Advanced", "sizes": ["M", "L", "XL"], "price": 29.99, "availability": True},
    "EC200": {"name": "Groundcell Pro", "sizes": ["L", "XL"], "price": 39.99, "availability": False},
}

@app.route('/api/products/<product_code>', methods=['GET'])
def get_product_info(product_code):
    """
    Endpoint to retrieve product information based on product code.
    :param product_code: The code of the product to query (e.g., EC100, EC150, EC200).
    :return: JSON response containing product details or an error message.
    """
    try:
        # Validate product code and fetch product details
        product = PRODUCTS.get(product_code.upper())
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify(product), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    :param error: The error object.
    :return: JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    :param error: The error object.
    :return: JSON response indicating an internal server error.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
