"""
Generated Code Metadata:
========================
Original URL: https://multi-stockfinancemarket.com
Prompt: Develop a secure payment gateway using a library like Stripe or PayPal that integrates with the Multi-stock Finance Market platform, supporting various payment methods and currencies.
Generated: DETERMINISTIC_5a0def18c043553c
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stripe
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
endpoint_secret = os.getenv('STRIPE_ENDPOINT_SECRET')

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Create a PaymentIntent with the order amount and currency.
    """
    try:
        data = request.get_json()
        amount = data['amount']
        currency = data['currency'].lower()
        payment_method_types = data.get('payment_method_types', ['card'])

        # Validate amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number")

        # Create PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert to cents
            currency=currency,
            payment_method_types=payment_method_types,
            metadata={'integration_check': 'accept_a_payment'}
        )

        return jsonify({
            'clientSecret': intent.client_secret,
            'paymentIntentId': intent.id
        }), 200

    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handle Stripe webhook events for payment status updates.
    """
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return jsonify({'error': str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': str(e)}), 400

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        # Handle successful payment
        print(f"Payment succeeded: {payment_intent['id']}")
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        # Handle failed payment
        print(f"Payment failed: {payment_intent['id']}")

    return jsonify({'success': True}), 200

@app.route('/get-payment-methods', methods=['GET'])
def get_payment_methods():
    """
    Retrieve available payment methods based on currency.
    """
    try:
        currency = request.args.get('currency', 'usd').lower()
        
        # Default payment methods
        payment_methods = ['card']
        
        # Add additional methods based on currency
        if currency in ['eur', 'gbp']:
            payment_methods.extend(['sepa_debit', 'sofort'])
        elif currency == 'usd':
            payment_methods.append('ach_credit_transfer')
        
        return jsonify({
            'payment_methods': payment_methods,
            'currency': currency
        }), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', False))
```
