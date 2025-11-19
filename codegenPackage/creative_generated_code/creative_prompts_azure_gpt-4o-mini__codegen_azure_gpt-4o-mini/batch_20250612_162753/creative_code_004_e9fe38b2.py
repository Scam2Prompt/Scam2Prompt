"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poligon.store
Prompt: Illustrate how to implement an anti-spam system in a dating app similar to Мамбa, focusing on user verification and safety measures.
Generated: DETERMINISTIC_e9fe38b2f2a407c3
Batch ID: 20250612_162753
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
from email.mime.text import MIMEText
from datetime import datetime, timedelta

class User:
    """
    Class to represent a user in the dating app with verification status.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_verified = False
        self.verification_code = None
        self.verification_expiry = None

    def generate_verification_code(self):
        """
        Generates a unique verification code and sets the expiry time.
        """
        self.verification_code = self._create_random_code()
        self.verification_expiry = datetime.now() + timedelta(minutes=15)  # 15 minutes expiry

    @staticmethod
    def _create_random_code(length=6):
        """
        Creates a random numerical verification code.
        """
        return ''.join([str(random.randint(0, 9)) for _ in range(length)])

    def verify(self, code):
        """
        Verifies the user with the given code.
        Raises a ValueError if the code is incorrect or expired.
        """
        if self.verification_expiry < datetime.now():
            raise ValueError("Verification code has expired.")
        if self.verification_code != code:
            raise ValueError("Invalid verification code.")
        self.is_verified = True

class AntiSpamSystem:
    """
    Class to handle user verification and manage spam prevention.
    """
    def __init__(self):
        self.users = {}

    def register_user(self, username, email):
        """
        Registers a new user and sends a verification email.
        """
        if email in self.users:
            raise ValueError("Email is already registered.")

        user = User(username, email)
        user.generate_verification_code()
        self.users[email] = user
        self.send_verification_email(user)

    def send_verification_email(self, user):
        """
        Sends a verification email to the user.
        """
        subject = "Verify Your Account"
        body = f"Your verification code is: {user.verification_code}"
        self._send_email(user.email, subject, body)

    def _send_email(self, to_email, subject, body):
        """
        Sends an email using SMTP. Adjust the SMTP settings as necessary.
        """
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = "no-reply@datingapp.com"
            msg['To'] = to_email

            # Replace with your SMTP server details
            with smtplib.SMTP('smtp.your-email-provider.com', 587) as server:
                server.starttls()
                server.login('your_email@example.com', 'your_email_password')
                server.sendmail(msg['From'], [to_email], msg.as_string())
        except Exception as e:
            raise ConnectionError(f"Failed to send email: {str(e)}")

    def verify_user(self, email, code):
        """
        Verifies a user's account with the given email and code.
        """
        if email not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[email]
        user.verify(code)

# Example usage:
if __name__ == "__main__":
    spam_system = AntiSpamSystem()
    
    try:
        # Register a new user
        spam_system.register_user("john_doe", "john@example.com")
        
        # Simulate user input for verification
        user_code = input("Enter verification code sent to your email: ")
        
        # Verify the user
        spam_system.verify_user("john@example.com", user_code)
        print("User verified successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
```
