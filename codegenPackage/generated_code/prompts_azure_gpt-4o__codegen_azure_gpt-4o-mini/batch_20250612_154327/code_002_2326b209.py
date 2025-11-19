"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Recommend libraries or tools for managing multiple email accounts on a hosting platform with unlimited bandwidth and free domain names, such as the one described on iFastNet.
Generated: DETERMINISTIC_2326b2097131796e
Batch ID: 20250612_154327
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
from typing import List, Dict

class EmailManager:
    """
    A class to manage multiple email accounts for sending emails.
    """

    def __init__(self, email_accounts: List[Dict[str, str]]):
        """
        Initializes the EmailManager with a list of email accounts.

        :param email_accounts: A list of dictionaries containing email account details.
        """
        self.email_accounts = email_accounts

    def send_email(self, to_email: str, subject: str, body: str, from_email: str):
        """
        Sends an email using the specified email account.

        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        :param from_email: Sender's email address.
        """
        # Find the email account details
        account = next((acc for acc in self.email_accounts if acc['email'] == from_email), None)
        if not account:
            raise ValueError(f"Email account {from_email} not found.")

        try:
            # Set up the server
            with smtplib.SMTP(account['smtp_server'], account['smtp_port']) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(account['email'], account['password'])

                # Create the email
                msg = MIMEMultipart()
                msg['From'] = from_email
                msg['To'] = to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.send_message(msg)
                print(f"Email sent successfully from {from_email} to {to_email}.")

        except smtplib.SMTPException as e:
            print(f"Failed to send email from {from_email} to {to_email}: {e}")

# Example usage
if __name__ == "__main__":
    # List of email accounts
    email_accounts = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587
        }
    ]

    # Create an instance of EmailManager
    email_manager = EmailManager(email_accounts)

    # Send an email
    try:
        email_manager.send_email(
            to_email='recipient@example.com',
            subject='Test Email',
            body='This is a test email.',
            from_email='user1@example.com'
        )
    except ValueError as ve:
        print(ve)
```
