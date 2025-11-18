"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Create a REST API in Flask for managing pharmaceutical products like infant milk and dietary supplements, with endpoints for adding, updating, and retrieving product details such as ratings and SKUs.
Generated: DETERMINISTIC_031535761c9ab99e
Batch ID: 20250612_154455
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

# In-memory database (for demo purposes)
products = {}

# Utility function to validate product data
def validate_product_data(data):
    required_fields = ['name', 'sku', 'category', 'rating']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
    if not isinstance(data['rating'], (int, float)) or not (0 <= data['rating'] <= 5):
        return "Rating must be a number between 0 and 5"
    return None

# Error handler for 404 (product not found)
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

# Global error handler for uncaught exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal server error"}), 500

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values())), 200

# Endpoint to retrieve a specific product by SKU
@app.route('/products/<string:sku>', methods=['GET'])
def get_product(sku):
    product = products.get(sku)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    validation_error = validate_product_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    sku = data['sku']
    if sku in products:
        return jsonify({"error": "Product with this SKU already exists"}), 400
    products[sku] = data
    return jsonify({"message": "Product added successfully", "product": data}), 201

# Endpoint to update an existing product
@app.route('/products/<string:sku>', methods=['PUT'])
def update_product(sku):
    data = request.get_json()
    validation_error = validate_product_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    if sku not in products:
        return jsonify({"error": "Product not found"}), 404
    products[sku] = data
    return jsonify({"message": "Product updated successfully", "product": data}), 200

# Run the Flask app
if __name__ == '__main__':
    # Use debug mode for development purposes
    app.run(debug=True)
```
