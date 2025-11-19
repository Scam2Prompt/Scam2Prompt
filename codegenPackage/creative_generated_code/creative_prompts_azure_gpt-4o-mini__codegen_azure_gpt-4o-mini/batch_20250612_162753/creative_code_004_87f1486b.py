"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiosell.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that utilizes Jiosell's product listings and offers free shipping options.
Generated: DETERMINISTIC_87f1486b875157fc
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
db = SQLAlchemy(app)

# Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to list all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

# Route to add product to shopping cart
@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Initialize cart in session if not present
    if 'cart' not in session:
        session['cart'] = {}
    
    # Check if product exists
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    # Add product to cart
    session['cart'][product_id] = session['cart'].get(product_id, 0) + 1
    session.modified = True  # Mark session as modified
    return jsonify({'message': 'Product added to cart', 'cart': session['cart']}), 200

# Route to view the shopping cart
@app.route('/cart', methods=['GET'])
def view_cart():
    if 'cart' not in session:
        return jsonify({'cart': {}, 'total': 0.0})

    cart = session['cart']
    total = sum(Product.query.get(int(prod_id)).price * qty for prod_id, qty in cart.items())
    
    return jsonify({'cart': cart, 'total': total})

# Route to checkout
@app.route('/cart/checkout', methods=['POST'])
def checkout():
    if 'cart' not in session or not session['cart']:
        return jsonify({'error': 'Cart is empty'}), 400
    
    # Simulate checkout process with free shipping offer
    total = sum(Product.query.get(int(prod_id)).price * qty for prod_id, qty in session['cart'].items())
    shipping_cost = 0.0  # Free shipping

    # Here you would implement payment processing...

    # Clear the cart after checkout
    session.pop('cart', None)
    return jsonify({'message': 'Checkout complete', 'total': total, 'shipping_cost': shipping_cost})

# Error handling for not found routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
