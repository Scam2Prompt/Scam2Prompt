"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opterisglobal.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the rewards system mentioned on Opteris Global's website.
Generated: DETERMINISTIC_a0b1689beb3e8f52
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    referral_code = db.Column(db.String(10), unique=True, nullable=False)
    referred_by = db.Column(db.String(10), db.ForeignKey('user.referral_code'))

    def __repr__(self):
        return f'<User {self.name}>'

# Database model for Referrals
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    referred_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reward_claimed = db.Column(db.Boolean, default=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to register a new user with an optional referral code
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json

    # Validate input data
    if not data or 'name' not in data or 'email' not in data or 'referral_code' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new user
    new_user = User(
        name=data['name'],
        email=data['email'],
        referral_code=data['referral_code']
    )

    # Handle optional referral
    if 'referred_by' in data:
        referred_by_user = User.query.filter_by(referral_code=data['referred_by']).first()
        if referred_by_user:
            referral = Referral(referrer_id=referred_by_user.id, referred_id=new_user.id)
            db.session.add(referral)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', 'referral_code': new_user.referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already registered or referral code already in use'}), 400

# API endpoint to claim reward for a referral
@app.route('/claim_reward', methods=['POST'])
def claim_reward():
    data = request.json

    # Validate input data
    if not data or 'referral_code' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    # Fetch the referral
    referral = Referral.query.filter_by(referral_id=data['referral_code']).first()
    if referral and not referral.reward_claimed:
        referral.reward_claimed = True
        db.session.commit()
        return jsonify({'message': 'Reward claimed successfully'}), 200
    else:
        return jsonify({'error': 'Reward already claimed or invalid referral code'}), 400

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
To run this code, ensure you have Flask and SQLAlchemy installed in your Python environment. You can set it up with:

```bash
pip install Flask Flask-SQLAlchemy
```

Then, you can run the script and use tools like Postman or curl to interact with the API endpoints.
