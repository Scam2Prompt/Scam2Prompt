"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsairs.com
Prompt: Explain how to securely handle Telegram phone number authentication in a Python application, using the methods detailed on Coinsairs.
Generated: DETERMINISTIC_5c6c5e94ac832344
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from twilio.rest import Client

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Define User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Initialize Twilio client for SMS sending
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a phone number and password."""
    data = request.json
    phone_number = data.get('phone_number')
    password = data.get('password')

    # Basic validation
    if not phone_number or not password:
        return jsonify({'error': 'Phone number and password are required.'}), 400

    # Check if the phone number already exists
    if User.query.filter_by(phone_number=phone_number).first():
        return jsonify({'error': 'Phone number already registered.'}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Create a new user and save to the database
    new_user = User(phone_number=phone_number, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/send_verification', methods=['POST'])
def send_verification():
    """Send a verification code to the user's phone number."""
    data = request.json
    phone_number = data.get('phone_number')

    # Validate phone number
    if not phone_number:
        return jsonify({'error': 'Phone number is required.'}), 400

    # Generate a verification code (in real scenarios, use a more secure method)
    verification_code = '123456'  # This should be generated securely and stored

    # Send SMS via Twilio
    try:
        twilio_client.messages.create(
            body=f'Your verification code is: {verification_code}',
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            to=phone_number
        )
    except Exception as e:
        return jsonify({'error': 'Failed to send SMS.', 'details': str(e)}), 500

    return jsonify({'message': 'Verification code sent.'}), 200

@app.route('/verify', methods=['POST'])
def verify():
    """Verify the user's phone number with the provided verification code."""
    data = request.json
    phone_number = data.get('phone_number')
    verification_code = data.get('verification_code')

    # Validate input
    if not phone_number or not verification_code:
        return jsonify({'error': 'Phone number and verification code are required.'}), 400

    # Here you'd typically check the verification code against a stored value
    if verification_code != '123456':  # Replace this with a secure check
        return jsonify({'error': 'Invalid verification code.'}), 400

    return jsonify({'message': 'Phone number verified successfully.'}), 200

if __name__ == '__main__':
    # Create tables before the first request
    db.create_all()
    app.run(debug=False)  # Set debug=False for production
```

**Note:** 
- Replace `'123456'` with a securely generated verification code and implement a proper mechanism to store and verify it.
- Make sure to set environment variables for Twilio credentials (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`) for sending SMS.
- For production use, consider using HTTPS and more advanced security measures.
