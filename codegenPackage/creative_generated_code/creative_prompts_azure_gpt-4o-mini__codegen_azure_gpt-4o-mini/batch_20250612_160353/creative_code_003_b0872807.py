"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: Create an API endpoint that allows users to check their account balance and transaction history, inspired by the features of 247signalfxtrade.
Generated: DETERMINISTIC_b0872807e00b0847
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User Account
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

# Model for Transaction History
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'credit' or 'debit'
    timestamp = db.Column(db.DateTime, nullable=False)

    user = db.relationship('UserAccount', backref=db.backref('transactions', lazy=True))

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/account/<int:user_id>/balance', methods=['GET'])
def get_balance(user_id):
    """Retrieve the account balance for a given user ID."""
    account = UserAccount.query.get(user_id)
    if account is None:
        raise NotFound("Account not found.")

    return jsonify({'user_id': account.id, 'username': account.username, 'balance': account.balance})

@app.route('/api/account/<int:user_id>/transactions', methods=['GET'])
def get_transactions(user_id):
    """Retrieve the transaction history for a given user ID."""
    account = UserAccount.query.get(user_id)
    if account is None:
        raise NotFound("Account not found.")

    transactions = Transaction.query.filter_by(user_id=user_id).all()
    transaction_list = [
        {
            'id': txn.id,
            'amount': txn.amount,
            'transaction_type': txn.transaction_type,
            'timestamp': txn.timestamp.isoformat()
        }
        for txn in transactions
    ]

    return jsonify({'user_id': account.id, 'transactions': transaction_list})

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
