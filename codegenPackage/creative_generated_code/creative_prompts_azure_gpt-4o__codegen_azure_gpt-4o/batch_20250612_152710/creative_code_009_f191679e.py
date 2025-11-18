"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Provide an example of using Stripe API to integrate payment processing for a dental clinic's website, allowing patients to pay for services like same-day crowns or Invisalign treatments online.
Generated: DETERMINISTIC_f191679e02c5f4fb
Batch ID: 20250612_152710
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.yourdentalclinic.com/payment-cancelled": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.yourdentalclinic.com/payment-success?session_id={CHECKOUT_SESSION_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# File: stripe_payment_integration.py

import stripe
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# Stripe API secret key (replace with your actual secret key)
stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"

# Define your clinic's service prices
PRICE_LIST = {
    "same_day_crown": 1200,  # Price in USD cents ($12.00)
    "invisalign": 3500,      # Price in USD cents ($35.00)
}

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """
    Endpoint to create a Stripe Checkout Session.
    Expects a JSON payload with the 'service' key specifying the service type.
    """
    try:
        # Parse the requested service from the incoming request
        data = request.json
        service = data.get("service")
        
        if service not in PRICE_LIST:
            return jsonify({"error": "Invalid service type"}), 400
        
        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': service.replace('_', ' ').title(),  # Human-readable service name
                        },
                        'unit_amount': PRICE_LIST[service],
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://www.yourdentalclinic.com/payment-success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://www.yourdentalclinic.com/payment-cancelled',
        )
        
        # Return the session URL to the frontend
        return jsonify({"checkout_url": session.url}), 200
    
    except stripe.error.StripeError as e:
        # Handle Stripe API errors gracefully
        return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        # Handle other server-side errors
        return jsonify({"error": "An error occurred while processing your request"}), 500


if __name__ == '__main__':
    # Start the Flask app (for local development)
    app.run(debug=True)
```
