"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Write code to implement a subscription-based payment model for online health services using Stripe API, including monthly and yearly plans.
Generated: DETERMINISTIC_da5a00562e416668
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for the Stripe API
stripe.api_key = 'your_stripe_secret_key'  # Replace with your actual Stripe secret key

# Define subscription plans
MONTHLY_PLAN_ID = 'your_monthly_plan_id'  # Replace with your actual monthly plan ID
YEARLY_PLAN_ID = 'your_yearly_plan_id'    # Replace with your actual yearly plan ID

@app.route('/create-customer', methods=['POST'])
def create_customer():
    """
    Creates a new customer in Stripe and returns the customer ID.
    Expects a JSON payload with a 'email' field.
    """
    data = request.get_json()

    if not data or 'email' not in data:
        abort(400, description="Missing email in request data.")

    try:
        customer = stripe.Customer.create(
            email=data['email'],
        )
        return jsonify({"customer_id": customer.id}), 201
    except Exception as e:
        abort(500, description=str(e))

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Subscribes a customer to a plan (monthly or yearly).
    Expects a JSON payload with 'customer_id' and 'plan' fields.
    """
    data = request.get_json()

    if not data or 'customer_id' not in data or 'plan' not in data:
        abort(400, description="Missing customer_id or plan in request data.")
    
    if data['plan'] not in ['monthly', 'yearly']:
        abort(400, description="Invalid plan. Choose either 'monthly' or 'yearly'.")

    plan_id = MONTHLY_PLAN_ID if data['plan'] == 'monthly' else YEARLY_PLAN_ID

    try:
        subscription = stripe.Subscription.create(
            customer=data['customer_id'],
            items=[{'plan': plan_id}],
        )
        return jsonify({"subscription_id": subscription.id}), 201
    except Exception as e:
        abort(500, description=str(e))

@app.route('/cancel-subscription', methods=['POST'])
def cancel_subscription():
    """
    Cancels an existing subscription.
    Expects a JSON payload with 'subscription_id' field.
    """
    data = request.get_json()

    if not data or 'subscription_id' not in data:
        abort(400, description="Missing subscription_id in request data.")

    try:
        subscription = stripe.Subscription.retrieve(data['subscription_id'])
        subscription.delete()
        return jsonify({"status": "Subscription canceled"}), 200
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
