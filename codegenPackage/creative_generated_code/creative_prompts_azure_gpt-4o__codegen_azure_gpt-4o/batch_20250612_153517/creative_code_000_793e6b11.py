"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kvtech.ae
Prompt: Write code to integrate a secure payment gateway for an e-commerce website designed by KEVI Technologies, ensuring compatibility with credit/debit card transactions.
Generated: DETERMINISTIC_793e6b11a57ece47
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: payment_gateway_integration.py

import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Stripe API secret key (replace with your actual secret key)
STRIPE_SECRET_KEY = "sk_test_your_secret_key_here"
stripe.api_key = STRIPE_SECRET_KEY

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    API endpoint to handle payment intents for credit/debit card transactions.
    This creates a payment intent using Stripe's secure payment gateway.
    """
    try:
        # Parse payment details from the request
        request_data = request.json
        if not request_data:
            return jsonify({"error": "Invalid request body"}), 400

        # Ensure required fields are present
        amount = request_data.get("amount")  # Amount in cents (e.g., $10.00 → 1000)
        currency = request_data.get("currency", "usd")  # Default to USD currency

        if not amount or not isinstance(amount, int):
            return jsonify({"error": "Invalid or missing 'amount' field"}), 400

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
            description="Payment for KEVI Technologies e-commerce"
        )

        # Return client secret to the frontend for further processing
        return jsonify({
            "clientSecret": payment_intent["client_secret"]
        })

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle Stripe webhooks for payment events.
    Ensure that webhooks are verified securely.
    """
    # Get webhook payload and headers
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    webhook_secret = "whsec_your_webhook_secret_key_here"  # Replace with your actual webhook secret

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # Handle the event type
        if event["type"] == "payment_intent.succeeded":
            payment_intent = event["data"]["object"]
            print(f"Payment succeeded: {payment_intent['id']}")

        elif event["type"] == "payment_intent.payment_failed":
            payment_intent = event["data"]["object"]
            print(f"Payment failed: {payment_intent['id']}")

        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"})

    except stripe.error.SignatureVerificationError as e:
        # Handle invalid webhook signature
        return jsonify({"error": f"Invalid webhook signature: {str(e)}"}), 400

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": f"Webhook processing error: {str(e)}"}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=False)
```

Note:
1. Replace `STRIPE_SECRET_KEY` and `webhook_secret` with actual keys from your Stripe account.
2. Deploy the Flask app on a secure server (e.g., HTTPS-enabled environment) for production use.
3. Ensure security best practices such as environment variable management for storing sensitive keys.
