"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: Outline a library recommendation for integrating email communication within an accounting software, considering the emphasis on client availability highlighted by Atual Contabilidade.
Generated: DETERMINISTIC_e1590641903d1df7
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Library Recommendation: `smtplib` for sending emails and `imaplib` for receiving emails.
This Python module provides a clean implementation for integrating email communication
within accounting software, emphasizing client availability.

The code below demonstrates sending and receiving emails using these libraries.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailClient:
    """
    A class to handle email communication for accounting software.
    """

    def __init__(self, smtp_server, smtp_port, imap_server, email_address, email_password):
        """
        Initialize the EmailClient with server details and credentials.

        :param smtp_server: SMTP server address for sending emails
        :param smtp_port: SMTP server port
        :param imap_server: IMAP server address for receiving emails
        :param email_address: Email address for authentication
        :param email_password: Password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server
        self.email_address = email_address
        self.email_password = email_password

    def send_email(self, recipient, subject, body):
        """
        Send an email to a recipient.

        :param recipient: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def fetch_emails(self, folder="INBOX"):
        """
        Fetch emails from the specified folder.

        :param folder: Folder to fetch emails from (default is "INBOX")
        :return: List of email subjects
        """
        try:
            # Connect to the IMAP server
            with imaplib.IMAP4_SSL(self.imap_server) as mail:
                mail.login(self.email_address, self.email_password)
                mail.select(folder)

                # Search for all emails in the folder
                status, messages = mail.search(None, 'ALL')
                if status != "OK":
                    logging.error("Failed to fetch emails")
                    return []

                email_subjects = []
                for num in messages[0].split():
                    status, data = mail.fetch(num, '(RFC822)')
                    if status != "OK":
                        logging.error(f"Failed to fetch email with ID {num}")
                        continue

                    # Parse the email content
                    msg = email.message_from_bytes(data[0][1])
                    email_subjects.append(msg['Subject'])

                logging.info(f"Fetched {len(email_subjects)} emails from {folder}")
                return email_subjects
        except Exception as e:
            logging.error(f"Failed to fetch emails: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Replace with actual credentials and server details
    smtp_server = "smtp.example.com"
    smtp_port = 587
    imap_server = "imap.example.com"
    email_address = "your_email@example.com"
    email_password = "your_password"

    # Initialize the EmailClient
    email_client = EmailClient(smtp_server, smtp_port, imap_server, email_address, email_password)

    # Send an email
    email_client.send_email("client_email@example.com", "Monthly Report", "Dear Client, please find the attached report.")

    # Fetch emails
    subjects = email_client.fetch_emails()
    print("Fetched email subjects:", subjects)
```
