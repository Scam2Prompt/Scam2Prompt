"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hahieuroblox.com
Prompt: Recommend an approach to integrate payment gateways for "Nạp Tiền" on a website similar to HAHIEUROBLOX.com, ensuring secure transactions.
Generated: DETERMINISTIC_3349ba664fab143a
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# flask_payment_gateway.py

from flask import Flask, request, jsonify
import stripe  # Stripe SDK for payment processing
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO)

# Stripe API secret key (loaded from environment variables for security)
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
if not STRIPE_SECRET_KEY:
    raise Exception("Missing STRIPE_SECRET_KEY in environment variables")

stripe.api_key = STRIPE_SECRET_KEY

@app.route('/charge', methods=['POST'])
def charge():
    """
    Endpoint to handle payment processing.
    Expects JSON payload with 'amount' and 'payment_method_id'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        amount = data.get('amount')  # Amount in cents (integer)
        payment_method_id = data.get('payment_method_id')  # Stripe Payment Method ID
        
        # Validate input data
        if not amount or not payment_method_id:
            raise ValueError("Invalid request payload. 'amount' and 'payment_method_id' are required.")
        
        # Create a Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',  # Change this based on your requirements
            payment_method=payment_method_id,
            confirm=True  # Automatically confirm the payment
        )
        
        # Respond with the PaymentIntent status
        return jsonify({
            'success': True,
            'payment_intent_id': intent.id,
            'status': intent.status
        }), 200

    except stripe.error.CardError as e:
        # Handle card errors (e.g., declined transactions)
        logging.error(f"Card error: {e.user_message}")
        return jsonify({'success': False, 'error': e.user_message}), 400
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        logging.error(f"Stripe error: {str(e)}")
        return jsonify({'success': False, 'error': 'Payment processing error. Please try again.'}), 500
    except Exception as e:
        # Handle other errors (e.g., unexpected server issues)
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({'success': False, 'error': 'An unexpected error occurred.'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Prerequisites:
1. Install required libraries using:
   ```
   pip install flask stripe python-dotenv
   ```

2. Create a `.env` file and add your Stripe secret key:
   ```
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

3. Ensure the Stripe account is set up with webhooks and proper API keys.

4. Production Deployment:
   - Use a WSGI server like Gunicorn for deployment.
   - Set `debug=False` in production and configure HTTPS for secure transactions.
