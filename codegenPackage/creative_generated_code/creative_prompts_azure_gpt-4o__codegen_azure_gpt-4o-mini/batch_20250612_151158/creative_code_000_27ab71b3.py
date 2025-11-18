"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://networkitcnetworkmo.com
Prompt: Write a Python script to automate the process of extracting the "Unsubscribe" link from emails sent via VertiStream's email marketing service.
Generated: DETERMINISTIC_27ab71b313793fb0
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import imaplib
import email
from email.header import decode_header
import re

class EmailExtractor:
    def __init__(self, email_user, email_pass, imap_server='imap.gmail.com'):
        """
        Initializes the EmailExtractor with user credentials and IMAP server.
        
        :param email_user: str - The email address of the user.
        :param email_pass: str - The password for the user's email account.
        :param imap_server: str - The IMAP server address. Default is Gmail's server.
        """
        self.email_user = email_user
        self.email_pass = email_pass
        self.imap_server = imap_server
        self.connection = None

    def connect(self):
        """Connect to the email server using IMAP."""
        try:
            self.connection = imaplib.IMAP4_SSL(self.imap_server)
            self.connection.login(self.email_user, self.email_pass)
            print("Successfully connected to the email server.")
        except imaplib.IMAP4.error as e:
            print(f"Failed to connect to the email server: {e}")
            raise

    def fetch_emails(self, folder='INBOX'):
        """
        Fetches emails from the specified folder.
        
        :param folder: str - The email folder to search. Default is 'INBOX'.
        :return: list - A list of email IDs in the specified folder.
        """
        try:
            self.connection.select(folder)
            status, messages = self.connection.search(None, 'ALL')
            email_ids = messages[0].split()
            return email_ids
        except Exception as e:
            print(f"Failed to fetch emails: {e}")
            raise

    def extract_unsubscribe_link(self, email_body):
        """
        Extracts the 'Unsubscribe' link from the email body.
        
        :param email_body: str - The raw email body content.
        :return: str or None - The 'Unsubscribe' link if found, otherwise None.
        """
        # Regular expression to find the 'Unsubscribe' link
        match = re.search(r'(https?://[^\s]+)', email_body)
        return match.group(0) if match else None

    def process_emails(self):
        """Processes fetched emails to extract 'Unsubscribe' links."""
        email_ids = self.fetch_emails()
        for email_id in email_ids:
            try:
                # Fetch the email by ID
                status, msg_data = self.connection.fetch(email_id, '(RFC822)')
                raw_email = msg_data[0][1]
                mail = email.message_from_bytes(raw_email)

                # Decode email subject
                subject, _ = decode_header(mail['Subject'])[0]
                subject = subject.decode() if isinstance(subject, bytes) else subject

                # Check if the email is multipart
                if mail.is_multipart():
                    for part in mail.walk():
                        if part.get_content_type() == 'text/plain':
                            email_body = part.get_payload(decode=True).decode()
                            break
                else:
                    email_body = mail.get_payload(decode=True).decode()

                # Extract 'Unsubscribe' link
                unsubscribe_link = self.extract_unsubscribe_link(email_body)
                if unsubscribe_link:
                    print(f"Unsubscribe link found in '{subject}': {unsubscribe_link}")
                else:
                    print(f"No Unsubscribe link found in '{subject}'.")

            except Exception as e:
                print(f"Error processing email ID {email_id}: {e}")

    def close_connection(self):
        """Closes the connection to the email server."""
        if self.connection:
            self.connection.logout()
            print("Connection closed.")

if __name__ == "__main__":
    # Replace with your email and password
    EMAIL_USER = 'your_email@example.com'
    EMAIL_PASS = 'your_email_password'

    extractor = EmailExtractor(EMAIL_USER, EMAIL_PASS)
    try:
        extractor.connect()
        extractor.process_emails()
    finally:
        extractor.close_connection()
```

**Note:** Be sure to replace `'your_email@example.com'` and `'your_email_password'` with your actual email credentials. Using environment variables or a secure vault to manage sensitive information is recommended for production code.
