"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfiul.epizy.com
Prompt: Explain how to configure multiple email accounts using iFastNet's hosting services in a web application.
Generated: DETERMINISTIC_e0922cf0dc669dfa
Batch ID: 20250612_163251
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
    """Class to represent an email account for sending emails using iFastNet's SMTP server."""
    
    def __init__(self, email, password, smtp_server, smtp_port):
        """
        Initialize EmailAccount with provided credentials and SMTP settings.

        Args:
            email (str): The email address for the account.
            password (str): The password for the email account.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port number for the SMTP server.
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, body):
        """
        Send an email to the specified recipient.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            body (str): The body content of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            
            return True

        except Exception as e:
            # Log the exception (in a real application you might want to log this to a file or monitoring system)
            print(f"Error sending email: {e}")
            return False

def configure_multiple_email_accounts(accounts):
    """
    Configure and send test emails using multiple email accounts.

    Args:
        accounts (list): A list of dicts containing email configuration such as email, password, smtp_server, and smtp_port.
    """
    for account_info in accounts:
        # Create EmailAccount instance
        email_account = EmailAccount(
            email=account_info['email'],
            password=account_info['password'],
            smtp_server=account_info['smtp_server'],
            smtp_port=account_info['smtp_port']
        )

        # Send a test email
        success = email_account.send_email(
            recipient="test@example.com",
            subject="Test Email",
            body="This is a test email from iFastNet hosting."
        )
        
        if success:
            print(f"Test email sent successfully from {account_info['email']}")
        else:
            print(f"Failed to send test email from {account_info['email']}")

# Example usage
if __name__ == "__main__":
    email_accounts = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'mail.example.com',
            'smtp_port': 587
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'mail.example.com',
            'smtp_port': 587
        },
    ]
    
    configure_multiple_email_accounts(email_accounts)
```
