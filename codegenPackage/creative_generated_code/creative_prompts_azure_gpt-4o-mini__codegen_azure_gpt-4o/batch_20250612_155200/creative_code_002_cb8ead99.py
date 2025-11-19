"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-azuki.com
Prompt: Provide an example of how to implement a shopping cart API that includes the CHIKARA cooling shirt and its specifications.
Generated: DETERMINISTIC_cb8ead9999f0f0ed
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data, including the CHIKARA Cooling Shirt specifications
PRODUCTS = [
    {
        "id": 1,
        "name": "CHIKARA Cooling Shirt",
        "description": "Lightweight, moisture-wicking shirt with advanced cooling technology.",
        "price": 29.99,
        "sizes": ["S", "M", "L", "XL"],
        "colors": ["Blue", "Black", "Gray"],
        "quantity_available": 100
    }
]

# Initialize an empty shopping cart
shopping_cart = []

@app.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to retrieve the list of available products.
    """
    return jsonify({"products": PRODUCTS}), 200


@app.route("/cart", methods=["GET"])
def get_cart():
    """
    Endpoint to retrieve the current state of the shopping cart.
    """
    return jsonify({"shopping_cart": shopping_cart}), 200


@app.route("/cart", methods=["POST"])
def add_to_cart():
    """
    Endpoint to add a product to the shopping cart.
    Expects a JSON payload with product_id, quantity, size, and color.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        size = data.get("size")
        color = data.get("color")

        # Validate input data
        if not product_id or not quantity or not size or not color:
            return jsonify({"error": "Missing required fields"}), 400

        # Find product in the product catalog
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check if requested quantity is available
        if product["quantity_available"] < quantity:
            return jsonify({"error": "Insufficient stock available"}), 400

        # Add product to cart
        cart_item = {
            "product_id": product["id"],
            "name": product["name"],
            "quantity": quantity,
            "size": size,
            "color": color,
            "price": product["price"],
            "total_price": product["price"] * quantity
        }
        shopping_cart.append(cart_item)

        # Update available product quantity
        product["quantity_available"] -= quantity

        return jsonify({"message": "Product added to cart", "cart_item": cart_item}), 201

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while adding the product to the cart"}), 500


@app.route("/cart/<int:product_id>", methods=["DELETE"])
def remove_from_cart(product_id):
    """
    Endpoint to remove a product from the shopping cart by product ID.
    """
    try:
        # Find the item in the cart
        cart_item = next((item for item in shopping_cart if item["product_id"] == product_id), None)
        if not cart_item:
            return jsonify({"error": "Product not found in the cart"}), 404

        # Restore product quantity back to the inventory
        product = next((p for p in PRODUCTS if p["id"] == cart_item["product_id"]), None)
        if product:
            product["quantity_available"] += cart_item["quantity"]

        # Remove the item from the cart
        shopping_cart.remove(cart_item)

        return jsonify({"message": "Product removed from cart", "cart_item": cart_item}), 200

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while removing the product from the cart"}), 500


if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```
