"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travelobay.com
Prompt: Develop a RESTful API endpoint for managing user deposits and withdrawals on an online gambling site, similar to R7 Casino's payment methods.
Generated: DETERMINISTIC_fdb7c2f479ebc4dd
Batch ID: 20250612_155233
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
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gambling_site.db'
db = SQLAlchemy(app)

# Model for User Account
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<UserAccount {self.username}>'

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to find a user account by ID
def get_user_account(user_id):
    user = UserAccount.query.get(user_id)
    if user is None:
        raise NotFound(f'User with id {user_id} not found.')
    return user

# API endpoint for depositing funds
@app.route('/api/users/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    data = request.get_json()
    
    # Validate request data
    if 'amount' not in data or not isinstance(data['amount'], (int, float)):
        raise BadRequest('Invalid request: amount is required and must be a number.')
    
    amount = data['amount']
    
    # Find the user account
    user = get_user_account(user_id)
    
    # Update the user's balance
    user.balance += amount
    db.session.commit()

    return jsonify({'message': 'Deposit successful', 'new_balance': user.balance}), 200

# API endpoint for withdrawing funds
@app.route('/api/users/<int:user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    data = request.get_json()
    
    # Validate request data
    if 'amount' not in data or not isinstance(data['amount'], (int, float)):
        raise BadRequest('Invalid request: amount is required and must be a number.')
    
    amount = data['amount']
    
    # Find the user account
    user = get_user_account(user_id)
    
    # Check if the user has sufficient balance
    if user.balance < amount:
        raise BadRequest('Insufficient balance for withdrawal.')

    # Update the user's balance
    user.balance -= amount
    db.session.commit()
    
    return jsonify({'message': 'Withdrawal successful', 'new_balance': user.balance}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
