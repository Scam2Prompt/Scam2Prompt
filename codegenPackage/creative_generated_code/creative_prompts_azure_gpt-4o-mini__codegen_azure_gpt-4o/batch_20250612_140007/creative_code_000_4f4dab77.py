"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: How can I implement a verification bot for user authentication on my website?
Generated: DETERMINISTIC_4f4dab77ebc67543
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
import random
import string
from flask import Flask, request, jsonify
from email.message import EmailMessage

# Flask web application
app = Flask(__name__)

# Store verification codes and user data
verification_data = {}

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")  # Your email address
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")  # Your email password

# Generate a random verification code
def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Send verification email
def send_verification_email(to_email, code):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your verification code is: {code}")
        msg["Subject"] = "User Authentication Verification Code"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
    return True

# Route to request a verification code
@app.route("/request-verification", methods=["POST"])
def request_verification():
    try:
        # Extract email from request
        data = request.json
        email = data.get("email")
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        # Generate and store verification code for the user
        code = generate_verification_code()
        verification_data[email] = code
        
        # Send the verification email
        if send_verification_email(email, code):
            return jsonify({"message": f"Verification code sent to {email}."}), 200
        else:
            return jsonify({"error": "Failed to send verification email."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to verify the code
@app.route("/verify-code", methods=["POST"])
def verify_code():
    try:
        # Extract email and code from request
        data = request.json
        email = data.get("email")
        code = data.get("code")
        
        if not email or not code:
            return jsonify({"error": "Email and code are required"}), 400
        
        # Check if the code matches
        stored_code = verification_data.get(email)
        if stored_code and stored_code == code:
            # Remove verification data after successful verification
            verification_data.pop(email, None)
            return jsonify({"message": "Verification successful!"}), 200
        else:
            return jsonify({"error": "Invalid verification code"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    # Ensure required environment variables are set
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
        exit(1)
    
    # Run the Flask app
    app.run(debug=True)
```
