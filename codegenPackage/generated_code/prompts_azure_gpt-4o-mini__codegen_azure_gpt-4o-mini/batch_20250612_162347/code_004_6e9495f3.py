"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Suggest a code snippet for implementing a subscription model for a newsletter like The Infinite Game, aimed at self-improvement and entrepreneurship.
Generated: DETERMINISTIC_6e9495f3cbe3c5b4
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
import stripe

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up Stripe API key
stripe.api_key = 'your_stripe_secret_key'

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle new subscriptions.
    Expects JSON with 'email' and 'payment_method_id'.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'email' not in data or 'payment_method_id' not in data:
        raise BadRequest("Missing 'email' or 'payment_method_id' in request data.")
    
    email = data['email']
    payment_method_id = data['payment_method_id']

    # Create a new subscription in Stripe
    try:
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id,
            },
        )
        
        # Create a subscription in Stripe
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'price': 'your_stripe_price_id'}],  # Replace with your price ID
            expand=['latest_invoice.payment_intent'],
        )
        
        # Save subscription to the database
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({'subscription_id': subscription.id, 'status': 'subscribed'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/unsubscribe/<email>', methods=['DELETE'])
def unsubscribe(email):
    """
    Endpoint to handle unsubscriptions.
    Expects the email of the subscriber.
    """
    # Find the subscription in the database
    subscription = Subscription.query.filter_by(email=email).first()
    
    if not subscription:
        return jsonify({'error': 'Subscription not found.'}), 404

    # Deactivate the subscription
    subscription.active = False
    db.session.commit()

    return jsonify({'status': 'unsubscribed'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
