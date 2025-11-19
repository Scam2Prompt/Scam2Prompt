"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Generate a code snippet for a web application that allows users to donate to social services like CEFOR, focusing on children and adolescents in vulnerable situations.
Generated: DETERMINISTIC_13157e157d12cc4d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Configure Stripe API key (replace with your actual secret key)
stripe.api_key = "sk_test_your_stripe_secret_key"

# Database model for donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(255), nullable=True)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/donate', methods=['POST'])
def donate():
    """
    Endpoint to handle donations.
    Expects JSON payload with 'name', 'email', 'amount', 'message', and 'payment_method_id'.
    """
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        email = data.get('email')
        amount = data.get('amount')  # Amount in USD
        message = data.get('message', '')
        payment_method_id = data.get('payment_method_id')

        # Validate input
        if not name or not email or not amount or not payment_method_id:
            return jsonify({"error": "Missing required fields"}), 400

        # Convert amount to cents for Stripe (e.g., $10.00 -> 1000 cents)
        amount_in_cents = int(float(amount) * 100)

        # Create a payment intent with Stripe
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True,
        )

        # Save donation to the database
        donation = Donation(name=name, email=email, amount=amount, message=message)
        db.session.add(donation)
        db.session.commit()

        return jsonify({"success": True, "message": "Donation successful!"}), 200

    except stripe.error.CardError as e:
        # Handle card errors from Stripe
        return jsonify({"error": str(e.user_message)}), 400
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/donations', methods=['GET'])
def get_donations():
    """
    Endpoint to retrieve all donations.
    """
    try:
        donations = Donation.query.all()
        result = [
            {
                "id": donation.id,
                "name": donation.name,
                "email": donation.email,
                "amount": donation.amount,
                "message": donation.message,
            }
            for donation in donations
        ]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
