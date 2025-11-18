"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Create a step-by-step guide for implementing a secure PIN change feature in a web application, referencing the process outlined on the Heritage Bank website (e.g., using OTP and PIN Change Number).
Generated: DETERMINISTIC_8c93bf1268b4f353
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: pin_change.py

from flask import Flask, request, jsonify
import hashlib
import random
from twilio.rest import Client

# Flask web application setup
app = Flask(__name__)

# Example database simulation
# In production, replace with a secure database system
users_db = {
    "user1": {"phone": "+1234567890", "pin": "1234"}
}

# Twilio credentials (replace with your actual credentials in production)
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

# OTP storage for validation (temporary storage, use a secure mechanism in production)
otp_storage = {}

# Helper function to hash PIN using SHA-256
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

# Step 1: Request PIN Change - Generate OTP
@app.route('/request_pin_change', methods=['POST'])
def request_pin_change():
    """
    Endpoint to request a PIN change. Generates and sends OTP to user's phone.
    """
    try:
        data = request.json
        username = data.get("username")

        # Validate username
        if username not in users_db:
            return jsonify({"error": "User not found"}), 404

        # Generate OTP
        otp = random.randint(100000, 999999)
        otp_storage[username] = otp

        # Send OTP via SMS using Twilio
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        phone_number = users_db[username]["phone"]

        client.messages.create(
            body=f"Your OTP for PIN change is {otp}",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        return jsonify({"message": "OTP sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Step 2: Validate OTP and Change PIN
@app.route('/validate_otp_and_change_pin', methods=['POST'])
def validate_otp_and_change_pin():
    """
    Endpoint to validate OTP and change the user's PIN.
    """
    try:
        data = request.json
        username = data.get("username")
        otp = data.get("otp")
        new_pin = data.get("new_pin")

        # Validate user
        if username not in users_db:
            return jsonify({"error": "User not found"}), 404
        
        # Validate OTP
        if otp_storage.get(username) != otp:
            return jsonify({"error": "Invalid OTP"}), 400

        # Validate new PIN (basic check: length and numeric)
        if not new_pin or len(new_pin) != 4 or not new_pin.isdigit():
            return jsonify({"error": "Invalid PIN format"}), 400

        # Hash the new PIN and update the user's PIN
        hashed_pin = hash_pin(new_pin)
        users_db[username]["pin"] = hashed_pin

        # Remove OTP from storage after successful usage
        del otp_storage[username]

        return jsonify({"message": "PIN changed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Step 3: Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Basic health check endpoint to verify the server is running.
    """
    return jsonify({"status": "Running"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes for Deployment:
1. Replace Twilio credentials with secure values.
2. Use a secure database (e.g., PostgreSQL, MySQL) for storing user data in production.
3. Implement HTTPS and secure headers for production readiness.
4. Limit OTP retries and implement rate limiting to prevent abuse.
5. Rotate OTP periodically to enhance security.
