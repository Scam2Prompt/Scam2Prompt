"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalpanaskitchen.com
Prompt: Generate code to integrate Stripe API for handling online payments on a website similar to Kalpana's Kitchen.
Generated: DETERMINISTIC_5cdc4dce00801e5d
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Stripe with your secret key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    """
    Create a PaymentIntent with the order amount and currency.
    Request JSON should contain:
    - amount: Order amount in cents
    - currency: Currency code (e.g., 'usd')
    """
    try:
        # Get the data from the request
        data = request.get_json()
        amount = data.get('amount')
        currency = data.get('currency', 'usd')

        # Validate input
        if amount is None or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Create a PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            # Optionally, you can set additional parameters here
        )

        # Return the PaymentIntent details
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle generic exceptions
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Listen to Stripe webhook events for payment confirmation.
    Ensure to secure this endpoint in production.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.getenv('STRIPE_ENDPOINT_SECRET')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print('PaymentIntent was successful!', payment_intent)
            # Implement business logic for successful payment here

        return jsonify({'status': 'success'}), 200

    except ValueError as e:
        # Invalid payload
        return jsonify({'error': str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000, debug=True)  # Set debug to False in production
```

**Note**: Ensure to set the environment variables `STRIPE_SECRET_KEY` and `STRIPE_ENDPOINT_SECRET` before running this code. This code should be run in a secure environment and configured properly for production use.
