"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Generate code to integrate two-factor authentication into a Point of Sale login system for enhanced security.
Generated: DETERMINISTIC_695baf31b9c60bd8
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import smtplib
import sqlite3
from email.mime.text import MIMEText

class TwoFactorAuthPOS:
    def __init__(self):
        # Initialize database connection
        self.conn = sqlite3.connect("pos_users.db")
        self.cursor = self.conn.cursor()
        self.setup_database()
    
    def setup_database(self):
        """Create the users table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def hash_password(self, password):
        """Hash the password using SHA-256 for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password, email):
        """Register a new user with a hashed password."""
        try:
            password_hash = self.hash_password(password)
            self.cursor.execute("INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)", 
                                (username, password_hash, email))
            self.conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")

    def send_otp(self, email):
        """Generate and send a one-time password (OTP) to the user's email."""
        otp = random.randint(100000, 999999)  # 6-digit OTP
        try:
            # Set up email server (example for Gmail)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"

            # Email content
            msg = MIMEText(f"Your OTP for logging into the Point of Sale system is: {otp}")
            msg["Subject"] = "Your Point of Sale Login OTP"
            msg["From"] = sender_email
            msg["To"] = email

            # Send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
            
            return otp
        except Exception as e:
            print(f"Error sending OTP: {e}")
            return None

    def login_user(self, username, password):
        """Authenticate user and implement 2FA using OTP."""
        self.cursor.execute("SELECT password_hash, email FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        
        if not user:
            print("Error: User not found.")
            return False

        stored_password_hash, email = user
        if self.hash_password(password) != stored_password_hash:
            print("Error: Incorrect password.")
            return False
        
        # Send OTP for two-factor authentication
        otp = self.send_otp(email)
        if otp is None:
            print("Error: Unable to send OTP.")
            return False

        # Verify OTP
        entered_otp = input("Enter the OTP sent to your email: ")
        if str(otp) == entered_otp:
            print("Login successful. Welcome!")
            return True
        else:
            print("Error: Incorrect OTP.")
            return False

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

# Example usage
# Ensure to replace your_email@gmail.com and your_password with valid credentials to test sending email.

if __name__ == "__main__":
    # Initialize the TwoFactorAuthPOS system
    pos_system = TwoFactorAuthPOS()

    # Register a user (only for testing, should be done separately in production)
    # pos_system.register_user("test_user", "password123", "test_user@example.com")

    # User login
    username = input("Enter username: ")
    password = input("Enter password: ")
    pos_system.login_user(username, password)

    # Close database connection
    pos_system.close_connection()
```

**Note:** Replace `your_email@gmail.com` and `your_password` with valid email credentials for sending the OTP via email. For production, consider using a secure email service or API like SendGrid or AWS SES to avoid exposing credentials in code.
