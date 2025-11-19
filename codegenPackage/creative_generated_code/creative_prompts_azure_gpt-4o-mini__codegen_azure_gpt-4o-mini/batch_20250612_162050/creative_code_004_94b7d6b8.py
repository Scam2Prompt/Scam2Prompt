"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Illustrate how to implement a referral program API to enhance customer engagement, similar to the one described on The Digital Age's site.
Generated: DETERMINISTIC_94b7d6b8c219c51f
Batch ID: 20250612_162050
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    referral_code = db.Column(db.String(10), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with an optional referral code.
    Request JSON body should include email and optional referral_code.
    """
    data = request.get_json()
    email = data.get('email')
    referral_code = data.get('referral_code')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Generate a unique referral code for the new user
    new_referral_code = str(uuid.uuid4())[:10]

    new_user = User(email=email, referral_code=new_referral_code)

    # Handle referral logic
    if referral_code:
        referrer = User.query.filter_by(referral_code=referral_code).first()
        if referrer:
            new_user.referred_by = referrer.id
        else:
            return jsonify({"error": "Invalid referral code"}), 400

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists"}), 400

    return jsonify({
        "message": "User registered successfully",
        "referral_code": new_referral_code
    }), 201

@app.route('/referrals/<user_id>', methods=['GET'])
def get_referrals(user_id):
    """
    Get all users referred by a specific user.
    """
    referrals = User.query.filter_by(referred_by=user_id).all()
    referral_emails = [user.email for user in referrals]

    return jsonify({
        "user_id": user_id,
        "referrals": referral_emails
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
