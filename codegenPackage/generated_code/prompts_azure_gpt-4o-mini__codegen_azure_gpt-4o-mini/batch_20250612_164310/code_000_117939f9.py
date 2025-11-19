"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a shopping cart with items, similar to the "Carrinho de Compras" feature on aquarelaesmalte.
Generated: DETERMINISTIC_117939f9d393ed84
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from flask import Flask, render_template, session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Sample data for products (in a real application, this would come from a database)
products = {
    1: {'name': 'Nail Polish A', 'price': 10.00},
    2: {'name': 'Nail Polish B', 'price': 12.50},
    3: {'name': 'Nail Polish C', 'price': 8.75},
}

@app.route('/')
def index():
    """Render the homepage with available products."""
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Add a product to the shopping cart."""
    if product_id not in products:
        flash('Product not found!', 'error')
        return redirect(url_for('index'))

    # Initialize the cart in the session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = {}

    # Add the product to the cart or update the quantity
    if product_id in session['cart']:
        session['cart'][product_id] += 1
    else:
        session['cart'][product_id] = 1

    flash('Product added to cart!', 'success')
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    """Display the shopping cart with items."""
    cart_items = session.get('cart', {})
    cart_details = {product_id: {'name': products[product_id]['name'], 
                                  'price': products[product_id]['price'], 
                                  'quantity': quantity} 
                    for product_id, quantity in cart_items.items() if product_id in products}

    total_price = sum(item['price'] * item['quantity'] for item in cart_details.values())
    return render_template('cart.html', cart=cart_details, total_price=total_price)

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """Remove a product from the shopping cart."""
    if 'cart' in session and product_id in session['cart']:
        del session['cart'][product_id]
        flash('Product removed from cart!', 'success')
    else:
        flash('Product not found in cart!', 'error')
    
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    """Render the checkout page."""
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('index'))

    return render_template('checkout.html', cart=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
</head>
<body>
    <h1>Available Products</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for product_id, product in products.items() %}
            <li>
                {{ product.name }} - ${{ product.price }}
                <form action="{{ url_for('add_to_cart', product_id=product_id) }}" method="post">
                    <button type="submit">Add to Cart</button>
                </form>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('cart') }}">View Cart</a>
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
    <title>Your Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    {% if cart %}
        <ul>
            {% for item in cart.values() %}
                <li>
                    {{ item.name }} - ${{ item.price }} x {{ item.quantity }}
                    <form action="{{ url_for('remove_from_cart', product_id=item.id) }}" method="post">
                        <button type="submit">Remove</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
        <h2>Total: ${{ total_price }}</h2>
        <a href="{{ url_for('checkout') }}">Checkout</a>
    {% else %}
        <p>Your cart is empty!</p>
    {% endif %}
    <a href="{{ url_for('index') }}">Continue Shopping</a>
</body>
</html>
```

```html
<!-- templates/checkout.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout</title>
</head>
<body>
    <h1>Checkout</h1>
    <p>Thank you for your purchase!</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

### Note:
- Ensure you have Flask installed in your environment (`pip install Flask`).
- Replace `'your_secret_key'` with a strong secret key for session management.
- This code is a basic implementation and should be expanded with proper user authentication, payment processing, and database integration for a production-ready application.
