"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the referral income model used by SupremeProFund.
Generated: DETERMINISTIC_66a3aa1e2801b52e
Batch ID: 20250612_160156
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
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    referral_code = db.Column(db.String(36), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)
    referrals = db.relationship('User', backref='referrer', remote_side=[id])

    def __init__(self, username, password, referred_by=None):
        self.username = username
        self.password = generate_password_hash(password)
        self.referral_code = str(uuid.uuid4())  # Unique referral code
        self.referred_by = referred_by


# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# User Registration Endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    referred_by = data.get('referred_by')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    try:
        new_user = User(username=username, password=password, referred_by=referred_by)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.', 'referral_code': new_user.referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists.'}), 409

# User Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful!', 'referral_code': user.referral_code}), 200
    return jsonify({'message': 'Invalid username or password.'}), 401

# Referral Statistics Endpoint
@app.route('/referrals/<referral_code>', methods=['GET'])
def get_referrals(referral_code):
    user = User.query.filter_by(referral_code=referral_code).first()

    if not user:
        return jsonify({'message': 'Referral code not found.'}), 404

    referrals_count = len(user.referrals)
    return jsonify({'referral_code': referral_code, 'referrals_count': referrals_count}), 200

# Error handling
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'An internal error occurred, please try again later.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
