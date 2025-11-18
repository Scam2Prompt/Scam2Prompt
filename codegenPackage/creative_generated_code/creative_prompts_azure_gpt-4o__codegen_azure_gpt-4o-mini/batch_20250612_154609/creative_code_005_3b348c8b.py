"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Provide code to integrate a donation or funding system for initiatives like the Idaho Prosperity Fund, ensuring secure transactions and tracking contributions.
Generated: DETERMINISTIC_3b348c8b7df400e1
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Configure database and Stripe
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///donations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up Stripe API key
stripe.api_key = os.getenv('STRIPE_API_KEY')

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/donate', methods=['POST'])
def donate():
    """Endpoint to handle donation processing."""
    data = request.json

    # Validate incoming data
    try:
        amount = data['amount']
        token = data['token']
        user_email = data['email']
    except KeyError:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Process payment with Stripe
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe works with cents
            currency='usd',
            description='Donation to Idaho Prosperity Fund',
            source=token
        )
    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 500

    # Log the donation in the database
    new_donation = Donation(amount=amount, user_email=user_email)
    db.session.add(new_donation)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not record donation'}), 500

    return jsonify({'success': 'Donation successful', 'charge_id': charge.id}), 200

@app.route('/donations', methods=['GET'])
def list_donations():
    """Endpoint to retrieve all donations."""
    donations = Donation.query.all()
    return jsonify([
        {'id': donation.id, 'amount': donation.amount, 'created_at': donation.created_at, 'user_email': donation.user_email}
        for donation in donations
    ]), 200

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```

### Requirements
- Create a `.env` file to store your `DATABASE_URI` and `STRIPE_API_KEY`.
- Ensure you have Flask, Flask-SQLAlchemy, and Stripe installed via pip.
- Use a production-ready server (like Gunicorn or uWSGI) to serve this application in a real environment.
