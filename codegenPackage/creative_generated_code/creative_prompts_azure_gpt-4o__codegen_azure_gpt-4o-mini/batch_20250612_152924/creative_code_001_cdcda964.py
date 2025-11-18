"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delourier.com
Prompt: Generate code to implement a secure payment system for a luxury fashion e-commerce website like Delourier, ensuring compatibility with worldwide shipping and free shipping options.
Generated: DETERMINISTIC_cdcda964ad6e41de
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Change to your production database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Stripe API
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')  # Store your Stripe secret key in environment variables

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='USD')
    status = db.Column(db.String(20), default='pending')

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password required"}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(email=data['email'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/create_payment', methods=['POST'])
def create_payment():
    """Create a payment intent."""
    data = request.get_json()
    if 'amount' not in data or 'currency' not in data or 'email' not in data:
        return jsonify({"error": "Amount, currency, and email required"}), 400

    try:
        # Create a PaymentIntent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency=data['currency'],
            payment_method_types=["card"],
        )

        # Save the order in the database
        user = User.query.filter_by(email=data['email']).first()
        new_order = Order(user_id=user.id, amount=data['amount'] / 100, currency=data['currency'])
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"clientSecret": intent['client_secret']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/order_status/<int:order_id>', methods=['GET'])
def order_status(order_id):
    """Check the status of an order."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"order_id": order.id, "status": order.status}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a basic secure payment system using Flask, SQLAlchemy for database interactions, and Stripe for payment processing. Ensure you have your Stripe secret key and environment configured for production usage.
