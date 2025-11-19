"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Generate a code snippet for a web application that allows users to donate to social services like CEFOR, focusing on children and adolescents in vulnerable situations.
Generated: DETERMINISTIC_13157e157d12cc4d
Batch ID: 20250612_162051
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

# Initialize Flask app
app = Flask(__name__)

# Set up Stripe API key (replace 'your_stripe_secret_key' with your actual secret key)
stripe.api_key = "your_stripe_secret_key"

# Route for processing donations
@app.route('/donate', methods=['POST'])
def donate():
    """
    Endpoint to handle donations. Accepts JSON payload:
    {
        "amount": <donation_amount_in_cents>,
        "currency": <currency_code>,
        "payment_method_id": <stripe_payment_method_id>,
        "email": <donor_email>
    }
    Returns a JSON response with success or error messages.
    """
    try:
        # Parse the request data
        data = request.json
        amount = data.get('amount')
        currency = data.get('currency', 'usd')  # Default currency is USD
        payment_method_id = data.get('payment_method_id')
        email = data.get('email')

        # Validate input
        if not amount or not payment_method_id or not email:
            return jsonify({"error": "Invalid input. 'amount', 'payment_method_id', and 'email' are required."}), 400

        # Create a payment intent
        intent = stripe.PaymentIntent.create(
            amount=amount,  # Donation amount in cents
            currency=currency,
            payment_method=payment_method_id,
            receipt_email=email,
            confirm=True  # Automatically confirm the payment
        )

        # Return success response
        return jsonify({"message": "Donation successful!", "payment_intent": intent}), 200
    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({"error": f"Card error: {e.user_message}"}), 400
    except stripe.error.StripeError as e:
        # Handle other Stripe errors
        return jsonify({"error": f"Payment error: {e.user_message}"}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route for health check
@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"}), 200

# Run the app
if __name__ == '__main__':
    # Use debug=True in development only. Set debug=False in production.
    app.run(debug=True)
```

### Notes for Deployment:
1. Replace `your_stripe_secret_key` with the actual Stripe secret key in a secure way (e.g., environment variables).
2. Ensure HTTPS for secure transmission of payment and sensitive data.
3. Set `debug=False` when deploying to production.
