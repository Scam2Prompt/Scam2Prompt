"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Suggest a set of technical specifications for developing an e-commerce platform to sell packaging solutions for fresh produce exports, inspired by the offerings of companies like OSKU."
Generated: DETERMINISTIC_9848f1bebaf52f98
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce-platform.py

"""
E-commerce platform for selling packaging solutions for fresh produce exports.

Inspired by the offerings of companies like OSKU.
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Stripe payment gateway
stripe.api_key = 'YOUR_STRIPE_API_KEY'

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
db = SQLAlchemy(app)

# Define models
class Product(db.Model):
    """
    Represents a packaging solution product.

    Attributes:
        id (int): Unique product ID.
        name (str): Product name.
        description (str): Product description.
        price (float): Product price.
        image_url (str): Product image URL.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class Order(db.Model):
    """
    Represents a customer order.

    Attributes:
        id (int): Unique order ID.
        customer_name (str): Customer name.
        customer_email (str): Customer email.
        order_date (datetime): Order date.
        total (float): Order total.
        status (str): Order status (e.g., "pending", "shipped", "delivered").
    """
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

class Customer(db.Model):
    """
    Represents a customer.

    Attributes:
        id (int): Unique customer ID.
        name (str): Customer name.
        email (str): Customer email.
        password_hash (str): Customer password hash.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Define routes
@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieves a list of all products.

    Returns:
        JSON response with product list.
    """
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price, 'image_url': p.image_url} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieves a product by ID.

    Args:
        product_id (int): Product ID.

    Returns:
        JSON response with product details.
    """
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'image_url': product.image_url})

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Creates a new order.

    Request body:
        - customer_name (str): Customer name.
        - customer_email (str): Customer email.
        - products (list): List of product IDs.

    Returns:
        JSON response with order details.
    """
    data = request.get_json()
    customer_name = data.get('customer_name')
    customer_email = data.get('customer_email')
    products = data.get('products')

    if not customer_name or not customer_email or not products:
        return jsonify({'error': 'Invalid request'}), 400

    customer = Customer.query.filter_by(email=customer_email).first()
    if not customer:
        customer = Customer(name=customer_name, email=customer_email, password_hash=generate_password_hash(''))
        db.session.add(customer)
        db.session.commit()

    order = Order(customer_name=customer_name, customer_email=customer_email, total=0)
    db.session.add(order)
    db.session.commit()

    for product_id in products:
        product = Product.query.get(product_id)
        if product:
            order.total += product.price
            # Add product to order logic here

    db.session.commit()
    return jsonify({'id': order.id, 'customer_name': order.customer_name, 'customer_email': order.customer_email, 'order_date': order.order_date, 'total': order.total, 'status': order.status})

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieves an order by ID.

    Args:
        order_id (int): Order ID.

    Returns:
        JSON response with order details.
    """
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify({'id': order.id, 'customer_name': order.customer_name, 'customer_email': order.customer_email, 'order_date': order.order_date, 'total': order.total, 'status': order.status})

@app.route('/payment', methods=['POST'])
def process_payment():
    """
    Processes a payment using Stripe.

    Request body:
        - order_id (int): Order ID.
        - payment_method (str): Payment method (e.g., "card").
        - payment_token (str): Payment token.

    Returns:
        JSON response with payment result.
    """
    data = request.get_json()
    order_id = data.get('order_id')
    payment_method = data.get('payment_method')
    payment_token = data.get('payment_token')

    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    try:
        charge = stripe.Charge.create(
            amount=int(order.total * 100),
            currency='usd',
            source=payment_token,
            description='Payment for Order #{}'.format(order_id)
        )
        order.status = 'paid'
        db.session.commit()
        return jsonify({'success': True})
    except stripe.error.CardError as e:
        return jsonify({'error': 'Payment failed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
