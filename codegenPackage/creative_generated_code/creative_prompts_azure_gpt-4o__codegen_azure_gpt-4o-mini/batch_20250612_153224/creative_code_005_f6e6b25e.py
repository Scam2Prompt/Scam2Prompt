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
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure database and Stripe
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')

# Initialize database and other extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Stripe Configuration
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Database Models
class User(db.Model):
    """Model representing a user."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    subscription_status = db.Column(db.String(20), default='inactive')

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

class Subscription(db.Model):
    """Model representing a subscription."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stripe_subscription_id = db.Column(db.String(100), unique=True)

# Create a user
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.json
    try:
        new_user = User(email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Create a subscription
@app.route('/subscribe', methods=['POST'])
def subscribe_user():
    """Subscribe a user to the Masterclass and mentorship."""
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404

    try:
        # Create a subscription in Stripe
        subscription = stripe.Subscription.create(
            customer=user.stripe_customer_id,
            items=[
                {'price': os.getenv('STRIPE_PRICE_ID')},
            ],
            trial_period_days=7  # Optional: A trial period
        )
        
        new_subscription = Subscription(user_id=user.id, stripe_subscription_id=subscription.id)
        db.session.add(new_subscription)
        db.session.commit()
        
        # Update user subscription status
        user.subscription_status = 'active'
        db.session.commit()

        return jsonify({'message': 'Subscription created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Cancel a subscription
@app.route('/cancel', methods=['POST'])
def cancel_subscription():
    """Cancel the user's subscription."""
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    subscription = Subscription.query.filter_by(user_id=user.id).first()
    
    if not subscription:
        return jsonify({'error': 'No active subscription found'}), 404

    try:
        stripe.Subscription.delete(subscription.stripe_subscription_id)
        db.session.delete(subscription)
        db.session.commit()

        # Update user subscription status
        user.subscription_status = 'inactive'
        db.session.commit()

        return jsonify({'message': 'Subscription canceled successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

In a production setup, ensure to:
- Use a robust database solution (like PostgreSQL).
- Store sensitive keys in environment variables.
- Configure proper logging for error handling.
- Implement HTTPS for secure data transmission.
