"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citygardenmexico.com.mx
Prompt: Suggest an API for e-commerce that could be used to replicate the functionality of City Garden México's online plant store, and write code to implement a shopping cart feature.
Generated: DETERMINISTIC_aa2a3cda43bb8f7e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_api.py

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for simplicity
products = [
    {"id": "1", "name": "Monstera Plant", "price": 500, "stock": 10},
    {"id": "2", "name": "Succulent", "price": 200, "stock": 25},
    {"id": "3", "name": "Ficus Tree", "price": 800, "stock": 5},
]

shopping_carts = {}  # Dictionary to hold shopping carts per user/session

# Helper function to find product by ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

# Endpoint: Get all products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

# Endpoint: Create a new shopping cart
@app.route("/api/cart", methods=["POST"])
def create_cart():
    # Generate a unique cart ID
    cart_id = str(uuid.uuid4())
    shopping_carts[cart_id] = {"items": []}
    return jsonify({"cart_id": cart_id, "message": "Shopping cart created successfully."}), 201

# Endpoint: Get shopping cart details
@app.route("/api/cart/<cart_id>", methods=["GET"])
def get_cart(cart_id):
    cart = shopping_carts.get(cart_id)
    if not cart:
        return jsonify({"error": "Cart not found."}), 404
    return jsonify(cart), 200

# Endpoint: Add product to cart
@app.route("/api/cart/<cart_id>/add", methods=["POST"])
def add_to_cart(cart_id):
    cart = shopping_carts.get(cart_id)
    if not cart:
        return jsonify({"error": "Cart not found."}), 404

    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404
    if product["stock"] < quantity:
        return jsonify({"error": "Insufficient stock."}), 400

    # Deduct stock and add product to cart
    product["stock"] -= quantity
    cart["items"].append({"product_id": product_id, "quantity": quantity, "name": product["name"], "price": product["price"]})
    
    return jsonify({"message": "Product added to cart successfully.", "cart": cart}), 200

# Endpoint: Remove product from cart
@app.route("/api/cart/<cart_id>/remove", methods=["POST"])
def remove_from_cart(cart_id):
    cart = shopping_carts.get(cart_id)
    if not cart:
        return jsonify({"error": "Cart not found."}), 404

    data = request.get_json()
    product_id = data.get("product_id")

    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404

    item_to_remove = None
    for item in cart["items"]:
        if item["product_id"] == product_id:
            item_to_remove = item
            product["stock"] += item["quantity"]
            break

    if not item_to_remove:
        return jsonify({"error": "Product not in cart."}), 404

    cart["items"].remove(item_to_remove)
    return jsonify({"message": "Product removed from cart successfully.", "cart": cart}), 200

# Endpoint: Checkout cart
@app.route("/api/cart/<cart_id>/checkout", methods=["POST"])
def checkout_cart(cart_id):
    cart = shopping_carts.get(cart_id)
    if not cart:
        return jsonify({"error": "Cart not found."}), 404

    if not cart["items"]:
        return jsonify({"error": "Cart is empty."}), 400

    # Calculate total price
    total_price = sum(item["price"] * item["quantity"] for item in cart["items"])

    # Clear shopping cart
    shopping_carts.pop(cart_id)

    return jsonify({"message": "Checkout successful.", "total_price": total_price}), 200

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```
