"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gamees.org
Prompt: Write code to implement a referral system for "3 Patti Bounty" apps, allowing users to earn rewards for inviting others, as mentioned on https://gamees.org.
Generated: DETERMINISTIC_e05fc77b44bf941b
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Model representing a user in the system."""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    referral_code = db.Column(db.String(10), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)
    rewards = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.referral_code}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user and generate a referral code."""
    data = request.json
    referral_code = data.get('referral_code')
    referred_by = data.get('referred_by')

    # Validate referral code if provided
    if referred_by and not User.query.filter_by(referral_code=referred_by).first():
        abort(400, description="Invalid referee code")

    new_user = User(referral_code=referral_code, referred_by=referred_by)
    
    # Try to add the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()

        # Update rewards for the referrer if applicable
        if referred_by:
            referrer = User.query.filter_by(referral_code=referred_by).first()
            if referrer:
                referrer.rewards += 10  # Reward for the referrer
                db.session.commit()

        return jsonify({"message": "User registered successfully", "referral_code": referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Referral code must be unique")

@app.route('/rewards/<referral_code>', methods=['GET'])
def get_rewards(referral_code):
    """Get the rewards of a user by their referral code."""
    user = User.query.filter_by(referral_code=referral_code).first()
    if not user:
        abort(404, description="User not found")

    return jsonify({"referral_code": referral_code, "rewards": user.rewards})

@app.errorhandler(400)
def handle_bad_request(error):
    """Handle bad requests with a custom response."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def handle_not_found(error):
    """Handle not found errors with a custom response."""
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
