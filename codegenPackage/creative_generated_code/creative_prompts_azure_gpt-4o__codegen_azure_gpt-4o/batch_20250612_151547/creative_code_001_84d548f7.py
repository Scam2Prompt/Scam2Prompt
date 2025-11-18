"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Recommend an API or library that can be used to manage an e-commerce website selling Brother embroidery machines, including features for currency conversion and cart management.
Generated: DETERMINISTIC_84d548f7ae300840
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use Flask for managing an e-commerce website
selling Brother embroidery machines. It integrates the forex-python library
for currency conversion and provides basic cart management functionality.

Dependencies:
1. Flask: Web framework for Python.
2. forex-python: Library for currency conversion.

Install dependencies:
pip install Flask forex-python
"""

from flask import Flask, jsonify, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)

# Initialize currency converter
currency_rates = CurrencyRates()

# In-memory cart storage (for demonstration purposes, replace with DB in production)
cart = {}

# Product catalog (replace with DB in production)
products = {
    1: {"name": "Brother SE1900 Embroidery Machine", "price_usd": 999.99},
    2: {"name": "Brother PE535 Embroidery Machine", "price_usd": 399.99},
    3: {"name": "Brother PE800 Embroidery Machine", "price_usd": 899.99},
}


@app.route("/products", methods=["GET"])
def get_products():
    """
    Endpoint to fetch all products.
    :return: JSON response with product catalog.
    """
    return jsonify(products), 200


@app.route("/cart", methods=["GET"])
def view_cart():
    """
    Endpoint to view the cart.
    :return: JSON response with cart details.
    """
    return jsonify(cart), 200


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    """
    Endpoint to add an item to the cart.
    :request: JSON containing 'product_id' and 'quantity'.
    :return: JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        # Validate product ID
        if product_id not in products:
            return jsonify({"error": "Invalid product ID"}), 400

        # Add product to cart
        if product_id in cart:
            cart[product_id]["quantity"] += quantity
        else:
            cart[product_id] = {
                "name": products[product_id]["name"],
                "price_usd": products[product_id]["price_usd"],
                "quantity": quantity,
            }

        return jsonify({"message": "Product added to cart successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    """
    Endpoint to remove an item from the cart.
    :request: JSON containing 'product_id'.
    :return: JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        product_id = data.get("product_id")

        # Validate product ID
        if product_id not in cart:
            return jsonify({"error": "Product not in cart"}), 400

        # Remove product from cart
        del cart[product_id]

        return jsonify({"message": "Product removed from cart successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/cart/checkout", methods=["POST"])
def checkout():
    """
    Endpoint to calculate total cart value in a specified currency.
    :request: JSON containing 'currency' (default is USD).
    :return: JSON response with total value in the requested currency.
    """
    try:
        data = request.get_json()
        currency = data.get("currency", "USD").upper()

        # Calculate total cart value in USD
        total_usd = sum(item["price_usd"] * item["quantity"] for item in cart.values())

        # Convert total to requested currency
        if currency != "USD":
            total_converted = currency_rates.convert("USD", currency, total_usd)
        else:
            total_converted = total_usd

        return jsonify({"total": round(total_converted, 2), "currency": currency}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    """
    Start the Flask application.
    """
    app.run(debug=True)
```
