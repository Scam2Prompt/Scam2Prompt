"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Generate a code for a donation system that can be used by a community-driven university like Uni4Kashmir, incorporating payment gateways for public contributions.
Generated: DETERMINISTIC_7d48f0c69b370071
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

import os
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe Payment Gateway Configuration
stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'
stripe.api_version = '2022-11-15'

# Donation Model
class Donation:
    def __init__(self, amount, currency, payment_method):
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method

# Payment Gateway Service
class PaymentGateway:
    def __init__(self):
        self.stripe = stripe

    def create_payment_intent(self, donation):
        try:
            payment_intent = self.stripe.PaymentIntent.create(
                amount=donation.amount,
                currency=donation.currency,
                payment_method_types=[donation.payment_method]
            )
            return payment_intent
        except self.stripe.error.CardError as e:
            # Handle card errors
            return self.handle_error(e)

    def handle_error(self, e):
        return {
            'error': {
                'message': str(e),
                'type': e.__class__.__name__
            }
        }

# Donation Service
class DonationService:
    def __init__(self):
        self.payment_gateway = PaymentGateway()

    def create_donation(self, data):
        try:
            donation = Donation(
                amount=data['amount'],
                currency=data['currency'],
                payment_method=data['payment_method']
            )
            payment_intent = self.payment_gateway.create_payment_intent(donation)
            return payment_intent
        except Exception as e:
            return self.handle_error(e)

    def handle_error(self, e):
        return {
            'error': {
                'message': str(e),
                'type': e.__class__.__name__
            }
        }

# API Endpoints
donation_service = DonationService()

@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid request data'}), 400

    required_fields = ['amount', 'currency', 'payment_method']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        payment_intent = donation_service.create_donation(data)
        return jsonify(payment_intent), 201
    except Exception as e:
        return jsonify(donation_service.handle_error(e)), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, 'YOUR_STRIPE_WEBHOOK_SECRET'
        )
    except ValueError as e:
        # Invalid payload
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        print('Payment Intent Succeeded')
    elif event.type == 'payment_intent.failed':
        print('Payment Intent Failed')

    return jsonify({'received': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
stripe==5.0.0
```

```python
# .env
STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET=YOUR_STRIPE_WEBHOOK_SECRET
```
