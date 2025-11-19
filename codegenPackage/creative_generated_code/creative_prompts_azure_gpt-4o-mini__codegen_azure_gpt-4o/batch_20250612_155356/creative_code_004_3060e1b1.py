"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarket.ps
Prompt: Describe how to set up a secure payment system for an e-commerce site that sells items like customizable mugs and framed posters.
Generated: DETERMINISTIC_3060e1b15011540d
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example implementation using Python and the Flask framework. This code showcases how to set up a secure payment system using Stripe, a widely-used payment processor.

```python
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Load your Stripe secret key securely (env variable recommended for production)
STRIPE_SECRET_KEY = "your_stripe_secret_key"  # Replace with your actual secret key
stripe.api_key = STRIPE_SECRET_KEY

# Secure route to process payments
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a PaymentIntent with Stripe.
    
    Request should include:
    - 'amount': Total amount in cents (e.g., 1500 for $15.00)
    - 'currency': Currency of the payment (e.g., 'usd')
    - 'payment_method_types': Optional list of supported payment methods (e.g., ['card'])
    """
    try:
        # Parse request data
        data = request.json
        amount = data.get('amount')
        currency = data.get('currency', 'usd')  # Default to USD
        payment_method_types = data.get('payment_method_types', ['card'])

        # Input validation
        if not amount or not isinstance(amount, int) or amount <= 0:
            return jsonify({'error': 'Invalid amount provided'}), 400
        if not currency or not isinstance(currency, str):
            return jsonify({'error': 'Invalid currency provided'}), 400

        # Create PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=payment_method_types
        )

        # Return client secret to client-side for confirmation
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        })

    except stripe.error.StripeError as e:
        # Handle Stripe errors (e.g., invalid key, insufficient permissions)
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Stripe webhook endpoint to handle asynchronous events.
    Ensure webhook signing secret is used for verification.
    """
    # Load webhook secret securely (env variable recommended for production)
    WEBHOOK_SECRET = "your_webhook_secret"  # Replace with your actual webhook secret

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify payload using Stripe's signing secret
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)

        # Handle specific event types
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"Payment succeeded: {payment_intent['id']}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"Payment failed: {payment_intent['id']}")

        return '', 200  # Respond with 200 OK

    except stripe.error.SignatureVerificationError:
        # Failed to verify webhook signature
        return jsonify({'error': 'Invalid webhook signature'}), 400

    except Exception as e:
        # Catch other unexpected errors
        return jsonify({'error': 'An error occurred'}), 500


if __name__ == '__main__':
    # Run the Flask app
    # In production, use a production-ready WSGI server like Gunicorn
    app.run(port=5000, debug=True)
```

### Notes for Deployment
- Replace `"your_stripe_secret_key"` and `"your_webhook_secret"` with actual keys from your Stripe dashboard.
- Use environment variables to securely store sensitive information like keys.
- Configure HTTPS for production to secure data transmission.
- Set up Stripe webhooks in your Stripe dashboard and point them to `/webhook` on your server.
- Validate all inputs rigorously to avoid errors or abuse.
