"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://11tesorosibericos.com
Prompt: Create an API endpoint that allows users to filter and search for Iberian ham products based on criteria such as type (e.g., Bellota, Cebo) and weight, reflecting the product structure of 11 Tesoros Ibéricos.
Generated: DETERMINISTIC_0e6cce1e96862936
Batch ID: 20250612_163952
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

# Sample data representing Iberian ham products
PRODUCTS = [
    {"id": 1, "name": "Bellota Ham Slice", "type": "Bellota", "weight": 500, "price": 45.99},
    {"id": 2, "name": "Cebo Ham Slice", "type": "Cebo", "weight": 400, "price": 29.99},
    {"id": 3, "name": "Bellota Whole Ham", "type": "Bellota", "weight": 7000, "price": 329.99},
    {"id": 4, "name": "Cebo Whole Ham", "type": "Cebo", "weight": 6000, "price": 249.99},
]

@app.route('/api/products', methods=['GET'])
def filter_products():
    """
    API endpoint to filter and search for Iberian ham products.
    Query parameters:
    - type: Filter by type (e.g., Bellota, Cebo)
    - min_weight: Minimum weight in grams
    - max_weight: Maximum weight in grams
    Returns a JSON array of filtered products.
    """
    try:
        # Retrieve query parameters
        product_type = request.args.get('type')
        min_weight = request.args.get('min_weight', type=int)
        max_weight = request.args.get('max_weight', type=int)

        # Filter products based on query parameters
        filtered_products = PRODUCTS
        if product_type:
            filtered_products = [product for product in filtered_products if product['type'].lower() == product_type.lower()]
        if min_weight is not None:
            filtered_products = [product for product in filtered_products if product['weight'] >= min_weight]
        if max_weight is not None:
            filtered_products = [product for product in filtered_products if product['weight'] <= max_weight]

        # Return the filtered products as JSON
        return jsonify(filtered_products), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return JSON responses.
    """
    return jsonify({"error": e.name, "code": e.code, "description": e.description}), e.code


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found", "code": 404}), 404


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
