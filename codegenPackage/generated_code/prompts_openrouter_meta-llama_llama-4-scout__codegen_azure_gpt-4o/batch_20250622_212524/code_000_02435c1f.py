"""
Generated Code Metadata:
========================
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for selling feminine and masculine shoes, including sandals and social shoes.
Generated: DETERMINISTIC_02435c1f09e05462
Batch ID: 20250622_212524
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

# Mock database for storing product information
products = [
    {"id": 1, "name": "Women's Sandals", "category": "Feminine", "type": "Sandals", "price": 50.00},
    {"id": 2, "name": "Men's Sandals", "category": "Masculine", "type": "Sandals", "price": 55.00},
    {"id": 3, "name": "Women's Social Shoes", "category": "Feminine", "type": "Social Shoes", "price": 80.00},
    {"id": 4, "name": "Men's Social Shoes", "category": "Masculine", "type": "Social Shoes", "price": 85.00},
]

# Mock shopping cart
shopping_cart = []

@app.route('/')
def home():
    """
    Home page displaying all products.
    """
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """
    Add a product to the shopping cart.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        shopping_cart.append(product)
        flash(f"{product['name']} added to cart!", "success")
    else:
        flash("Product not found!", "error")
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    """
    View the shopping cart.
    """
    total_price = sum(item['price'] for item in shopping_cart)
    return render_template('cart.html', shopping_cart=shopping_cart, total_price=total_price)

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Handle checkout process.
    """
    if not shopping_cart:
        flash("Your cart is empty!", "error")
        return redirect(url_for('view_cart'))
    
    # Simulate checkout process
    shopping_cart.clear()
    flash("Checkout successful! Thank you for your purchase.", "success")
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Templates (HTML files)
You will need to create the following HTML files in a `templates` folder:

#### `home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>E-Commerce Home</title>
</head>
<body>
    <h1>Welcome to the Shoe Store</h1>
    <ul>
        {% for product in products %}
        <li>
            {{ product.name }} - ${{ product.price }}
            <a href="{{ url_for('add_to_cart', product_id=product.id) }}">Add to Cart</a>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('view_cart') }}">View Cart</a>
</body>
</html>
```

#### `cart.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    <ul>
        {% for item in shopping_cart %}
        <li>{{ item.name }} - ${{ item.price }}</li>
        {% endfor %}
    </ul>
    <p>Total Price: ${{ total_price }}</p>
    <form action="{{ url_for('checkout') }}" method="post">
        <button type="submit">Checkout</button>
    </form>
    <a href="{{ url_for('home') }}">Continue Shopping</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```
