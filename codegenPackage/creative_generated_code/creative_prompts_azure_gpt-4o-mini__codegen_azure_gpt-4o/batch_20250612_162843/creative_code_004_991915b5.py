"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Provide an example of a secure password reset function for a TMS application, referencing the user authentication process used in MultiTMS.
Generated: DETERMINISTIC_991915b5ef8d1cb0
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import secrets
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Mock database (replace with actual database connection in production)
mock_db = {
    "users": {
        "user@example.com": {
            "password_hash": generate_password_hash("SecurePassword123!"),
            "reset_token": None,
            "token_expiry": None
        }
    }
}


def generate_secure_token():
    """
    Generate a cryptographically secure token for password reset.
    """
    return secrets.token_hex(32)


@app.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    """
    Endpoint to request a password reset. Generates a secure token and sets expiry.
    """
    try:
        email = request.json.get('email')
        if not email or email not in mock_db["users"]:
            return jsonify({"error": "Invalid email address"}), 400

        # Generate reset token and expiry
        reset_token = generate_secure_token()
        token_expiry = datetime.utcnow() + timedelta(minutes=30)  # Token valid for 30 minutes

        # Store token and expiry in the database
        mock_db["users"][email]["reset_token"] = reset_token
        mock_db["users"][email]["token_expiry"] = token_expiry

        # In production, send this token as a part of an email to the user
        return jsonify({"message": "Password reset token generated", "reset_token": reset_token}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/reset-password', methods=['POST'])
def reset_password():
    """
    Endpoint to reset the password using the token.
    """
    try:
        email = request.json.get('email')
        new_password = request.json.get('new_password')
        reset_token = request.json.get('reset_token')

        if not email or email not in mock_db["users"]:
            return jsonify({"error": "Invalid email address"}), 400

        user = mock_db["users"][email]
        # Validate reset token
        if user["reset_token"] != reset_token or datetime.utcnow() > user["token_expiry"]:
            return jsonify({"error": "Invalid or expired reset token"}), 400

        # Validate password strength (basic example)
        if len(new_password) < 8 or not any(char.isdigit() for char in new_password) or not any(char.isupper() for char in new_password):
            return jsonify({"error": "Password does not meet complexity requirements"}), 400

        # Update the password and clear the reset token
        user["password_hash"] = generate_password_hash(new_password)
        user["reset_token"] = None
        user["token_expiry"] = None

        return jsonify({"message": "Password successfully reset"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
