"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Generate a code snippet for a donation system that allows users to contribute to the Shiv Vedika Trust, ensuring secure transactions.
Generated: DETERMINISTIC_8e553906e00d2bbf
Batch ID: 20250612_155601
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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set Stripe API key (ensure to set this in your environment variables)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Donation {self.id}: ${self.amount}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/donate', methods=['POST'])
def donate():
    """
    Process a donation to the Shiv Vedika Trust.

    Request JSON payload should include:
    - amount: float, the donation amount
    - token: string, the Stripe token for secure payment processing
    """

    try:
        # Get data from the request
        data = request.get_json()
        amount = data.get('amount')
        token = data.get('token')

        # Validate input
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid amount, must be a positive number.'}), 400
        
        if not token:
            return jsonify({'error': 'Payment token is required.'}), 400
        
        # Create a charge using Stripe
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Amount in cents
            currency='usd',
            source=token,
            description='Donation to Shiv Vedika Trust'
        )

        # Record the donation in the database
        donation = Donation(amount=amount)
        db.session.add(donation)
        db.session.commit()

        return jsonify({'success': True, 'id': donation.id, 'amount': donation.amount}), 201

    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({'error': str(e)}), 402
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred while processing the donation.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

Make sure to configure your environment with the appropriate Stripe secret key before running the application.
