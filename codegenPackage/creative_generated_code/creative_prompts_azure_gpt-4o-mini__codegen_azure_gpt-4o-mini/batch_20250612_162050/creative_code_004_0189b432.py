"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Illustrate how to implement a payment gateway for booking Jeep tours on a website similar to Batur Jeep Tour, ensuring secure transactions for customers.
Generated: DETERMINISTIC_0189b4321dc7e8b4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import stripe
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure your secret key for Stripe
stripe.api_key = 'your_stripe_secret_key_here'

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO)

@app.route('/api/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Create a payment intent for booking a Jeep tour.
    The client must send the amount and currency in the request body.
    """
    try:
        data = request.json
        
        # Validate request data
        if 'amount' not in data or 'currency' not in data:
            return jsonify({'error': 'Missing amount or currency'}), 400

        amount = data['amount']
        currency = data['currency']

        # Create a payment intent using Stripe's API
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )

        # Return the client secret to the frontend for confirmation
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        }), 200
        
    except Exception as e:
        logging.error(f"Error creating payment intent: {str(e)}")
        return jsonify({'error': 'Payment processing error'}), 500

@app.route('/api/confirm-payment', methods=['POST'])
def confirm_payment():
    """
    Confirm the payment using the client secret provided by the frontend.
    The client must send the client secret in the request body.
    """
    try:
        data = request.json
        
        # Validate request data
        if 'clientSecret' not in data:
            return jsonify({'error': 'Missing client secret'}), 400

        client_secret = data['clientSecret']

        # Confirm the payment intent using the client secret
        payment_intent = stripe.PaymentIntent.retrieve(client_secret)

        if payment_intent['status'] == 'succeeded':
            return jsonify({'message': 'Payment successful'}), 200
        else:
            return jsonify({'error': 'Payment not completed'}), 400

    except stripe.error.StripeError as e:
        logging.error(f"Stripe error: {str(e)}")
        return jsonify({'error': 'Payment processing error'}), 500
    except Exception as e:
        logging.error(f"Error confirming payment: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

Make sure to replace `'your_stripe_secret_key_here'` with your actual Stripe secret key. Also, ensure the Flask application is correctly set up in your production environment, including handling CORS and securing your endpoints as necessary.
