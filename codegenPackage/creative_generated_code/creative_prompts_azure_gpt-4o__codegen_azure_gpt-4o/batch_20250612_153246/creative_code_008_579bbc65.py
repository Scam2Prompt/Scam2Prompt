"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Write code to integrate a payment gateway into a holistic therapy website for services like pregnancy massage and custom therapies, ensuring secure transactions.
Generated: DETERMINISTIC_579bbc65238e997a
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com/cancel": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.com/success?session_id={CHECKOUT_SESSION_ID": {
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
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe configuration
stripe.api_key = "sk_test_your_secret_key"  # Replace with your actual Stripe secret key

# Prices for services (in cents)
SERVICE_PRICES = {
    "pregnancy_massage": 10000,  # $100.00
    "custom_therapy": 15000      # $150.00
}

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """
    Endpoint to create a Stripe Checkout Session for payment processing.
    Expects JSON payload with 'service' and 'email'.
    """
    try:
        # Parse request data
        data = request.json
        service = data.get("service")
        email = data.get("email")

        # Validate service
        if service not in SERVICE_PRICES:
            return jsonify({"error": "Invalid service selected"}), 400

        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': service.replace("_", " ").title()
                    },
                    'unit_amount': SERVICE_PRICES[service],
                },
                'quantity': 1,
            }],
            mode='payment',
            customer_email=email,
            success_url='https://yourwebsite.com/success?session_id={CHECKOUT_SESSION_ID}',  # Replace with your success URL
            cancel_url='https://yourwebsite.com/cancel',  # Replace with your cancel URL
        )

        # Return the session ID for client-side use
        return jsonify({"sessionId": session.id})
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": f"Stripe error: {str(e)}"}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint for Stripe Webhooks to handle payment events securely.
    """
    # Replace with your Stripe webhook secret
    webhook_secret = "whsec_your_webhook_secret"

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # Process the event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            print(f"Payment was successful for session: {session['id']}")  # Replace with actual handling logic

        return jsonify({"status": "success"}), 200
    except ValueError:
        # Invalid payload
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

Note:
- Replace placeholders like `sk_test_your_secret_key`, `whsec_your_webhook_secret`, and URLs with actual values before deploying.
- Ensure your server runs securely in production (e.g., use HTTPS).
- Test thoroughly before deployment.
