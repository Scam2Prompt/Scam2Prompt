"""
Generated Code Metadata:
========================
Original URL: https://thewatchplaza53.pk
Prompt: Write a Python code snippet to create an e-commerce website for selling replica watches, including a shopping cart and wishlist features, similar to The Watch Plaza.
Generated: DETERMINISTIC_c649312f33761181
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Database URI
db = SQLAlchemy(app)

# Define the database models
class Product(db.Model):
    """Model for products in the store."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

class CartItem(db.Model):
    """Model for items in the shopping cart."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

class WishlistItem(db.Model):
    """Model for items in the wishlist."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with a list of products."""
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Add a product to the shopping cart."""
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    flash('Product added to cart!', 'success')
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    """Render the shopping cart page."""
    cart_items = [Product.query.get(id) for id in session.get('cart', [])]
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_wishlist/<int:product_id>', methods=['POST'])
def add_to_wishlist(product_id):
    """Add a product to the wishlist."""
    wishlist_item = WishlistItem(product_id=product_id)
    db.session.add(wishlist_item)
    db.session.commit()
    flash('Product added to wishlist!', 'success')
    return redirect(url_for('index'))

@app.route('/wishlist')
def wishlist():
    """Render the wishlist page."""
    wishlist_items = WishlistItem.query.all()
    products = [Product.query.get(item.product_id) for item in wishlist_items]
    return render_template('wishlist.html', products=products)

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """Remove a product from the shopping cart."""
    session['cart'] = [id for id in session.get('cart', []) if id != product_id]
    flash('Product removed from cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/remove_from_wishlist/<int:product_id>', methods=['POST'])
def remove_from_wishlist(product_id):
    """Remove a product from the wishlist."""
    item = WishlistItem.query.filter_by(product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash('Product removed from wishlist!', 'success')
    return redirect(url_for('wishlist'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Create the necessary HTML templates (`index.html`, `cart.html`, `wishlist.html`) to render the pages correctly.
- Replace `'your_secret_key'` with a secure random key for production use.
- This code is a basic structure and should be expanded with features like user authentication, payment processing, and more for a complete e-commerce solution.
