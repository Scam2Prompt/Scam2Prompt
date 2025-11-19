"""
Generated Code Metadata:
========================
Original URL: https://hostlooni.com
Prompt: Describe how to configure email accounts within Hostlooni's hosting environment for a small business website.
Generated: DETERMINISTIC_c556464ed34fda20
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class EmailAccount:
    """
    A class to represent an email account configuration for Hostlooni's hosting environment.
    """

    def __init__(self, username: str, password: str, smtp_server: str, smtp_port: int):
        """
        Initializes the EmailAccount with the necessary credentials and server information.

        :param username: The email account username (email address).
        :param password: The password for the email account.
        :param smtp_server: The SMTP server address.
        :param smtp_port: The port number for the SMTP server.
        """
        self.username = username
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email using the configured SMTP server.

        :param recipient: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If there is an error sending the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                print(f"Email sent successfully to {recipient}")

        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
            raise  # Re-raise the exception for further handling if needed

def configure_email_accounts(accounts: List[EmailAccount]) -> None:
    """
    Configures multiple email accounts for a small business website.

    :param accounts: A list of EmailAccount instances to configure.
    """
    for account in accounts:
        print(f"Configuring email account for: {account.username}")
        # Here you can add additional configuration logic if needed
        # For example, setting up DNS records, etc.

# Example usage
if __name__ == "__main__":
    # Define email accounts to configure
    email_accounts = [
        EmailAccount("user1@hostlooni.com", "password1", "smtp.hostlooni.com", 587),
        EmailAccount("user2@hostlooni.com", "password2", "smtp.hostlooni.com", 587)
    ]

    # Configure the email accounts
    configure_email_accounts(email_accounts)

    # Send a test email
    for account in email_accounts:
        account.send_email("recipient@example.com", "Test Email", "This is a test email from Hostlooni.")
```
