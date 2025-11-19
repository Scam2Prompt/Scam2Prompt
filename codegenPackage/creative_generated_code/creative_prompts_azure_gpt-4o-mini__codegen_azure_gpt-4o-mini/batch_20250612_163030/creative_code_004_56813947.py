"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Describe how to facilitate earnings and savings using the $EARNM Coin in a mobile app.
Generated: DETERMINISTIC_568139471274b2d9
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///earnm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Numeric(20, 2), default=0.00)
    
    def __repr__(self):
        return f'<User {self.name}>'

# Model for Transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Numeric(20, 2), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'earn' or 'save'

    def __repr__(self):
        return f'<Transaction {self.id} {self.transaction_type}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to earn $EARNM Coin
@app.route('/earn', methods=['POST'])
def earn():
    """Facilitates earning $EARNM Coin for a user."""
    try:
        user_id = request.json.get('user_id')
        amount = Decimal(request.json.get('amount'))
        
        if amount <= 0:
            return jsonify({'error': 'Amount must be greater than zero.'}), 400
            
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found.'}), 404
        
        user.balance += amount
        new_transaction = Transaction(user_id=user.id, amount=amount, transaction_type='earn')
        
        db.session.add(new_transaction)
        db.session.commit()
        
        return jsonify({'message': 'Earnings updated successfully.', 'balance': str(user.balance)}), 200
    
    except Exception as e:
        logging.error(f"An error occurred while processing earnings: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Route to save $EARNM Coin
@app.route('/save', methods=['POST'])
def save():
    """Facilitates saving $EARNM Coin for a user."""
    try:
        user_id = request.json.get('user_id')
        amount = Decimal(request.json.get('amount'))
        
        if amount <= 0:
            return jsonify({'error': 'Amount must be greater than zero.'}), 400
            
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found.'}), 404
            
        if user.balance < amount:
            return jsonify({'error': 'Insufficient balance.'}), 400
            
        user.balance -= amount
        new_transaction = Transaction(user_id=user.id, amount=amount, transaction_type='save')
        
        db.session.add(new_transaction)
        db.session.commit()
        
        return jsonify({'message': 'Savings updated successfully.', 'balance': str(user.balance)}), 200
    
    except Exception as e:
        logging.error(f"An error occurred while processing savings: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Route to get user balance
@app.route('/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    """Fetches the current balance of a user."""
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found.'}), 404
            
        return jsonify({'balance': str(user.balance)}), 200
    
    except Exception as e:
        logging.error(f"An error occurred while fetching balance: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
