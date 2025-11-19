"""
Generated Code Metadata:
========================
Original URL: https://hypurrfiapp.com
Prompt: "How can I implement HypurrFi's referral system in my web application, and what are the benefits of using it?"
Generated: DETERMINISTIC_9fbe14138d8a5e92
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Referral System Implementation for HypurrFi in a Web Application

This code demonstrates how to implement a referral system for HypurrFi.
The system allows users to generate referral codes, track referrals, and reward users for successful referrals.

Benefits of using HypurrFi's referral system:
1. Increased user engagement and acquisition.
2. Incentivized sharing of the platform.
3. Easy tracking of referral performance.
4. Boosts brand loyalty and growth.

Dependencies:
- Flask: Web framework for Python.
- SQLAlchemy: ORM for database interactions.
- SQLite: Lightweight database for demonstration purposes.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    """
    User model to store user information and referral codes.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    referral_code = db.Column(db.String(50), unique=True, nullable=False)
    referred_by = db.Column(db.String(50), nullable=True)  # Stores the referral code of the referrer

class Referral(db.Model):
    """
    Referral model to track referrals and their status.
    """
    id = db.Column(db.Integer, primary_key=True)
    referrer_code = db.Column(db.String(50), nullable=False)  # Referral code of the referrer
    referred_email = db.Column(db.String(100), nullable=False)  # Email of the referred user
    status = db.Column(db.String(20), default="pending")  # Status: pending, completed, failed

# Create database tables
with app.app_context():
    db.create_all()

# Helper function to generate unique referral codes
def generate_referral_code():
    return str(uuid.uuid4())[:8]  # Generate a short unique code

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Accepts JSON payload with 'name', 'email', and optional 'referral_code'.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        referral_code = data.get('referral_code')  # Optional referral code

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Check if email is already registered
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email is already registered"}), 400

        # Generate a unique referral code for the new user
        new_referral_code = generate_referral_code()

        # Create a new user
        new_user = User(name=name, email=email, referral_code=new_referral_code, referred_by=referral_code)
        db.session.add(new_user)

        # Track referral if a referral code was provided
        if referral_code:
            referral = Referral(referrer_code=referral_code, referred_email=email)
            db.session.add(referral)

        db.session.commit()

        return jsonify({"message": "User registered successfully", "referral_code": new_referral_code}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get referral statistics for a user
@app.route('/referrals/<referral_code>', methods=['GET'])
def get_referral_stats(referral_code):
    """
    Endpoint to retrieve referral statistics for a given referral code.
    """
    try:
        # Validate referral code
        user = User.query.filter_by(referral_code=referral_code).first()
        if not user:
            return jsonify({"error": "Invalid referral code"}), 404

        # Get referrals made by the user
        referrals = Referral.query.filter_by(referrer_code=referral_code).all()
        referral_data = [
            {"referred_email": r.referred_email, "status": r.status} for r in referrals
        ]

        return jsonify({"referral_code": referral_code, "referrals": referral_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update referral status
@app.route('/referrals/update', methods=['POST'])
def update_referral_status():
    """
    Endpoint to update the status of a referral.
    Accepts JSON payload with 'referred_email' and 'status'.
    """
    try:
        data = request.json
        referred_email = data.get('referred_email')
        status = data.get('status')

        if not referred_email or not status:
            return jsonify({"error": "Referred email and status are required"}), 400

        # Find the referral
        referral = Referral.query.filter_by(referred_email=referred_email).first()
        if not referral:
            return jsonify({"error": "Referral not found"}), 404

        # Update the status
        referral.status = status
        db.session.commit()

        return jsonify({"message": "Referral status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
