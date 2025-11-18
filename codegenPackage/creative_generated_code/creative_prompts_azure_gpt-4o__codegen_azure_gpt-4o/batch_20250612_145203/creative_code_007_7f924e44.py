"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write code to integrate a payment gateway for mobile RV repair services, allowing customers in Phoenix, AZ to pay online for inspections, repairs, and upgrades.
Generated: DETERMINISTIC_7f924e44d86b1fb0
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace with your actual Stripe keys)
STRIPE_PUBLIC_KEY = "pk_test_XXXXXXXXXXXXXXXXXXXXXXXX"
STRIPE_SECRET_KEY = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"

# Set secret key for Stripe integration
stripe.api_key = STRIPE_SECRET_KEY

# Route to display Stripe public key (for the frontend)
@app.route("/stripe-public-key", methods=["GET"])
def stripe_public_key():
    """
    Endpoint to provide the Stripe public key to the frontend.
    """
    return jsonify({"publicKey": STRIPE_PUBLIC_KEY})

# Route to create a Stripe payment intent
@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    """
    Endpoint to create a payment intent for a given amount and service description.
    Input: JSON body with 'amount' and 'description'.
    Output: JSON response with client secret for payment intent.
    """
    try:
        # Parse request data
        data = request.json
        amount = data.get("amount")  # Amount in cents
        description = data.get("description")  # Description of the service
        
        if not amount or not description:
            return jsonify({"error": "Missing required parameters: 'amount' and 'description'"}), 400
        
        # Create a payment intent using Stripe API
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",  # Currency code
            description=description,
            payment_method_types=["card"]  # Accept card payments
        )
        
        # Return client secret to the frontend
        return jsonify({"clientSecret": intent["client_secret"]})
    
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An error occurred: " + str(e)}), 500

# Route for health check
@app.route("/health", methods=["GET"])
def health():
    """
    Simple health endpoint to verify the service is running.
    """
    return jsonify({"status": "Service is up and running!"})

# Start the Flask app
if __name__ == "__main__":
    # Run the app in debug mode for local testing
    app.run(host="0.0.0.0", port=5000, debug=True)
```
