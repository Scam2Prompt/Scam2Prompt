"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smrk85.cc
Prompt: What are the best practices for developing a lottery app similar to "幸运彩票," focusing on user experience and transaction security?
Generated: DETERMINISTIC_209efdfdfd604389
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import hashlib
import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# Lottery Ticket model
class LotteryTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    numbers = db.Column(db.String(20))
    
    def __init__(self, user_id, numbers):
        self.user_id = user_id
        self.numbers = numbers

# Schemas for Serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class LotteryTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LotteryTicket

# Create tables
with app.app_context():
    db.create_all()

# Error handling decorator
def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return decorated_function

# User registration
@app.route('/register', methods=['POST'])
@handle_exceptions
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    return UserSchema().dump(new_user), 201

# User login
@app.route('/login', methods=['POST'])
@handle_exceptions
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return UserSchema().dump(user), 200
    return jsonify({"error": "Invalid username or password."}), 401

# Purchase Lottery Ticket
@app.route('/purchase_ticket', methods=['POST'])
@handle_exceptions
def purchase_ticket():
    user_id = request.json.get('user_id')
    numbers = request.json.get('numbers')

    if not user_id or not numbers:
        return jsonify({"error": "User ID and numbers are required."}), 400

    new_ticket = LotteryTicket(user_id, numbers)
    db.session.add(new_ticket)
    db.session.commit()

    return LotteryTicketSchema().dump(new_ticket), 201

# Generate Random Lottery Numbers
@app.route('/generate_numbers', methods=['GET'])
@handle_exceptions
def generate_numbers():
    numbers = random.sample(range(1, 50), 6)  # Generate 6 unique numbers between 1 and 49
    return jsonify({"numbers": sorted(numbers)}), 200

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```
