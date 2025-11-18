"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Write code for a subscription-based platform that provides access to the "Masterclass Temperamentos" and weekly live mentorship sessions, with payment integration for installment plans.
Generated: DETERMINISTIC_f6e6b25e78c478f7
Batch ID: 20250612_153224
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
import stripe

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'
app.config['STRIPE_PUBLIC_KEY'] = 'your_stripe_public_key'
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Initialize the database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subscription_status = db.Column(db.String(50), nullable=False, default="inactive")

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plan = db.Column(db.String(50), nullable=False)  # e.g., "monthly", "yearly", "installment"
    stripe_subscription_id = db.Column(db.String(100), nullable=False)

# Routes
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Route to handle new subscriptions."""
    try:
        data = request.json
        user_id = data.get('user_id')
        plan = data.get('plan')

        # Retrieve user from the database
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Stripe payment setup
        stripe_customer = stripe.Customer.create(
            email=user.email,
            name=user.name
        )

        # Choose a Stripe price ID based on the plan (configured in Stripe dashboard)
        price_id_mapping = {
            "monthly": "price_monthly_id",
            "yearly": "price_yearly_id",
            "installment": "price_installment_id"
        }
        price_id = price_id_mapping.get(plan)
        if not price_id:
            return jsonify({"error": "Invalid plan"}), 400

        # Create Stripe subscription
        stripe_subscription = stripe.Subscription.create(
            customer=stripe_customer.id,
            items=[{"price": price_id}]
        )

        # Save subscription to the database
        subscription = Subscription(
            user_id=user_id,
            plan=plan,
            stripe_subscription_id=stripe_subscription.id
        )
        db.session.add(subscription)
        user.subscription_status = "active"
        db.session.commit()

        return jsonify({"message": "Subscription created successfully"}), 201
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/mentorship_sessions', methods=['GET'])
def mentorship_sessions():
    """Route for retrieving weekly mentorship sessions."""
    try:
        # Assuming mentorship sessions are hardcoded for simplicity
        sessions = [
            {"week": 1, "topic": "Understanding Temperaments", "date": "2023-10-01"},
            {"week": 2, "topic": "Applying Temperaments Effectively", "date": "2023-10-08"},
            {"week": 3, "topic": "Advanced Temperament Techniques", "date": "2023-10-15"},
        ]
        return jsonify({"sessions": sessions}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Route to handle subscription cancellation."""
    try:
        data = request.json
        user_id = data.get('user_id')

        # Retrieve user and subscription from the database
        subscription = Subscription.query.filter_by(user_id=user_id).first()
        if not subscription:
            return jsonify({"error": "Subscription not found"}), 404

        # Cancel Stripe subscription
        stripe.Subscription.delete(subscription.stripe_subscription_id)

        # Update database
        user = User.query.filter_by(id=user_id).first()
        user.subscription_status = "inactive"
        db.session.delete(subscription)
        db.session.commit()

        return jsonify({"message": "Subscription canceled successfully"}), 200
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/register', methods=['POST'])
def register():
    """Route to register a new user."""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "User already exists"}), 400

        # Create new user
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Initialize the database
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
