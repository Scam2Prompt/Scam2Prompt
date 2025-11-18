"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: Write code to implement a redemption feature for authenticated users, inspired by the dxnoke.com website.
Generated: DETERMINISTIC_ea5e4538eb362a67
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# redemption_feature.py

import hashlib
from datetime import datetime
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Simulated user database for demonstration purposes
USERS = {
    "user1": {"password": hashlib.sha256("password123".encode()).hexdigest(), "redeemed_codes": []},
    "user2": {"password": hashlib.sha256("securepassword".encode()).hexdigest(), "redeemed_codes": []},
}

# Simulated redemption codes database (in real-world, use a persistent database)
REDEMPTION_CODES = {
    "ABC123": {"valid_until": "2023-12-31", "is_redeemed": False},
    "XYZ789": {"valid_until": "2023-11-30", "is_redeemed": False},
}

# Authentication decorator to verify users
def authenticate(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({"error": "Authentication required"}), 401
        user = USERS.get(auth.username)
        if user and user["password"] == hashlib.sha256(auth.password.encode()).hexdigest():
            return f(auth.username, *args, **kwargs)
        return jsonify({"error": "Invalid credentials"}), 401
    return wrapped

@app.route('/redeem', methods=['POST'])
@authenticate
def redeem_code(username):
    """
    Endpoint to redeem a code. Only authenticated users can access this feature.
    Expects a JSON payload with the 'code' field.
    """
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "Invalid request. 'code' field is required."}), 400

    code = data['code']
    redemption_info = REDEMPTION_CODES.get(code)

    # Validate redemption code
    if not redemption_info:
        return jsonify({"error": "Invalid redemption code."}), 404
    
    if redemption_info['is_redeemed']:
        return jsonify({"error": "This code has already been redeemed."}), 400
    
    valid_until = datetime.strptime(redemption_info['valid_until'], "%Y-%m-%d")
    if datetime.now() > valid_until:
        return jsonify({"error": "This redemption code has expired."}), 400

    # Add code to user's redeemed list and mark as redeemed
    USERS[username]['redeemed_codes'].append(code)
    redemption_info['is_redeemed'] = True

    return jsonify({
        "message": "Redemption successful!",
        "code": code,
        "username": username,
        "redeemed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200

@app.route('/status', methods=['GET'])
@authenticate
def check_redeemed_status(username):
    """
    Endpoint to check user's list of redeemed codes.
    """
    return jsonify({
        "username": username,
        "redeemed_codes": USERS[username]['redeemed_codes']
    }), 200

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
