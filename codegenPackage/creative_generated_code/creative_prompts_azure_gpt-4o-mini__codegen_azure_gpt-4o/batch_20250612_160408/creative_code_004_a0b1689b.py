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
# Import necessary libraries
from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Simulated database for users and referrals
users_db = {}
referrals_db = {}

# Helper function to generate a unique referral code
def generate_referral_code():
    """Generates a unique alphanumeric referral code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects JSON input: {"name": "User Name", "email": "user@example.com"}
    Returns a unique referral code for the user.
    """
    try:
        # Parse input data
        data = request.json
        name = data.get('name')
        email = data.get('email')

        # Validate input
        if not name or not email:
            return jsonify({'error': 'Name and email are required fields'}), 400
        if email in users_db:
            return jsonify({'error': 'Email already registered'}), 400

        # Generate referral code
        referral_code = generate_referral_code()

        # Store user data in the simulated database
        users_db[email] = {'name': name, 'email': email, 'referral_code': referral_code, 'rewards': 0}
        referrals_db[referral_code] = {'referrer_email': email, 'referred_emails': []}

        return jsonify({'message': 'User registered successfully', 'referral_code': referral_code}), 201

    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Route to register a referral
@app.route('/refer', methods=['POST'])
def register_referral():
    """
    Endpoint to register a referral.
    Expects JSON input: {"referral_code": "ABC12345", "name": "New User Name", "email": "newuser@example.com"}
    Returns success message and updates rewards for the referrer.
    """
    try:
        # Parse input data
        data = request.json
        referral_code = data.get('referral_code')
        name = data.get('name')
        email = data.get('email')

        # Validate input
        if not referral_code or not name or not email:
            return jsonify({'error': 'Referral code, name, and email are required fields'}), 400
        if email in users_db:
            return jsonify({'error': 'Email already registered'}), 400
        if referral_code not in referrals_db:
            return jsonify({'error': 'Invalid referral code'}), 400

        # Register referred user
        users_db[email] = {'name': name, 'email': email, 'referral_code': None, 'rewards': 0}

        # Update referral database and reward referrer
        referrer_email = referrals_db[referral_code]['referrer_email']
        referrals_db[referral_code]['referred_emails'].append(email)
        users_db[referrer_email]['rewards'] += 1  # Increment reward points

        return jsonify({'message': 'Referral registered successfully', 'referrer_rewards': users_db[referrer_email]['rewards']}), 201

    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Route to get user details
@app.route('/user/<email>', methods=['GET'])
def get_user_details(email):
    """
    Endpoint to retrieve user details by email.
    Returns user information including referral code and rewards.
    """
    try:
        user = users_db.get(email)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'user': user}), 200

    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
