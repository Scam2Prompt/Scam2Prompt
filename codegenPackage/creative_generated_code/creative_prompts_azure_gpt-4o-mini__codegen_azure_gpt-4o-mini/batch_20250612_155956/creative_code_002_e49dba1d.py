"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtch.pro
Prompt: What are the steps to handle email verification for user accounts in a Telegram-based login system like the one on mtch.pro?
Generated: DETERMINISTIC_e49dba1d96fa855c
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import uuid
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    verification_token = db.Column(db.String(200), nullable=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Email verification serializer
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Function to send verification email
def send_verification_email(email, token):
    msg = MIMEMultipart()
    msg['From'] = 'noreply@yourdomain.com'
    msg['To'] = email
    msg['Subject'] = 'Email Verification'

    link = request.url_root + 'verify_email/' + token
    body = f'Please click the link to verify your email: {link}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.yourdomain.com', 587) as server:
            server.starttls()
            server.login('your_email@yourdomain.com', 'your_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')

    # Basic error handling for missing email
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create new user with verification token
    new_user = User(email=email)
    token = s.dumps(email, salt='email-verify-salt')
    new_user.verification_token = token
    db.session.add(new_user)
    db.session.commit()

    # Send verification email
    send_verification_email(email, token)

    return jsonify({"message": "Registration successful, please check your email to verify."}), 201

# Route to verify email
@app.route('/verify_email/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = s.loads(token, salt='email-verify-salt', max_age=86400)  # Token valid for 1 day
    except SignatureExpired:
        return jsonify({"error": "Verification link expired."}), 400
    except BadSignature:
        return jsonify({"error": "Invalid verification link."}), 400

    # Update user verification status
    user = User.query.filter_by(email=email).first()
    if user:
        user.is_verified = True
        user.verification_token = None  # Clear the token after successful verification
        db.session.commit()
        return jsonify({"message": "Email verified successfully."}), 200

    return jsonify({"error": "User not found."}), 404

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask app in debug mode
```
