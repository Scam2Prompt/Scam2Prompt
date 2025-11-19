"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Suggest an API for managing fee payments online for a school, similar to the "Pay Fees" feature on the Deepti Convent Higher Secondary School website, and demonstrate its implementation.
Generated: DETERMINISTIC_38698c61f68928ca
Batch ID: 20250612_153225
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_fees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the FeePayment model
class FeePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    status = db.Column(db.String(20), default='Pending')  # e.g., Pending, Completed, Failed

    def __repr__(self):
        return f'<FeePayment {self.id} - Student: {self.student_id}, Amount: {self.amount}, Status: {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new fee payment
@app.route('/api/fee_payment', methods=['POST'])
def create_fee_payment():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        amount = data.get('amount')
        payment_date = data.get('payment_date')

        # Validate input data
        if not student_id or not amount or not payment_date:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new fee payment record
        new_payment = FeePayment(student_id=student_id, amount=amount, payment_date=payment_date)
        db.session.add(new_payment)
        db.session.commit()

        logging.info(f'Fee payment created: {new_payment}')
        return jsonify({'message': 'Fee payment created successfully', 'payment_id': new_payment.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Payment already exists for this student on this date'}), 409
    except Exception as e:
        logging.error(f'Error creating fee payment: {e}')
        return jsonify({'error': 'An error occurred while processing the request'}), 500

# API endpoint to retrieve fee payment details
@app.route('/api/fee_payment/<int:payment_id>', methods=['GET'])
def get_fee_payment(payment_id):
    payment = FeePayment.query.get(payment_id)
    if payment:
        return jsonify({
            'id': payment.id,
            'student_id': payment.student_id,
            'amount': payment.amount,
            'payment_date': payment.payment_date,
            'status': payment.status
        }), 200
    else:
        return jsonify({'error': 'Payment not found'}), 404

# API endpoint to update the status of a fee payment
@app.route('/api/fee_payment/<int:payment_id>', methods=['PUT'])
def update_fee_payment(payment_id):
    try:
        data = request.get_json()
        status = data.get('status')

        if not status:
            return jsonify({'error': 'Missing required field: status'}), 400

        payment = FeePayment.query.get(payment_id)
        if not payment:
            return jsonify({'error': 'Payment not found'}), 404

        payment.status = status
        db.session.commit()

        logging.info(f'Fee payment updated: {payment}')
        return jsonify({'message': 'Fee payment status updated successfully'}), 200

    except Exception as e:
        logging.error(f'Error updating fee payment: {e}')
        return jsonify({'error': 'An error occurred while processing the request'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
