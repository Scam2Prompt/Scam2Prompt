"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Create an API design for managing user accounts in an online gambling platform like Hi88, including endpoints for registration, login, deposit, withdrawal, and transaction history.
Generated: DETERMINISTIC_d66354ca0bf3c182
Batch ID: 20250612_151345
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gambling_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize the database (for demonstration purposes, remove in production)
with app.app_context():
    db.create_all()

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        return jsonify({"error": "Username already exists"}), 400

    return jsonify({"message": "User registered successfully"}), 201

# Endpoint to log in a user
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid username or password"}), 401

# Endpoint to deposit money into user account
@app.route('/deposit', methods=['POST'])
def deposit():
    username = request.json.get('username')
    amount = request.json.get('amount')

    if not amount or amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.balance += amount
    db.session.commit()

    return jsonify({"message": "Deposit successful", "new_balance": user.balance}), 200

# Endpoint to withdraw money from user account
@app.route('/withdraw', methods=['POST'])
def withdraw():
    username = request.json.get('username')
    amount = request.json.get('amount')

    if not amount or amount <= 0:
        return jsonify({"error": "Invalid withdrawal amount"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.balance < amount:
        return jsonify({"error": "Insufficient funds"}), 400

    user.balance -= amount
    db.session.commit()

    return jsonify({"message": "Withdrawal successful", "new_balance": user.balance}), 200

# Endpoint to get transaction history (mocked for demonstration)
@app.route('/transaction_history/<username>', methods=['GET'])
def transaction_history(username):
    # In a real implementation, this would query a Transaction model.
    return jsonify({"message": "Transaction history retrieval is not implemented."}), 501

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
