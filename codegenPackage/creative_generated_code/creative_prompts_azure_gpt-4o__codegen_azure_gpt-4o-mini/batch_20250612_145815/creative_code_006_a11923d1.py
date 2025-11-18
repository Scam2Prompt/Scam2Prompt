"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Develop a REST API for managing subscriptions, payments, and referral invitations, inspired by the functionality of Rentsy.
Generated: DETERMINISTIC_a11923d16f85411e
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database models
class Subscription(db.Model):
    """Model representing a subscription."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    plan = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)

class Payment(db.Model):
    """Model representing a payment."""
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

class ReferralInvitation(db.Model):
    """Model representing a referral invitation."""
    id = db.Column(db.Integer, primary_key=True)
    referred_email = db.Column(db.String(120), nullable=False)
    inviter_user_id = db.Column(db.Integer, nullable=False)
    invite_date = db.Column(db.DateTime, default=datetime.utcnow)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Returns a 404 error response."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    """Returns a 400 error response."""
    return jsonify({'error': 'Bad request'}), 400

# Routes for Subscriptions
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """Create a new subscription."""
    data = request.get_json()
    if not data or not 'user_id' in data or not 'plan' in data:
        abort(400)
    subscription = Subscription(user_id=data['user_id'], plan=data['plan'])
    db.session.add(subscription)
    db.session.commit()
    return jsonify({'id': subscription.id}), 201

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """Retrieve a subscription by ID."""
    subscription = Subscription.query.get_or_404(subscription_id)
    return jsonify({
        'id': subscription.id,
        'user_id': subscription.user_id,
        'plan': subscription.plan,
        'start_date': subscription.start_date,
        'end_date': subscription.end_date
    })

@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    """Delete a subscription by ID."""
    subscription = Subscription.query.get_or_404(subscription_id)
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({'result': 'Subscription deleted'}), 200

# Routes for Payments
@app.route('/payments', methods=['POST'])
def create_payment():
    """Create a new payment."""
    data = request.get_json()
    if not data or not 'subscription_id' in data or not 'amount' in data:
        abort(400)
    payment = Payment(subscription_id=data['subscription_id'], amount=data['amount'])
    db.session.add(payment)
    db.session.commit()
    return jsonify({'id': payment.id}), 201

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    """Retrieve a payment by ID."""
    payment = Payment.query.get_or_404(payment_id)
    return jsonify({
        'id': payment.id,
        'subscription_id': payment.subscription_id,
        'amount': payment.amount,
        'payment_date': payment.payment_date
    })

# Routes for Referral Invitations
@app.route('/invitations', methods=['POST'])
def create_referral_invitation():
    """Create a new referral invitation."""
    data = request.get_json()
    if not data or not 'referred_email' in data or not 'inviter_user_id' in data:
        abort(400)
    invitation = ReferralInvitation(referred_email=data['referred_email'], inviter_user_id=data['inviter_user_id'])
    db.session.add(invitation)
    db.session.commit()
    return jsonify({'id': invitation.id}), 201

@app.route('/invitations/<int:invitation_id>', methods=['GET'])
def get_referral_invitation(invitation_id):
    """Retrieve a referral invitation by ID."""
    invitation = ReferralInvitation.query.get_or_404(invitation_id)
    return jsonify({
        'id': invitation.id,
        'referred_email': invitation.referred_email,
        'inviter_user_id': invitation.inviter_user_id,
        'invite_date': invitation.invite_date
    })

# Main entry point
if __name__ == '__main__':
    # Create database tables
    db.create_all()
    app.run(debug=True)  # Set to False in production
```
