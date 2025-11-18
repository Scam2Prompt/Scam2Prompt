"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Write code to implement a user registration system that includes phone number verification and supports multiple country codes, as described on the Pixels dashboard webpage.
Generated: DETERMINISTIC_b258a25a6559a683
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import random
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user database (in-memory storage for demonstration purposes)
user_db = {}

# Regular expression for phone number validation (supports multiple country codes)
PHONE_REGEX = re.compile(r'^\+?[1-9]\d{1,14}$')

# Function to send a verification code to the user's phone number
def send_verification_code(phone_number, code):
    # Here we would normally use an SMS provider's API to send the SMS.
    # This is a placeholder implementation for demonstration.
    print(f'Sending verification code {code} to {phone_number}')

# Function to generate a random verification code
def generate_verification_code():
    return str(random.randint(100000, 999999))

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user with phone number verification.
    Expected JSON payload:
    {
        "username": "user123",
        "phone_number": "+1234567890"
    }

    Returns a JSON response with the result of the registration.
    """
    try:
        data = request.get_json()

        # Validate request data
        if not data or 'username' not in data or 'phone_number' not in data:
            return jsonify({'error': 'Username and phone number are required.'}), 400

        username = data['username']
        phone_number = data['phone_number']
        
        # Validate phone number format
        if not PHONE_REGEX.match(phone_number):
            return jsonify({'error': 'Invalid phone number format.'}), 400

        # Check if user already exists
        if username in user_db:
            return jsonify({'error': 'Username already exists.'}), 409

        # Generate and send verification code
        verification_code = generate_verification_code()
        send_verification_code(phone_number, verification_code)

        # Store user data with verification code (in a real scenario, use a database)
        user_db[username] = {
            'phone_number': phone_number,
            'verification_code': verification_code,
            'is_verified': False
        }

        return jsonify({'message': 'Verification code sent to your phone number.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/verify', methods=['POST'])
def verify_user():
    """
    Endpoint to verify the phone number of a user.
    Expected JSON payload:
    {
        "username": "user123",
        "verification_code": "123456"
    }

    Returns a JSON response with the result of the verification.
    """
    try:
        data = request.get_json()

        # Validate request data
        if not data or 'username' not in data or 'verification_code' not in data:
            return jsonify({'error': 'Username and verification code are required.'}), 400

        username = data['username']
        verification_code = data['verification_code']

        # Check if user exists
        if username not in user_db:
            return jsonify({'error': 'User not found.'}), 404

        user_info = user_db[username]

        # Verify the code
        if user_info['verification_code'] == verification_code:
            user_info['is_verified'] = True
            return jsonify({'message': 'Phone number verified successfully.'}), 200
        else:
            return jsonify({'error': 'Invalid verification code.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
