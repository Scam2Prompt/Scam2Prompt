"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that mimics the purchasing process on Danda Loja, including payment options.
Generated: DETERMINISTIC_685fee4047c2220a
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Model representing a product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Model representing a cart item
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Home route to display products
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

# Route to add a product to the cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}

    # Update cart quantity
    session['cart'][str(product_id)] = session['cart'].get(str(product_id), 0) + 1
    flash('Product added to cart!', 'success')
    return redirect(url_for('home'))

# Route to view the shopping cart
@app.route('/cart')
def view_cart():
    cart_items = []
    total_price = 0.0
    if 'cart' in session:
        for product_id, quantity in session['cart'].items():
            product = Product.query.get(product_id)
            if product:
                total_price += product.price * quantity
                cart_items.append({'product': product, 'quantity': quantity})
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Route to remove an item from the cart
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        session['cart'].pop(str(product_id), None)
        flash('Product removed from cart!', 'success')
    return redirect(url_for('view_cart'))

# Route to checkout
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Route to process payment (mock implementation)
@app.route('/process_payment', methods=['POST'])
def process_payment():
    try:
        # Here you would integrate with a payment gateway
        payment_method = request.form['payment_method']
        if payment_method not in ['credit_card', 'paypal']:
            raise ValueError("Invalid payment method")

        # Mock payment processing
        flash('Payment processed successfully!', 'success')
        session.pop('cart', None)  # Clear cart after payment
        return redirect(url_for('home'))

    except ValueError as ve:
        flash(str(ve), 'danger')
        return redirect(url_for('checkout'))
    except Exception as e:
        flash('An error occurred while processing your payment. Please try again.', 'danger')
        return redirect(url_for('checkout'))

if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: The above code assumes you have a Flask environment set up. You need to create the corresponding HTML templates (`home.html`, `cart.html`, and `checkout.html`) for it to function properly. Also, make sure to run the database migrations if you are using a different database.
