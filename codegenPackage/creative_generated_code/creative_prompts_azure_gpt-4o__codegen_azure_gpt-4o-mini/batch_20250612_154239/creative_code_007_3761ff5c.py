"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombatexchange.rf.gd
Prompt: Provide code examples for configuring multiple email accounts on a hosting service with features like those offered by iFastNet.
Generated: DETERMINISTIC_3761ff5c48fbd0f2
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAccount:
    """Class to represent an email account."""

    def __init__(self, email: str, password: str, smtp_server: str, smtp_port: int):
        """Initialize the email account with necessary credentials."""
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient: str, subject: str, body: str):
        """Send an email using the account's SMTP settings."""
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)  # Login to the email account
                server.sendmail(self.email, recipient, msg.as_string())  # Send the email
                print(f"Email sent successfully from {self.email} to {recipient}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email from {self.email} to {recipient}. Error: {e}")

def main():
    """Main function to configure and send emails from multiple accounts."""
    
    # List of email account configurations
    email_accounts = [
        EmailAccount(email='user1@example.com', password='password1', smtp_server='smtp.example.com', smtp_port=587),
        EmailAccount(email='user2@example.com', password='password2', smtp_server='smtp.example.com', smtp_port=587),
        # Add more accounts as needed
    ]

    # Example of sending an email from each account
    for account in email_accounts:
        account.send_email(recipient='recipient@example.com',
                           subject='Test Email',
                           body='This is a test email from configured email accounts.')

if __name__ == "__main__":
    main()
```
