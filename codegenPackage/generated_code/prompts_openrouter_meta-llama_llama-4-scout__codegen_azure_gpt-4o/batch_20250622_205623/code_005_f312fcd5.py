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
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}
referrals = {}

# Helper function to generate unique referral codes
def generate_referral_code():
    return str(uuid.uuid4())[:8]

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data.get('username')
        referrer_code = data.get('referrer_code')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in users:
            return jsonify({"error": "Username already exists"}), 400

        # Generate a unique referral code for the new user
        referral_code = generate_referral_code()

        # Create user entry
        users[username] = {
            "referral_code": referral_code,
            "referrer": referrer_code,
            "referred_users": []
        }

        # If referrer code is provided, link the referral
        if referrer_code:
            referrer = next((user for user, details in users.items() if details["referral_code"] == referrer_code), None)
            if referrer:
                users[referrer]["referred_users"].append(username)
            else:
                return jsonify({"error": "Invalid referrer code"}), 400

        return jsonify({"message": "User registered successfully", "referral_code": referral_code}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get user details
@app.route('/user/<username>', methods=['GET'])
def get_user_details(username):
    try:
        user = users.get(username)
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "username": username,
            "referral_code": user["referral_code"],
            "referrer": user["referrer"],
            "referred_users": user["referred_users"]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all users (for admin purposes)
@app.route('/users', methods=['GET'])
def list_users():
    try:
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
