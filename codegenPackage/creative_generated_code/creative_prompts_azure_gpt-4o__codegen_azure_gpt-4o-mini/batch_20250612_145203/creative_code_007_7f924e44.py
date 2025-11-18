"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write code to integrate a payment gateway for mobile RV repair services, allowing customers in Phoenix, AZ to pay online for inspections, repairs, and upgrades.
Generated: DETERMINISTIC_7f924e44d86b1fb0
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure Stripe with your secret key
stripe.api_key = 'your_stripe_secret_key'

# Configure SQLite database for transaction records
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for payment transactions
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/pay', methods=['POST'])
def pay():
    """
    Process a payment via Stripe.
    
    Expected JSON payload:
    {
        "amount": float,
        "currency": "USD",
        "source": "token from stripe",
        "description": "Service Description"
    }
    """
    try:
        # Parse the JSON request body
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ('amount', 'currency', 'source')):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a charge using Stripe
        charge = stripe.Charge.create(
            amount=int(data['amount'] * 100),  # amount in cents
            currency=data['currency'],
            source=data['source'],
            description=data.get('description', 'RV Repair Service Payment')
        )
        
        # Record the transaction in the database
        payment = Payment(
            amount=data['amount'],
            currency=data['currency'],
            status=charge['status']
        )
        db.session.add(payment)
        db.session.commit()
        
        return jsonify({"success": True, "charge_id": charge['id']}), 200
    
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An error occurred: " + str(e)}), 500

@app.route('/payments', methods=['GET'])
def get_payments():
    """
    Retrieve all payment records.
    
    Returns:
    A JSON list of all payment transactions.
    """
    try:
        payments = Payment.query.all()
        payment_list = [{
            "id": payment.id,
            "amount": payment.amount,
            "currency": payment.currency,
            "status": payment.status,
            "created_at": payment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for payment in payments]
        return jsonify(payment_list), 200
    
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
