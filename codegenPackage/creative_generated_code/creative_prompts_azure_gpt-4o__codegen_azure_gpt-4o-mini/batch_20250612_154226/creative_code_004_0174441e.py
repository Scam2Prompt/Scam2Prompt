"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoclaim.rf.gd
Prompt: Write a script to test the compatibility of a Python app with a hosting provider that supports multiple email accounts and no daily hit limits, such as iFastNet.
Generated: DETERMINISTIC_0174441e37fae300
Batch ID: 20250612_154226
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
from typing import List, Tuple

class EmailTester:
    """A class to test the compatibility of a Python app with an email server."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailTester with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port to use for the SMTP server
        :param username: Username for the email account
        :param password: Password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_test_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Sends a test email to the specified recipient.

        :param recipient: The email address to send the test email to
        :param subject: The subject of the test email
        :param body: The body content of the test email
        :return: True if the email was sent successfully, otherwise False
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, msg.as_string())
            
            return True  # Email sent successfully
        except Exception as e:
            print(f"Error sending email: {e}")
            return False  # Email sending failed


def test_email_accounts(test_accounts: List[Tuple[str, str, str]], smtp_server: str, smtp_port: int, username: str, password: str):
    """
    Tests multiple email accounts by sending a test email.

    :param test_accounts: A list of tuples containing (recipient_email, subject, body)
    :param smtp_server: The SMTP server address
    :param smtp_port: The port for the SMTP server
    :param username: Username for the email account
    :param password: Password for the email account
    """
    tester = EmailTester(smtp_server, smtp_port, username, password)
    
    for recipient, subject, body in test_accounts:
        print(f"Sending test email to: {recipient}")
        success = tester.send_test_email(recipient, subject, body)
        
        if success:
            print(f"Test email sent successfully to: {recipient}")
        else:
            print(f"Failed to send test email to: {recipient}")


if __name__ == "__main__":
    # Configuration for the email server
    SMTP_SERVER = 'smtp.example.com'  # Replace with actual SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS
    USERNAME = 'your-email@example.com'  # Replace with your email
    PASSWORD = 'your-email-password'  # Replace with your email password

    # Test accounts: (recipient_email, subject, body)
    test_accounts = [
        ('test1@example.com', 'Test Email 1', 'This is a test email for account 1.'),
        ('test2@example.com', 'Test Email 2', 'This is a test email for account 2.'),
        # Add more test accounts as needed
    ]

    # Execute the test
    test_email_accounts(test_accounts, SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
```
