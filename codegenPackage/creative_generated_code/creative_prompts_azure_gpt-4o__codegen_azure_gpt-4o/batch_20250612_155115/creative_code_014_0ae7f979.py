"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Create a Flask API to manage product filtering based on user-selected attributes like material, style, and fit, and return JSON responses for front-end integration.
Generated: DETERMINISTIC_0ae7f9797287060c
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing products in a database
PRODUCTS = [
    {"id": 1, "name": "T-Shirt", "material": "cotton", "style": "casual", "fit": "regular"},
    {"id": 2, "name": "Jeans", "material": "denim", "style": "classic", "fit": "slim"},
    {"id": 3, "name": "Jacket", "material": "leather", "style": "formal", "fit": "regular"},
    {"id": 4, "name": "Sweater", "material": "wool", "style": "casual", "fit": "loose"},
]

@app.route('/filter-products', methods=['POST'])
def filter_products():
    """
    Endpoint to filter products based on user-selected attributes.
    Expects a JSON payload with optional keys: material, style, fit.
    Returns a filtered list of products.
    """
    try:
        # Parse JSON request data
        filters = request.get_json()
        if not filters:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400
        
        # Validate filters (optional keys: material, style, fit)
        valid_keys = {"material", "style", "fit"}
        for key in filters.keys():
            if key not in valid_keys:
                return jsonify({"error": f"Invalid filter key: {key}"}), 400

        # Filter the products based on the provided attributes
        filtered_products = [product for product in PRODUCTS if all(
            product.get(key) == value for key, value in filters.items())]

        # Return filtered products in JSON format
        return jsonify({"filtered_products": filtered_products}), 200

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/products', methods=['GET'])
def list_all_products():
    """
    Endpoint to retrieve all available products.
    Returns a list of all products in JSON format.
    """
    return jsonify({"products": PRODUCTS}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
