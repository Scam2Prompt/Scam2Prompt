"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain.hstn.me
Prompt: Recommend an API or library for managing multiple email accounts on iFastNet hosting, as described in their features.
Generated: DETERMINISTIC_54ace31766d12bac
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the `imaplib` and `smtplib` libraries (built into Python)
to manage multiple email accounts. For iFastNet hosting, the script assumes 
IMAP and SMTP protocols are supported. You can retrieve, send, and manage 
emails as per the hosting provider's documentation.

Note: Replace placeholders with actual values such as email credentials 
      and server addresses provided by iFastNet.

Dependencies:
- imaplib (for receiving and managing emails)
- smtplib (for sending emails)
"""

import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define a class to manage multiple email accounts
class EmailAccountManager:
    def __init__(self, imap_server, smtp_server, email_address, password):
        """
        Initialize the EmailAccountManager with server details and credentials.
        """
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.email_address = email_address
        self.password = password
        self.imap_connection = None
        self.smtp_connection = None

    def connect_imap(self):
        """
        Connect to the IMAP server.
        """
        try:
            self.imap_connection = imaplib.IMAP4_SSL(self.imap_server)
            self.imap_connection.login(self.email_address, self.password)
            print(f"IMAP: Connected and authenticated as {self.email_address}")
        except Exception as e:
            print(f"IMAP Connection Error: {e}")

    def connect_smtp(self):
        """
        Connect to the SMTP server.
        """
        try:
            self.smtp_connection = smtplib.SMTP(self.smtp_server, 587)
            self.smtp_connection.starttls()  # Secure the connection
            self.smtp_connection.login(self.email_address, self.password)
            print(f"SMTP: Connected and authenticated as {self.email_address}")
        except Exception as e:
            print(f"SMTP Connection Error: {e}")

    def fetch_emails(self, folder="INBOX", search_criteria="ALL"):
        """
        Fetch emails from a specific folder using search criteria.
        """
        if not self.imap_connection:
            print("IMAP: Not connected.")
            return []

        try:
            self.imap_connection.select(folder)
            status, messages = self.imap_connection.search(None, search_criteria)
            email_ids = messages[0].split()
            print(f"IMAP: {len(email_ids)} messages found in {folder}.")
            return email_ids
        except Exception as e:
            print(f"IMAP Fetch Error: {e}")
            return []

    def send_email(self, to_address, subject, body):
        """
        Send an email to a specific recipient.
        """
        if not self.smtp_connection:
            print("SMTP: Not connected.")
            return

        try:
            message = MIMEMultipart()
            message["From"] = self.email_address
            message["To"] = to_address
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            self.smtp_connection.sendmail(self.email_address, to_address, message.as_string())
            print(f"SMTP: Email sent to {to_address}.")
        except Exception as e:
            print(f"SMTP Send Error: {e}")

    def disconnect_imap(self):
        """
        Disconnect from the IMAP server.
        """
        if self.imap_connection:
            self.imap_connection.logout()
            print("IMAP: Disconnected.")

    def disconnect_smtp(self):
        """
        Disconnect from the SMTP server.
        """
        if self.smtp_connection:
            self.smtp_connection.quit()
            print("SMTP: Disconnected.")


# Example usage:
if __name__ == "__main__":
    # Replace the placeholders with actual server details and credentials.
    imap_server = "your_imap_server"  # e.g., "imap.example.com"
    smtp_server = "your_smtp_server"  # e.g., "smtp.example.com"
    email_address = "your_email@example.com"
    password = "your_email_password"

    # Initialize the manager
    email_manager = EmailAccountManager(imap_server, smtp_server, email_address, password)

    # Connect to servers
    email_manager.connect_imap()
    email_manager.connect_smtp()

    # Fetch emails
    email_manager.fetch_emails()

    # Send an email
    email_manager.send_email("recipient@example.com", "Test Subject", "This is a test email.")

    # Disconnect from servers
    email_manager.disconnect_imap()
    email_manager.disconnect_smtp()
```
