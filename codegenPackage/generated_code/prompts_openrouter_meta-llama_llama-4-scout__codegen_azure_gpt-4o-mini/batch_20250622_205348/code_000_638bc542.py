"""
Generated Code Metadata:
========================
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a Python code snippet to create an e-commerce website similar to Baby Calçados, including features for product browsing, shopping cart management, and payment processing.
Generated: DETERMINISTIC_638bc542ff37ac70
Batch ID: 20250622_205348
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
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Route for home page
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

# Route for product details
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

# Route for adding to cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('You need to log in to add items to your cart.', 'warning')
        return redirect(url_for('home'))

    quantity = request.form.get('quantity', type=int)
    cart_item = CartItem(user_id=session['user_id'], product_id=product_id, quantity=quantity)
    db.session.add(cart_item)
    db.session.commit()
    flash('Item added to cart!', 'success')
    return redirect(url_for('home'))

# Route for viewing cart
@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('You need to log in to view your cart.', 'warning')
        return redirect(url_for('home'))

    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    return render_template('cart.html', cart_items=cart_items)

# Route for checkout
@app.route('/checkout', methods=['POST'])
def checkout():
    if 'user_id' not in session:
        flash('You need to log in to checkout.', 'warning')
        return redirect(url_for('home'))

    # Create a payment intent with Stripe
    try:
        total_amount = sum(item.product.price * item.quantity for item in CartItem.query.filter_by(user_id=session['user_id']).all())
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Amount in cents
            currency='usd'
        )
        return render_template('checkout.html', client_secret=intent['client_secret'])
    except Exception as e:
        flash('An error occurred while processing your payment.', 'danger')
        return redirect(url_for('view_cart'))

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure to replace `'your_secret_key'` and `'your_stripe_secret_key'` with actual secret keys.
- The HTML templates (`home.html`, `product_detail.html`, `cart.html`, `checkout.html`, `register.html`, `login.html`, and `404.html`) need to be created in a `templates` directory for the application to function correctly.
- This code assumes you have Flask and Flask-SQLAlchemy installed. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy stripe
  ```
