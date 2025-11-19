"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vidhyaclinic.com
Prompt: How can I implement a secure payment system for a betting platform similar to those listed on vidhyaclinic.com?
Generated: DETERMINISTIC_2c2354427ed20761
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
import stripe
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Set Stripe API key from environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Ensure Stripe API key is set
if not stripe.api_key:
    raise EnvironmentError("Stripe Secret Key not found in environment variables.")

# Set up Flask route for payment processing
@app.route('/process_payment', methods=['POST'])
def process_payment():
    """
    Endpoint to process payment securely via Stripe.
    Expects a JSON payload with 'amount' and 'currency'.
    """
    try:
        # Parse request data
        data = request.json

        # Validate input data
        if not data or 'amount' not in data or 'currency' not in data:
            return jsonify({"error": "Invalid request payload"}), 400
        amount = data['amount']
        currency = data['currency']

        if not isinstance(amount, int) or amount <= 0:
            return jsonify({"error": "Amount must be a positive integer"}), 400
        if not isinstance(currency, str) or len(currency) != 3:
            return jsonify({"error": "Currency must be a 3-letter code"}), 400

        # Create a payment intent using Stripe API
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],  # Restrict to card payments
        )

        # Return client_secret to client for payment confirmation
        return jsonify({
            "client_secret": payment_intent['client_secret'],
        })
    except stripe.error.StripeError as e:
        # Catch Stripe-specific errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Catch all other errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Main block to run Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Requirements:
1. Install dependencies: `pip install flask stripe python-dotenv`
2. Create a `.env` file to store your Stripe secret key (`STRIPE_SECRET_KEY`). Example:
   ```
   STRIPE_SECRET_KEY=sk_test_XXXXXXXXXXXXXXXXXXXXXXXX
   ```
