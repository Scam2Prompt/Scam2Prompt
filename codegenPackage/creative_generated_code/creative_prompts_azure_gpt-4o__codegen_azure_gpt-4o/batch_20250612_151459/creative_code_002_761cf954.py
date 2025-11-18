"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Recommend libraries or tools to manage multiple email accounts on iFastNet hosting, considering their unlimited disk space and free domain name offerings.
Generated: DETERMINISTIC_761cf9540d3dc813
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that uses the IMAP and SMTP protocols to manage multiple email accounts hosted on iFastNet. It leverages popular libraries like `imaplib` and `smtplib` for email operations and `email` for handling email content. 

```python
# email_manager.py

import imaplib
import smtplib
from email.message import EmailMessage
from typing import List, Tuple


class EmailManager:
    """
    A class to manage multiple email accounts using IMAP and SMTP protocols.
    Designed for iFastNet hosting or similar platforms.
    """

    def __init__(self, email_host: str, smtp_port: int = 587, imap_port: int = 993):
        """
        Initialize the EmailManager with the host and default ports.

        :param email_host: The host for email services (e.g., 'mail.ifastnet.com').
        :param smtp_port: The SMTP port (default is 587).
        :param imap_port: The IMAP port (default is 993).
        """
        self.email_host = email_host
        self.smtp_port = smtp_port
        self.imap_port = imap_port

    def send_email(self, sender_email: str, sender_password: str, recipient_email: str, subject: str, body: str):
        """
        Send an email using SMTP.

        :param sender_email: The email address of the sender.
        :param sender_password: The password for the sender's email account.
        :param recipient_email: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        """
        try:
            # Create an SMTP session
            server = smtplib.SMTP(self.email_host, self.smtp_port)
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Authenticate

            # Create the email message
            msg = EmailMessage()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.set_content(body)

            # Send the email
            server.send_message(msg)
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()

    def fetch_emails(self, email_account: str, password: str, mailbox: str = 'INBOX') -> List[Tuple[str, str]]:
        """
        Fetch emails from the specified mailbox using IMAP.

        :param email_account: The email account to fetch emails from.
        :param password: The password for the email account.
        :param mailbox: The mailbox to fetch emails from (default is 'INBOX').
        :return: A list of tuples containing email subject and sender.
        """
        try:
            # Connect to the IMAP server
            mail = imaplib.IMAP4_SSL(self.email_host, self.imap_port)
            mail.login(email_account, password)  # Authenticate
            mail.select(mailbox)  # Select the mailbox

            # Search for all emails
            status, email_ids = mail.search(None, 'ALL')
            if status != 'OK':
                raise Exception("Failed to retrieve emails.")

            emails = []
            for email_id in email_ids[0].split():
                # Fetch the email
                status, data = mail.fetch(email_id, '(RFC822)')
                if status != 'OK':
                    raise Exception(f"Failed to fetch email with ID {email_id}.")

                # Parse the email content
                raw_email = data[0][1]
                msg = EmailMessage()
                msg.set_payload(raw_email)

                subject = msg['Subject']
                sender = msg['From']
                emails.append((subject, sender))

            return emails
        except Exception as e:
            print(f"Error fetching emails: {e}")
            return []
        finally:
            mail.logout()


# Example usage
if __name__ == "__main__":
    # Replace the below values with your own credentials and host details.
    EMAIL_HOST = "mail.ifastnet.com"
    email_manager = EmailManager(email_host=EMAIL_HOST)

    # Sending an email
    email_manager.send_email(
        sender_email="your_email@ifastnet.com",
        sender_password="your_password",
        recipient_email="recipient_email@example.com",
        subject="Test Email",
        body="This is a test email sent from the email manager."
    )

    # Fetching emails
    emails = email_manager.fetch_emails(
        email_account="your_email@ifastnet.com",
        password="your_password"
    )
    for subject, sender in emails:
        print(f"Subject: {subject}, Sender: {sender}")
```

Save this script as `email_manager.py`, replace placeholder credentials with actual ones, and run it. Make sure to install any dependencies (`pip install secure-smtplib` or equivalent) based on your exact requirements.
