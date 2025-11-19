"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspicious-euler-473151.netlify.app
Prompt: Generate code to integrate a Mac email client with Exchange server settings.
Generated: DETERMINISTIC_f985a3347f72142c
Batch ID: 20250612_163817
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
import imaplib
import email
import ssl

class ExchangeClient:
    """
    A class to represent an Exchange email client for sending and receiving emails.
    """

    def __init__(self, email_address, password, smtp_server, imap_server, smtp_port=587, imap_port=993):
        """
        Initializes the ExchangeClient with necessary credentials and server settings.

        Args:
            email_address (str): The email address of the user.
            password (str): The password for the email account.
            smtp_server (str): The SMTP server address for sending emails.
            imap_server (str): The IMAP server address for receiving emails.
            smtp_port (int, optional): The port for the SMTP server. Defaults to 587.
            imap_port (int, optional): The port for the IMAP server. Defaults to 993.
        """
        self.email_address = email_address
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.smtp_port = smtp_port
        self.imap_port = imap_port

    def send_email(self, to_address, subject, body):
        """
        Sends an email using the SMTP server.

        Args:
            to_address (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Raises:
            Exception: If sending the email fails.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_address
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email_address, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
            print(f"Email sent to {to_address} successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def receive_emails(self):
        """
        Connects to the IMAP server and retrieves unread emails.

        Returns:
            list: A list of unread email messages.

        Raises:
            Exception: If connecting to the IMAP server fails.
        """
        try:
            # Connect to the IMAP server and log in
            with imaplib.IMAP4_SSL(self.imap_server, self.imap_port) as mail:
                mail.login(self.email_address, self.password)  # Log in to the IMAP server
                mail.select("inbox")  # Select the inbox folder

                # Search for all unread emails
                result, data = mail.search(None, 'UNSEEN')
                unread_email_ids = data[0].split()

                emails = []
                for email_id in unread_email_ids:
                    result, msg_data = mail.fetch(email_id, '(RFC822)')
                    raw_email = msg_data[0][1]
                    msg = email.message_from_bytes(raw_email)
                    emails.append(msg)

                return emails
        except Exception as e:
            print(f"Failed to receive emails: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Replace with your actual email settings
    EMAIL_ADDRESS = "user@example.com"
    PASSWORD = "your_password"
    SMTP_SERVER = "smtp.example.com"
    IMAP_SERVER = "imap.example.com"

    exchange_client = ExchangeClient(EMAIL_ADDRESS, PASSWORD, SMTP_SERVER, IMAP_SERVER)

    # Send a test email
    exchange_client.send_email("recipient@example.com", "Test Subject", "This is a test email body.")

    # Receive unread emails
    unread_emails = exchange_client.receive_emails()
    for email in unread_emails:
        print(f"From: {email['From']}, Subject: {email['Subject']}")
```
