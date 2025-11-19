"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: What are the best practices for building an API that handles payment options for Chevrolet car buyers?
Generated: DETERMINISTIC_0cbb1cf321e18188
Batch ID: 20250612_164321
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Payment model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(20), nullable=False)  # e.g., 'credit_card', 'paypal'

# Create a schema for validating payment data
class PaymentSchema(Schema):
    buyer_id = fields.Str(required=True)
    amount = fields.Float(required=True)
    method = fields.Str(required=True)

# Initialize the schema
payment_schema = PaymentSchema()

@app.route('/payment', methods=['POST'])
def create_payment():
    """Endpoint to create a new payment option for a Chevrolet car buyer."""
    try:
        # Validate and deserialize the input
        data = request.get_json()
        payment_data = payment_schema.load(data)

        # Create a new payment record
        new_payment = Payment(**payment_data)
        db.session.add(new_payment)
        db.session.commit()

        logging.info(f"Payment created successfully: {new_payment.id}")
        return jsonify(payment_schema.dump(new_payment)), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the payment."}), 500

@app.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    """Endpoint to retrieve a payment option by ID."""
    try:
        payment = Payment.query.get_or_404(payment_id)
        return jsonify(payment_schema.dump(payment)), 200
    except Exception as e:
        logging.error(f"Error retrieving payment: {str(e)}")
        return jsonify({"error": "Payment not found."}), 404

@app.route('/payments', methods=['GET'])
def list_payments():
    """Endpoint to list all payment options."""
    try:
        payments = Payment.query.all()
        return jsonify(payment_schema.dump(payments, many=True)), 200
    except Exception as e:
        logging.error(f"Error retrieving payments: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving payments."}), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```
