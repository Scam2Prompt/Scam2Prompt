"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babylnon.foundation
Prompt: Generate a code snippet that demonstrates how to implement a secure payment system for domain purchases similar to the one described on babylnon.foundation.
Generated: DETERMINISTIC_06a132ce6c2d01d3
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_PUBLIC_KEY = "your_public_key_here"
STRIPE_SECRET_KEY = "your_secret_key_here"

# Configure Stripe with the secret key
stripe.api_key = STRIPE_SECRET_KEY

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a payment intent for purchasing a domain.
    Expects a JSON payload with { "domain_name": string, "price": float }
    """
    try:
        # Get the domain details from the request
        data = request.json
        if not data or 'domain_name' not in data or 'price' not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        domain_name = data['domain_name']
        price = data['price']

        # Convert price to cents (Stripe requires amounts in cents)
        amount = int(price * 100)

        # Create a payment intent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",  # Change currency as needed
            metadata={"domain_name": domain_name},
        )

        # Return the client secret and other details to the frontend
        return jsonify({
            "clientSecret": payment_intent['client_secret'],
            "domainName": domain_name,
            "amount": amount
        })

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle webhook events from Stripe.
    Ensure you configure this endpoint in your Stripe dashboard.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = "your_webhook_secret_here"  # Replace with your actual webhook secret

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            domain_name = payment_intent['metadata']['domain_name']
            print(f"Payment succeeded for domain: {domain_name}")
            # You can now handle domain registration or related processes

        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            domain_name = payment_intent['metadata']['domain_name']
            print(f"Payment failed for domain: {domain_name}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Notes:
- Replace `your_public_key_here`, `your_secret_key_here`, and `your_webhook_secret_here` with your actual Stripe API keys.
- Ensure proper security measures (e.g., HTTPS) are in place for production use.
- Configure the `/webhook` endpoint in the Stripe dashboard and only accept requests from Stripe.
