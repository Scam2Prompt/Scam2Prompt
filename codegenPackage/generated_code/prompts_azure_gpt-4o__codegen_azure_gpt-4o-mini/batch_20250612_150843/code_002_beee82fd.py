"""
Generated Code Metadata:
========================
Original URL: https://everix-edge-gpt.com
Prompt: Generate code for a web-based cryptocurrency trading platform that supports multiple devices and includes features such as account funding, withdrawal systems, and broker integration, inspired by Everix Edge GPT.
Generated: DETERMINISTIC_beee82fdcf21b83d
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///trading_platform.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'fund' or 'withdraw'
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'error': 'Invalid username or password.'}), 401

# Route for funding account
@app.route('/fund', methods=['POST'])
def fund_account():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')

    if amount <= 0:
        return jsonify({'error': 'Amount must be greater than zero.'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    user.balance += amount
    transaction = Transaction(user_id=user.id, amount=amount, transaction_type='fund')
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Account funded successfully.', 'new_balance': user.balance}), 200

# Route for withdrawing from account
@app.route('/withdraw', methods=['POST'])
def withdraw_account():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')

    if amount <= 0:
        return jsonify({'error': 'Amount must be greater than zero.'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    if user.balance < amount:
        return jsonify({'error': 'Insufficient balance.'}), 400

    user.balance -= amount
    transaction = Transaction(user_id=user.id, amount=amount, transaction_type='withdraw')
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Withdrawal successful.', 'new_balance': user.balance}), 200

# Route for getting user balance
@app.route('/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404
    return jsonify({'balance': user.balance}), 200

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Note:
- Ensure you have the necessary packages installed (`Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `Werkzeug`).
- Set the `DATABASE_URL` environment variable for production use.
- This code is a basic implementation and should be extended with features like authentication tokens, input validation, and security measures for production readiness.
