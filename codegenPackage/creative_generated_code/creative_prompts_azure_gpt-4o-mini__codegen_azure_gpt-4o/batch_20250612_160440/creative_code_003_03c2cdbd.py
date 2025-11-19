"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Develop a code snippet for a secure login system that includes two-factor authentication, inspired by the security measures at Finance Investment Limited.
Generated: DETERMINISTIC_03c2cdbd560f404f
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3
import smtplib
import random
import string
from email.mime.text import MIMEText

# Database setup
DB_FILE = 'users.db'
CONN = sqlite3.connect(DB_FILE)
CURSOR = CONN.cursor()

# Create users table if it doesn't exist
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
CONN.commit()


def hash_password(password, salt):
    """
    Hashes a password using SHA-256 with a provided salt.
    :param password: The password to be hashed.
    :param salt: The salt to augment the hashing process.
    :return: The hashed password.
    """
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()


def generate_salt():
    """
    Generates a random salt for password hashing.
    :return: A random string used as salt.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def send_otp_email(email, otp):
    """
    Sends a one-time password (OTP) to the user's email address.
    :param email: The user's email address.
    :param otp: The generated OTP to send.
    """
    try:
        smtp_server = "smtp.example.com"  # Replace with real SMTP server
        smtp_port = 587
        smtp_username = "your_email@example.com"  # Replace with valid email
        smtp_password = "your_password"  # Replace with valid password

        # Construct the email
        msg = MIMEText(f"Your one-time password (OTP) is: {otp}")
        msg['Subject'] = "Your OTP for Secure Login"
        msg['From'] = smtp_username
        msg['To'] = email

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, [email], msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


def register_user(username, password, email):
    """
    Registers a new user by storing their hashed password, salt, and email.
    :param username: The username of the new user.
    :param password: The plaintext password of the new user.
    :param email: The email address of the new user.
    """
    salt = generate_salt()
    password_hash = hash_password(password, salt)

    try:
        CURSOR.execute('INSERT INTO users (username, password_hash, salt, email) VALUES (?, ?, ?, ?)',
                       (username, password_hash, salt, email))
        CONN.commit()
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")


def login_user(username, password):
    """
    Authenticates a user by verifying their password and sending an OTP for 2FA.
    :param username: The username of the user.
    :param password: The plaintext password of the user.
    """
    try:
        CURSOR.execute('SELECT password_hash, salt, email FROM users WHERE username = ?', (username,))
        user_data = CURSOR.fetchone()

        if not user_data:
            print("Error: Invalid username.")
            return

        password_hash, salt, email = user_data

        # Verify password
        if password_hash == hash_password(password, salt):
            print("Password verified.")

            # Generate and send OTP
            otp = ''.join(random.choices(string.digits, k=6))
            send_otp_email(email, otp)

            # Ask for OTP verification
            entered_otp = input("Enter the OTP sent to your email: ")
            if entered_otp == otp:
                print("Login successful!")
            else:
                print("Error: Incorrect OTP.")
        else:
            print("Error: Incorrect password.")
    except Exception as e:
        print(f"Login failed due to an error: {e}")


# Example usage
if __name__ == "__main__":
    print("Registering a new user...")
    register_user("john_doe", "secure_password123", "john_doe@example.com")

    print("Attempting to log in...")
    login_user("john_doe", "secure_password123")
```

### Notes:
1. Replace placeholders like `smtp.example.com`, `your_email@example.com`, and `your_password` with actual SMTP configuration.
2. Never hard-code sensitive credentials in production; use environment variables or secure vaults.
3. This code is for demonstration purposes and doesn't include advanced security features like rate-limiting or encryption at rest.
