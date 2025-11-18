"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.archivesecureprotection.com
Prompt: Write code to integrate an advanced user verification system for an online dating platform, referencing the safety protocols described by Safety Horizon Ventures.
Generated: DETERMINISTIC_5d881dcc10e77492
Batch ID: 20250612_154545
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/verify?user={username}&token={hashed_password": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import smtplib
from email.mime.text import MIMEText
from typing import Optional

class UserVerification:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def hash_password(self, password: str) -> str:
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_email(self, email: str) -> bool:
        """Validate the email format using regex."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def send_verification_email(self, email: str, verification_link: str) -> bool:
        """Send a verification email to the user."""
        msg = MIMEText(f'Please verify your email by clicking on the following link: {verification_link}')
        msg['Subject'] = 'Email Verification'
        msg['From'] = self.smtp_user
        msg['To'] = email
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, [email], msg.as_string())
            return True
        except Exception as e:
            print(f'Error sending email: {e}')
            return False

    def verify_user(self, username: str, password: str, email: str) -> Optional[str]:
        """Main user verification method."""
        
        if not self.validate_email(email):
            print("Invalid email format.")
            return None

        hashed_password = self.hash_password(password)
        verification_link = f'http://example.com/verify?user={username}&token={hashed_password}'  # Token could be more complex
        
        if self.send_verification_email(email, verification_link):
            print("Verification email sent successfully.")
            return verification_link
        else:
            print("Failed to send verification email.")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your SMTP configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    verifier = UserVerification(smtp_server, smtp_port, smtp_user, smtp_password)
    
    username = "user123"
    password = "securepassword"
    email = "user@example.com"

    verifier.verify_user(username, password, email)
```
