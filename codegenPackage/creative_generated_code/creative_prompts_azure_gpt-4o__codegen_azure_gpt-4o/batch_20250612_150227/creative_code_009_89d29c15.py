"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binarygoldenoptions.com
Prompt: Generate code to implement a secure password reset feature for an investment platform, similar to the one described on Binary Golden Options.
Generated: DETERMINISTIC_89d29c1577f4ada9
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import hashlib
import secrets
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database for demonstration purposes
mock_db = {
    "users": {},  # Example structure: {email: {"password_hash": ..., "reset_token": ..., "token_expiry": ...}}
}

# Helper function to generate a secure token
def generate_secure_token():
    return secrets.token_urlsafe(32)

# Helper function to hash a password securely
def hash_password(password):
    return generate_password_hash(password)

# Password reset request endpoint
@app.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    try:
        data = request.get_json()
        email = data.get("email")
        
        # Validate input
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        user = mock_db["users"].get(email)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Generate reset token and expiry
        reset_token = generate_secure_token()
        token_expiry = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
        
        # Save reset token and expiry in the database
        user["reset_token"] = reset_token
        user["token_expiry"] = token_expiry
        
        # Simulate sending the reset email (replace with actual email logic)
        print(f"Password reset token for {email}: {reset_token}")
        
        return jsonify({"message": "Password reset email sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Password reset endpoint
@app.route('/reset-password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
        email = data.get("email")
        reset_token = data.get("reset_token")
        new_password = data.get("new_password")
        
        # Validate input
        if not email or not reset_token or not new_password:
            return jsonify({"error": "Email, reset token, and new password are required"}), 400
        
        user = mock_db["users"].get(email)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        # Verify reset token and expiry
        if user.get("reset_token") != reset_token:
            return jsonify({"error": "Invalid reset token"}), 403
        
        if datetime.utcnow() > user.get("token_expiry"):
            return jsonify({"error": "Reset token has expired"}), 403
        
        # Hash the new password and save it in the database
        user["password_hash"] = hash_password(new_password)
        
        # Clear reset token and expiry
        user["reset_token"] = None
        user["token_expiry"] = None
        
        return jsonify({"message": "Password reset successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a user for testing purposes (this would normally be done through registration)
@app.route('/add-user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        
        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        
        if email in mock_db["users"]:
            return jsonify({"error": "User already exists"}), 400
        
        # Add user to the database with hashed password
        mock_db["users"][email] = {"password_hash": hash_password(password), "reset_token": None, "token_expiry": None}
        
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
