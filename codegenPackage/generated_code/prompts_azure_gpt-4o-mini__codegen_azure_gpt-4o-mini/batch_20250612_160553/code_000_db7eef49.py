"""
Generated Code Metadata:
========================
Original URL: https://fornm.network
Prompt: How can I implement a secure payment system for purchasing domain names similar to the one described on fornm.network?
Generated: DETERMINISTIC_db7eef4943f5e37a
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from stripe import Stripe, error as stripe_error

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///payments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Stripe with secret key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Database model for storing payment transactions
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return jsonify({'error': 'User registration failed.'}), 500

@app.route('/pay', methods=['POST'])
def pay():
    """Process a payment for a domain purchase."""
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')

    if not user_id or not amount:
        return jsonify({'error': 'User ID and amount are required.'}), 400

    try:
        # Create a payment intent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Amount in cents
            currency='usd',
            payment_method_types=['card'],
        )

        # Record the payment in the database
        new_payment = Payment(user_id=user_id, amount=amount, status='pending')
        db.session.add(new_payment)
        db.session.commit()

        return jsonify({'client_secret': payment_intent['client_secret']}), 200
    except stripe_error.StripeError as e:
        logging.error(f"Stripe error: {e.user_message}")
        return jsonify({'error': 'Payment processing failed.'}), 500
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
        return jsonify({'error': 'Payment processing failed.'}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle Stripe webhook events."""
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET'))

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            # Update payment status in the database
            payment = Payment.query.filter_by(id=payment_intent['metadata']['payment_id']).first()
            if payment:
                payment.status = 'succeeded'
                db.session.commit()

        return jsonify({'status': 'success'}), 200
    except ValueError as e:
        logging.error(f"Invalid payload: {e}")
        return jsonify({'error': 'Invalid payload.'}), 400
    except stripe.error.SignatureVerificationError as e:
        logging.error(f"Invalid signature: {e}")
        return jsonify({'error': 'Invalid signature.'}), 400
    except Exception as e:
        logging.error(f"Webhook error: {e}")
        return jsonify({'error': 'Webhook error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variables `DATABASE_URL`, `STRIPE_SECRET_KEY`, and `STRIPE_WEBHOOK_SECRET` before running the application.
