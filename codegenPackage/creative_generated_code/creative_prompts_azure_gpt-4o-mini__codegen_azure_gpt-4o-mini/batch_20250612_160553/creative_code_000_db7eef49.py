"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fornm.network
Prompt: How can I implement a secure payment system for purchasing domain names similar to the one described on fornm.network?
Generated: DETERMINISTIC_db7eef4943f5e37a
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import stripe
import os

# Initialize Flask application
app = Flask(__name__)

# Configure Stripe with your secret key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')  # Set your Stripe secret key in an environment variable

# Payment endpoint to handle domain purchase
@app.route('/purchase_domain', methods=['POST'])
def purchase_domain():
    try:
        # Parse request data
        data = request.json
        domain_name = data.get('domain_name')
        payment_method_id = data.get('payment_method_id')
        amount = data.get('amount')  # Amount in cents

        # Validate input
        if not domain_name or not payment_method_id or not amount:
            raise BadRequest("Missing required fields: domain_name, payment_method_id, or amount.")

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method=payment_method_id,
            confirmation_method='automatic',
            confirm=True
        )

        # Assume domain registration logic here (omitted for brevity)
        # register_domain(domain_name)

        # Return success response
        return jsonify({
            'success': True,
            'payment_intent': payment_intent.id,
            'message': f'Domain {domain_name} purchased successfully!'
        }), 200

    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({'error': str(e)}), 400
    except BadRequest as e:
        # Handle bad request errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # General error handling
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(port=5000, debug=False)  # Run the Flask app
```

Make sure to set the `STRIPE_SECRET_KEY` environment variable before running the application. Adjust the domain registration logic as needed.
