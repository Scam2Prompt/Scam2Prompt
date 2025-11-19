"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Illustrate how to implement a referral system in a web application similar to Fintradeoptions, allowing users to refer friends and earn bonuses.
Generated: DETERMINISTIC_3d3bfde6bc37f9ca
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    referral_code = db.Column(db.String(120), unique=True, nullable=False)
    referred_by = db.Column(db.String(120), nullable=True)
    bonus = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user with an optional referral code.
    Returns the created user's information and any bonus earned from referrals.
    """
    data = request.get_json()

    username = data.get('username')
    referral_code = data.get('referral_code')

    if not username:
        return jsonify({"error": "Username is required."}), 400

    # Generate a unique referral code (could be more complex in production)
    new_referral_code = f"REF-{username}"

    # Create a new user instance
    new_user = User(username=username, referral_code=new_referral_code, referred_by=referral_code)

    try:
        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        # Check if there is a referral code
        if referral_code:
            referrer = User.query.filter_by(referral_code=referral_code).first()
            if referrer:
                # Update referrer's bonus
                referrer.bonus += 10  # Example bonus amount
                db.session.commit()

        return jsonify({
            "username": username,
            "referral_code": new_referral_code,
            "bonus": new_user.bonus
        }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username or referral code already exists."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve all users and their bonuses.
    """
    users = User.query.all()
    user_list = [
        {"username": user.username, "referral_code": user.referral_code, "bonus": user.bonus}
        for user in users
    ]
    return jsonify(user_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
- Flask (`pip install Flask`)
- Flask-SQLAlchemy (`pip install Flask-SQLAlchemy`)
- SQLite (included with Python)

### Usage Instructions:
1. Start the Flask application: `python referral_system.py`
2. Use a REST client (like Postman) to make requests to the endpoints:
   - `POST /register` with JSON body `{"username": "example_user", "referral_code": "REF-X"}` to register a user.
   - `GET /users` to retrieve all users and their bonuses.
