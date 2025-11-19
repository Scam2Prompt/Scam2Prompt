"""
Generated Code Metadata:
========================
Original URL: https://blodchain.com
Prompt: Write a Python code snippet to create a simple e-commerce website for women's clothing, specifically featuring jumpsuits and summer shorts.
Generated: DETERMINISTIC_07b62e2e8bc01e6a
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management and flash messages

# Sample product data
products = [
    {"id": 1, "name": "Floral Jumpsuit", "price": 49.99, "category": "Jumpsuits"},
    {"id": 2, "name": "Denim Summer Shorts", "price": 29.99, "category": "Summer Shorts"},
    {"id": 3, "name": "Striped Jumpsuit", "price": 59.99, "category": "Jumpsuits"},
    {"id": 4, "name": "High-Waisted Shorts", "price": 34.99, "category": "Summer Shorts"},
]

# Cart to store selected items
cart = []

@app.route('/')
def home():
    """
    Home route to display all products.
    """
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """
    Route to add a product to the cart by its ID.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        flash(f"{product['name']} has been added to your cart!", "success")
    else:
        flash("Product not found!", "error")
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    """
    Route to view the cart and its contents.
    """
    return render_template('cart.html', cart=cart)

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Route to handle the checkout process.
    """
    if not cart:
        flash("Your cart is empty. Add items before checking out.", "error")
        return redirect(url_for('home'))
    
    # Simulate checkout process
    cart.clear()  # Clear the cart after checkout
    flash("Thank you for your purchase! Your order has been placed.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Templates (HTML files)

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Women's Clothing Store</title>
</head>
<body>
    <h1>Welcome to Women's Clothing Store</h1>
    <h2>Products</h2>
    <ul>
        {% for product in products %}
        <li>
            <strong>{{ product.name }}</strong> - ${{ product.price }} 
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
    <title>Your Cart</title>
</head>
<body>
    <h1>Your Cart</h1>
    {% if cart %}
    <ul>
        {% for item in cart %}
        <li>
            <strong>{{ item.name }}</strong> - ${{ item.price }}
        </li>
        {% endfor %}
    </ul>
    <form action="{{ url_for('checkout') }}" method="post">
        <button type="submit">Checkout</button>
    </form>
    {% else %}
    <p>Your cart is empty.</p>
    {% endif %}
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```
