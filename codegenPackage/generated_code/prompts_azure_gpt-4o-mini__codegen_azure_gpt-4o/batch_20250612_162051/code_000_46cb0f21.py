"""
Generated Code Metadata:
========================
Original URL: https://gloclinicaesthetics.com
Prompt: Generate a code snippet for a web application that allows users to browse and purchase skincare products, similar to those offered by Glo Clinic Aesthetics.
Generated: DETERMINISTIC_46cb0f212cc8d5fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Mock database for skincare products
PRODUCTS = [
    {"id": 1, "name": "Hydrating Serum", "price": 29.99, "description": "A serum to keep your skin hydrated."},
    {"id": 2, "name": "Sunscreen SPF 50", "price": 19.99, "description": "Protect your skin from harmful UV rays."},
    {"id": 3, "name": "Vitamin C Cream", "price": 24.99, "description": "Brighten your skin with Vitamin C."},
]

# Mock shopping cart
CART = []

@app.route('/')
def home():
    """
    Home route to display available skincare products.
    """
    return render_template('home.html', products=PRODUCTS)

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """
    Add a product to the shopping cart.
    """
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    CART.append(product)
    return jsonify({"message": f"{product['name']} added to cart", "cart": CART}), 200

@app.route('/cart')
def view_cart():
    """
    View the shopping cart.
    """
    return render_template('cart.html', cart=CART)

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Checkout route to simulate a purchase.
    """
    if not CART:
        return jsonify({"error": "Cart is empty"}), 400

    # Simulate clearing the cart after purchase
    CART.clear()
    return jsonify({"message": "Purchase successful! Thank you for your order."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Products</title>
</head>
<body>
    <h1>Welcome to Glo Clinic Aesthetics</h1>
    <h2>Available Products</h2>
    <ul>
        {% for product in products %}
        <li>
            <h3>{{ product.name }}</h3>
            <p>{{ product.description }}</p>
            <p>Price: ${{ product.price }}</p>
            <form action="{{ url_for('add_to_cart', product_id=product.id) }}" method="post">
                <button type="submit">Add to Cart</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('view_cart') }}">View Cart</a>
</body>
</html>
```

```html
<!-- templates/cart.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    {% if cart %}
    <ul>
        {% for item in cart %}
        <li>
            <h3>{{ item.name }}</h3>
            <p>Price: ${{ item.price }}</p>
        </li>
        {% endfor %}
    </ul>
    <form action="{{ url_for('checkout') }}" method="post">
        <button type="submit">Checkout</button>
    </form>
    {% else %}
    <p>Your cart is empty.</p>
    {% endif %}
    <a href="{{ url_for('home') }}">Back to Products</a>
</body>
</html>
```
