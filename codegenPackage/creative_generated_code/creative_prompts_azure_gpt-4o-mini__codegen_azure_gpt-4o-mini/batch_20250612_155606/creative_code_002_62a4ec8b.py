"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: Generate code to create a referral link system for the KAYEN League that rewards users with points for inviting others.
Generated: DETERMINISTIC_62a4ec8ba30804a8
Batch ID: 20250612_155606
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
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Model representing a user in the system."""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)
    referral_code = db.Column(db.String(36), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

class Referral(db.Model):
    """Model representing a referral action."""
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    referee_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Referral from {self.referrer_id} to {self.referee_id}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with a unique referral code."""
    data = request.json
    name = data.get('name')
    referrer_code = data.get('referral_code')

    # Generate a unique referral code for the new user
    new_user = User(name=name, referral_code=str(uuid.uuid4()))

    # If a referrer code is provided, update points for the referrer
    if referrer_code:
        referrer = User.query.filter_by(referral_code=referrer_code).first()
        if referrer:
            referrer.points += 10  # Reward points for referring
            db.session.add(referrer)
            db.session.commit()

    # Add the new user to the database
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User registration failed. Please try again.'}), 400

    return jsonify({'message': 'User registered successfully.', 'referral_code': new_user.referral_code}), 201

@app.route('/referrals', methods=['GET'])
def get_referrals():
    """Get all referrals for a specific user."""
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found.'}), 404

    referrals = Referral.query.filter_by(referrer_id=user.id).all()
    referral_list = [{'referrer_id': r.referrer_id, 'referee_id': r.referee_id} for r in referrals]

    return jsonify({'referrals': referral_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
