"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinstantmining.com
Prompt: Create a REST API to manage user accounts, deposits, and withdrawals securely, inspired by the account management features of Globalinstantmining.
Generated: DETERMINISTIC_15598775e7c7fc1b
Batch ID: 20250612_150227
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Create a new user account
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        return jsonify({'message': 'User already exists'}), 409
    
    return jsonify({'message': 'User created successfully'}), 201

# Retrieve user account details
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'username': user.username,
        'balance': user.balance
    }), 200

# Deposit funds into a user account
@app.route('/api/users/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    amount = data.get('amount')

    if amount is None or amount <= 0:
        return jsonify({'message': 'Invalid deposit amount'}), 400

    user.balance += amount
    db.session.commit()
    
    return jsonify({'message': 'Deposit successful', 'new_balance': user.balance}), 200

# Withdraw funds from a user account
@app.route('/api/users/<int:user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    amount = data.get('amount')

    if amount is None or amount <= 0:
        return jsonify({'message': 'Invalid withdrawal amount'}), 400

    if user.balance < amount:
        return jsonify({'message': 'Insufficient funds'}), 400

    user.balance -= amount
    db.session.commit()
    
    return jsonify({'message': 'Withdrawal successful', 'new_balance': user.balance}), 200

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

### Requirements:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Werkzeug

### Installation:
You can install the required packages using pip:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```

### Usage:
1. Run the application.
2. Use a tool like Postman or Curl to interact with the REST API.
