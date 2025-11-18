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
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
import sqlite3

# Flask app initialization
app = Flask(__name__)

# Database configuration
DB_FILE = 'users.db'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'    # Replace with your email password

# Generate random verification code
def generate_verification_code(length=6):
    """Generate a random alphanumeric verification code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Send email function
def send_verification_email(email, verification_code):
    """
    Send a password reset verification code to the user's email.
    Args:
        email (str): Recipient's email address.
        verification_code (str): Verification code to send.
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Password Reset Verification Code'

        body = f"Your password reset verification code is: {verification_code}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Verification email sent to {email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# API route: Request password reset
@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    """
    Handle 'Forgot Password' requests.
    Request Body:
        email (str): Email address of the user requesting password reset.
    """
    try:
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Check if email exists in the database
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User with this email does not exist"}), 404

        # Generate and store verification code
        verification_code = generate_verification_code()
        cursor.execute("UPDATE users SET verification_code = ? WHERE email = ?", (verification_code, email))
        conn.commit()
        conn.close()

        # Send verification email
        send_verification_email(email, verification_code)

        return jsonify({"message": "Verification code sent to your email"}), 200

    except Exception as e:
        print(f"Error in forgot_password: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

# API route: Verify code and reset password
@app.route('/reset_password', methods=['POST'])
def reset_password():
    """
    Handle password reset requests.
    Request Body:
        email (str): Email address of the user resetting password.
        verification_code (str): Verification code sent to the user's email.
        new_password (str): New password to set.
    """
    try:
        data = request.json
        email = data.get('email')
        verification_code = data.get('verification_code')
        new_password = data.get('new_password')

        if not email or not verification_code or not new_password:
            return jsonify({"error": "Email, verification code, and new password are required"}), 400

        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Verify the code and reset the password
        cursor.execute("SELECT verification_code FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        if not result or result[0] != verification_code:
            return jsonify({"error": "Invalid verification code"}), 400

        cursor.execute("UPDATE users SET password = ?, verification_code = NULL WHERE email = ?", (new_password, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "Password reset successfully"}), 200

    except Exception as e:
        print(f"Error in reset_password: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

# Initialize the database (for demo purposes)
def initialize_database():
    """Initialize the SQLite database with a users table."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                verification_code TEXT
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")

# Main entry point
if __name__ == '__main__':
    initialize_database()  # Ensure the database is set up
    app.run(debug=True)    # Start the Flask app
```
