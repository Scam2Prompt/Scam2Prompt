"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Provide an example of using Stripe API to integrate payment processing for a dental clinic's website, allowing patients to pay for services like same-day crowns or Invisalign treatments online.
Generated: DETERMINISTIC_f191679e02c5f4fb
Batch ID: 20250612_152710
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

# Initialize Flask app
app = Flask(__name__)

# Set your secret key. Remember to switch to your live secret key in production!
# You can find your API keys in your Stripe dashboard.
stripe.api_key = 'sk_test_your_secret_key_here'

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    """
    Creates a PaymentIntent with the specified amount and currency.
    This endpoint should be called when a user initiates a payment for services.
    """
    try:
        # Extract payment details from the request
        data = request.get_json()
        amount = data.get('amount')  # amount in cents
        currency = data.get('currency', 'usd')  # default currency is USD

        # Ensure amount is provided and valid
        if amount is None or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Create a new PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"]  # You can specify additional methods if needed
        )

        # Respond with the client secret of the PaymentIntent
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500


@app.route('/payment-status', methods=['POST'])
def payment_status():
    """
    Endpoint to check the payment status using the PaymentIntent ID. 
    This can be useful for confirming the payment has been successful.
    """
    try:
        data = request.get_json()
        payment_intent_id = data.get('payment_intent_id')

        # Ensure payment_intent_id is provided
        if not payment_intent_id:
            return jsonify({'error': 'PaymentIntent ID is required'}), 400

        # Retrieve the PaymentIntent status
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        return jsonify({
            'status': payment_intent['status']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Notes:
- Ensure you replace `'sk_test_your_secret_key_here'` with your actual Stripe secret key.
- The Flask app runs on port 5000. You can change this as needed.
- You may want to implement additional security measures, such as CORS and input validation, depending on the requirements of your production environment.
