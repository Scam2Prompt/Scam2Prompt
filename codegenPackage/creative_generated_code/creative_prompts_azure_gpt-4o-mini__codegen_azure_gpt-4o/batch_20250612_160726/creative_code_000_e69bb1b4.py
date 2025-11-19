"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symibyotic.fi
Prompt: How can I implement a secure payment system for purchasing domain names similar to the one described on symibyotic.fi?
Generated: DETERMINISTIC_e69bb1b4f3df0a91
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a secure payment system for purchasing domain names. It uses Python and integrates with Stripe for payment processing. The implementation assumes you have set up a Stripe account and obtained the API keys.

```python
import stripe
from flask import Flask, request, jsonify

# Flask application setup
app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_SECRET_KEY = "your_secret_key_here"  # Keep this secret and secure!
STRIPE_PUBLISHABLE_KEY = "your_publishable_key_here"

# Configure Stripe
stripe.api_key = STRIPE_SECRET_KEY

# List of available domain names and their prices (hardcoded for simplicity)
DOMAIN_PRICES = {
    "example.com": 10.00,  # Price in USD
    "mysite.net": 15.00,
    "coolwebsite.org": 20.00
}

@app.route('/domains', methods=['GET'])
def list_domains():
    """
    Endpoint to list available domain names and their prices.
    """
    return jsonify(DOMAIN_PRICES)

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe Payment Intent for purchasing a domain.
    """
    try:
        # Parse request data
        data = request.json
        domain_name = data.get('domain_name')

        if domain_name not in DOMAIN_PRICES:
            return jsonify({"error": "Invalid domain name selected."}), 400

        # Retrieve domain price
        amount = int(DOMAIN_PRICES[domain_name] * 100)  # Convert to cents

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method_types=['card'],
            description=f"Purchase of domain: {domain_name}"
        )

        return jsonify({
            "client_secret": payment_intent['client_secret']
        })

    except stripe.error.StripeError as e:
        # Handle Stripe API errors gracefully
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint for handling Stripe webhooks to verify payment success.
    """
    webhook_secret = "your_webhook_secret_here"  # Replace with your actual webhook secret

    # Retrieve the raw request data
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"Payment succeeded for PaymentIntent ID: {payment_intent['id']}")

        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"Payment failed for PaymentIntent ID: {payment_intent['id']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        return jsonify({"error": "Invalid webhook signature."}), 400

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Replace placeholders like `your_secret_key_here` and `your_webhook_secret_here` with actual values from your Stripe account.
2. Make sure to secure sensitive information like API keys and webhook secrets in environment variables or a secure configuration file.
3. Use HTTPS in production to ensure communication security.
4. Set `debug=False` when deploying to production to prevent sensitive information leakage.
