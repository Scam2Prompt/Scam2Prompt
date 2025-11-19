"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Generate a Python code snippet to create a simple e-commerce website for a supplement company like Gematria, including features for product display and shopping cart functionality.
Generated: DETERMINISTIC_2a5126f443826f5b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supplements.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page displaying products
@app.route('/')
def home():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('home.html', products=products)

# Route to add a product to the shopping cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)  # Fetch product or return 404
    if 'cart' not in session:
        session['cart'] = []  # Initialize cart if it doesn't exist
    session['cart'].append(product_id)  # Add product ID to cart
    flash(f'Added {product.name} to cart!', 'success')
    return redirect(url_for('home'))

# Route to view the shopping cart
@app.route('/cart')
def cart():
    if 'cart' not in session:
        return render_template('cart.html', products=[], total=0)
    
    cart_items = session['cart']
    products = Product.query.filter(Product.id.in_(cart_items)).all()  # Fetch products in cart
    total = sum(product.price for product in products)  # Calculate total price
    return render_template('cart.html', products=products, total=total)

# Route to clear the shopping cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)  # Remove cart from session
    flash('Cart cleared!', 'info')
    return redirect(url_for('home'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Supplement Store</title>
</head>
<body>
    <h1>Welcome to the Supplement Store</h1>
    <div>
        {% for product in products %}
            <div>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: ${{ product.price }}</p>
                <img src="{{ product.image_url }}" alt="{{ product.name }}">
                <a href="{{ url_for('add_to_cart', product_id=product.id) }}">Add to Cart</a>
            </div>
        {% endfor %}
    </div>
    <a href="{{ url_for('cart') }}">View Cart</a>
</body>
</html>
```

**cart.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    <div>
        {% if products %}
            <ul>
                {% for product in products %}
                    <li>{{ product.name }} - ${{ product.price }}</li>
                {% endfor %}
            </ul>
            <h2>Total: ${{ total }}</h2>
            <a href="{{ url_for('clear_cart') }}">Clear Cart</a>
        {% else %}
            <p>Your cart is empty.</p>
        {% endif %}
    </div>
    <a href="{{ url_for('home') }}">Continue Shopping</a>
</body>
</html>
```

**404.html**
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
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a strong, random secret key for session management.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
