"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eldoraa.com
Prompt: Illustrate how to implement a secure payment process for online purchases similar to what is offered on Eldoraa.com.
Generated: DETERMINISTIC_05799e207f6dc326
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe  # Stripe SDK for secure payment processing
import logging  # For logging errors and events
from flask import Flask, request, jsonify  # Web framework for handling HTTP requests
from dotenv import load_dotenv  # To load environment variables
import os  # To access environment variables

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Set up Stripe API key securely from environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Route for handling payment processing
@app.route('/process-payment', methods=['POST'])
def process_payment():
    """
    Endpoint to process online payments using Stripe.
    Expects a JSON payload with:
    - amount: The payment amount in cents (integer).
    - currency: The three-letter currency code (e.g., 'usd').
    - payment_method_id: The Stripe payment method ID.
    """
    try:
        # Parse the JSON payload from the request
        data = request.get_json()
        amount = data.get('amount')
        currency = data.get('currency')
        payment_method_id = data.get('payment_method_id')

        # Validate input data
        if amount is None or currency is None or payment_method_id is None:
            return jsonify({"error": "Invalid request. Missing required fields."}), 400

        # Create a PaymentIntent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,  # Payment amount in cents
            currency=currency,  # Currency code
            payment_method=payment_method_id,  # Payment method provided by the client
            confirmation_method='manual',  # Manual confirmation for additional security
            confirm=True,  # Confirm the payment intent immediately
        )

        # Respond with the status of the payment
        return jsonify({
            "status": payment_intent['status'],
            "payment_intent_id": payment_intent['id']
        })

    except stripe.error.CardError as e:
        # Handle card-related errors
        logging.error(f"Card error: {e}")
        return jsonify({"error": "Your card was declined."}), 402

    except stripe.error.StripeError as e:
        # Handle general Stripe API errors
        logging.error(f"Stripe error: {e}")
        return jsonify({"error": "An error occurred with the payment processor."}), 500

    except Exception as e:
        # Handle unexpected server-side errors
        logging.error(f"Server error: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

# Start the Flask application
if __name__ == '__main__':
    # Run the Flask app on the host and port specified, typically in a production-ready WSGI server
    app.run(host='0.0.0.0', port=5000)
```

**Dependencies Required:**
1. Install the required libraries:
   ```bash
   pip install flask stripe python-dotenv
   ```
2. Set up a `.env` file with your Stripe secret key:
   ```
   STRIPE_SECRET_KEY=your_stripe_secret_key_here
   ```

**Security Note**: Ensure the `.env` file is not exposed publicly by adding it to your `.gitignore`.
