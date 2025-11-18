"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Suggest an API for integrating payment options for underwater equipment purchases, including items like "баллоны и вентили," as described in the payment section of the Открытое море website.
Generated: DETERMINISTIC_34453e07b8e2e899
Batch ID: 20250612_150323
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for storing transactions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class Payment(db.Model):
    """Model representing a payment transaction."""
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Payment {self.id} - {self.item_name}>'

@app.route('/api/payments', methods=['POST'])
def create_payment():
    """API endpoint to create a payment for underwater equipment."""
    data = request.get_json()
    
    # Validate incoming data
    if not data or 'item_name' not in data or 'amount' not in data:
        return jsonify({'error': 'Invalid input, item_name and amount are required.'}), 400
    
    item_name = data['item_name']
    amount = data['amount']

    # Create a new payment instance
    new_payment = Payment(item_name=item_name, amount=amount, status='pending')

    # Attempt to save the payment to the database
    try:
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({'message': 'Payment created successfully!', 'payment_id': new_payment.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    """API endpoint to retrieve a payment by its ID."""
    payment = Payment.query.get(payment_id)
    
    if payment is None:
        return jsonify({'error': 'Payment not found.'}), 404
    
    return jsonify({
        'id': payment.id,
        'item_name': payment.item_name,
        'amount': payment.amount,
        'status': payment.status
    }), 200

@app.route('/api/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """API endpoint to delete a payment by its ID."""
    payment = Payment.query.get(payment_id)
    
    if payment is None:
        return jsonify({'error': 'Payment not found.'}), 404
    
    try:
        db.session.delete(payment)
        db.session.commit()
        return jsonify({'message': 'Payment deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```
