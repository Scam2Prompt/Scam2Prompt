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

```python
import smtplib
from imaplib import IMAP4_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

class EmailManager:
    """
    A class to manage multiple email accounts on iFastNet hosting.
    Provides functionalities to send and receive emails while handling multiple accounts.
    """

    def __init__(self, accounts: List[Dict[str, str]]):
        """
        Initialize the EmailManager with a list of email account credentials.

        :param accounts: A list of dictionaries, where each dictionary contains
                         'email', 'password', and 'smtp_server' for sending emails,
                         and 'imap_server' for receiving emails.
        """
        self.accounts = accounts

    def send_email(self, to: str, subject: str, body: str, account_index: int) -> bool:
        """
        Send an email using the specified account.

        :param to: Recipient email address.
        :param subject: Subject of the email.
        :param body: Body of the email.
        :param account_index: Index of the account to use for sending the email.
        :return: True if the email is sent successfully, False otherwise.
        """
        account = self.accounts[account_index]
        try:
            # Set up the SMTP server
            with smtplib.SMTP_SSL(account['smtp_server'], 465) as server:
                server.login(account['email'], account['password'])
                
                # Create the email
                msg = MIMEMultipart()
                msg['From'] = account['email']
                msg['To'] = to
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Error sending email from {account['email']}: {e}")
            return False

    def fetch_emails(self, account_index: int) -> List[str]:
        """
        Fetch unread emails from the specified account.

        :param account_index: Index of the account to fetch emails from.
        :return: A list of unread email subjects.
        """
        account = self.accounts[account_index]
        try:
            # Connect to the IMAP server
            with IMAP4_SSL(account['imap_server']) as mail:
                mail.login(account['email'], account['password'])
                mail.select('inbox')
                
                # Search for unread emails
                status, messages = mail.search(None, 'UNSEEN')
                email_ids = messages[0].split()
                
                # Retrieve email subjects
                subjects = []
                for email_id in email_ids:
                    status, msg_data = mail.fetch(email_id, '(RFC822)')
                    raw_email = msg_data[0][1]
                    subjects.append(self.get_subject(raw_email))
                
                return subjects
        except Exception as e:
            print(f"Error fetching emails for {account['email']}: {e}")
            return []

    @staticmethod
    def get_subject(raw_email: bytes) -> str:
        """
        Extract the subject from a raw email message.

        :param raw_email: The raw email message in bytes.
        :return: The subject of the email.
        """
        from email import message_from_bytes
        msg = message_from_bytes(raw_email)
        return msg['subject'] if msg['subject'] else "No Subject"

# Example usage:
if __name__ == "__main__":
    # Define email accounts with their credentials
    accounts = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'smtp.example.com',
            'imap_server': 'imap.example.com'
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'smtp.example.com',
            'imap_server': 'imap.example.com'
        }
    ]

    email_manager = EmailManager(accounts)

    # Send an email using the first account
    email_manager.send_email('recipient@example.com', 'Test Subject', 'This is a test email.', 0)

    # Fetch unread emails from the second account
    unread_subjects = email_manager.fetch_emails(1)
    print("Unread emails:", unread_subjects)
```
