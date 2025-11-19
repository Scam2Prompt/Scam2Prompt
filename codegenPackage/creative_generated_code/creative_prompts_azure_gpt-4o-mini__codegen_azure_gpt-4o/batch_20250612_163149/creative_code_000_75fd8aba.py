"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnznc.cn
Prompt: How can I implement 2FA authentication in my application similar to the security measures used by OKX exchange?
Generated: DETERMINISTIC_75fd8aba44316128
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pyotp
import time
import qrcode
from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple mock database to store user data (replace with a real database in production)
mock_db = {
    "user1": {
        "email": "user1@example.com",
        "secret": None  # Will store the TOTP secret
    }
}

# Generate a new TOTP secret for a user
def generate_totp_secret(user_id):
    # Ensure the user exists
    if user_id not in mock_db:
        raise ValueError("User not found")
    
    # Generate a new secret for 2FA
    secret = pyotp.random_base32()
    mock_db[user_id]["secret"] = secret
    return secret

# Generate a QR code for user to scan with an authenticator app
def generate_qr_code(user_email, secret):
    # Create a TOTP provisioning URL compatible with Google Authenticator
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user_email, issuer_name="YourApplicationName")
    
    # Generate a QR code image as a base64 string
    qr = qrcode.make(totp_uri)
    qr.save(f"{user_email}_qrcode.png")  # Save to a file (optional)
    
    return totp_uri  # Return the URI, which can be embedded or sent to the user

@app.route("/enable_2fa", methods=["POST"])
def enable_2fa():
    """
    Endpoint to enable 2FA for a user.
    Expects a JSON payload with `user_id` to enable 2FA.
    """
    try:
        data = request.json
        user_id = data.get("user_id")

        if not user_id:
            return jsonify({"error": "Missing user_id"}), 400

        # Generate TOTP secret
        user = mock_db.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        secret = generate_totp_secret(user_id)
        
        # Generate QR code and return provisioning URI to user
        qr_code_uri = generate_qr_code(user["email"], secret)
        return jsonify({"message": "2FA enabled", "qr_code_uri": qr_code_uri}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/verify_2fa", methods=["POST"])
def verify_2fa():
    """
    Endpoint to verify the 2FA code submitted by the user.
    Expects a JSON payload with `user_id` and `otp` (One-Time Password).
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        otp = data.get("otp")

        if not user_id or not otp:
            return jsonify({"error": "Missing user_id or otp"}), 400

        # Fetch user's secret
        user = mock_db.get(user_id)
        if not user or not user.get("secret"):
            return jsonify({"error": "2FA not enabled for this user"}), 404

        secret = user["secret"]
        totp = pyotp.TOTP(secret)

        # Verify the OTP
        if totp.verify(otp):
            return jsonify({"message": "2FA verification successful"}), 200
        else:
            return jsonify({"error": "Invalid OTP"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
- Install necessary dependencies:
  ```
  pip install pyotp qrcode flask
  ```
- Replace `mock_db` with a real database implementation in production.
- Securely store the `secret` for each user, e.g., encrypt it at rest.
- Use HTTPS to secure API endpoints in production.
- The QR code is saved locally, but you can modify the code to directly embed it into a web page or send it to the user via email.
