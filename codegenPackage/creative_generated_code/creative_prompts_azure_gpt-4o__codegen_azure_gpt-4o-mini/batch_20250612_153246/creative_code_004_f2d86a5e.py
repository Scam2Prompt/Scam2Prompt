"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Suggest an API to integrate online payment gateways for donations, similar to Youngistaan Foundation's "Donate Now" feature.
Generated: DETERMINISTIC_f2d86a5e14102d33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import stripe
import logging

# Initialize a Flask application
app = Flask(__name__)

# Configure Stripe with your secret key
stripe.api_key = 'sk_test_your_secret_key_here'

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/donate', methods=['POST'])
def donate():
    """
    Endpoint to handle donation requests.
    Expects JSON data with 'amount' and 'currency'.
    """
    try:
        # Get the donation data from the request
        data = request.get_json()

        # Validate input data
        amount = data.get('amount')
        currency = data.get('currency', 'usd')  # Default to USD if currency not provided

        if not amount or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Create a new charge
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe amount is in cents
            currency=currency,
            description='Donation',
            source=data.get('source')  # Source should be the payment token
        )

        # Log successful charge
        logging.info(f"Charge successful: {charge.id}")

        return jsonify({'success': True, 'charge_id': charge.id}), 200

    except stripe.error.CardError as e:
        logging.error(f"Card error: {e.user_message}")
        return jsonify({'error': 'Card declined'}), 402
    except Exception as e:
        logging.error(f"Error processing donation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
