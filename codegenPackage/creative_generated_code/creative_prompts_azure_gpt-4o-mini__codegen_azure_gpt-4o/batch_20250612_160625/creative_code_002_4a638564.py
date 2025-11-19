"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tkshop6.shop
Prompt: Create a sample API request to a shopping platform that includes error handling for unregistered routes.
Generated: DETERMINISTIC_4a6385641f274a8a
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for the shopping platform
products = [
    {"id": 1, "name": "T-shirt", "price": 20.99},
    {"id": 2, "name": "Jeans", "price": 49.99},
    {"id": 3, "name": "Sneakers", "price": 89.99},
]

@app.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to fetch all products.
    """
    return jsonify({"products": products}), 200

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Endpoint to fetch a single product by ID.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product}), 200
    else:
        # Return a 404 response if the product is not found
        return jsonify({"error": "Product not found"}), 404

@app.errorhandler(404)
def handle_404_error(error):
    """
    Global error handler for unregistered routes or missing resources.
    """
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def handle_500_error(error):
    """
    Global error handler for server-side errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
