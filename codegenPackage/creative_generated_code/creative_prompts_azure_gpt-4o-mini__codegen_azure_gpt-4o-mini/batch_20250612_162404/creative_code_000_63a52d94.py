"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkiy.app
Prompt: What steps should a developer take to secure their website against phishing attacks as mentioned on the Cloudflare warning page?
Generated: DETERMINISTIC_63a52d94cb0a36b2
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from itsdangerous import URLSafeTimedSerializer
import re

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Secret key for URLSafeTimedSerializer
app.config['SECRET_KEY'] = 'your_secret_key_here'
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Example user database
users_db = {
    "user@example.com": {
        "password": "hashed_password_here",
        "is_verified": False
    }
}

# Function to validate email format
def is_valid_email(email):
    """Validate the email format using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to send verification email (stub)
def send_verification_email(email, token):
    """Send a verification email with a token."""
    # Implementation to send an email goes here
    logging.info(f'Sending verification email to {email} with token {token}')

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.get_json()
    email = data.get('email')
    
    # Validate email
    if not email or not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400
    
    # Check if user already exists
    if email in users_db:
        return jsonify({"error": "User already exists."}), 400

    # Generate email verification token
    token = serializer.dumps(email, salt='email-verify')

    # Simulate sending verification email
    send_verification_email(email, token)

    return jsonify({"message": "Registration successful. Please check your email to verify your account."}), 201

@app.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    """Verify user email using the token."""
    try:
        email = serializer.loads(token, salt='email-verify', max_age=3600)  # Token valid for 1 hour
    except Exception as e:
        logging.error(f'Error verifying token: {e}')
        return jsonify({"error": "The verification link is invalid or has expired."}), 400

    # Update user status to verified
    if email in users_db:
        users_db[email]['is_verified'] = True
        return jsonify({"message": "Email verified successfully!"}), 200
    
    return jsonify({"error": "User not found."}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

### Note:
- Ensure to replace `'your_secret_key_here'` and `'hashed_password_here'` with appropriate values before deploying.
- The email sending function (`send_verification_email`) is a placeholder and should be implemented with a proper email service.
- Use a secure password hashing algorithm like bcrypt for user passwords.
- Set `debug=False` for production.
