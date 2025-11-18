"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbama-14n.pages.dev
Prompt: Generate a script to automate email verification for user registration, as outlined in the Bitbama account setup process.
Generated: DETERMINISTIC_681216352a23026f
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    verification_code = db.Column(db.String(10), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Generate a random verification code
def generate_verification_code(length=6):
    """Generate a random alphanumeric verification code."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Send verification email
def send_verification_email(email, code):
    """Send a verification email to the user."""
    sender_email = os.getenv('EMAIL_USER')
    sender_password = os.getenv('EMAIL_PASS')
    subject = "Verify Your Email Address"
    body = f"Your verification code is: {code}"

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the email server and send the email
        with smtplib.SMTP(os.getenv('EMAIL_SMTP_SERVER'), os.getenv('EMAIL_SMTP_PORT')) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    """Register a user and send a verification email."""
    data = request.json
    email = data.get('email')

    # Check if email is provided
    if not email:
        return jsonify({"error": "Email is required."}), 400

    # Check for existing user
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email is already registered."}), 400

    # Generate verification code
    verification_code = generate_verification_code()

    # Create new user
    new_user = User(email=email, verification_code=verification_code)
    db.session.add(new_user)
    db.session.commit()

    # Send verification email
    send_verification_email(email, verification_code)

    return jsonify({"message": "Registration successful. Please check your email for the verification code."}), 201

# Email verification endpoint
@app.route('/verify', methods=['POST'])
def verify_email():
    """Verify the user's email address using the verification code."""
    data = request.json
    email = data.get('email')
    code = data.get('code')

    # Check if email and code are provided
    if not email or not code:
        return jsonify({"error": "Email and verification code are required."}), 400

    # Find the user
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found."}), 404

    # Check verification code
    if user.verification_code == code:
        user.is_verified = True
        db.session.commit()
        return jsonify({"message": "Email verified successfully."}), 200
    else:
        return jsonify({"error": "Invalid verification code."}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure to set environment variables `EMAIL_USER`, `EMAIL_PASS`, `EMAIL_SMTP_SERVER`, and `EMAIL_SMTP_PORT` before running the script. This code uses Flask and SQLAlchemy and is designed to handle user registration and email verification processes effectively.
