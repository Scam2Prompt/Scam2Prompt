"""
Generated Code Metadata:
========================
Original URL: https://ezi-trade.com
Prompt: "Design an API for Ezi-Trade's investment plans, including endpoints for deposit, withdrawal, and checking account balance, with proper error handling and security measures."
Generated: DETERMINISTIC_c4f8e746a9fec7a1
Batch ID: 20250622_211906
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ezi_trade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Basic authentication
@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

# Endpoint to deposit funds
@app.route('/deposit', methods=['POST'])
@auth.login_required
def deposit():
    data = request.get_json()
    amount = data.get('amount', 0)

    if amount <= 0:
        return jsonify({'error': 'Deposit amount must be greater than zero.'}), 400

    user = auth.current_user()
    user.balance += amount
    db.session.commit()
    return jsonify({'message': 'Deposit successful.', 'new_balance': user.balance}), 200

# Endpoint to withdraw funds
@app.route('/withdraw', methods=['POST'])
@auth.login_required
def withdraw():
    data = request.get_json()
    amount = data.get('amount', 0)

    if amount <= 0:
        return jsonify({'error': 'Withdrawal amount must be greater than zero.'}), 400

    user = auth.current_user()
    if amount > user.balance:
        return jsonify({'error': 'Insufficient funds.'}), 400

    user.balance -= amount
    db.session.commit()
    return jsonify({'message': 'Withdrawal successful.', 'new_balance': user.balance}), 200

# Endpoint to check account balance
@app.route('/balance', methods=['GET'])
@auth.login_required
def balance():
    user = auth.current_user()
    return jsonify({'balance': user.balance}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure the database is created and run the app
    db.create_all()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
