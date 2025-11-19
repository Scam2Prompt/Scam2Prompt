"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Design an API for a referral mechanism in an NFT marketplace, inspired by CorgiAI's ecosystem.
Generated: DETERMINISTIC_f312fcd50406d478
Batch ID: 20250622_205623
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
from sqlalchemy.exc import IntegrityError
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing user information
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    referral_code = db.Column(db.String(36), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Model for tracking referrals
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    referred_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Referral {self.referrer_id} -> {self.referred_id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new user with an optional referral code
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    referral_code = data.get('referral_code')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Generate a unique referral code for the new user
    new_referral_code = str(uuid.uuid4())

    # Create a new user
    new_user = User(username=username, referral_code=new_referral_code)

    # Handle referral logic
    if referral_code:
        referrer = User.query.filter_by(referral_code=referral_code).first()
        if referrer:
            new_user.referred_by = referrer.id
            referral_record = Referral(referrer_id=referrer.id, referred_id=new_user.id)
            db.session.add(referral_record)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', 'referral_code': new_referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

# Endpoint to get user information
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'username': user.username,
        'referral_code': user.referral_code,
        'referred_by': user.referred_by
    }), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
