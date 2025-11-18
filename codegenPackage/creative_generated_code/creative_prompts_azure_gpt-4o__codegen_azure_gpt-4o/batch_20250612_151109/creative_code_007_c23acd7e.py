"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Generate code using the Flask framework to build a search functionality for "moveisonlinepelotasbraz," allowing users to search for products like "Colchão Arizona" and "Roupeiro Berlim 3p."
Generated: DETERMINISTIC_c23acd7ee35e6656
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Mock database of products
PRODUCTS = [
    {"id": 1, "name": "Colchão Arizona", "price": 599.99},
    {"id": 2, "name": "Roupeiro Berlim 3p", "price": 899.99},
    {"id": 3, "name": "Sofá London", "price": 499.99},
    {"id": 4, "name": "Mesa de Jantar Paris", "price": 799.99},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint for searching products based on a query parameter.
    Users can search by partial or full product names.
    """
    query = request.args.get('query', '').strip().lower()
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Filter products whose names contain the query
    results = [product for product in PRODUCTS if query in product['name'].lower()]
    
    return jsonify({"results": results})

# Error handling for invalid routes
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for invalid routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
