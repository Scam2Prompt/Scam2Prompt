"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babnylon.foundation
Prompt: How can I implement a secure payment system for domain name transactions similar to the one described on babnylon.foundation?
Generated: DETERMINISTIC_d6e7f7fcf74074f0
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load Stripe API key (Use environment variables for security in production)
STRIPE_API_KEY = "your_stripe_api_key_here"
stripe.api_key = STRIPE_API_KEY

# Route to handle payments
@app.route('/create-payment', methods=['POST'])
def create_payment():
    """
    Endpoint to handle payment creation for domain name transactions.
    Expected payload:
    {
        "domain_name": "example.com",
        "amount": 10000,  # Amount in cents (e.g., $100.00 = 10000)
        "currency": "usd",
        "email": "customer@example.com",
        "payment_method_id": "pm_xxx"
    }
    """
    try:
        data = request.json

        # Validate input
        if not data or not all(key in data for key in ("domain_name", "amount", "currency", "email", "payment_method_id")):
            return jsonify({"error": "Invalid payload. Required: domain_name, amount, currency, email, payment_method_id"}), 400

        # Create the payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=data["amount"],
            currency=data["currency"],
            payment_method=data["payment_method_id"],
            description=f"Payment for domain: {data['domain_name']}",
            receipt_email=data["email"],
            confirm=True  # Automatically confirm the payment intent
        )

        # Return successful payment response
        return jsonify({
            "success": True,
            "payment_intent_id": payment_intent.id,
            "status": payment_intent.status,
        })

    except stripe.error.CardError as e:
        # Handle card errors
        logging.error(f"Card error: {e.user_message}")
        return jsonify({"error": f"Card error: {e.user_message}"}), 400
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        logging.error(f"Stripe error: {str(e)}")
        return jsonify({"error": "Payment processing error, please try again later."}), 500
    except Exception as e:
        # Handle non-Stripe errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred, please try again later."}), 500

# Route to handle webhook events from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle webhook events from Stripe.
    Ensure the endpoint is verified and secure in production.
    """
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = "your_webhook_secret_here"  # Use environment variable in production

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        
        # Handle the event (example: payment_intent.succeeded)
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            logging.info(f"Payment succeeded for PaymentIntent ID: {payment_intent['id']}")

        # Return 200 OK for successful event handling
        return jsonify({"success": True}), 200

    except stripe.error.SignatureVerificationError as e:
        # Handle invalid signature
        logging.error(f"Webhook signature verification error: {str(e)}")
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the app (use a production-ready server like Gunicorn for deployment)
if __name__ == '__main__':
    app.run(debug=True)
```

---

### **Production Notes:**
1. Replace `your_stripe_api_key_here` and `your_webhook_secret_here` with environment variables for security purposes.
2. Ensure HTTPS is used in production for secure data transmission.
3. Use a robust server like **Gunicorn** or **uWSGI** for deployment, behind a reverse proxy like **NGINX**.
4. Configure Stripe webhook endpoints to only accept requests from Stripe's IP ranges using a firewall or IP filtering mechanism.
