"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.add-solution.de
Prompt: Suggest best practices for implementing multi-factor authentication (MFA) with OTP tokens in Outlook WebApp, as outlined on https://exchange.add-solution.de.
Generated: DETERMINISTIC_5d05dea51eff33c7
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
from email.mime.text import MIMEText
import time
import sqlite3

class OTPManager:
    def __init__(self, db_name='otp_database.db'):
        """Initialize the OTPManager with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create a table to store OTPs and their expiration times."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS otps (
                    email TEXT PRIMARY KEY,
                    otp TEXT NOT NULL,
                    expires_at INTEGER NOT NULL
                )
            ''')

    def generate_otp(self):
        """Generate a random 6-digit OTP."""
        return str(random.randint(100000, 999999))

    def send_otp(self, email, otp):
        """Send the OTP to the user's email."""
        msg = MIMEText(f"Your OTP is {otp}. It is valid for 5 minutes.")
        msg['Subject'] = 'Your OTP Code'
        msg['From'] = 'noreply@example.com'
        msg['To'] = email

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login('username', 'password')
                server.send_message(msg)
            print(f"OTP sent to {email}")
        except Exception as e:
            print(f"Failed to send OTP: {e}")

    def store_otp(self, email, otp):
        """Store the OTP and its expiration time in the database."""
        expires_at = int(time.time()) + 300  # OTP valid for 5 minutes
        with self.connection:
            self.connection.execute('''
                INSERT OR REPLACE INTO otps (email, otp, expires_at)
                VALUES (?, ?, ?)
            ''', (email, otp, expires_at))

    def verify_otp(self, email, otp):
        """Verify the received OTP against the stored value."""
        with self.connection:
            row = self.connection.execute('''
                SELECT otp, expires_at FROM otps WHERE email = ?
            ''', (email,)).fetchone()
            if row:
                stored_otp, expires_at = row
                if stored_otp == otp and time.time() < expires_at:
                    return True
                else:
                    return False
            return False

    def cleanup_expired_otps(self):
        """Remove expired OTPs from the database."""
        with self.connection:
            self.connection.execute('''
                DELETE FROM otps WHERE expires_at < ?
            ''', (int(time.time()),))

# Usage example
if __name__ == "__main__":
    otp_manager = OTPManager()

    user_email = "user@example.com"  # Replace with actual user email
    otp = otp_manager.generate_otp()
    otp_manager.store_otp(user_email, otp)
    otp_manager.send_otp(user_email, otp)

    # Simulate user input
    user_input_otp = input("Enter the OTP sent to your email: ")
    if otp_manager.verify_otp(user_email, user_input_otp):
        print("OTP verified successfully!")
    else:
        print("Invalid or expired OTP.")

    # Clean up expired OTPs
    otp_manager.cleanup_expired_otps()
```
