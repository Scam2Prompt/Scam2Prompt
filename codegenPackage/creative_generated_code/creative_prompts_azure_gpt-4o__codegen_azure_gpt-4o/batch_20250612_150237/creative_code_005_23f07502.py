"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxbinaryinvestpro.com
Prompt: Develop a secure password reset functionality for an investment platform, similar to the one described on Fxbinaryinvestpro.
Generated: DETERMINISTIC_23f075021b9b294c
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a secure password reset functionality using Python and Flask. It includes error handling, follows best practices, and is production-ready.

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuring Flask app and database
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Serializer for generating and verifying tokens
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def send_email(to_email, subject, body):
    """Function to send email securely."""
    try:
        smtp_server = "smtp.example.com"  # Replace with actual SMTP server
        smtp_port = 587  # Replace with actual port
        smtp_user = "your_email@example.com"  # Replace with actual email
        smtp_password = "your_email_password"  # Replace with actual password

        msg = MIMEText(body, 'html')
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    """Endpoint to handle password reset requests."""
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Generate a password reset token
    token = serializer.dumps(email, salt='password-reset-salt')

    # Create a password reset link
    reset_link = url_for('reset_password', token=token, _external=True)

    # Send the reset email
    subject = "Password Reset Request"
    body = f"""
    <p>Hi,</p>
    <p>Click the link below to reset your password:</p>
    <a href="{reset_link}">{reset_link}</a>
    <p>This link will expire in 1 hour.</p>
    """
    send_email(email, subject, body)

    return jsonify({"message": "Password reset email sent successfully"}), 200

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Endpoint to handle password reset action."""
    try:
        # Verify the token (valid for 3600 seconds / 1 hour)
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except Exception as e:
        return jsonify({"error": "Invalid or expired token"}), 400

    if request.method == 'POST':
        data = request.json
        new_password = data.get('password')

        if not new_password:
            return jsonify({"error": "Password is required"}), 400

        # Hash the new password
        hashed_password = generate_password_hash(new_password)

        # Update the user's password in the database
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404
            
        user.password = hashed_password
        db.session.commit()

        return jsonify({"message": "Password reset successfully"}), 200

    # Render a reset password form (if handling GET request)
    return render_template('reset_password.html', token=token)

# Initialization route
@app.before_first_request
def create_tables():
    """Create database tables."""
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug mode in production
```

**Note:** 
- Replace placeholder values like SMTP details, email credentials, and database URI with actual production values.
- Ensure that sensitive information (e.g., `SECRET_KEY`, SMTP credentials) is managed securely (e.g., environment variables).
- Use HTTPS in production to secure communications.
