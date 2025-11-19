"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamusk.app
Prompt: Generate a code snippet to implement a subscription feature for a web application similar to the one described on metamusk.app.
Generated: DETERMINISTIC_1685a4eb977e2657
Batch ID: 20250612_164115
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
from werkzeug.exceptions import NotFound, BadRequest
import stripe

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Stripe API
stripe.api_key = 'your_stripe_secret_key'

# Database model for User Subscription
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    stripe_subscription_id = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle subscription requests."""
    data = request.json
    email = data.get('email')
    payment_method_id = data.get('payment_method_id')
    
    if not email or not payment_method_id:
        raise BadRequest("Email and payment method ID are required.")

    try:
        # Create a new customer in Stripe
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id,
            },
        )

        # Create a subscription for the customer
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'price': 'your_stripe_price_id'}],  # Set your Stripe price ID
            expand=['latest_invoice.payment_intent'],
        )

        # Store the subscription in the database
        new_subscription = Subscription(
            email=email,
            stripe_subscription_id=subscription.id
        )
        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({'subscription_id': subscription.id, 'status': subscription.status}), 201

    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Handle other potential errors
        return jsonify({'error': 'An error occurred, please try again later.'}), 500

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """Endpoint to retrieve subscription details by ID."""
    subscription = Subscription.query.get(subscription_id)
    
    if not subscription:
        raise NotFound("Subscription not found.")

    return jsonify({
        'id': subscription.id,
        'email': subscription.email,
        'stripe_subscription_id': subscription.stripe_subscription_id
    })

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
