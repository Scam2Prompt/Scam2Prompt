"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: How can I implement a donation system for a server like the one described on SQUID.WTF?
Generated: DETERMINISTIC_befa36d59b9f8ac9
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import stripe

# Initialize the Flask app
app = Flask(__name__)

# Stripe API keys (replace with your own keys)
STRIPE_PUBLIC_KEY = "your-stripe-public-key"
STRIPE_SECRET_KEY = "your-stripe-secret-key"

# Set up Stripe client
stripe.api_key = STRIPE_SECRET_KEY

# Route to serve the donation page (HTML can be served separately)
@app.route('/donate', methods=['GET'])
def donate_page():
    return jsonify({"message": "Donation page - integrate your frontend to send donation requests here."})

# Route to handle donation payments
@app.route('/process_donation', methods=['POST'])
def process_donation():
    try:
        # Parse the donation details from the request
        data = request.json
        amount = data.get('amount')  # Amount in cents (e.g., $10 = 1000 cents)
        currency = data.get('currency', 'usd')  # Default to USD if not specified
        payment_method_id = data.get('payment_method_id')  # Stripe payment method ID

        # Validate input
        if not amount or int(amount) <= 0:
            return jsonify({"error": "Invalid donation amount"}), 400
        if not payment_method_id:
            return jsonify({"error": "Payment method ID is required"}), 400

        # Create a payment intent in Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount),  # Ensure amount is an integer
            currency=currency,
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True,
        )

        # Return success response
        return jsonify({"success": True, "payment_intent": payment_intent})
    except stripe.error.CardError as e:
        # Handle card-related errors
        return jsonify({"error": "Card error", "details": str(e)}), 400
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        return jsonify({"error": "Payment processing error", "details": str(e)}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to confirm payment (optional, for manual confirmation flows)
@app.route('/confirm_payment', methods=['POST'])
def confirm_payment():
    try:
        # Parse the payment intent ID from the request
        data = request.json
        payment_intent_id = data.get('payment_intent_id')
        
        # Validate input
        if not payment_intent_id:
            return jsonify({"error": "Payment Intent ID is required"}), 400
        
        # Confirm the payment in Stripe
        payment_intent = stripe.PaymentIntent.confirm(payment_intent_id)
        
        # Return success response
        return jsonify({"success": True, "payment_intent": payment_intent})
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": "Payment confirmation error", "details": str(e)}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Replace `your-stripe-public-key` and `your-stripe-secret-key` with your actual Stripe keys.
- Ensure your server is properly secured and configured for production use.
- Integrate this backend with a frontend where users can provide their payment details and donation amounts.
