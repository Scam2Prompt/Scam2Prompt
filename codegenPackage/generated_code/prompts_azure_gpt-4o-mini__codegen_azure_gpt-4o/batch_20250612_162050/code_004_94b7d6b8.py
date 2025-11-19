"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Illustrate how to implement a referral program API to enhance customer engagement, similar to the one described on The Digital Age's site.
Generated: DETERMINISTIC_94b7d6b8c219c51f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}  # Stores user data
referrals = {}  # Stores referral data

# Constants
REFERRAL_BONUS = 10  # Bonus points for successful referrals
EXPIRATION_DAYS = 30  # Referral code expiration period

# Helper function to generate unique referral codes
def generate_referral_code():
    return str(uuid.uuid4())[:8]

# Helper function to validate referral codes
def is_referral_code_valid(referral_code):
    referral = referrals.get(referral_code)
    if not referral:
        return False
    if datetime.now() > referral['expires_at']:
        return False
    return True

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
        referral_code = data.get('referral_code')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        if email in users:
            return jsonify({'error': 'Email already registered'}), 400

        # Create new user
        user_id = str(uuid.uuid4())
        users[email] = {
            'id': user_id,
            'name': name,
            'email': email,
            'points': 0,
            'referral_code': generate_referral_code(),
            'referred_by': None
        }

        # Handle referral code if provided
        if referral_code:
            if is_referral_code_valid(referral_code):
                referrer_email = referrals[referral_code]['referrer_email']
                users[email]['referred_by'] = referrer_email
                users[referrer_email]['points'] += REFERRAL_BONUS
                referrals[referral_code]['uses'] += 1
            else:
                return jsonify({'error': 'Invalid or expired referral code'}), 400

        # Generate a referral entry for the new user
        referrals[users[email]['referral_code']] = {
            'referrer_email': email,
            'created_at': datetime.now(),
            'expires_at': datetime.now() + timedelta(days=EXPIRATION_DAYS),
            'uses': 0
        }

        return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred during registration', 'details': str(e)}), 500

@app.route('/referral/<email>', methods=['GET'])
def get_referral_info(email):
    """
    Endpoint to retrieve referral information for a user.
    """
    try:
        user = users.get(email)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        referral_code = user['referral_code']
        referral_data = referrals.get(referral_code, {})
        return jsonify({
            'referral_code': referral_code,
            'points': user['points'],
            'referral_uses': referral_data.get('uses', 0),
            'referral_expires_at': referral_data.get('expires_at', None)
        }), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching referral info', 'details': str(e)}), 500

@app.route('/users', methods=['GET'])
def list_users():
    """
    Endpoint to list all registered users (for demonstration purposes).
    """
    try:
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching users', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
