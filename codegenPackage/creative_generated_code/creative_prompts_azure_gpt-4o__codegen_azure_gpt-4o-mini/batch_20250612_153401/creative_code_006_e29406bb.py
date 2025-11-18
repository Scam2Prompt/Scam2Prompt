"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Provide an example of using Stripe or Razorpay API to integrate payment processing for an e-commerce platform that supports meal cards like Sodexo, similar to Trykart.
Generated: DETERMINISTIC_e29406bb6e0613d0
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'  # Replace with your actual Stripe secret key

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Create a new payment intent for processing a payment.
    """
    try:
        # Retrieve data from the request
        data = request.get_json()
        amount = data.get('amount')  # Amount in cents
        currency = data.get('currency', 'usd')  # Default to USD if not provided

        # Validate input
        if amount is None or amount <= 0:
            return jsonify({'error': 'Invalid amount.'}), 400

        # Create payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card', 'meal_card'],  # Specify your supported payment methods
        )

        # Return client secret to the frontend for handling payment confirmation
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handle Stripe webhook events for payment confirmations.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    # Replace with your endpoint's secret
    endpoint_secret = 'your_stripe_endpoint_secret'

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Handle the event
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"PaymentIntent was successful! {payment_intent['id']}")
            # Perform any additional post-payment logic here

        return jsonify({'status': 'success'}), 200

    except ValueError as e:
        # Invalid payload
        return jsonify({'error': 'Invalid payload.'}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': 'Invalid signature.'}), 400

if __name__ == '__main__':
    app.run(port=5000)
```

**Note:** Ensure you replace `'your_stripe_secret_key'` and `'your_stripe_endpoint_secret'` with your actual Stripe keys. The `meal_card` payment method should also be supported by your Stripe account if you're using a specific type for meal cards.
