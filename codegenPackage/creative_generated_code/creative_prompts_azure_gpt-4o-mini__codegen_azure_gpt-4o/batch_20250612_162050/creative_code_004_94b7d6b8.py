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
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory storage for simplicity (use a database in production)
users = {}
referrals = {}

# Configurations (set environment variables in production)
REFERRAL_BONUS = 10  # Example bonus amount for successful referrals
BONUS_EXPIRY_DAYS = 30  # Referral bonus expiration period
MAX_REFERRALS_PER_USER = 5  # Limit referrals to avoid abuse

# Utility function to generate unique referral codes
def generate_referral_code():
    return str(uuid.uuid4())[:8]  # Short UUID for simplicity

@app.route('/api/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    If a referral code is provided, validate and apply referral bonuses.
    """
    data = request.json

    # Validate input
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required."}), 400

    if data.get('email') in users:
        return jsonify({"error": "User already exists."}), 400

    # Create new user
    user_id = str(uuid.uuid4())
    referral_code = generate_referral_code()
    users[data['email']] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "referral_code": referral_code,
        "referral_bonus": 0,
        "referrals_made": 0,
        "joined_at": datetime.now(),
    }

    # Process referral code if provided
    referred_by = data.get('referral_code')
    if referred_by:
        referring_user = next((user for user in users.values() if user["referral_code"] == referred_by), None)
        if referring_user:
            if referring_user["referrals_made"] < MAX_REFERRALS_PER_USER:
                referring_user["referral_bonus"] += REFERRAL_BONUS
                referring_user["referrals_made"] += 1
                referrals[user_id] = {
                    "referred_by": referring_user["id"],
                    "bonus_expiry": datetime.now() + timedelta(days=BONUS_EXPIRY_DAYS),
                }
            else:
                return jsonify({"error": "Referral limit reached for this user."}), 400
        else:
            return jsonify({"error": "Invalid referral code."}), 400

    return jsonify({"message": "User registered successfully!", "referral_code": referral_code}), 201

@app.route('/api/referrals/<email>', methods=['GET'])
def get_referrals(email):
    """
    Get referral details and bonuses for a user.
    """
    user = users.get(email)
    if not user:
        return jsonify({"error": "User not found."}), 404

    user_referrals = [
        {"referred_user_id": r_id, "bonus_expiry": r_data["bonus_expiry"]}
        for r_id, r_data in referrals.items()
        if r_data["referred_by"] == user["id"]
    ]

    return jsonify({
        "referral_bonus": user["referral_bonus"],
        "referrals_made": user["referrals_made"],
        "referrals": user_referrals,
    }), 200

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle internal server errors gracefully.
    """
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Entry point for running the server
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
