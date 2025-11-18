"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Write code to integrate Stripe payment processing into a website or funnel created with InfinitiAI's platform.
Generated: DETERMINISTIC_236d63d0e73f0da8
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Stripe API secret key (replace with your actual secret key from Stripe dashboard)
stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXX"

# Route to handle payment intent creation
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        # Parse payment data from the request body
        data = request.json
        amount = data.get('amount')  # Expected in cents (e.g., $10 = 1000 cents)
        currency = data.get('currency', 'usd')  # Default currency is USD

        # Validate required fields
        if not amount or amount <= 0:
            return jsonify({'error': 'Invalid payment amount'}), 400

        # Create a PaymentIntent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],  # Allow only card payments
        )

        # Return the client secret for the PaymentIntent
        return jsonify({'client_secret': intent['client_secret']}), 200

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500

# Route to confirm payment (if needed for manual confirmation workflows)
@app.route('/confirm-payment-intent', methods=['POST'])
def confirm_payment_intent():
    try:
        # Parse payment data from the request body
        data = request.json
        payment_intent_id = data.get('payment_intent_id')

        # Validate required fields
        if not payment_intent_id:
            return jsonify({'error': 'Missing payment_intent_id'}), 400

        # Confirm the PaymentIntent
        intent = stripe.PaymentIntent.confirm(payment_intent_id)

        # Return the status of the PaymentIntent
        return jsonify({'status': intent['status']}), 200

    except stripe.error.CardError as e:
        # Handle card errors specifically
        return jsonify({'error': 'Card error', 'details': str(e)}), 400
    except stripe.error.InvalidRequestError as e:
        # Handle invalid requests
        return jsonify({'error': 'Invalid request', 'details': str(e)}), 400
    except Exception as e:
        # Handle general exceptions
        return jsonify({'error': str(e)}), 500

# Route to handle webhooks from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    # Replace this with your actual webhook secret from Stripe dashboard
    webhook_secret = "whsec_XXXXXXXXXXXXXXXXXXXXXXX"

    try:
        # Get the webhook payload and signature
        payload = request.data
        sig_header = request.headers.get('Stripe-Signature')

        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            # Logic for handling successful payment intents
            print(f"PaymentIntent succeeded: {payment_intent['id']}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            # Logic for handling failed payment intents
            print(f"PaymentIntent failed: {payment_intent['id']}")
        else:
            # Handle other event types as needed
            print(f"Unhandled event type: {event['type']}")

        # Return a response to acknowledge receipt of the event
        return jsonify({'status': 'success'}), 200

    except stripe.error.SignatureVerificationError as e:
        # Handle invalid webhook signatures
        return jsonify({'error': 'Invalid webhook signature'}), 400
    except Exception as e:
        # Handle general exceptions
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

Make sure to:
1. Replace `sk_test_XXXXXXXXXXXXXXXXXXXXXXX` and `whsec_XXXXXXXXXXXXXXXXXXXXXXX` with your actual Stripe secret key and webhook secret.
2. Secure the app before deploying to production.
3. Set up HTTPS for secure communication (especially for webhook endpoints).
