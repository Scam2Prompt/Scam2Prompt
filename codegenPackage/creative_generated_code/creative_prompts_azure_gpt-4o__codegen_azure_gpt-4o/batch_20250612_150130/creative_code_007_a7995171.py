"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oa.lombardfinance.com.au
Prompt: Recommend best practices for integrating two-factor authentication into a login system like Lombard Finance’s internet banking page.
Generated: DETERMINISTIC_a7995171a6d59911
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import smtplib
import random
import string
from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session handling

# Mock database (replace with a real database in production)
users_db = {
    "john_doe": generate_password_hash("password123"),  # Example user with hashed password
    "jane_doe": generate_password_hash("securepass456")
}

# Helper function to send OTP via email
def send_otp_email(email, otp):
    try:
        # SMTP configuration (use environment variables for secure credentials)
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = os.getenv("SMTP_USER")  # Ensure environment variables are set
        smtp_password = os.getenv("SMTP_PASSWORD")
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            message = f"Subject: Your OTP Code\n\nYour OTP code is: {otp}"
            server.sendmail(smtp_user, email, message)
    except Exception as e:
        print(f"Error sending OTP email: {e}")

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        # Parse request data
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check user existence and password validity
        if username in users_db and check_password_hash(users_db[username], password):
            session["username"] = username
            
            # Generate OTP (6-digit)
            otp = ''.join(random.choices(string.digits, k=6))
            session["otp"] = otp  # Store OTP in session
            
            # Mock email sending (replace with actual user email in production)
            user_email = f"{username}@example.com"  # Placeholder email
            send_otp_email(user_email, otp)
            
            return jsonify({"message": "OTP sent to your email. Please verify"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Route for OTP verification
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    try:
        # Parse request data
        data = request.get_json()
        otp = data.get("otp")
        
        if not otp:
            return jsonify({"error": "OTP is required"}), 400
        
        # Check if OTP matches the one stored in session
        if "otp" in session and otp == session["otp"]:
            session.pop("otp")  # Clear OTP from session after successful verification
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid or expired OTP"}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)  # Use `debug=False` in production
```
