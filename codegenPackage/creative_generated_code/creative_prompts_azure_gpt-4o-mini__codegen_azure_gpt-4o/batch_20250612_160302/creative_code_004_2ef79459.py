"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: How can I implement a referral program in my investment platform like the one described on Zadepositslot?
Generated: DETERMINISTIC_2ef79459453c4200
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Database simulation (for demonstration purposes)
users = {}
referrals = {}

# Helper function to generate unique referral codes
def generate_referral_code():
    return str(uuid.uuid4())[:8]

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Each registered user gets a unique referral code.
    """
    try:
        data = request.json
        username = data.get('username')
        if not username:
            return jsonify({'error': 'Username is required'}), 400

        if username in users:
            return jsonify({'error': 'Username already exists'}), 400

        # Generate referral code for the new user
        referral_code = generate_referral_code()
        users[username] = {
            'referral_code': referral_code,
            'referrals': []
        }
        
        return jsonify({'message': 'User registered successfully', 'referral_code': referral_code}), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred during registration', 'details': str(e)}), 500

@app.route('/use-referral', methods=['POST'])
def use_referral():
    """
    Endpoint for a user to register using another user's referral code.
    """
    try:
        data = request.json
        referrer_code = data.get('referrer_code')
        new_username = data.get('new_username')

        if not referrer_code or not new_username:
            return jsonify({'error': 'Referrer code and new username are required'}), 400

        if new_username in users:
            return jsonify({'error': 'Username already exists'}), 400

        # Find the referrer by their referral code
        referrer = None
        for user, info in users.items():
            if info['referral_code'] == referrer_code:
                referrer = user
                break

        if not referrer:
            return jsonify({'error': 'Invalid referral code'}), 400

        # Register the new user
        referral_code = generate_referral_code()
        users[new_username] = {
            'referral_code': referral_code,
            'referrals': []
        }

        # Add the new user to the referrer's referral list
        users[referrer]['referrals'].append(new_username)

        return jsonify({'message': 'User registered successfully via referral', 'referral_code': referral_code}), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the referral', 'details': str(e)}), 500

@app.route('/referrals/<username>', methods=['GET'])
def get_referrals(username):
    """
    Endpoint to retrieve all referrals for a given user.
    """
    try:
        user = users.get(username)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'referrals': user['referrals']}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving referrals', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a simple referral program using `Flask` where users can register and generate referral codes. These codes can then be used by others to register and be tracked under the original user's referral list.
