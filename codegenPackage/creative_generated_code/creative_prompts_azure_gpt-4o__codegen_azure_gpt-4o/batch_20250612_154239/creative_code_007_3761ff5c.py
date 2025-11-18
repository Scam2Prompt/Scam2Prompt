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
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailAccount:
    """
    Class for configuring and sending emails using multiple accounts.
    """
    def __init__(self, email_address, password, smtp_server, smtp_port):
        """
        Initialize an email account.

        :param email_address: The email address for the account.
        :param password: The password for the account.
        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP port number.
        """
        self.email_address = email_address
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, to_address, subject, body):
        """
        Send an email using the configured account.

        :param to_address: Recipient email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        :raises Exception: Raises exception if email sending fails.
        """
        # Create a secure SSL context
        context = ssl.create_default_context()

        try:
            # Initialize SMTP connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)  # Secure connection
                server.login(self.email_address, self.password)  # Login
                
                # Create the email (MIME format)
                msg = MIMEMultipart()
                msg['From'] = self.email_address
                msg['To'] = to_address
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))  # Add the email body
                
                # Send the email
                server.sendmail(self.email_address, to_address, msg.as_string())
                print(f"Email sent successfully to {to_address}")

        except Exception as e:
            # Handle errors gracefully
            print(f"Failed to send email to {to_address}: {e}")
            raise


class HostingEmailManager:
    """
    Manage multiple email accounts for a hosting service.
    """
    def __init__(self):
        """
        Initialize the email manager with an empty list of accounts.
        """
        self.email_accounts = []

    def add_email_account(self, email_address, password, smtp_server, smtp_port):
        """
        Add a new email account to the manager.

        :param email_address: Email address to be added.
        :param password: Password for the account.
        :param smtp_server: SMTP server address.
        :param smtp_port: SMTP port number.
        """
        account = EmailAccount(email_address, password, smtp_server, smtp_port)
        self.email_accounts.append(account)
        print(f"Email account {email_address} added successfully.")

    def send_email_from_all_accounts(self, to_address, subject, body):
        """
        Send an email from all configured accounts.

        :param to_address: Recipient email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        """
        for account in self.email_accounts:
            try:
                account.send_email(to_address, subject, body)
            except Exception as e:
                print(f"Error sending email from {account.email_address}: {e}")


# Example usage:

if __name__ == "__main__":
    # Initialize the hosting email manager
    manager = HostingEmailManager()

    # Add email accounts
    manager.add_email_account(
        email_address="example1@example.com",
        password="password1",
        smtp_server="smtp.example.com",
        smtp_port=587
    )
    manager.add_email_account(
        email_address="example2@example.com",
        password="password2",
        smtp_server="smtp.example.com",
        smtp_port=587
    )

    # Send an email from all accounts
    manager.send_email_from_all_accounts(
        to_address="recipient@example.com",
        subject="Greetings from Hosting Email Manager",
        body="This is a test email sent from multiple accounts."
    )
```
