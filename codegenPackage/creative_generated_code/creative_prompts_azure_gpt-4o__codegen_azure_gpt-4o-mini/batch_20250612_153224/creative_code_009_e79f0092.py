"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corelabs.pe
Prompt: Write code to implement a secure payment gateway for an e-commerce platform, inspired by CoreLabs' focus on designing optimized and scalable online business solutions.
Generated: DETERMINISTIC_e79f00926092bc76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from cryptography.fernet import Fernet
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration for Stripe (ensure to use environment variables for sensitive data)
stripe.api_key = 'your_stripe_api_key'

# Encryption key for sensitive data
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

# Endpoint for processing payments
@app.route('/api/payment', methods=['POST'])
def process_payment():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        if not data:
            raise BadRequest("Invalid JSON data.")

        # Validate incoming data
        required_fields = ['amount', 'currency', 'payment_method_id']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f'Missing required field: {field}')

        amount = data['amount']
        currency = data['currency']
        payment_method_id = data['payment_method_id']

        # Create a new payment intent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method=payment_method_id,
            confirmation_method='automatic',
            confirm=True
        )

        # Log the successful payment
        logging.info(f'Payment successful: {payment_intent.id}')

        # Return a response with success status
        return jsonify({
            'status': 'success',
            'payment_intent_id': payment_intent.id
        }), 200

    except stripe.error.CardError as e:
        # Handle card errors from Stripe
        logging.error(f'Card error: {e.user_message}')
        return jsonify({'error': e.user_message}), 400
    except BadRequest as e:
        # Handle bad request errors
        logging.error(f'Bad request: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle any other exceptions
        logging.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Endpoint for generating an encryption key (for demonstration purposes)
@app.route('/api/encryption-key', methods=['GET'])
def get_encryption_key():
    return jsonify({'encryption_key': encryption_key.decode()}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Note:** This code assumes the use of Stripe for payment processing and Flask as the web framework. Always secure sensitive keys and credentials in environment variables. The `stripe.api_key` should be replaced with your actual Stripe API key. Properly handle logging in a production environment and consider using a more sophisticated configuration for logging and error management.
