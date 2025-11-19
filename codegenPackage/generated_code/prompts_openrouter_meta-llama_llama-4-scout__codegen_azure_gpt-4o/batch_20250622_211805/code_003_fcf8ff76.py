"""
Generated Code Metadata:
========================
Original URL: https://orange-pepe.pages.dev
Prompt: Develop a simple e-commerce platform using $ORPE as the sole payment method, allowing holders to purchase exclusive merchandise.
Generated: DETERMINISTIC_fcf8ff76ed5fdcb0
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_platform.py

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for products and orders
products = [
    {"id": 1, "name": "Exclusive T-Shirt", "price": 50, "currency": "$ORPE"},
    {"id": 2, "name": "Premium Hoodie", "price": 100, "currency": "$ORPE"},
    {"id": 3, "name": "Collector's Mug", "price": 25, "currency": "$ORPE"},
]

orders = []

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Fetch all available products.
    """
    return jsonify({"products": products}), 200

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place an order for a product using $ORPE as the payment method.
    """
    try:
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        # Validate input
        if not product_id or quantity <= 0:
            return jsonify({"error": "Invalid input"}), 400

        # Find the product
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Calculate total price
        total_price = product["price"] * quantity

        # Create order
        order = {
            "order_id": len(orders) + 1,
            "product": product["name"],
            "quantity": quantity,
            "total_price": total_price,
            "currency": product["currency"]
        }
        orders.append(order)

        return jsonify({"message": "Order placed successfully", "order": order}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Fetch all orders placed by users.
    """
    return jsonify({"orders": orders}), 200

# Main entry point
if __name__ == '__main__':
    """
    Start the Flask application.
    """
    app.run(debug=True)
```
