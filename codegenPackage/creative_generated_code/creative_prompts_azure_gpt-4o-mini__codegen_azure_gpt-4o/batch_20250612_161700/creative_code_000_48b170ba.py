"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: How can I implement a donation API for a non-profit organization like Amma Parivaar Orphanage to facilitate online contributions?
Generated: DETERMINISTIC_48b170ba10b8dd64
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# donation_api.py

from flask import Flask, request, jsonify
import stripe
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Stripe API key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Health Check Endpoint
@app.route("/health", methods=["GET"])
def health_check():
    """
    Endpoint to check if the API is running.
    """
    return jsonify({"status": "OK"}), 200

# Donation Endpoint
@app.route("/donate", methods=["POST"])
def donate():
    """
    Endpoint to process donations using Stripe.
    Expects a JSON payload with:
    - `email`: donor's email
    - `amount`: donation amount in cents (integer)
    - `currency`: currency code (default: 'usd')
    """
    try:
        # Parse JSON request data
        data = request.json

        # Validate input data
        email = data.get("email")
        amount = data.get("amount")
        currency = data.get("currency", "usd")  # Default to USD

        if not email or not amount:
            return jsonify({"error": "Email and amount are required"}), 400
        
        if not isinstance(amount, int) or amount <= 0:
            return jsonify({"error": "Amount must be a positive integer"}), 400

        # Create Stripe PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            receipt_email=email,
            description="Donation to Amma Parivaar Orphanage"
        )

        logging.info(f"Payment Intent created successfully for email: {email}, amount: {amount}")

        # Respond with client secret to complete the payment on the frontend
        return jsonify({
            "client_secret": payment_intent.client_secret,
            "message": "Payment initiated successfully"
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        logging.error(f"Stripe error: {e}")
        return jsonify({"error": "Payment processing failed. Please try again later."}), 500

    except Exception as e:
        # Catch-all error handling
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == "__main__":
    # Ensure the Stripe API key is set
    if not stripe.api_key:
        logging.critical("Stripe API key is missing. Please set it in the .env file.")
        raise EnvironmentError("Stripe API key is not configured")

    # Start the Flask server
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- To use this code, you'll need Python installed along with the `Flask`, `stripe`, and `python-dotenv` libraries (`pip install flask stripe python-dotenv`).
- Create a `.env` file in the project directory with the following content:
  ```
  STRIPE_SECRET_KEY=your_stripe_secret_key
  ```
