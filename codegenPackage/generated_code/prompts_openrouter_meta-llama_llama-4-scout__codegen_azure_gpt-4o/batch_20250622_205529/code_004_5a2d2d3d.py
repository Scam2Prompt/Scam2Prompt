"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: "Design an API for an e-commerce platform that specializes in fashion products, including endpoints for product listings, customer reviews, and order processing."
Generated: DETERMINISTIC_5a2d2d3d5a4c6bb9
Batch ID: 20250622_205529
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

# Mock data for demonstration purposes
products = [
    {"id": 1, "name": "T-Shirt", "price": 19.99, "category": "Clothing"},
    {"id": 2, "name": "Jeans", "price": 49.99, "category": "Clothing"},
    {"id": 3, "name": "Sneakers", "price": 89.99, "category": "Footwear"}
]

reviews = [
    {"product_id": 1, "review_id": 1, "rating": 5, "comment": "Great quality!"},
    {"product_id": 2, "review_id": 2, "rating": 4, "comment": "Fits well."}
]

orders = []

# Endpoint: Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Returns a list of all products.
    """
    return jsonify({"products": products}), 200

# Endpoint: Get product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Returns details of a specific product by ID.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product}), 200
    return jsonify({"error": "Product not found"}), 404

# Endpoint: Get reviews for a product
@app.route('/api/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    """
    Returns all reviews for a specific product.
    """
    product_reviews = [r for r in reviews if r["product_id"] == product_id]
    if product_reviews:
        return jsonify({"reviews": product_reviews}), 200
    return jsonify({"error": "No reviews found for this product"}), 404

# Endpoint: Add a review for a product
@app.route('/api/products/<int:product_id>/reviews', methods=['POST'])
def add_review(product_id):
    """
    Adds a new review for a specific product.
    """
    data = request.get_json()
    if not data or "rating" not in data or "comment" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_review = {
        "product_id": product_id,
        "review_id": len(reviews) + 1,
        "rating": data["rating"],
        "comment": data["comment"]
    }
    reviews.append(new_review)
    return jsonify({"message": "Review added successfully", "review": new_review}), 201

# Endpoint: Place an order
@app.route('/api/orders', methods=['POST'])
def place_order():
    """
    Places a new order.
    """
    data = request.get_json()
    if not data or "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid input"}), 400

    product = next((p for p in products if p["id"] == data["product_id"]), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    new_order = {
        "order_id": len(orders) + 1,
        "product_id": data["product_id"],
        "quantity": data["quantity"],
        "total_price": product["price"] * data["quantity"]
    }
    orders.append(new_order)
    return jsonify({"message": "Order placed successfully", "order": new_order}), 201

# Endpoint: Get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Returns a list of all orders.
    """
    return jsonify({"orders": orders}), 200

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
