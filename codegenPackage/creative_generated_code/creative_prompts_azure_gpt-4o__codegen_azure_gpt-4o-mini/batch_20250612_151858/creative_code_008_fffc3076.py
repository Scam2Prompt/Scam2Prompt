"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Generate a Python script using the Stripe API to implement flexible payment options for an e-commerce site, allowing customers to pay for branded fashion items with multiple credit cards, as offered on brandsoutlet.qa.
Generated: DETERMINISTIC_fffc30760f6428f6
Batch ID: 20250612_151858
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

# Set your Stripe secret key
stripe.api_key = 'sk_test_your_secret_key_here'

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Create a PaymentIntent to handle the payment for the order.
    """
    try:
        # Get amount and currency from the request body
        data = request.get_json()
        amount = data['amount']  # Amount should be in cents
        currency = data['currency']  # e.g., 'usd'

        # Create a PaymentIntent with the specified amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )

        # Return the client secret for the PaymentIntent
        return jsonify({'clientSecret': payment_intent['client_secret']}), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An error occurred while creating the payment intent.'}), 500

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Handle events sent from Stripe.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = 'whsec_your_webhook_secret_here'

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Handle the event based on its type
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
            print(f"PaymentIntent was successful! ID: {payment_intent['id']}")
        # Handle other event types here if needed

        return jsonify({'status': 'success'}), 200

    except ValueError as e:
        # Invalid payload
        return jsonify({'error': 'Invalid payload.'}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': 'Invalid signature.'}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An error occurred while processing the webhook.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

Ensure you replace `'sk_test_your_secret_key_here'` and `'whsec_your_webhook_secret_here'` with your actual Stripe API key and webhook secret. This code defines a simple Flask application with endpoints to create a payment intent and handle Stripe webhooks.
