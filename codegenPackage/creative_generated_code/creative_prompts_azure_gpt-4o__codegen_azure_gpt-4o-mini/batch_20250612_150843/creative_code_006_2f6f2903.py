"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-crypto-legacy.com
Prompt: Generate a step-by-step guide to implement a verification process for user accounts in an automated trading platform, ensuring secure withdrawals as outlined in Crypto Legacy.
Generated: DETERMINISTIC_2f6f2903147b7492
Batch ID: 20250612_150843
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
import hashlib
import sqlite3
from email.mime.text import MIMEText

# Configuration for email sending
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'

# Database configuration
DATABASE = 'users.db'

def create_database():
    """Creates a SQLite database and a users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        verification_code TEXT,
        is_verified BOOLEAN NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def send_verification_email(email, code):
    """Sends a verification email to the user with the provided code."""
    msg = MIMEText(f'Your verification code is: {code}')
    msg['Subject'] = 'Account Verification'
    msg['From'] = SMTP_USERNAME
    msg['To'] = email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, email, msg.as_string())
        print(f"Verification email sent to {email}.")
    except Exception as e:
        print(f"Error sending verification email: {e}")

def generate_verification_code(length=6):
    """Generates a random verification code of specified length."""
    return ''.join(random.choices(string.digits, k=length))

def register_user(email, password):
    """Registers a new user with a hashed password and sends a verification code."""
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    code = generate_verification_code()

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email, password_hash, verification_code) VALUES (?, ?, ?)', 
                       (email, password_hash, code))
        conn.commit()
        send_verification_email(email, code)
    except sqlite3.IntegrityError:
        print(f"Error: User with email {email} already exists.")
    except Exception as e:
        print(f"Error registering user: {e}")
    finally:
        conn.close()

def verify_user(email, code):
    """Verifies the user's account with the provided email and verification code."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT verification_code FROM users WHERE email = ?', (email,))
        result = cursor.fetchone()

        if result and result[0] == code:
            cursor.execute('UPDATE users SET is_verified = 1 WHERE email = ?', (email,))
            conn.commit()
            print(f"User {email} verified successfully.")
        else:
            print("Invalid verification code.")
    except Exception as e:
        print(f"Error verifying user: {e}")
    finally:
        conn.close()

def main():
    create_database()
    
    # Example usage
    email = 'user@example.com'
    password = 'securepassword123'
    
    # Register a new user
    register_user(email, password)
    
    # User enters the verification code (example for testing)
    verification_code = input(f"Enter the verification code sent to {email}: ")
    
    # Verify the user
    verify_user(email, verification_code)

if __name__ == "__main__":
    main()
```
