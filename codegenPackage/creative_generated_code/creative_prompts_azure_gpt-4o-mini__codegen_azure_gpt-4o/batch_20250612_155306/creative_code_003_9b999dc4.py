"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioti.fi
Prompt: Develop a code snippet that integrates a payment gateway for domain purchases, ensuring safe and secure transactions as highlighted on the symbioti.fi webpage.
Generated: DETERMINISTIC_9b999dc451d3dc00
Batch ID: 20250612_155306
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com/cancel": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import stripe  # Stripe is used as the payment gateway in this example
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure Stripe API keys (use environment variables in production)
STRIPE_SECRET_KEY = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"
STRIPE_PUBLIC_KEY = "pk_test_XXXXXXXXXXXXXXXXXXXXXXXX"
stripe.api_key = STRIPE_SECRET_KEY

# Define available domains for purchase
AVAILABLE_DOMAINS = {
    "example.com": 1000,  # price in cents ($10)
    "testsite.com": 1500,  # price in cents ($15)
    "symbioti.fi": 2500,  # price in cents ($25)
}

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """
    Handle the creation of a Stripe Checkout session for domain purchases.
    """
    try:
        # Parse requested domain from incoming JSON payload
        data = request.get_json()
        domain_name = data.get('domain_name')

        # Ensure the domain name is available for purchase
        if domain_name not in AVAILABLE_DOMAINS:
            return jsonify({"error": "Domain not available for purchase."}), 400

        # Create a Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],  # Accept credit cards
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': domain_name,
                    },
                    'unit_amount': AVAILABLE_DOMAINS[domain_name],
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://yourdomain.com/cancel',
        )

        # Return the session ID to the client
        return jsonify({"session_id": session.id})

    except stripe.error.StripeError as e:
        # General Stripe error handling
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Handle Stripe webhook events for payment confirmations.
    """
    endpoint_secret = "whsec_XXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual endpoint secret

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)

        # Handle specific event types
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            domain_name = session['display_items'][0]['custom']['name']

            # Here you can mark the domain as sold in your database or notify the user
            print(f"Payment successful for domain: {domain_name}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        # Handle invalid webhook signatures
        return jsonify({"error": "Invalid signature"}), 400

    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Run the Flask app on default port 5000
    app.run(debug=True)
```
