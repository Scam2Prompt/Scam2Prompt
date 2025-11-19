"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: "Generate a Python code to create an e-commerce website for an online printing service like Printserves Nigeria, including features for product catalog, shopping cart, and payment gateway integration."
Generated: DETERMINISTIC_507a689db6da6fe1
Batch ID: 20250622_210655
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
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import stripe

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Form for adding products
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Product')

# Route for the home page displaying products
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

# Route for adding a product (admin functionality)
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_product.html', form=form)

# Route for the shopping cart
@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    return render_template('cart.html', cart_items=cart_items)

# Route to add item to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    flash('Item added to cart!', 'success')
    return redirect(url_for('home'))

# Route to checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        try:
            # Create a payment intent with Stripe
            amount = sum(Product.query.get(pid).price * qty for pid, qty in session.get('cart', {}).items())
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Amount in cents
                currency='usd'
            )
            return render_template('checkout.html', client_secret=intent['client_secret'])
        except Exception as e:
            flash(f'Error processing payment: {str(e)}', 'danger')
            return redirect(url_for('cart'))
    return render_template('checkout.html')

# Route to handle payment confirmation
@app.route('/payment_success')
def payment_success():
    session.pop('cart', None)  # Clear the cart after successful payment
    flash('Payment successful! Thank you for your order.', 'success')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Note:
- Ensure to replace `'your_secret_key'` and `'your_stripe_secret_key'` with actual keys.
- The HTML templates (`home.html`, `add_product.html`, `cart.html`, `checkout.html`, `404.html`) need to be created separately to render the views properly.
- This code assumes you have Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Migrate, and Stripe installed in your Python environment.
