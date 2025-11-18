"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Create a Python script to handle "Forgot Password" functionality using email verification, referencing features like those on the HBsoft platform.
Generated: DETERMINISTIC_6b9c1f3651fb5f34
Batch ID: 20250612_153246
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
import string
import random
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your database URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Serializer for generating password reset tokens
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = os.environ.get('SMTP_USER')
        msg['To'] = to_email

        with smtplib.SMTP(os.environ.get('SMTP_SERVER'), os.environ.get('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASSWORD'))
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Handle forgot password requests."""
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        # Generate a password reset token
        token = s.dumps(email, salt='password-reset-salt')
        reset_url = f"{request.url_root}reset-password/{token}"
        body = f"Click the link to reset your password: {reset_url}"
        send_email(email, "Password Reset Request", body)
        return jsonify({"message": "Password reset email sent."}), 200
    
    return jsonify({"message": "Email not found."}), 404

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    """Handle password reset requests."""
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
    except Exception as e:
        return jsonify({"message": "Invalid or expired token."}), 400

    new_password = request.json.get('password')
    
    if not new_password:
        return jsonify({"message": "Password is required."}), 400
    
    user = User.query.filter_by(email=email).first()
    if user:
        user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        return jsonify({"message": "Password has been reset."}), 200
    
    return jsonify({"message": "User not found."}), 404

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Make sure to set up your environment variables for SMTP settings and the secret key. This code uses Flask, SQLAlchemy, and requires a running database to function correctly.
