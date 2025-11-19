"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://royaumehotel.com
Prompt: Generate a code snippet for a payment gateway integration that supports secure transactions for an online shop like RHINO88.
Generated: DETERMINISTIC_c0aa3243201505d2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe  # Stripe SDK for payment processing
from flask import Flask, request, jsonify  # Web framework for handling API requests

# Initialize Flask app
app = Flask(__name__)

# Configure Stripe secret key (Replace with your actual secret key)
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
stripe.api_key = STRIPE_SECRET_KEY

# Endpoint for creating payment intent
@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    try:
        # Parse request data
        data = request.json
        if not data or "amount" not in data or "currency" not in data:
            return jsonify({"error": "Invalid request data"}), 400
        
        # Create a PaymentIntent with the specified amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=int(data["amount"]),  # Amount in the smallest unit (e.g., cents for USD)
            currency=data["currency"],  # ISO currency code (e.g., 'usd')
            payment_method_types=["card"],  # Supported payment methods
        )
        return jsonify({
            "clientSecret": payment_intent["client_secret"]  # Return client secret to the frontend
        })
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An error occurred"}), 500

# Endpoint for webhook to handle payment events
@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    # Webhook secret (configure this in your Stripe dashboard)
    WEBHOOK_SECRET = "whsec_YourWebhookSecretKey"

    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        return jsonify({"error": "Invalid signature"}), 400

    # Handle specific Stripe events (e.g., payment success)
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        print(f"Payment succeeded for: {payment_intent['id']}")
        # Handle post-payment actions (e.g., order fulfillment)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    # Run the Flask app
    app.run(port=5000)
```

**Notes:**
1. Replace `STRIPE_SECRET_KEY` and `WEBHOOK_SECRET` with the actual credentials from your Stripe dashboard.
2. Make sure the webhook URL is registered in Stripe and uses HTTPS in production.
3. Secure your API keys and sensitive information using environment variables or secret management tools.
4. Test thoroughly in both development and production environments.
