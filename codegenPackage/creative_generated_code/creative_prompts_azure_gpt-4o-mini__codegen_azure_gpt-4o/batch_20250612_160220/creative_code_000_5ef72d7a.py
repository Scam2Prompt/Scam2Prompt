"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyi.foundation
Prompt: Generate a code snippet for a secure payment integration for domain purchases similar to the process described on storyi.foundation.
Generated: DETERMINISTIC_5ef72d7a7767f9f5
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, secure, and production-ready Python code snippet for integrating a payment gateway using Flask and Stripe for domain purchases.

```python
import os
from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Set up Stripe API key from environment variable for security
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")  # Ensure STRIPE_SECRET_KEY is set in the environment

# Route for creating a payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        # Parse the request body for domain purchase details
        data = request.json
        domain_name = data.get("domain_name")
        amount = data.get("amount")

        if not domain_name or not amount:
            return jsonify({"error": "Missing domain_name or amount"}), 400

        # Convert amount to cents (Stripe expects smallest currency unit)
        amount_in_cents = int(amount * 100)

        # Create a Stripe PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency="usd",  # Adjust currency as needed
            description=f"Purchase of domain: {domain_name}",
            metadata={"domain_name": domain_name}
        )

        # Respond with the client secret (used for payment confirmation)
        return jsonify({"client_secret": payment_intent.client_secret}), 200

    except Exception as e:
        # Handle exceptions and provide feedback
        return jsonify({"error": str(e)}), 500


# Route for handling webhook events from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    try:
        # Verify the webhook signature for security
        payload = request.data
        sig_header = request.headers.get('Stripe-Signature')
        webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")  # Ensure STRIPE_WEBHOOK_SECRET is set in the environment

        if not webhook_secret:
            return jsonify({"error": "Webhook secret not configured"}), 500

        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # Handle the event (e.g., payment succeeded)
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            domain_name = payment_intent['metadata']['domain_name']

            # Process successful payment (e.g., register domain, send confirmation email)
            print(f"Payment succeeded for domain: {domain_name}")

        # Respond with 200 OK
        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app
    # Use SSL/TLS in production and a proper WSGI server (e.g., Gunicorn or uWSGI)
    app.run(debug=True)
```

### Environment Variables Required:
- `STRIPE_SECRET_KEY`: Your Stripe secret key.
- `STRIPE_WEBHOOK_SECRET`: Stripe webhook secret for verifying incoming requests.

### Install Required Dependencies:
```bash
pip install flask stripe
```

### Notes:
- This code is designed to be used securely in production. Make sure to test thoroughly and use HTTPS for deployment.
- Handle sensitive data like API keys and webhook secrets securely using environment variables or a secret management system.
