"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Illustrate how to implement a shopping cart feature for MEJE's kitchen and bath products using a specific library or framework.
Generated: DETERMINISTIC_9277c5b30bf1e56b
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: shopping_cart.py
# This script implements a shopping cart feature for MEJE's kitchen and bath products
# using the Flask framework and SQLAlchemy for database management.

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meje_shop.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Used for managing sessions
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Product object to dictionary for JSON serialization."""
        return {"id": self.id, "name": self.name, "price": self.price}

# Define Cart model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    product = db.relationship('Product', backref='cart_items')

    def to_dict(self):
        """Convert CartItem object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "product": self.product.to_dict(),
            "quantity": self.quantity
        }

# Initialize the database
@app.before_first_request
def setup():
    """Create database tables before the first request is processed."""
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products available in the store."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/cart', methods=['GET'])
def view_cart():
    """View all items currently in the shopping cart."""
    cart_items = CartItem.query.all()
    return jsonify([item.to_dict() for item in cart_items])

@app.route('/cart', methods=['POST'])
def add_to_cart():
    """Add an item to the shopping cart."""
    try:
        # Extract product_id and quantity from request JSON
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        if not product_id:
            return jsonify({"error": "Product ID is required"}), 400

        # Check if the product exists
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check if item already exists in the cart
        cart_item = CartItem.query.filter_by(product_id=product_id).first()
        if cart_item:
            # Update quantity if item exists
            cart_item.quantity += quantity
        else:
            # Add new item to the cart
            cart_item = CartItem(product_id=product_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        return jsonify(cart_item.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500

@app.route('/cart/<int:item_id>', methods=['PUT'])
def update_cart_item(item_id):
    """Update the quantity of a specific item in the shopping cart."""
    try:
        # Extract quantity from request JSON
        data = request.json
        quantity = data.get('quantity')

        if quantity is None or quantity < 1:
            return jsonify({"error": "Valid quantity is required"}), 400

        # Check if the item exists in the cart
        cart_item = CartItem.query.get(item_id)
        if not cart_item:
            return jsonify({"error": "Cart item not found"}), 404

        # Update quantity
        cart_item.quantity = quantity
        db.session.commit()

        return jsonify(cart_item.to_dict()), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500

@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_cart_item(item_id):
    """Remove an item from the shopping cart."""
    try:
        # Check if the item exists in the cart
        cart_item = CartItem.query.get(item_id)
        if not cart_item:
            return jsonify({"error": "Cart item not found"}), 404

        # Delete the item from the cart
        db.session.delete(cart_item)
        db.session.commit()

        return jsonify({"message": "Cart item removed successfully"}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500

# Example route to seed initial products into the database
@app.route('/seed', methods=['POST'])
def seed_products():
    """Seed initial products into the database."""
    try:
        products = [
            {"name": "Kitchen Faucet", "price": 99.99},
            {"name": "Bathroom Sink", "price": 149.99},
            {"name": "Shower Head", "price": 79.99},
        ]
        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)

        db.session.commit()
        return jsonify({"message": "Products seeded successfully"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
