"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Illustrate how to implement a payment processing system in a web application for booking DJ services, including options for cash, credit/debit cards, and digital wallets as described on the site.
Generated: DETERMINISTIC_71ac28f4d37bea10
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_processor.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
import stripe

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'  # Replace with your actual Stripe secret key
db = SQLAlchemy(app)

# Define a Payment model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Initialize Stripe
stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/api/payment', methods=['POST'])
def process_payment():
    """
    Process a payment based on the selected method.
    Accepts JSON payload with 'amount', 'method', and optional 'token' for card payments.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'amount' not in data or 'method' not in data:
        raise BadRequest("Missing required fields: 'amount' and 'method'.")

    amount = data['amount']
    method = data['method']
    status = 'failed'

    try:
        if method == 'credit_card':
            token = data.get('token')
            if not token:
                raise BadRequest("Token is required for credit card payments.")
            # Process credit card payment
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Amount in cents
                currency='usd',
                source=token,
                description='DJ Service Booking Payment'
            )
            status = 'succeeded' if charge['paid'] else 'failed'

        elif method == 'cash':
            # Handle cash payment (no external processing)
            status = 'succeeded'

        elif method == 'digital_wallet':
            # Placeholder for digital wallet processing
            # Implement specific logic for digital wallets here
            status = 'succeeded'

        else:
            raise BadRequest("Invalid payment method. Use 'credit_card', 'cash', or 'digital_wallet'.")

        # Save payment record to the database
        payment = Payment(amount=amount, method=method, status=status)
        db.session.add(payment)
        db.session.commit()

        return jsonify({'status': status, 'payment_id': payment.id}), 200

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error processing payment: {e}")
        return jsonify({'status': 'failed', 'error': str(e)}), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Notes:
- Replace `'your_stripe_secret_key'` with your actual Stripe secret key.
- Ensure that you have Flask and Stripe installed in your environment (`pip install Flask Flask-SQLAlchemy stripe`).
- This code is a basic implementation and should be extended with proper logging, security measures, and validation as needed for production use.
