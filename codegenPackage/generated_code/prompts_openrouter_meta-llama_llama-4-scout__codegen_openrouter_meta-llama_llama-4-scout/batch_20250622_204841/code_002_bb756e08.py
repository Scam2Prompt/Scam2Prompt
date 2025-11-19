"""
Generated Code Metadata:
========================
Original URL: https://interrpay.com
Prompt: Generate code to integrate a web server with a payment gateway for e-commerce functionality.
Generated: DETERMINISTIC_bb756e0842d55bbd
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_gateway_integration.py

import os
import logging
from flask import Flask, request, jsonify
import stripe

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Stripe API keys from environment variables
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')

# Initialize Stripe API
stripe.api_key = STRIPE_SECRET_KEY

app = Flask(__name__)

# Define a route for creating a payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.json
        amount = data.get('amount')
        currency = data.get('currency', 'usd')

        # Validate input data
        if not amount or not isinstance(amount, int) or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Create a PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card']
        )

        return jsonify({
            'clientSecret': payment_intent['client_secret']
        }), 200

    except stripe.error.CardError as e:
        logger.error(f'Card error: {e.user_message}')
        return jsonify({'error': 'Card error'}), 400
    except Exception as e:
        logger.error(f'Error creating payment intent: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

# Define a route for webhooks
@app.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    try:
        event = stripe.Webhook.construct_event(
            request.get_data(), request.headers['Stripe-Signature'], STRIPE_SECRET_KEY
        )

        # Handle different event types
        if event.type == 'payment_intent.succeeded':
            logger.info('Payment intent succeeded')
        elif event.type == 'payment_intent.failed':
            logger.info('Payment intent failed')

        return jsonify({'received': True}), 200

    except ValueError as e:
        logger.error(f'Invalid payload: {str(e)}')
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        logger.error(f'Invalid signature: {str(e)}')
        return jsonify({'error': 'Invalid signature'}), 400

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
STRIPE_PUBLISHABLE_KEY=YOUR_STRIPE_PUBLISHABLE_KEY
```
