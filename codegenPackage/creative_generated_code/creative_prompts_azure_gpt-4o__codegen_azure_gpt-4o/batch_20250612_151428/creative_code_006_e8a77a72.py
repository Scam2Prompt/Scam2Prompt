"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Suggest a library or framework to implement a secure payment system for hiring police uniforms and replica firearms, including handling security deposits and credit card details as described on Powered Production Film Services.
Generated: DETERMINISTIC_e8a77a72a5d0929d
Batch ID: 20250612_151428
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
from stripe import Stripe
import os

# Initialize Flask application
app = Flask(__name__)

# Load environment variables (e.g., Stripe Secret Key)
# Make sure to use environment variables for sensitive information in production.
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

# Initialize Stripe client
stripe.api_key = STRIPE_SECRET_KEY  # Set Stripe secret key

# Define API endpoint for payment processing
@app.route("/process-payment", methods=["POST"])
def process_payment():
    """
    Endpoint to handle secure payment processing.

    Expected Payload:
    {
        "amount": 1000,  # Amount in cents
        "currency": "usd",  # Currency code
        "source": "tok_visa",  # Payment source token, e.g., card token
        "description": "Hiring police uniforms and replica firearms",
        "security_deposit": 500  # Security deposit in cents
    }
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate required fields
        required_fields = ["amount", "currency", "source", "description", "security_deposit"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Create payment intent to handle both payment and security deposit
        payment_intent = stripe.PaymentIntent.create(
            amount=data["amount"] + data["security_deposit"],  # Total payment including security deposit
            currency=data["currency"],
            description=data["description"],
            payment_method=data["source"],
            confirm=True  # Automatically confirm the payment
        )

        # Return success response
        return jsonify({"message": "Payment processed successfully", "payment_intent": payment_intent}), 200

    except stripe.error.CardError as e:
        # Handle card errors (e.g., insufficient funds, expired card, etc.)
        return jsonify({"error": str(e.error.message)}), 400
    except stripe.error.RateLimitError:
        # Handle rate limit errors (too many requests)
        return jsonify({"error": "Rate limit error. Please try again later."}), 429
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return jsonify({"error": f"Invalid request: {str(e)}"}), 400
    except stripe.error.AuthenticationError:
        # Handle authentication errors (e.g., invalid API key)
        return jsonify({"error": "Authentication error. Check Stripe API key."}), 401
    except stripe.error.APIConnectionError:
        # Handle connection errors
        return jsonify({"error": "Network error. Please try again."}), 503
    except stripe.error.StripeError as e:
        # Handle other Stripe errors
        return jsonify({"error": f"Stripe error: {str(e)}"}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Define a health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify that the service is running.
    """
    return jsonify({"status": "ok"}), 200

# Run Flask application
if __name__ == "__main__":
    # Ensure environment variables are properly configured
    if not STRIPE_SECRET_KEY:
        raise EnvironmentError("Stripe secret key must be set in environment variables.")

    # Run Flask app in debug mode (set to False in production)
    app.run(debug=True)
```
