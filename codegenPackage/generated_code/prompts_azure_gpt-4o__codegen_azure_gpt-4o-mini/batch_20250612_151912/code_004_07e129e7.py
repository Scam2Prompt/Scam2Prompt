"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: Write a script to implement a "View Cart" functionality for an online store, similar to the one described on Adhive Marketplace.
Generated: DETERMINISTIC_07e129e7c7eedbb4
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# view_cart.py

from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the CartItem model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert CartItem to dictionary for JSON response."""
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/cart', methods=['GET'])
def view_cart():
    """View the items in the shopping cart."""
    try:
        # Retrieve cart items from the database
        cart_items = CartItem.query.all()
        return jsonify([item.to_dict() for item in cart_items]), 200
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error retrieving cart items: {e}")
        return jsonify({"error": "Unable to retrieve cart items."}), 500

@app.route('/cart', methods=['POST'])
def add_to_cart():
    """Add an item to the shopping cart."""
    try:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        # Validate input
        if not product_id or quantity <= 0:
            return jsonify({"error": "Invalid product ID or quantity."}), 400

        # Create a new cart item
        new_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()

        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error adding item to cart: {e}")
        return jsonify({"error": "Unable to add item to cart."}), 500

@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    """Remove an item from the shopping cart."""
    try:
        item = CartItem.query.get(item_id)
        if not item:
            return jsonify({"error": "Item not found."}), 404

        db.session.delete(item)
        db.session.commit()

        return jsonify({"message": "Item removed from cart."}), 200
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error removing item from cart: {e}")
        return jsonify({"error": "Unable to remove item from cart."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask and SQLAlchemy to create a simple "View Cart" functionality for an online store.
- It includes routes to view, add, and remove items from the cart, with appropriate error handling and logging.
- Ensure to install Flask and Flask-SQLAlchemy before running the script:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
