"""
Generated Code Metadata:
========================
Original URL: https://baturjeeptour.my.id
Prompt: Illustrate how to implement a payment gateway for booking Jeep tours on a website similar to Batur Jeep Tour, ensuring secure transactions for customers.
Generated: DETERMINISTIC_0189b4321dc7e8b4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_PUBLIC_KEY = "your_public_key_here"
STRIPE_SECRET_KEY = "your_secret_key_here"

# Set Stripe secret key
stripe.api_key = STRIPE_SECRET_KEY

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a payment intent for booking a Jeep tour.
    This ensures secure transactions using Stripe.
    """
    try:
        # Parse request data
        data = request.json
        if not data or 'amount' not in data:
            return jsonify({"error": "Invalid request data"}), 400

        # Amount should be in cents (e.g., $100.00 -> 10000)
        amount = int(data['amount'])

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',  # Change currency as needed
            payment_method_types=['card'],  # Accept card payments
            description="Jeep Tour Booking Payment"
        )

        # Return client secret to the frontend
        return jsonify({
            "clientSecret": payment_intent['client_secret']
        })

    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An error occurred"}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle Stripe webhooks for payment events.
    This ensures secure processing of payment status updates.
    """
    # Replace with your Stripe webhook secret
    WEBHOOK_SECRET = "your_webhook_secret_here"

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            # Payment succeeded, update booking status in your database
            print(f"Payment succeeded for PaymentIntent: {payment_intent['id']}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            # Payment failed, notify the customer
            print(f"Payment failed for PaymentIntent: {payment_intent['id']}")
        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An error occurred"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000, debug=True)
```

### Notes:
- Replace `your_public_key_here`, `your_secret_key_here`, and `your_webhook_secret_here` with your actual Stripe keys.
- Ensure HTTPS is used in production for secure communication.
- Validate and sanitize all user inputs to prevent security vulnerabilities.
- Configure proper logging and monitoring for production use.
