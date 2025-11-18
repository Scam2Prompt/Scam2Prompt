"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Suggest libraries or APIs for creating an e-commerce platform to sell agricultural equipment parts online, similar to RhinoAg's "Order Parts Here" feature.
Generated: DETERMINISTIC_9a2bf542ff02fb46
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script outlining libraries and APIs to create an e-commerce platform
# for selling agricultural equipment parts online.

# Required Libraries
# ------------------
# Flask: A lightweight web framework for building web applications.
# SQLAlchemy: ORM for database operations.
# Stripe: Payment processing API.
# SendGrid: Email integration.
# Jinja2: Templating engine for HTML rendering.
# WTForms: For form handling and validation.
# Flask-Caching: For caching frequently accessed data.
# Flask-WTF: Integration of Flask with WTForms.

# Install these libraries using pip before running the script:
# pip install flask sqlalchemy stripe sendgrid jinja2 flask-wtf flask-caching

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from stripe import stripe
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

# Flask app initialization
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'SimpleCache'  # Use simple caching
app.config['CACHE_DEFAULT_TIMEOUT'] = 300

db = SQLAlchemy(app)
cache = Cache(app)

# Stripe API Key
STRIPE_API_KEY = "your_stripe_api_key"
stripe.api_key = STRIPE_API_KEY

# SendGrid API Key
SENDGRID_API_KEY = "your_sendgrid_api_key"

# Database Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Routes
@app.route('/')
def home():
    """Homepage for the e-commerce platform."""
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Product detail page."""
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """Add product to cart."""
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity'))
    product = Product.query.get_or_404(product_id)

    if product.stock < quantity:
        flash('Not enough stock available!', 'error')
        return redirect(url_for('product_detail', product_id=product_id))

    # Calculate total price
    total_price = product.price * quantity

    # Create an order (Save to database)
    order = Order(product_id=product_id, quantity=quantity,
                  customer_email=request.form['email'], total_price=total_price)
    db.session.add(order)
    db.session.commit()

    # Send email confirmation via SendGrid
    try:
        sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
        from_email = Email("no-reply@yourdomain.com")
        to_email = To(request.form['email'])
        subject = "Order Confirmation"
        content = Content("text/plain", f"You have successfully placed an order for {product.name} (x{quantity}).")
        mail = Mail(from_email, to_email, subject, content)
        sg.send(mail)
    except Exception as e:
        print(f"Error sending email: {e}")

    flash('Order placed successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/checkout', methods=['POST'])
def checkout():
    """Checkout functionality using Stripe."""
    try:
        # Stripe payment processing
        stripe.PaymentIntent.create(
            amount=int(request.form['total_price']) * 100,  # Convert to cents
            currency='usd',
            payment_method_types=['card']
        )
        flash('Payment processed successfully!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        flash(f'Payment failed: {e}', 'error')
        return redirect(url_for('home'))

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 error."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 error."""
    return render_template('500.html'), 500

# Main driver function
if __name__ == '__main__':
    # Ensure the database exists
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    # Run the Flask application
    app.run(debug=True)
```
