"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Illustrate how to implement a secure payment gateway for an investment platform like MET LIFE INVESTS using a popular payment processing library.
Generated: DETERMINISTIC_0bab6d940e922c38
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///investments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up Stripe API key
stripe.api_key = os.getenv('STRIPE_API_KEY')

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid credentials!"}), 401

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    """Create a payment intent for investment."""
    data = request.json
    amount = data.get('amount')  # Amount should be in cents

    try:
        # Create a payment intent using Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method_types=['card'],
        )
        return jsonify({"clientSecret": payment_intent['client_secret']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle Stripe webhooks."""
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    # Verify the webhook signature
    endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            print('PaymentIntent was successful!')
        elif event['type'] == 'payment_intent.payment_failed':
            print('PaymentIntent failed!')

        return jsonify({'status': 'success'}), 200
    except ValueError as e:
        # Invalid payload
        return jsonify({'error': str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
```

Please ensure to set the required environment variables (`DATABASE_URI`, `STRIPE_API_KEY`, and `STRIPE_WEBHOOK_SECRET`) before running the application.
