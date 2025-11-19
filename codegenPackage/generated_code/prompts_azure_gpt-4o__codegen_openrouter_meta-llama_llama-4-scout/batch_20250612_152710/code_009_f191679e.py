"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Provide an example of using Stripe API to integrate payment processing for a dental clinic's website, allowing patients to pay for services like same-day crowns or Invisalign treatments online.
Generated: DETERMINISTIC_f191679e02c5f4fb
Batch ID: 20250612_152710
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/create-payment-intent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/confirm-payment-intent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set Stripe API keys
stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'
stripe.api_version = '2022-11-15'

# Define a function to create a payment intent
def create_payment_intent(amount, currency, payment_method_types):
    """
    Create a PaymentIntent with the specified amount, currency, and payment method types.

    Args:
        amount (int): The amount to charge in cents.
        currency (str): The currency to charge in (e.g. 'usd').
        payment_method_types (list): A list of payment method types (e.g. ['card']).

    Returns:
        dict: The created PaymentIntent.
    """
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=payment_method_types
        )
        return payment_intent
    except stripe.error.CardError as e:
        # Handle card errors
        return {'error': str(e)}
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return {'error': str(e)}
    except Exception as e:
        # Handle other exceptions
        return {'error': str(e)}

# Define a function to retrieve a payment intent
def retrieve_payment_intent(payment_intent_id):
    """
    Retrieve a PaymentIntent by its ID.

    Args:
        payment_intent_id (str): The ID of the PaymentIntent to retrieve.

    Returns:
        dict: The retrieved PaymentIntent.
    """
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return payment_intent
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return {'error': str(e)}
    except Exception as e:
        # Handle other exceptions
        return {'error': str(e)}

# Define a route to create a payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing request data'}), 400

    amount = data.get('amount')
    currency = data.get('currency', 'usd')
    payment_method_types = data.get('payment_method_types', ['card'])

    if not amount:
        return jsonify({'error': 'Missing amount'}), 400

    payment_intent = create_payment_intent(amount, currency, payment_method_types)
    if 'error' in payment_intent:
        return jsonify(payment_intent), 400

    return jsonify(payment_intent)

# Define a route to confirm a payment intent
@app.route('/confirm-payment-intent', methods=['POST'])
def confirm_payment_intent_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing request data'}), 400

    payment_intent_id = data.get('payment_intent_id')
    if not payment_intent_id:
        return jsonify({'error': 'Missing payment intent ID'}), 400

    try:
        payment_intent = stripe.PaymentIntent.confirm(
            payment_intent_id,
            payment_method=data.get('payment_method_id')
        )
        return jsonify(payment_intent)
    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({'error': str(e)}), 400
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**Example Usage:**

Create a payment intent:
```bash
curl -X POST \
  http://localhost:5000/create-payment-intent \
  -H 'Content-Type: application/json' \
  -d '{"amount": 1000, "currency": "usd", "payment_method_types": ["card"]}'
```

Confirm a payment intent:
```bash
curl -X POST \
  http://localhost:5000/confirm-payment-intent \
  -H 'Content-Type: application/json' \
  -d '{"payment_intent_id": "pi_123456789", "payment_method_id": "pm_123456789"}'
```
