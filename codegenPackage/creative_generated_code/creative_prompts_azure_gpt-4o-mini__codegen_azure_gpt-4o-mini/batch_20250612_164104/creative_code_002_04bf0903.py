"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: What are the steps to create an OTC marketplace for secure crypto transactions, as outlined in the Base Mafia project?
Generated: DETERMINISTIC_04bf090306cbd4a6
Batch ID: 20250612_164104
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
from werkzeug.security import generate_password_hash, check_password_hash
import os
import jwt
import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///otc_marketplace.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key_here')
db = SQLAlchemy(app)

# Model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Model for Transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.id}>'

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required."}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Invalid credentials."}), 401

    # Generate JWT token
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'])
    return jsonify({"token": token})

# Route for creating a transaction
@app.route('/transaction', methods=['POST'])
def create_transaction():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing!"}), 403

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired."}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token."}), 401

    buyer_id = data['user_id']
    seller_id = request.json.get('seller_id')
    amount = request.json.get('amount')

    if not seller_id or not amount:
        return jsonify({"message": "Seller ID and amount are required."}), 400

    new_transaction = Transaction(buyer_id=buyer_id, seller_id=seller_id, amount=amount)

    try:
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

# Route for getting all transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    output = []

    for transaction in transactions:
        output.append({
            'id': transaction.id,
            'buyer_id': transaction.buyer_id,
            'seller_id': transaction.seller_id,
            'amount': transaction.amount,
            'timestamp': transaction.timestamp
        })

    return jsonify(output)

# Function to create database
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()  # Create the database
    app.run(debug=True)  # Run the app
```
