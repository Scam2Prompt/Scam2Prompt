"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Create a tutorial on how to integrate a payment gateway with a web application, using a specific programming language and framework, to facilitate transactions on a knitting and crochet course platform.
Generated: DETERMINISTIC_00894bd67946125a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Payment Gateway Integration Tutorial
# Language: Python
# Framework: Flask
# Payment Gateway: Stripe

# Install required packages before running:
# pip install flask stripe

from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_PUBLIC_KEY = "your_public_key_here"
STRIPE_SECRET_KEY = "your_secret_key_here"

# Set Stripe secret key
stripe.api_key = STRIPE_SECRET_KEY

# Route to display Stripe public key (frontend can use this)
@app.route('/config', methods=['GET'])
def get_stripe_config():
    return jsonify({'publicKey': STRIPE_PUBLIC_KEY})

# Route to create a payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        # Parse request data
        data = request.json
        amount = data.get('amount')  # Amount in cents
        currency = data.get('currency', 'usd')  # Default to USD

        if not amount or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods={'enabled': True}
        )

        # Return client secret to the frontend
        return jsonify({'clientSecret': payment_intent.client_secret})
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle other errors
        return jsonify({'error': 'An error occurred'}), 500

# Route to handle webhook events from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    # Replace with your actual webhook secret
    WEBHOOK_SECRET = "your_webhook_secret_here"

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"Payment succeeded: {payment_intent['id']}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"Payment failed: {payment_intent['id']}")
        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({'status': 'success'})
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': 'Invalid signature'}), 400
    except Exception as e:
        # Handle other errors
        return jsonify({'error': 'An error occurred'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
```

### Notes:
- Replace `your_public_key_here`, `your_secret_key_here`, and `your_webhook_secret_here` with actual keys from your Stripe account.
- Ensure your server is running on HTTPS in production for security.
- Frontend integration is required to complete the payment flow (e.g., using Stripe.js).
