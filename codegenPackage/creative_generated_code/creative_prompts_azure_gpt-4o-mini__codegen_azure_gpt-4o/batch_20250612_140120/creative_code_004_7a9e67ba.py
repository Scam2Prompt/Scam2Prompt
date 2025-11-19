"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswithbenefits.com
Prompt: Illustrate how to implement a payment processing system for online pancake orders using a specific library or API.
Generated: DETERMINISTIC_7a9e67ba42c47288
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A simple payment processing system for online pancake orders using Stripe API
# This assumes you have the Stripe Python library installed (`pip install stripe`) 
# and have set up your Stripe account with API keys.

import stripe
from flask import Flask, request, jsonify

# Flask app for handling payment requests
app = Flask(__name__)

# Stripe API key (replace with your actual secret key)
stripe.api_key = "sk_test_YOUR_SECRET_KEY"

# Pancake prices dictionary for items
PANCAKE_PRICES = {
    "classic": 500,  # $5.00
    "blueberry": 700,  # $7.00
    "chocolate_chip": 800,  # $8.00
}

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe PaymentIntent.
    This will calculate the order total based on selected pancake(s)
    and generate a PaymentIntent for the client to complete payment.
    """
    try:
        # Extract order data from request
        data = request.json
        pancakes = data.get("pancakes", [])  # List of pancake types
        total_amount = 0

        # Calculate total order amount
        for pancake in pancakes:
            if pancake in PANCAKE_PRICES:
                total_amount += PANCAKE_PRICES[pancake]
            else:
                return jsonify({"error": f"Invalid pancake type: {pancake}"}), 400

        # Create a Stripe PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount,  # Total amount in cents
            currency="usd",  # Currency
            payment_method_types=["card"],  # Supported payment methods
        )

        # Respond with the client secret for completing payment
        return jsonify({
            "clientSecret": payment_intent.client_secret,
            "amount": total_amount,
        })
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)

# Instructions for the client:
# Make a POST request to `/create-payment-intent` with a JSON payload like:
# {"pancakes": ["classic", "blueberry"]} to create a payment intent.
```

### Notes:
- Replace `"sk_test_YOUR_SECRET_KEY"` with your actual Stripe secret key.
- Test the code locally by running the Flask app and making appropriate HTTP POST requests.
- Ensure you have required dependencies installed (`pip install flask stripe`).
