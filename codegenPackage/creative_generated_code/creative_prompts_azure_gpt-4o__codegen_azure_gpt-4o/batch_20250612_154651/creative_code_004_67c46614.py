"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappchainweb.rf.gd
Prompt: Provide an example of configuring multiple email accounts for a web hosting service with unlimited disk space and bandwidth, as described on iFastNet.
Generated: DETERMINISTIC_67c46614bf11af97
Batch ID: 20250612_154651
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
    """
    A class to represent an email account for configuration.
    """
    def __init__(self, email_address, password, smtp_server, smtp_port):
        self.email_address = email_address
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email using this account.

        :param recipient_email: str - The recipient's email address
        :param subject: str - The subject of the email
        :param body: str - The body of the email
        :return: None
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable encryption
                server.login(self.email_address, self.password)
                server.send_message(msg)
            print(f"Email sent successfully to {recipient_email}.")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}. Error: {e}")

# Example configuration of multiple email accounts
def configure_email_accounts():
    """
    Configures multiple email accounts for the web hosting service.

    :return: List[EmailAccount] - A list of configured email accounts
    """
    try:
        email_accounts = [
            EmailAccount("account1@example.com", "password1", "smtp.example.com", 587),
            EmailAccount("account2@example.com", "password2", "smtp.example.com", 587),
            EmailAccount("account3@example.com", "password3", "smtp.example.com", 587)
        ]
        print("Email accounts configured successfully.")
        return email_accounts
    except Exception as e:
        print(f"Failed to configure email accounts. Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Configure email accounts
    email_accounts = configure_email_accounts()

    if email_accounts:
        # Send test email from the first configured account
        email_accounts[0].send_email(
            recipient_email="recipient@example.com",
            subject="Test Email",
            body="This is a test email sent from a configured email account."
        )
```
