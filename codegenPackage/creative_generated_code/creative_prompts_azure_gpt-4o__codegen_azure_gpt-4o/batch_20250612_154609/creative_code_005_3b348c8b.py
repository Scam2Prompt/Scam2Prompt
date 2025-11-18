"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Provide code to integrate a donation or funding system for initiatives like the Idaho Prosperity Fund, ensuring secure transactions and tracking contributions.
Generated: DETERMINISTIC_3b348c8b7df400e1
Batch ID: 20250612_154609
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

app = Flask(__name__)

# Stripe API keys (use environment variables in production for security)
STRIPE_SECRET_KEY = "your_secret_key_here"
STRIPE_PUBLIC_KEY = "your_public_key_here"

# Initialize Stripe with the secret key
stripe.api_key = STRIPE_SECRET_KEY

# Error message constants
ERROR_INVALID_INPUT = "Invalid input. Please ensure all required fields are provided."
ERROR_STRIPE_PAYMENT_FAILED = "Payment failed. Please try again later."

# Donation tracking dictionary (use a database in production)
donation_records = {}

@app.route('/donate', methods=['POST'])
def donate():
    """
    Endpoint to handle donation requests.
    Expects a JSON payload with `amount`, `currency`, and `email`.
    """
    try:
        data = request.json
        # Validate input data
        if 'amount' not in data or 'currency' not in data or 'email' not in data:
            return jsonify({"error": ERROR_INVALID_INPUT}), 400

        # Extract data
        amount = int(data['amount'])  # Amount in cents
        currency = data['currency']  # e.g., 'usd'
        email = data['email']

        # Create a PaymentIntent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            receipt_email=email,
            description="Donation to Idaho Prosperity Fund",
        )

        # Return the client secret to the frontend for further processing
        return jsonify({"client_secret": payment_intent['client_secret']}), 200

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": ERROR_STRIPE_PAYMENT_FAILED, "details": str(e)}), 500
    except Exception as e:
        # Handle generic exceptions
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/track_donations', methods=['POST'])
def track_donations():
    """
    Endpoint to track donations. Updates the donation record after payment confirmation.
    Expects a JSON payload with `email` and `amount`.
    """
    try:
        data = request.json
        # Validate input data
        if 'email' not in data or 'amount' not in data:
            return jsonify({"error": ERROR_INVALID_INPUT}), 400

        email = data['email']
        amount = int(data['amount'])

        # Update donation records
        if email in donation_records:
            donation_records[email] += amount
        else:
            donation_records[email] = amount

        return jsonify({"message": "Donation tracked successfully.", "total_donations": donation_records[email]}), 200

    except Exception as e:
        # Handle generic exceptions
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/get_donation_summary', methods=['GET'])
def get_donation_summary():
    """
    Endpoint to retrieve donation summary.
    Returns the total donations for each email.
    """
    try:
        return jsonify(donation_records), 200

    except Exception as e:
        # Handle generic exceptions
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app (use a production WSGI server like Gunicorn or uWSGI for deployment)
    app.run(debug=True)  # Disable debug mode in production
```

### Notes:
- Replace `your_secret_key_here` and `your_public_key_here` with actual Stripe keys.
- Use environment variables or a secure secrets manager to store sensitive keys in production.
- Replace the in-memory `donation_records` dictionary with a database for scalability and persistence.
