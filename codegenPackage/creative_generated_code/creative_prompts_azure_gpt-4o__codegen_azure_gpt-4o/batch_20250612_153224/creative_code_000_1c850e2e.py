"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to integrate a secure payment gateway for online fee collection in a school management system, referencing features described in Him Saral's software.
Generated: DETERMINISTIC_1c850e2e27b186c6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import stripe
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure Stripe API key securely
# Ensure your Stripe secret key is stored securely, such as using environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Define a route for fee payment
@app.route('/pay_fee', methods=['POST'])
def pay_fee():
    """
    Endpoint to handle online fee payment.
    Expects JSON payload containing:
    - `student_id`: Unique identifier for student
    - `amount`: Fee amount to be charged in smallest currency unit (e.g., cents for USD)
    - `currency`: Currency code (e.g., 'usd')
    - `payment_method_id`: Stripe payment method identifier
    """
    try:
        # Parse JSON payload from request
        data = request.json
        student_id = data.get('student_id')
        amount = data.get('amount')
        currency = data.get('currency', 'usd')
        payment_method_id = data.get('payment_method_id')

        # Validate required fields
        if not student_id or not amount or not payment_method_id:
            return jsonify({"error": "Missing required fields"}), 400

        # Create a payment intent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method=payment_method_id,
            confirm=True,  # Automatically confirm the payment
            metadata={"student_id": student_id}
        )

        # Return success response with payment details
        return jsonify({
            "success": True,
            "payment_intent_id": payment_intent.id,
            "status": payment_intent.status
        }), 200

    except stripe.error.CardError as e:
        # Handle card-related errors
        return jsonify({"error": f"Card Error: {e.user_message}"}), 400
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return jsonify({"error": f"Invalid Request: {e.user_message}"}), 400
    except stripe.error.AuthenticationError as e:
        # Handle authentication errors
        return jsonify({"error": "Authentication Error: Please check your API key"}), 401
    except stripe.error.APIConnectionError as e:
        # Handle API connection errors
        return jsonify({"error": "Network Error: Please try again later"}), 502
    except stripe.error.StripeError as e:
        # Handle generic Stripe errors
        return jsonify({"error": f"Stripe Error: {e.user_message}"}), 500
    except Exception as e:
        # Handle general server errors
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

# Run Flask application
if __name__ == '__main__':
    # Use a secure port in production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Notes:
- **Dependencies**: Install required dependencies using `pip install flask stripe`.
- **Environment Variables**: Set `STRIPE_SECRET_KEY` securely to your Stripe secret key.
- **Production Best Practices**: In production, use HTTPS and proper logging. Never expose secret keys in code or logs.
