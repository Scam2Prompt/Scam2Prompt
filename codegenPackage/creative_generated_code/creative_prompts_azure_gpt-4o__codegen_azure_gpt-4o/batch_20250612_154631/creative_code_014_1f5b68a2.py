"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluestockmarkets.com
Prompt: Develop a secure login system for BlueStockMarkets that supports multi-factor authentication and protects user data during account creation and sign-in processes.
Generated: DETERMINISTIC_1f5b68a21282fdb7
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
import secrets
import smtplib
import os
import pyotp

# Constants
DATABASE_FILE = "bluestockmarkets.db"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_EMAIL = "noreply@bluestockmarkets.com"
SMTP_PASSWORD = "your_email_password"

# Securely initialize database
def init_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            mfa_secret TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Hash password securely
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

# Verify password securely
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Generate MFA secret
def generate_mfa_secret():
    return pyotp.random_base32()

# Send email with OTP
def send_email(recipient_email, otp):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        message = f"Subject: Your OTP Code\n\nYour OTP code is: {otp}"
        server.sendmail(SMTP_EMAIL, recipient_email, message)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Register a new user securely
def register_user(email, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        # Generate MFA secret
        mfa_secret = generate_mfa_secret()
        
        # Hash the password
        password_hash = hash_password(password)
        
        # Insert user data into database
        cursor.execute("INSERT INTO users (email, password_hash, mfa_secret) VALUES (?, ?, ?)", 
                       (email, password_hash, mfa_secret))
        conn.commit()
        
        print("User registered successfully. Please save your MFA secret securely.")
        print(f"MFA Secret: {mfa_secret}")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

# Authenticate user
def authenticate_user(email, password, otp):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        # Retrieve user data
        cursor.execute("SELECT password_hash, mfa_secret FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if user is None:
            print("Error: Invalid email or password.")
            return False
        
        # Validate password
        password_hash, mfa_secret = user
        if not verify_password(password, password_hash):
            print("Error: Invalid email or password.")
            return False
        
        # Validate OTP
        totp = pyotp.TOTP(mfa_secret)
        if not totp.verify(otp):
            print("Error: Invalid OTP.")
            return False
        
        print("Authentication successful!")
        return True
    except Exception as e:
        print(f"Error during authentication: {e}")
    finally:
        conn.close()

# Main functionality for testing
if __name__ == "__main__":
    # Initialize the database
    init_db()
    
    # Mock user registration
    print("Registering a new user...")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    register_user(email, password)
    
    # Mock user authentication
    print("\nAuthenticating a user...")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    otp = input("Enter your OTP: ")
    authenticate_user(email, password, otp)
```
