"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypr.pages.dev
Prompt: Create an API endpoint that allows users to connect and join a service using referral codes, similar to the functionality described on Hyperliquid.
Generated: DETERMINISTIC_d3e76bab227d1edd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database simulation
users = {}
referral_codes = {}

# Endpoint to join the service using a referral code
@app.route('/join', methods=['POST'])
def join_service():
    """
    API endpoint to join the service using a referral code.
    Expects JSON payload: {"username": "<username>", "referral_code": "<referral_code>"}
    """
    try:
        # Extract data from the request payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        username = data.get('username')
        referral_code = data.get('referral_code')

        # Input validation
        if not username or not referral_code:
            return jsonify({"error": "Username and referral code are required"}), 400

        # Check if user already exists
        if username in users:
            return jsonify({"error": "User already exists"}), 409

        # Validate referral code
        if referral_code not in referral_codes:
            return jsonify({"error": "Invalid referral code"}), 404

        # Create a new user and link the referral code
        user_id = str(uuid4())  # Generate unique user ID
        users[username] = {
            "user_id": user_id,
            "username": username,
            "referral_code": referral_code
        }

        # Update referral usage count
        referral_codes[referral_code]['usage_count'] += 1

        return jsonify({
            "message": "User successfully joined",
            "user": users[username]
        }), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Endpoint to create a referral code
@app.route('/create_referral_code', methods=['POST'])
def create_referral_code():
    """
    API endpoint to create a new referral code.
    Expects JSON payload: {"creator_username": "<creator_username>"}
    """
    try:
        # Extract data from the request payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        creator_username = data.get('creator_username')
        
        # Input validation
        if not creator_username:
            return jsonify({"error": "Creator username is required"}), 400

        # Check if creator exists
        if creator_username not in users:
            return jsonify({"error": "Creator does not exist"}), 404

        # Generate a new referral code
        referral_code = str(uuid4())
        referral_codes[referral_code] = {
            "creator": creator_username,
            "usage_count": 0
        }

        return jsonify({
            "message": "Referral code successfully created",
            "referral_code": referral_code
        }), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Endpoint to get referral code details
@app.route('/referral_code/<referral_code>', methods=['GET'])
def get_referral_code(referral_code):
    """
    API endpoint to retrieve details of a referral code.
    """
    try:
        # Validate referral code
        if referral_code not in referral_codes:
            return jsonify({"error": "Referral code not found"}), 404

        # Return referral code details
        return jsonify(referral_codes[referral_code]), 200

    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
