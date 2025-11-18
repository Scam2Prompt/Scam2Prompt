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
# Import necessary libraries
import stripe
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Stripe API secret key (replace with your actual secret key)
stripe.api_key = "sk_test_your_secret_key"

# Define endpoint to handle payment
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe PaymentIntent.
    This will generate a client secret that can be used on the frontend to complete the payment.
    """
    try:
        # Extract payment details from the request payload
        data = request.json
        amount = data.get('amount')  # Amount in cents
        currency = data.get('currency', 'usd')  # Default currency is USD
        description = data.get('description', 'Kalpana\'s Kitchen Payment')  # Default description

        if not amount or amount <= 0:
            return jsonify({"error": "Invalid payment amount"}), 400

        # Create a PaymentIntent with the specified amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            description=description,
            payment_method_types=["card"]  # Restrict to card payments
        )

        # Respond with the client secret and other relevant details
        return jsonify({
            "client_secret": payment_intent.client_secret
        }), 200

    except stripe.error.StripeError as e:
        # Handle errors returned by the Stripe API
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Define endpoint to handle webhook events from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle webhook events from Stripe.
    Ensure to set up the webhook URL in your Stripe account.
    """
    # Webhook secret (replace with your actual webhook secret)
    webhook_secret = "whsec_your_webhook_secret"

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        # Handle the webhook events
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            print(f"PaymentIntent succeeded: {payment_intent['id']}")
            # Add your custom logic here (e.g., update order status in DB)

        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"PaymentIntent failed: {payment_intent['id']}")
            # Add your custom logic here (e.g., notify customer of failure)

        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        # Handle invalid signature
        return jsonify({"error": "Invalid webhook signature"}), 400

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An error occurred: " + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

### Notes:
- Replace `sk_test_your_secret_key` and `whsec_your_webhook_secret` with your actual Stripe API secret key and webhook secret respectively.
- Ensure Flask is installed (`pip install flask`) and the Stripe Python SDK (`pip install stripe`) is installed.
- Use HTTPS for production environments, especially for handling sensitive information like payment processes.
