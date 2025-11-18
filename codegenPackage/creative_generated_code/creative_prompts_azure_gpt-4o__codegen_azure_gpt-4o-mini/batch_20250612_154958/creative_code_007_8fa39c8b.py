"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Develop a web application that integrates payment gateways for 심바공구's e-commerce site, ensuring compatibility with Korean payment systems like KG INISIS.
Generated: DETERMINISTIC_8fa39c8b8713a6e6
Batch ID: 20250612_154958
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
import requests
import logging

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for storing payment information
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/pay', methods=['POST'])
def process_payment():
    """
    Endpoint to process payment via KG INISIS or other payment gateways.
    Expects JSON with 'amount' and 'payment_method'.
    """
    try:
        data = request.get_json()
        amount = data.get('amount')
        payment_method = data.get('payment_method')

        # Validate input
        if not amount or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid amount provided.'}), 400
        
        if not payment_method:
            return jsonify({'error': 'Payment method is required.'}), 400

        # Here would be the implementation of payment gateway logic
        # For KG INISIS, you would typically send an API request to their endpoint
        # This is a placeholder for actual payment processing logic
        payment_response = fake_payment_gateway(amount, payment_method)

        # Example of a successful payment response
        if payment_response['status'] == 'success':
            # Save the payment information to the database
            payment = Payment(amount=amount, payment_method=payment_method, status='Completed')
            db.session.add(payment)
            db.session.commit()
            return jsonify({'message': 'Payment processed successfully!', 'payment_id': payment.id}), 200
        else:
            return jsonify({'error': 'Payment failed. Please try again.'}), 500

    except Exception as e:
        logging.error(f"Error processing payment: {e}")
        return jsonify({'error': 'An error occurred while processing the payment.'}), 500

def fake_payment_gateway(amount, payment_method):
    """
    This function simulates payment processing.
    In a real-world scenario, this would interact with the actual payment gateway API.
    """
    # Simulate a successful payment response
    return {'status': 'success'}

@app.route('/api/payments', methods=['GET'])
def get_payments():
    """
    Endpoint to retrieve payment records from the database.
    """
    try:
        payments = Payment.query.all()
        payment_list = [{'id': p.id, 'amount': p.amount, 'payment_method': p.payment_method, 'status': p.status} for p in payments]
        return jsonify(payment_list), 200
    except Exception as e:
        logging.error(f"Error retrieving payments: {e}")
        return jsonify({'error': 'An error occurred while retrieving payments.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
