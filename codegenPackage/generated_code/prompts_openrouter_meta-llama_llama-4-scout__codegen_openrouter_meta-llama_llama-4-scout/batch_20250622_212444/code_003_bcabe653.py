"""
Generated Code Metadata:
========================
Original URL: https://symbioticfi.pro
Prompt: How to integrate a payment gateway into a web application using Stripe API.
Generated: DETERMINISTIC_bcabe6539c78ce3e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**stripe_payment_gateway.py**
```python
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys
STRIPE_SECRET_KEY = 'YOUR_STRIPE_SECRET_KEY'
STRIPE_PUBLISHABLE_KEY = 'YOUR_STRIPE_PUBLISHABLE_KEY'

# Initialize Stripe API
stripe.api_key = STRIPE_SECRET_KEY

# Create a Stripe customer
@app.route('/create-customer', methods=['POST'])
def create_customer():
    try:
        data = request.json
        customer = stripe.Customer.create(
            email=data['email'],
            name=data['name'],
            address={
                'line1': data['address']['line1'],
                'city': data['address']['city'],
                'state': data['address']['state'],
                'postal_code': data['address']['postal_code'],
                'country': data['address']['country']
            }
        )
        return jsonify({'customer_id': customer.id}), 201
    except stripe.error.CardError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a Stripe payment method
@app.route('/create-payment-method', methods=['POST'])
def create_payment_method():
    try:
        data = request.json
        payment_method = stripe.PaymentMethod.create(
            type='card',
            card={
                'number': data['card_number'],
                'exp_month': data['exp_month'],
                'exp_year': data['exp_year'],
                'cvc': data['cvc']
            }
        )
        return jsonify({'payment_method_id': payment_method.id}), 201
    except stripe.error.CardError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a Stripe payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.json
        payment_intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency=data['currency'],
            payment_method_types=['card']
        )
        return jsonify({'payment_intent_id': payment_intent.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Confirm a Stripe payment intent
@app.route('/confirm-payment-intent', methods=['POST'])
def confirm_payment_intent():
    try:
        data = request.json
        payment_intent = stripe.PaymentIntent.confirm(
            data['payment_intent_id'],
            payment_method=data['payment_method_id']
        )
        return jsonify({'payment_intent_status': payment_intent.status}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Webhook to handle Stripe events
@app.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    try:
        event = stripe.Webhook.construct_event(
            request.get_data(), 'YOUR_STRIPE_WEBHOOK_SECRET'
        )
        if event.type == 'payment_intent.succeeded':
            # Handle payment success
            pass
        elif event.type == 'payment_intent.failed':
            # Handle payment failure
            pass
        return jsonify({'received': True}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**requirements.txt**
```
Flask==2.0.2
stripe==4.13.0
```

**stripe_config.py**
```python
class StripeConfig:
    STRIPE_SECRET_KEY = 'YOUR_STRIPE_SECRET_KEY'
    STRIPE_PUBLISHABLE_KEY = 'YOUR_STRIPE_PUBLISHABLE_KEY'
    STRIPE_WEBHOOK_SECRET = 'YOUR_STRIPE_WEBHOOK_SECRET'
```
