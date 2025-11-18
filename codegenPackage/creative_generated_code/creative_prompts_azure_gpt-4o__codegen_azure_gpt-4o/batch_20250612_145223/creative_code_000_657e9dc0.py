"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write code for a user authentication system that includes email-based registration and password recovery, inspired by the login functionality described on the Vertiv employee benefits portal.
Generated: DETERMINISTIC_657e9dc0a00ba4ea
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
import hashlib
import sqlite3
from email.mime.text import MIMEText

# Database setup
DB_FILE = "user_auth.db"

def initialize_database():
    """
    Initializes the SQLite database and creates the necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            recovery_token TEXT
        )
    """)
    conn.commit()
    conn.close()

# Utility functions
def validate_email(email):
    """
    Validates if the given email is in the correct format.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def hash_password(password):
    """
    Returns a hash of the given password using SHA256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def send_email(recipient, subject, body):
    """
    Sends an email to the given recipient.
    NOTE: Replace SMTP settings with production-ready credentials.
    """
    try:
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = "your_email@example.com"
        smtp_password = "your_password"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = smtp_user
        msg["To"] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, recipient, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Authentication system
def register_user(email, password):
    """
    Registers a new user with their email and password.
    """
    if not validate_email(email):
        print("Invalid email format.")
        return False

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    password_hash = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, password_hash))
        conn.commit()
        print("Registration successful.")
        return True
    except sqlite3.IntegrityError:
        print("Email is already registered.")
        return False
    finally:
        conn.close()

def login_user(email, password):
    """
    Authenticates a user with their email and password.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    password_hash = hash_password(password)

    try:
        cursor.execute("SELECT * FROM users WHERE email = ? AND password_hash = ?", (email, password_hash))
        user = cursor.fetchone()
        if user:
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False
    finally:
        conn.close()

def generate_recovery_token(email):
    """
    Generates a password recovery token for the given email and sends it via email.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user:
            recovery_token = hashlib.sha256((email + str(hashlib.os.urandom(16))).encode()).hexdigest()
            cursor.execute("UPDATE users SET recovery_token = ? WHERE email = ?", (recovery_token, email))
            conn.commit()
            send_email(email, "Password Recovery", f"Your recovery token is: {recovery_token}")
            print("Recovery token sent to email.")
            return True
        else:
            print("Email not found.")
            return False
    finally:
        conn.close()

def reset_password(email, recovery_token, new_password):
    """
    Resets the user's password using the recovery token.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ? AND recovery_token = ?", (email, recovery_token))
        user = cursor.fetchone()
        if user:
            new_password_hash = hash_password(new_password)
            cursor.execute("UPDATE users SET password_hash = ?, recovery_token = NULL WHERE email = ?", (new_password_hash, email))
            conn.commit()
            print("Password reset successful.")
            return True
        else:
            print("Invalid email or recovery token.")
            return False
    finally:
        conn.close()

# Application entry point
if __name__ == "__main__":
    initialize_database()
    print("Welcome to the User Authentication System.")

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Recover Password")
        print("4. Reset Password")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register_user(email, password)
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login_user(email, password)
        elif choice == "3":
            email = input("Enter your email: ")
            generate_recovery_token(email)
        elif choice == "4":
            email = input("Enter your email: ")
            recovery_token = input("Enter your recovery token: ")
            new_password = input("Enter your new password: ")
            reset_password(email, recovery_token, new_password)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
