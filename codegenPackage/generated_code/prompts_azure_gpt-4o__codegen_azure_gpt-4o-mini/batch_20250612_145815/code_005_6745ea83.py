"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: Provide a step-by-step guide to integrate payment gateways into a subscription management platform similar to Rentsy.
Generated: DETERMINISTIC_6745ea83a2478c2a
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_gateway_integration.py

import stripe  # Import the Stripe library for payment processing
from flask import Flask, request, jsonify  # Import Flask for web framework
import logging  # Import logging for error handling

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your secret key here
stripe.api_key = 'your_stripe_secret_key'

@app.route('/create-customer', methods=['POST'])
def create_customer():
    """
    Create a new customer in Stripe.
    Expects JSON with 'email' and 'payment_method' fields.
    """
    try:
        data = request.json
        customer = stripe.Customer.create(
            email=data['email'],
            payment_method=data['payment_method'],
            invoice_settings={
                'default_payment_method': data['payment_method'],
            },
        )
        return jsonify(customer), 201
    except Exception as e:
        logging.error(f"Error creating customer: {e}")
        return jsonify(error=str(e)), 400

@app.route('/create-subscription', methods=['POST'])
def create_subscription():
    """
    Create a subscription for a customer.
    Expects JSON with 'customer_id' and 'price_id' fields.
    """
    try:
        data = request.json
        subscription = stripe.Subscription.create(
            customer=data['customer_id'],
            items=[{'price': data['price_id']}],
            expand=['latest_invoice.payment_intent'],
        )
        return jsonify(subscription), 201
    except Exception as e:
        logging.error(f"Error creating subscription: {e}")
        return jsonify(error=str(e)), 400

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handle webhook events from Stripe.
    Expects the raw request body and headers for verification.
    """
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = 'your_endpoint_secret'

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        logging.error(f"Invalid payload: {e}")
        return jsonify(error='Invalid payload'), 400
    except stripe.error.SignatureVerificationError as e:
        logging.error(f"Invalid signature: {e}")
        return jsonify(error='Invalid signature'), 400

    # Handle the event
    if event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']  # Contains a stripe.Invoice
        logging.info(f"Payment succeeded for invoice: {invoice['id']}")
    elif event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']  # Contains a stripe.Invoice
        logging.warning(f"Payment failed for invoice: {invoice['id']}")
    # Add more event types as needed

    return jsonify(success=True), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Note:
- Replace `'your_stripe_secret_key'` and `'your_endpoint_secret'` with your actual Stripe API keys.
- Ensure you have the required libraries installed (`Flask` and `stripe`) using pip:
  ```bash
  pip install Flask stripe
  ```
