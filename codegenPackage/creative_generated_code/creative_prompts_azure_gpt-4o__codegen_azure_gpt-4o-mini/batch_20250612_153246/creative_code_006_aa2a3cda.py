"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citygardenmexico.com.mx
Prompt: Suggest an API for e-commerce that could be used to replicate the functionality of City Garden México's online plant store, and write code to implement a shopping cart feature.
Generated: DETERMINISTIC_aa2a3cda43bb8f7e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Model for the shopping cart
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a product to the cart
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    try:
        data = request.json
        product_id = data['product_id']
        quantity = data['quantity']

        # Validate input
        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than zero."}), 400

        # Check if the product exists
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({"error": "Product not found."}), 404

        # Add item to session cart
        if 'cart' not in session:
            session['cart'] = {}

        if product_id in session['cart']:
            session['cart'][product_id] += quantity
        else:
            session['cart'][product_id] = quantity

        return jsonify({"message": "Product added to cart.", "cart": session['cart']}), 200

    except KeyError:
        return jsonify({"error": "Invalid input."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view the shopping cart
@app.route('/cart', methods=['GET'])
def view_cart():
    cart = session.get('cart', {})
    return jsonify({"cart": cart}), 200

# Route to remove a product from the cart
@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    try:
        data = request.json
        product_id = data['product_id']

        if 'cart' in session and product_id in session['cart']:
            del session['cart'][product_id]
            return jsonify({"message": "Product removed from cart.", "cart": session['cart']}), 200
        else:
            return jsonify({"error": "Product not found in cart."}), 404

    except KeyError:
        return jsonify({"error": "Invalid input."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to checkout (dummy implementation)
@app.route('/checkout', methods=['POST'])
def checkout():
    if 'cart' not in session or not session['cart']:
        return jsonify({"error": "Cart is empty."}), 400

    # Here would be the payment processing and order creation logic
    session.pop('cart', None)  # Clear the cart after checkout
    return jsonify({"message": "Checkout successful."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes
- This code implements a basic shopping cart feature using Flask and SQLAlchemy.
- It includes routes to add, view, and remove items from the cart, as well as a mock checkout process.
- Proper error handling and validation are included to ensure robustness.
