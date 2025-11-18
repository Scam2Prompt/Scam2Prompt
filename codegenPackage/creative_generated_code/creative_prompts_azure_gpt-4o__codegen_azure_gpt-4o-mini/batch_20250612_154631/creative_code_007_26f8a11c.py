"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluestockmarkets.com
Prompt: Develop a backend system for BlueStockMarkets that supports multiple cryptocurrency payment methods and fiat currency transactions.
Generated: DETERMINISTIC_26f8a11c20b3ad85
Batch ID: 20250612_154631
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
from sqlalchemy.exc import IntegrityError
from decimal import Decimal
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///marketplace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False) # 'crypto' or 'fiat'
    status = db.Column(db.String(20), default='pending') # 'pending', 'completed', 'failed'

    def __repr__(self):
        return f'<Transaction {self.id}, User: {self.user_id}, Amount: {self.amount}, Currency: {self.currency}, Status: {self.status}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new transaction
@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    
    try:
        # Validate input data
        user_id = data['user_id']
        currency = data['currency']
        amount = Decimal(data['amount'])
        transaction_type = data['transaction_type']

        if currency not in ['USD', 'EUR', 'BTC', 'ETH']:
            return jsonify({'error': 'Unsupported currency'}), 400

        if transaction_type not in ['fiat', 'crypto']:
            return jsonify({'error': 'Invalid transaction type'}), 400

        # Create a new transaction record
        new_transaction = Transaction(user_id=user_id, currency=currency, amount=amount, transaction_type=transaction_type)
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({'message': 'Transaction created', 'transaction_id': new_transaction.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Transaction could not be created due to integrity error'}), 500
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid data type: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Endpoint to retrieve a user's transactions
@app.route('/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    try:
        transactions = Transaction.query.filter_by(user_id=user_id).all()
        if not transactions:
            return jsonify({'message': 'No transactions found for this user'}), 404

        return jsonify([{
            'id': t.id,
            'currency': t.currency,
            'amount': str(t.amount),
            'transaction_type': t.transaction_type,
            'status': t.status
        } for t in transactions]), 200

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variable `DATABASE_URI` before running the application, or it will default to a SQLite database for local development.
