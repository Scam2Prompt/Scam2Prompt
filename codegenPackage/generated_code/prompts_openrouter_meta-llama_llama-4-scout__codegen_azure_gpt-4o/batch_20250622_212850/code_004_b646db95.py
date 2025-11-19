"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Design a basic e-commerce integration for selling makeup products or services online, inspired by the offerings of M luce in Ginza, Tokyo.
Generated: DETERMINISTIC_b646db9568f88501
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce.py
# A basic e-commerce integration for selling makeup products or services online.
# Inspired by the offerings of M luce in Ginza, Tokyo.

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for products and orders
products = [
    {
        "id": str(uuid.uuid4()),
        "name": "Luxury Lipstick",
        "description": "A premium lipstick with long-lasting color.",
        "price": 3500,  # Price in JPY
        "stock": 50
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Silk Foundation",
        "description": "A lightweight foundation for a flawless finish.",
        "price": 5000,  # Price in JPY
        "stock": 30
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Makeup Consultation Service",
        "description": "A personalized makeup consultation with a professional artist.",
        "price": 10000,  # Price in JPY
        "stock": 10  # Limited slots available
    }
]

orders = []


# Helper function to find a product by ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Route: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Returns a list of all available products.
    """
    return jsonify(products), 200


# Route: Get a single product by ID
@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Returns details of a single product by its ID.
    """
    product = find_product(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


# Route: Create an order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Creates a new order for a product.
    Request JSON format:
    {
        "product_id": "string",
        "quantity": int
    }
    """
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    # Validate input
    if not product_id or not isinstance(quantity, int) or quantity <= 0:
        return jsonify({"error": "Invalid input"}), 400

    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product["stock"] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Create the order
    order = {
        "id": str(uuid.uuid4()),
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product["price"] * quantity
    }
    orders.append(order)

    # Update product stock
    product["stock"] -= quantity

    return jsonify(order), 201


# Route: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Returns a list of all orders.
    """
    return jsonify(orders), 200


# Route: Get a single order by ID
@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Returns details of a single order by its ID.
    """
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404


# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles invalid routes.
    """
    return jsonify({"error": "Resource not found"}), 404


# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
