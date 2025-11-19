"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: Generate an API call that verifies user credentials for accessing a password-protected store.
Generated: DETERMINISTIC_38b751200536c32d
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data: In production, replace with a secure database
USER_DATA = {
    "username": "user1",
    "password_hash": hashlib.sha256("securepassword".encode()).hexdigest(),  # Pre-hashed password
}

@app.route('/verify-credentials', methods=['POST'])
def verify_credentials():
    """
    Endpoint to verify user credentials for accessing a password-protected store.
    Expects JSON payload with 'username' and 'password' fields.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, JSON payload required"}), 400

        # Validate required fields
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return jsonify({"error": "Both 'username' and 'password' are required"}), 400

        # Check if the username exists in the mock database
        if USER_DATA.get("username") != username:
            return jsonify({"error": "Invalid username or password"}), 401

        # Hash the provided password to compare with the stored hash
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if USER_DATA.get("password_hash") != password_hash:
            return jsonify({"error": "Invalid username or password"}), 401

        # Success response
        return jsonify({"message": "Credentials verified successfully"}), 200

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
