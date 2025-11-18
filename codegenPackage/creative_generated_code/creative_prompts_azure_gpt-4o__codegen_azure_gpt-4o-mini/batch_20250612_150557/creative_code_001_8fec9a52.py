"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solak.web.app
Prompt: Generate code to integrate Stripe for adding funds to a wallet, similar to the functionality provided on the NFT Solak platform.
Generated: DETERMINISTIC_8fec9a528d9ba517
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallets.db'  # Use your preferred database
db = SQLAlchemy(app)

# Set your Stripe secret key
stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'

# Define a Wallet model to store user wallet information
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Create a payment intent to add funds to the user's wallet.
    """
    data = request.get_json()

    # Validate incoming data
    try:
        user_id = data['user_id']
        amount = data['amount']  # Amount in cents
    except KeyError:
        raise BadRequest("Missing user_id or amount")

    # Create a payment intent with Stripe
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            metadata={'user_id': user_id}
        )
        return jsonify({'client_secret': intent['client_secret']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Handle webhook events from Stripe to update user wallet balances.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    endpoint_secret = 'YOUR_STRIPE_ENDPOINT_SECRET'
    event = None

    # Verify the webhook signature
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle the payment intent succeeded event
    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        user_id = intent['metadata']['user_id']
        amount_received = intent['amount_received'] / 100  # Convert cents to dollars

        # Update the user's wallet balance
        wallet = Wallet.query.filter_by(user_id=user_id).first()
        if wallet:
            wallet.balance += amount_received
            db.session.commit()

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

### Notes:
- Replace `YOUR_STRIPE_SECRET_KEY` and `YOUR_STRIPE_ENDPOINT_SECRET` with your actual Stripe keys.
- Use a proper database URI in `SQLALCHEMY_DATABASE_URI`.
- Ensure Flask and Stripe libraries are installed in your environment (`pip install Flask Flask-SQLAlchemy stripe`).
- This code includes error handling for missing data, failed Stripe API calls, and webhook signature verification.
