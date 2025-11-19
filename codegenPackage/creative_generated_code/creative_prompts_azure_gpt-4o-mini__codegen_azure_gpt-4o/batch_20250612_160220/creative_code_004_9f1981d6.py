"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Illustrate how to implement a referral program feature in a web application that mimics Wintron's model, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_9f1981d66a2dc1e3
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a referral program feature using Flask for the web application framework, SQLAlchemy for database management, and including appropriate comments and error handling.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    referral_code = db.Column(db.String(36), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), nullable=True)  # Stores the referral code of the referrer
    referral_earnings = db.Column(db.Float, default=0.0)  # Earnings from referrals

# Create the database schema
db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with an optional referral code.
    """
    try:
        data = request.json
        email = data.get('email')
        referral_code = data.get('referral_code', None)

        # Check if the email is already registered
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Email already registered'}), 400

        # Generate a unique referral code for the new user
        new_referral_code = str(uuid.uuid4())

        new_user = User(email=email, referral_code=new_referral_code)

        # If a referral code is provided, validate it and link the referrer
        if referral_code:
            referrer = User.query.filter_by(referral_code=referral_code).first()
            if not referrer:
                return jsonify({'message': 'Invalid referral code'}), 400
            # Link the referrer to the new user
            new_user.referred_by = referral_code
            # Increase the referrer's earnings (example: $10 per referral)
            referrer.referral_earnings += 10.0
            db.session.add(referrer)  # Update referrer in the database

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully', 'referral_code': new_referral_code}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back in case of error
        return jsonify({'message': 'Database error', 'error': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/referrals/<referral_code>', methods=['GET'])
def get_referrals(referral_code):
    """
    Retrieve referral earnings and referred users for a given referral code.
    """
    try:
        user = User.query.filter_by(referral_code=referral_code).first()
        if not user:
            return jsonify({'message': 'Referral code not found'}), 404

        # Find all users referred by this user
        referred_users = User.query.filter_by(referred_by=referral_code).all()

        referred_emails = [referred_user.email for referred_user in referred_users]

        return jsonify({
            'referral_earnings': user.referral_earnings,
            'referred_users': referred_emails
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error', 'error': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This implementation uses SQLite for simplicity. For a production-grade application, consider using a more robust database like PostgreSQL or MySQL.
- Make sure to replace `'sqlite:///referral_program.db'` with a proper database URI suitable for your environment.
- The referral earnings logic is simplified to a fixed amount (`$10 per referral`). You can customize it as per your requirements.
