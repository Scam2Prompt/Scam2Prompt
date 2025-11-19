"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gematria.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that includes Gematria's science-driven supplements, focusing on user experience.
Generated: DETERMINISTIC_f3da5b1452e63c71
Batch ID: 20250612_162504
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

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Shopping cart functionality
class ShoppingCart:
    @staticmethod
    def add_to_cart(product_id):
        """Add a product to the shopping cart"""
        if 'cart' not in session:
            session['cart'] = {}
        
        # Increment the product quantity in the cart
        session['cart'][product_id] = session['cart'].get(product_id, 0) + 1
        session.modified = True  # Mark session as modified

    @staticmethod
    def remove_from_cart(product_id):
        """Remove a product from the shopping cart"""
        if 'cart' in session and product_id in session['cart']:
            del session['cart'][product_id]
            session.modified = True

    @staticmethod
    def get_cart_items():
        """Retrieve all items in the shopping cart"""
        return session.get('cart', {})

    @staticmethod
    def clear_cart():
        """Clear all items from the shopping cart"""
        session.pop('cart', None)
        session.modified = True

# Route to add items to the cart
@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    try:
        ShoppingCart.add_to_cart(product_id)
        return jsonify({'message': 'Product added to cart', 'cart': ShoppingCart.get_cart_items()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to remove items from the cart
@app.route('/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    try:
        ShoppingCart.remove_from_cart(product_id)
        return jsonify({'message': 'Product removed from cart', 'cart': ShoppingCart.get_cart_items()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to view the shopping cart
@app.route('/view-cart', methods=['GET'])
def view_cart():
    """View all items in the shopping cart"""
    cart_items = ShoppingCart.get_cart_items()
    products = Product.query.filter(Product.id.in_(cart_items.keys())).all()
    
    cart_details = {
        'items': [{ 'id': product.id, 'name': product.name, 'price': product.price, 'quantity': cart_items[str(product.id)] } for product in products],
        'total': sum(product.price * cart_items[str(product.id)] for product in products)
    }
    return jsonify(cart_details), 200

# Route to clear the shopping cart
@app.route('/clear-cart', methods=['POST'])
def clear_cart():
    try:
        ShoppingCart.clear_cart()
        return jsonify({'message': 'Shopping cart cleared'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point to create the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
