"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-aml.com
Prompt: Provide an example of how to set up a monthly subscription for the AMLBot service in a web application, including wallet count limits.
Generated: DETERMINISTIC_3991d8b52a4fcac4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
db = SQLAlchemy(app)

# Initialize Stripe with your secret key
stripe.api_key = 'your_stripe_secret_key'

# Create a Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    wallet_count_limit = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Create a new subscription for a user.
    Expects a JSON payload with user_id, payment_method_id, and wallet_count_limit.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        payment_method_id = data.get('payment_method_id')
        wallet_count_limit = data.get('wallet_count_limit')

        # Validate input
        if not user_id or not payment_method_id or wallet_count_limit is None:
            return jsonify({'error': 'Invalid input'}), 400

        # Create a customer in Stripe
        customer = stripe.Customer.create(
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id,
            },
        )

        # Create a subscription in Stripe
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'price': 'your_stripe_price_id',  # Replace with your price ID
                },
            ],
            expand=['latest_invoice.payment_intent'],
        )

        # Calculate the subscription end date (1 month later)
        end_date = datetime.now() + timedelta(days=30)

        # Save subscription details to the database
        new_subscription = Subscription(
            user_id=user_id,
            start_date=datetime.now(),
            end_date=end_date,
            wallet_count_limit=wallet_count_limit
        )
        db.session.add(new_subscription)
        db.session.commit()

        # Respond with subscription details
        return jsonify({
            'subscription_id': subscription.id,
            'status': subscription.status,
            'wallet_count_limit': wallet_count_limit,
            'end_date': end_date
        }), 201

    except Exception as e:
        # Log the error and return a response
        app.logger.error(f"Error creating subscription: {e}")
        return jsonify({'error': 'Subscription creation failed'}), 500

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Retrieve all subscriptions for a specific user.
    Expects a query parameter `user_id`.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    subscriptions = Subscription.query.filter_by(user_id=user_id).all()
    result = [
        {
            'id': sub.id,
            'start_date': sub.start_date,
            'end_date': sub.end_date,
            'wallet_count_limit': sub.wallet_count_limit
        } for sub in subscriptions
    ]
    
    return jsonify(result), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
