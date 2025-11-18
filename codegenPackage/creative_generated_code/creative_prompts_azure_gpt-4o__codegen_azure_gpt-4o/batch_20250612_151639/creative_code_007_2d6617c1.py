"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiodigital.live
Prompt: Write code to create a secure payment gateway for purchasing digital products like the "Corporate Trainer Toolkit" from Spec Digital Sales.
Generated: DETERMINISTIC_2d6617c177f63fe9
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation of a secure payment gateway using Flask. For production use, you would need to configure proper security measures such as HTTPS, secure API keys, and compliance with PCI DSS standards.

```python
# payment_gateway.py

from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Stripe API keys (replace with your actual keys; keep them secret)
STRIPE_SECRET_KEY = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
STRIPE_PUBLIC_KEY = 'pk_test_TYooMQauvdEDq54NiTphI7jx'

stripe.api_key = STRIPE_SECRET_KEY

# Product details (example: Corporate Trainer Toolkit)
PRODUCTS = {
    "corporate_trainer_toolkit": {
        "name": "Corporate Trainer Toolkit",
        "price_cents": 5000,  # Price in cents ($50.00)
        "currency": "usd"
    }
}

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Creates a Stripe Payment Intent for the specified product.
    """
    try:
        data = request.json
        product_id = data.get('product_id')

        if not product_id or product_id not in PRODUCTS:
            return jsonify({"error": "Invalid product ID"}), 400

        product = PRODUCTS[product_id]

        # Create a PaymentIntent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=product["price_cents"],
            currency=product["currency"],
            payment_method_types=["card"]
        )

        return jsonify({
            "client_secret": payment_intent.client_secret
        })
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Handles Stripe webhook events for payment updates.
    """
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = 'whsec_test_secret'  # Replace with your webhook signing secret

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        # Handle specific event types (e.g., payment success)
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"Payment for {payment_intent['amount']} succeeded.")

        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"Payment failed: {payment_intent['last_payment_error']['message']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


if __name__ == '__main__':
    # Use "ssl_context='adhoc'" for HTTPS in development; configure proper SSL in production.
    app.run(host='0.0.0.0', port=5000)
```

**Setup Instructions:**
1. Install dependencies:
   ```bash
   pip install flask stripe
   ```

2. Replace `STRIPE_SECRET_KEY`, `STRIPE_PUBLIC_KEY`, and `webhook_secret` with your actual Stripe credentials.

3. Run the Flask app:
   ```bash
   python payment_gateway.py
   ```

4. Use HTTPS in production and ensure compliance with PCI DSS standards.
