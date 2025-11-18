"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Generate code to create a slot game interface that supports wallet-based transactions, including features for bonus distribution and tracking "สล็อตใช้วอเลทเครดิตฟรี."
Generated: DETERMINISTIC_a4488f576d6ebb30
Batch ID: 20250612_151420
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slot_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model for wallet management
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    wallet_balance = db.Column(db.Float, default=0.0)
    bonus_balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a Transaction model to track wallet transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # 'credit' or 'debit'
    
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

# Endpoint to add funds to user wallet
@app.route('/add_funds', methods=['POST'])
def add_funds():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    if amount <= 0:
        return jsonify({'error': 'Amount must be greater than zero'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.wallet_balance += amount
    new_transaction = Transaction(user_id=user.id, amount=amount, transaction_type='credit')

    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Funds added successfully', 'new_balance': user.wallet_balance}), 200

# Endpoint to distribute bonuses
@app.route('/distribute_bonus', methods=['POST'])
def distribute_bonus():
    data = request.json
    username = data.get('username')
    bonus_amount = data.get('bonus_amount')

    if bonus_amount <= 0:
        return jsonify({'error': 'Bonus amount must be greater than zero'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.bonus_balance += bonus_amount
    db.session.commit()
    return jsonify({'message': 'Bonus distributed successfully', 'new_bonus_balance': user.bonus_balance}), 200

# Endpoint to view user wallet and bonuses
@app.route('/wallet_info', methods=['GET'])
def wallet_info():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'username': user.username,
        'wallet_balance': user.wallet_balance,
        'bonus_balance': user.bonus_balance
    }), 200

# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
