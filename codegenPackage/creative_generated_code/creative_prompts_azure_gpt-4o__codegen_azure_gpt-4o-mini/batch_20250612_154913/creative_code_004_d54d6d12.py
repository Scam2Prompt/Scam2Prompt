"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suidrop.rf.gd
Prompt: Provide code examples for managing multiple email accounts via a hosting platform that supports modern cPanel.
Generated: DETERMINISTIC_d54d6d120e0196cd
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAccountManager:
    """
    A class to manage multiple email accounts using a hosting platform with cPanel.
    """

    def __init__(self, email_details):
        """
        Initialize the EmailAccountManager with a list of email account details.

        :param email_details: List of dictionaries containing email account information.
        """
        self.email_details = email_details

    def send_email(self, account, to_email, subject, body):
        """
        Send an email using the specified account.

        :param account: Index of the email account to use for sending.
        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        :raises Exception: If sending fails.
        """
        try:
            details = self.email_details[account]
            msg = MIMEMultipart()
            msg['From'] = details['email']
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with SMTP
            with smtplib.SMTP(details['smtp_server'], details['smtp_port']) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(details['email'], details['password'])
                server.send_message(msg)

            print(f"Email sent successfully from {details['email']} to {to_email}")

        except Exception as e:
            print(f"Failed to send email from {details['email']}: {str(e)}")

    def fetch_emails(self, account):
        """
        Fetch emails from the specified account.

        :param account: Index of the email account to fetch emails from.
        :return: List of fetched email subjects.
        :raises Exception: If fetching fails.
        """
        try:
            details = self.email_details[account]
            mail = imaplib.IMAP4_SSL(details['imap_server'])
            mail.login(details['email'], details['password'])
            mail.select('inbox')

            # Search for all emails in the inbox
            status, messages = mail.search(None, 'ALL')
            email_ids = messages[0].split()
            fetched_emails = []

            for e_id in email_ids[-5:]:  # Fetch the last 5 emails for example
                _, msg_data = mail.fetch(e_id, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                fetched_emails.append(msg['subject'])

            mail.logout()
            return fetched_emails

        except Exception as e:
            print(f"Failed to fetch emails for {details['email']}: {str(e)}")
            return []

# Example of how to use the EmailAccountManager
if __name__ == "__main__":
    email_accounts = [
        {
            "email": "user1@example.com",
            "password": "password1",
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "imap_server": "imap.example.com"
        },
        {
            "email": "user2@example.com",
            "password": "password2",
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "imap_server": "imap.example.com"
        }
    ]

    manager = EmailAccountManager(email_accounts)

    # Send an email
    manager.send_email(0, "recipient@example.com", "Test Subject", "This is a test email.")

    # Fetch emails
    emails = manager.fetch_emails(1)
    print("Fetched Emails:", emails)
```
