"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Write code to integrate Stripe payment processing into a website or funnel created with InfinitiAI's platform.
Generated: DETERMINISTIC_236d63d0e73f0da8
Batch ID: 20250612_154115
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://js.stripe.com/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com/cancel": {
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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import stripe
import os

# Initialize Flask application
app = Flask(__name__)

# Set Stripe API key from environment variables for security
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/checkout', methods=['GET'])
def checkout():
    """Render the checkout page."""
    return render_template('checkout.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """Create a new Stripe Checkout session."""
    try:
        # Create a new Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': request.json['product_name'],  # Product name from request
                        },
                        'unit_amount': request.json['amount'],  # Amount from request in cents
                    },
                    'quantity': request.json['quantity'],  # Quantity from request
                },
            ],
            mode='payment',
            success_url='https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://yourdomain.com/cancel',
        )
        return jsonify({'id': checkout_session.id})  # Return session ID for client-side use
    except Exception as e:
        # Handle exceptions and return error message
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(port=5000)
```

### `checkout.html` template example (must be created in the templates directory)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <h1>Checkout</h1>
    <button id="checkout-button">Pay Now</button>

    <script>
        const stripe = Stripe('YOUR_PUBLIC_STRIPE_KEY');  // Replace with your public key

        document.getElementById('checkout-button').addEventListener('click', () => {
            fetch('/create-checkout-session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_name: 'Example Product',
                    amount: 2000,  // Amount in cents
                    quantity: 1,
                }),
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.id) {
                    // Redirect to Stripe Checkout
                    return stripe.redirectToCheckout({ sessionId: data.id });
                } else {
                    console.error(data.error);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
```

### Notes:
- Replace `'YOUR_PUBLIC_STRIPE_KEY'` and `'https://yourdomain.com'` with your actual Stripe public key and your domain.
- Ensure you have Flask and Stripe libraries installed (`pip install Flask stripe`).
- Set the `STRIPE_SECRET_KEY` environment variable with your Stripe secret key for security.
