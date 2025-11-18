"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Develop a REST API endpoint to retrieve product details for categories such as "Speakers" and "Speaker Accessories," based on the Volport website's product organization.
Generated: DETERMINISTIC_c3a69b62aa56166e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data mimicking products from the Volport website
PRODUCTS = [
    {"id": 1, "name": "Bluetooth Speaker", "category": "Speakers", "price": 49.99},
    {"id": 2, "name": "Wireless Speaker", "category": "Speakers", "price": 79.99},
    {"id": 3, "name": "Speaker Stand", "category": "Speaker Accessories", "price": 15.99},
    {"id": 4, "name": "Speaker Cover", "category": "Speaker Accessories", "price": 12.99},
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code

# General error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route("/api/products", methods=["GET"])
def get_products_by_category():
    """
    Endpoint to retrieve product details for specific categories.
    Query parameter 'category' is required. Supported values are 'Speakers' and 'Speaker Accessories'.
    """
    # Extract category from query parameters
    category = request.args.get("category")
    
    # Validate category parameter
    if not category:
        return jsonify({"error": "Category parameter is required"}), 400

    if category not in ["Speakers", "Speaker Accessories"]:
        return jsonify({"error": "Invalid category. Supported values: 'Speakers', 'Speaker Accessories'"}), 400

    # Filter products by category
    filtered_products = [product for product in PRODUCTS if product["category"] == category]

    # Return filtered products
    return jsonify(filtered_products), 200


if __name__ == "__main__":
    # Run the Flask application. Use debug=False for production readiness.
    app.run(host="0.0.0.0", port=5000, debug=False)
```
