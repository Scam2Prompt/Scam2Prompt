"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Explain how to integrate a payment gateway for online fee payments in a school ERP system like Him Saral.
Generated: DETERMINISTIC_794a70ce2dd3daa8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python example using the Flask framework and a payment gateway API (e.g., Stripe) to integrate online fee payments in a school ERP system:

```python
# Import necessary modules
from flask import Flask, request, jsonify
import stripe

# Create Flask app
app = Flask(__name__)

# Stripe API secret key (replace with your own secret key from Stripe dashboard)
app.config['STRIPE_SECRET_KEY'] = 'sk_test_your_secret_key'
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Route to render payment page (frontend integration omitted for brevity)
@app.route('/payment', methods=['POST'])
def create_payment():
    """
    Endpoint to create a payment session for fee payment.
    This will generate a payment intent using Stripe API.
    """
    try:
        # Parse fee amount and student details from the request
        data = request.json
        fee_amount = data['fee_amount']
        student_id = data['student_id']
        student_email = data['student_email']

        # Validate input data
        if fee_amount <= 0:
            return jsonify({"error": "Invalid fee amount"}), 400
        if not student_id or not student_email:
            return jsonify({"error": "Missing student details"}), 400

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(fee_amount * 100),  # Convert to cents
            currency="usd",
            receipt_email=student_email,  # Send receipt to the student's email
            metadata={"student_id": student_id}  # Store student information
        )

        return jsonify({
            "client_secret": payment_intent['client_secret'],
            "message": "Payment session created successfully"
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle other runtime errors
        return jsonify({"error": "An error occurred while processing the payment"}), 500

# Route to handle webhook events from Stripe
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle webhook events from Stripe.
    This will update the database based on payment status.
    """
    # Your Stripe webhook secret (replace with your actual secret key)
    webhook_secret = 'whsec_your_webhook_secret'

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        # Handle the event type
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            
            # Extract student ID from metadata
            student_id = payment_intent['metadata']['student_id']

            # TODO: Update the database to mark the fee as paid for the student
            # Example: database.update_fee_payment(student_id, status='Paid')

            print(f"Payment successful for student ID: {student_id}")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            
            # Extract student ID from metadata
            student_id = payment_intent['metadata']['student_id']

            # TODO: Update the database to log the payment failure for the student
            # Example: database.update_fee_payment(student_id, status='Failed')

            print(f"Payment failed for student ID: {student_id}")
        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"}), 200

    except ValueError as e:
        # Invalid payload
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An error occurred while processing webhook"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
```

### Notes:
- Replace `sk_test_your_secret_key` and `whsec_your_webhook_secret` with your actual Stripe API keys from the Stripe dashboard.
- This code demonstrates the server-side integration for a payment gateway. The frontend (for the user interface) is not included.
- Proper database integration should be added to store and update payment records.
- The code follows best practices for error handling and modular design to ensure reliability in a production environment.
