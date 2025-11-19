"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Create an API endpoint for an investment platform that allows users to retrieve their transaction history and current account balance, similar to the features offered by Ezi-Trade.
Generated: DETERMINISTIC_a3c5c504ac620a9c
Batch ID: 20250612_160220
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'  # Change to your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for User's Account
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

# Model for Transaction History
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'credit' or 'debit'
    timestamp = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

@app.route('/api/account/<int:user_id>', methods=['GET'])
def get_account_info(user_id):
    """
    Retrieve the account balance and transaction history for a specific user.
    
    :param user_id: The ID of the user whose account information is requested
    :return: JSON object containing user's balance and transaction history
    """
    try:
        user = User.query.get_or_404(user_id)  # Fetch user or return 404 if not found
        transactions = Transaction.query.filter_by(user_id=user.id).all()
        
        # Prepare transaction history
        transaction_history = [
            {
                'id': t.id,
                'amount': t.amount,
                'transaction_type': t.transaction_type,
                'timestamp': t.timestamp.isoformat()
            }
            for t in transactions
        ]
        
        response = {
            'username': user.username,
            'balance': user.balance,
            'transactions': transaction_history
        }
        return jsonify(response), 200  # Return success response

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500  # Return internal server error

if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Run the application
```
