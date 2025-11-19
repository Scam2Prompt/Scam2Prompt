"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s5thbag.ru
Prompt: Design a RESTful API endpoint for managing product listings, including luxury fashion items and accessories, as highlighted on Luminelle Style.
Generated: DETERMINISTIC_2375c4f53c969a49
Batch ID: 20250612_140402
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

# In-memory datastore to simulate database
products = []

# Helper function to find a product by ID
def find_product(product_id):
    return next((product for product in products if product["id"] == product_id), None)

@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler."""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

@app.route("/products", methods=["GET"])
def get_products():
    """
    Get all product listings.
    Returns:
        JSON response containing all products.
    """
    return jsonify({"products": products})

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Get details of a specific product by ID.
    Args:
        product_id (int): ID of the product.
    Returns:
        JSON response containing the product details or error message if not found.
    """
    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

@app.route("/products", methods=["POST"])
def create_product():
    """
    Create a new product listing.
    Request Body:
        JSON payload containing product details (name, price, category).
    Returns:
        JSON response containing the created product or error messages for invalid input.
    """
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "category" not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    # Creating a new product object
    new_product = {
        "id": len(products) + 1,  # Simple auto-increment ID
        "name": data["name"],
        "price": data["price"],
        "category": data["category"],
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    Update an existing product listing.
    Args:
        product_id (int): ID of the product to update.
    Request Body:
        JSON payload containing updated product details (name, price, category).
    Returns:
        JSON response containing the updated product or error messages.
    """
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "category" not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Update the product details
    product.update({
        "name": data["name"],
        "price": data["price"],
        "category": data["category"],
    })
    return jsonify(product)

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Delete an existing product listing.
    Args:
        product_id (int): ID of the product to delete.
    Returns:
        JSON response confirming deletion or error message if not found.
    """
    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == "__main__":
    # Starting the Flask application
    app.run(debug=True)
```
