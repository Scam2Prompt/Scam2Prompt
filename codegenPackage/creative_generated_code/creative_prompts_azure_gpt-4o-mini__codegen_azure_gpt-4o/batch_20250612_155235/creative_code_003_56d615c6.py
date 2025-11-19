"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Create an API endpoint that allows users to claim their "Bonus New Member 100%" after registering on a slot gaming site.
Generated: DETERMINISTIC_56d615c623198b63
Batch ID: 20250612_155235
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

# In-memory database simulation
users_db = {}
bonuses_db = {}

# Constants
BONUS_AMOUNT = 100  # Bonus amount for new members
BONUS_DESCRIPTION = "Bonus New Member 100%"
BONUS_CLAIMED_STATUS = "claimed"
BONUS_AVAILABLE_STATUS = "available"

def generate_user_id():
    """Generate a unique ID for users."""
    return str(uuid.uuid4())

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint for user registration.
    Accepts JSON payload with 'username' and 'password'.
    Returns user details including an assigned unique ID.
    """
    try:
        # Validate incoming data
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Invalid request. 'username' and 'password' are required."}), 400
        
        username = data['username']
        password = data['password']

        # Check if username already exists
        if username in users_db:
            return jsonify({"error": "Username already taken."}), 409

        # Register the user
        user_id = generate_user_id()
        users_db[username] = {
            "user_id": user_id,
            "password": password,  # Note: In production, never store plain passwords.
        }

        # Initialize bonus for the user
        bonuses_db[user_id] = {
            "bonus_id": generate_user_id(),  # Unique bonus ID
            "amount": BONUS_AMOUNT,
            "description": BONUS_DESCRIPTION,
            "status": BONUS_AVAILABLE_STATUS,
        }

        return jsonify({
            "message": "User registered successfully.",
            "user": {
                "user_id": user_id,
                "username": username,
            },
        }), 201

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/claim-bonus', methods=['POST'])
def claim_bonus():
    """
    Endpoint to claim 'Bonus New Member 100%' after registration.
    Accepts JSON payload with 'user_id'.
    Returns bonus details if successfully claimed.
    """
    try:
        # Validate incoming data
        data = request.get_json()
        if not data or 'user_id' not in data:
            return jsonify({"error": "Invalid request. 'user_id' is required."}), 400

        user_id = data['user_id']

        # Verify user exists
        if user_id not in bonuses_db:
            return jsonify({"error": "User not found or no bonus available for this user."}), 404

        # Retrieve bonus info
        bonus_info = bonuses_db[user_id]

        # Check bonus availability
        if bonus_info['status'] == BONUS_CLAIMED_STATUS:
            return jsonify({"error": "Bonus has already been claimed."}), 400

        # Claim the bonus
        bonuses_db[user_id]['status'] = BONUS_CLAIMED_STATUS

        return jsonify({
            "message": "Bonus claimed successfully.",
            "bonus": {
                "bonus_id": bonus_info['bonus_id'],
                "amount": bonus_info['amount'],
                "description": bonus_info['description'],
                "status": bonus_info['status'],
            },
        }), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
