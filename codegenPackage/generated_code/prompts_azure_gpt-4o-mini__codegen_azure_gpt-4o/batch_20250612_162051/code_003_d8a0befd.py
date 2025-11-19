"""
Generated Code Metadata:
========================
Original URL: https://zkoutdoor.pk
Prompt: Develop a RESTful API endpoint for managing inventory in a furniture e-commerce application, allowing for CRUD operations on products such as sofas and hanging lamps.
Generated: DETERMINISTIC_d8a0befd47b22a47
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
inventory = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Helper function to validate product data
def validate_product_data(data):
    required_fields = ["name", "category", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return False, "Price must be a positive number"
    if not isinstance(data["quantity"], int) or data["quantity"] < 0:
        return False, "Quantity must be a non-negative integer"
    return True, None

# Create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    is_valid, error_message = validate_product_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    product_id = len(inventory) + 1
    inventory[product_id] = {
        "id": product_id,
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    return jsonify(inventory[product_id]), 201

# Retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(list(inventory.values())), 200

# Retrieve a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = inventory.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = inventory.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.json
    is_valid, error_message = validate_product_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    product.update({
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "quantity": data["quantity"]
    })
    return jsonify(product), 200

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = inventory.pop(product_id, None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
