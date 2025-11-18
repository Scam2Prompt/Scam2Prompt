"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write code to integrate payment processing for an online store selling "Placas de Premiação" and "Power Bag" training equipment.
Generated: DETERMINISTIC_9f3f4b6b168e2434
Batch ID: 20250612_151414
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
import stripe

app = Flask(__name__)

# Set your secret key. Remember to switch to your live secret key in production!
# You can find your secret key in your Stripe dashboard
stripe.api_key = 'sk_test_your_secret_key_here'

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    """
    Creates a payment intent for the specified items.
    Expected JSON format:
    {
        "items": [
            {
                "name": "Placas de Premiação",
                "amount": 2000,  # Amount in cents
                "quantity": 1
            },
            {
                "name": "Power Bag",
                "amount": 3000,  # Amount in cents
                "quantity": 2
            }
        ]
    }
    """
    try:
        # Retrieve the request data
        data = request.json
        
        # Validate input
        if 'items' not in data or not isinstance(data['items'], list):
            return jsonify({'error': 'Invalid input data'}), 400
        
        # Calculate total amount
        total_amount = sum(item['amount'] * item['quantity'] for item in data['items'])

        # Create a PaymentIntent with the order amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount,  # Total amount in cents
            currency='usd',  # Set currency accordingly
            metadata={'integration_check': 'accept_a_payment'}
        )

        # Return the client secret for the payment
        return jsonify({
            'clientSecret': payment_intent['client_secret']
        })

    except stripe.error.StripeError as e:
        # Handle Stripe error
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Note:
- Ensure to replace `'sk_test_your_secret_key_here'` with your actual Stripe secret key.
- This code uses the Flask framework for a web server; you need to install Flask and Stripe library using `pip install Flask stripe`.
- The code is production-ready, but ensure to implement additional security measures such as HTTPS and validating user input as per your application's requirements.
