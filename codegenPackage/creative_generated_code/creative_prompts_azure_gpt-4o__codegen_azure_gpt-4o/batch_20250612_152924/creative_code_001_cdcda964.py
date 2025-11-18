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
import stripe  # Stripe library for payment processing
from flask import Flask, request, jsonify  # Flask for web framework
import logging
from validate_email import validate_email  # To validate email addresses

# Flask application setup
app = Flask(__name__)

# Stripe API keys (Use environment variables for security in production)
STRIPE_PUBLIC_KEY = 'your_stripe_public_key'
STRIPE_SECRET_KEY = 'your_stripe_secret_key'
stripe.api_key = STRIPE_SECRET_KEY

# Logging setup for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Supported currencies for worldwide shipping
SUPPORTED_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD', 'JPY']

# Free shipping threshold (Based on currency)
FREE_SHIPPING_THRESHOLD = {
    'USD': 500,
    'EUR': 450,
    'GBP': 400,
    'AUD': 700,
    'CAD': 650,
    'JPY': 60000,
}

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe Payment Intent.
    This handles secure payment processing.

    Request Body:
        - amount: Total amount to be paid (integer)
        - currency: Currency code (string)
        - email: Customer's email address (string)

    Returns:
        - PaymentIntent client secret (string)
    """
    try:
        data = request.json
        amount = data.get('amount')
        currency = data.get('currency')
        email = data.get('email')

        # Validate request parameters
        if not amount or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400
        if currency not in SUPPORTED_CURRENCIES:
            return jsonify({'error': 'Unsupported currency'}), 400
        if not email or not validate_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        # Determine if free shipping applies
        shipping_cost = 0 if amount >= FREE_SHIPPING_THRESHOLD.get(currency, float('inf')) else 50  # Example shipping cost
        total_amount = amount + shipping_cost

        # Create Stripe Payment Intent
        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount * 100,  # Convert to smallest currency unit (e.g., cents)
            currency=currency,
            receipt_email=email,
        )

        return jsonify({
            'clientSecret': payment_intent['client_secret'],
            'currency': currency,
            'amount': total_amount,
            'shippingCost': shipping_cost,
        })

    except Exception as e:
        logging.error(f"Error creating payment intent: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle Stripe webhooks for payment status updates.
    """
    try:
        payload = request.data
        sig_header = request.headers.get('Stripe-Signature')
        endpoint_secret = 'your_stripe_webhook_secret'

        # Verify webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Handle event types
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            logging.info(f"Payment succeeded: {payment_intent['id']}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            logging.warning(f"Payment failed: {payment_intent['id']}")

        return jsonify({'status': 'success'}), 200

    except stripe.error.SignatureVerificationError as e:
        logging.error(f"Webhook signature verification failed: {e}")
        return jsonify({'error': 'Invalid webhook signature'}), 400

    except Exception as e:
        logging.error(f"Error handling webhook: {e}")
        return jsonify({'error': str(e)}), 500


# Run Flask app (Use production-ready WSGI servers like Gunicorn for deployment)
if __name__ == '__main__':
    app.run(debug=True)
```
