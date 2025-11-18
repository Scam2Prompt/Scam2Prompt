"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a REST API endpoint to retrieve details of "Combined Suction and Irrigation Cannulae" based on product code 25-185, as described on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_f5d497ae44ab13f0
Batch ID: 20250612_153246
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

# Sample data representing products available in the Curative Surgical Industry
PRODUCTS = [
    {
        "product_code": "25-185",
        "name": "Combined Suction and Irrigation Cannulae",
        "description": "Designed for precise suction and irrigation during surgical procedures.",
        "manufacturer": "Curative Surgical Industry",
        "price": "$150.00",
        "availability": "In Stock",
    },
    # Additional products can be added here
]

@app.route('/api/products/<string:product_code>', methods=['GET'])
def get_product_details(product_code):
    """
    REST API endpoint to retrieve product details based on the product code.

    :param product_code: The unique code identifying the product.
    :return: JSON response containing product details or an error message.
    """
    try:
        # Find the product by product code
        product = next((p for p in PRODUCTS if p["product_code"] == product_code), None)

        if product is None:
            # If the product is not found, return a 404 error with a descriptive message
            abort(404, description=f"Product with code {product_code} not found.")

        return jsonify(product), 200

    except Exception as e:
        # Handle unexpected errors and return a 500 Internal Server Error
        abort(500, description=f"An unexpected error occurred: {str(e)}")

# Custom error handler for 404 errors
@app.errorhandler(404)
def resource_not_found(error):
    """
    Custom handler for 404 Resource Not Found errors.

    :param error: Error description.
    :return: JSON error message.
    """
    return jsonify({"error": "Not Found", "message": error.description}), 404

# Custom error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom handler for 500 Internal Server Error.

    :param error: Error description.
    :return: JSON error message.
    """
    return jsonify({"error": "Internal Server Error", "message": error.description}), 500

if __name__ == '__main__':
    # Run the Flask application
    # Ensure debug mode is disabled in production
    app.run(debug=False)
```
