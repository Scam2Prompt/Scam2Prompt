"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: "Develop a simple e-commerce website for selling nail art supplies, including airbrush stencils and nail art accessories, similar to Airstyleart."
Generated: DETERMINISTIC_947bba12f567f1cb
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a simple implementation of an e-commerce website for selling nail art supplies using Python's Flask framework. This code includes basic functionality for displaying products, adding them to a cart, and checking out.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Sample product data (in a real application, this would come from a database)
PRODUCTS = [
    {"id": 1, "name": "Airbrush Stencil Set", "price": 15.99, "description": "High-quality stencils for nail art."},
    {"id": 2, "name": "Nail Art Accessories Kit", "price": 25.99, "description": "Complete kit for nail art enthusiasts."},
    {"id": 3, "name": "Glitter Nail Polish", "price": 8.99, "description": "Add sparkle to your nails with this polish."},
]

# Initialize cart in session
@app.before_request
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def home():
    """
    Home page displaying available products.
    """
    return render_template('home.html', products=PRODUCTS)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """
    Add a product to the shopping cart.
    """
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
        session.modified = True
        flash(f"{product['name']} added to cart!", "success")
    else:
        flash("Product not found.", "error")
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    """
    View the shopping cart.
    """
    return render_template('cart.html', cart=session['cart'])

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """
    Checkout page for completing the purchase.
    """
    if request.method == 'POST':
        # Simulate order processing (in a real app, integrate payment gateway)
        session['cart'] = []  # Clear the cart after checkout
        session.modified = True
        flash("Thank you for your purchase!", "success")
        return redirect(url_for('home'))
    return render_template('checkout.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nail Art Supplies</title>
</head>
<body>
    <h1>Welcome to Nail Art Supplies</h1>
    <h2>Products</h2>
    <ul>
        {% for product in products %}
        <li>
            <strong>{{ product.name }}</strong> - ${{ product.price }}<br>
            {{ product.description }}<br>
            <a href="{{ url_for('add_to_cart', product_id=product.id) }}">Add to Cart</a>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('view_cart') }}">View Cart</a>
</body>
</html>
```

#### `templates/cart.html`
```html
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
            <strong>{{ item.name }}</strong> - ${{ item.price }}
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('checkout') }}">Checkout</a>
    {% else %}
    <p>Your cart is empty.</p>
    {% endif %}
    <a href="{{ url_for('home') }}">Continue Shopping</a>
</body>
</html>
```

#### `templates/checkout.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout</title>
</head>
<body>
    <h1>Checkout</h1>
    <form method="POST">
        <p>Enter your payment details (simulated):</p>
        <button type="submit">Complete Purchase</button>
    </form>
    <a href="{{ url_for('view_cart') }}">Back to Cart</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

### Notes:
- Install Flask using `pip install flask`.
- Run the app with `python app.py`.
- This is a basic implementation. For production, consider adding a database, user authentication, and integrating a payment gateway.
