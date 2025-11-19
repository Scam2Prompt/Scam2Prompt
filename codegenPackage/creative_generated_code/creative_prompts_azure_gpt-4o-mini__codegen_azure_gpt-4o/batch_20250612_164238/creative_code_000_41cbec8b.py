"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Generate a code snippet for a secure payment integration for an online lottery platform like HONGTOGEL, ensuring user data protection.
Generated: DETERMINISTIC_41cbec8b22e2a10f
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe  # Stripe SDK for payment processing
import logging
import os
from flask import Flask, request, jsonify

# Flask app setup
app = Flask(__name__)

# Configure Stripe API keys securely (use environment variables)
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

if not STRIPE_API_KEY or not STRIPE_WEBHOOK_SECRET:
    raise ValueError("Stripe API keys must be set as environment variables.")

stripe.api_key = STRIPE_API_KEY

# Logger setup for monitoring and debugging
logging.basicConfig(level=logging.INFO)

@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    """
    Endpoint to create a payment intent.
    This is used to initiate a payment securely and communicates with Stripe's API.
    """
    try:
        # Parse request data
        data = request.json
        if not data or "amount" not in data or "currency" not in data:
            return jsonify({"error": "Invalid request data"}), 400

        # Ensure valid data
        amount = int(data["amount"])
        currency = data["currency"]

        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400

        # Create payment intent using Stripe API
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,  # Amount in smallest currency unit (e.g., cents)
            currency=currency,  # Currency (e.g., "usd")
            payment_method_types=["card"],  # Accept card payments
        )

        # Return client secret for front-end usage
        return jsonify({"client_secret": payment_intent.client_secret}), 200

    except stripe.error.StripeError as e:
        logging.error(f"Stripe error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    """
    Stripe webhook handler to process events securely.
    Used for listening to Stripe events like payment confirmation.
    """
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Verify webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )

        # Handle the event
        if event["type"] == "payment_intent.succeeded":
            payment_intent = event["data"]["object"]
            logging.info(f"Payment succeeded: {payment_intent['id']}")
            # Add business logic here (e.g., update user account, send confirmation)
        elif event["type"] == "payment_intent.payment_failed":
            payment_intent = event["data"]["object"]
            logging.warning(f"Payment failed: {payment_intent['id']}")
            # Handle failed payments as necessary
        else:
            logging.info(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        logging.error(f"Webhook signature verification failed: {e}")
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=False)  # Ensure debug is False for production
```

**Note:** Replace `STRIPE_API_KEY` and `STRIPE_WEBHOOK_SECRET` with actual environment variables in production. Ensure HTTPS is used for secure communication.
