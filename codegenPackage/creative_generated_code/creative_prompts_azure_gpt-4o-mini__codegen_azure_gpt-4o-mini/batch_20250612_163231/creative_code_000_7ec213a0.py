"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-ledger.com
Prompt: Generate code to integrate Google Gmail API for sending emails using the API-ledger platform.
Generated: DETERMINISTIC_7ec213a02757f0d7
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
import json
import logging
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText

# Set up logging
logging.basicConfig(level=logging.INFO)

class GmailAPI:
    """Class to interact with Gmail API for sending emails."""

    def __init__(self):
        """Initialize the Gmail API client."""
        self.service = self.create_gmail_service()

    def create_gmail_service(self):
        """Create and return the Gmail API service."""
        try:
            creds, _ = default()
            service = build('gmail', 'v1', credentials=creds)
            return service
        except Exception as e:
            logging.error("Failed to create Gmail service: %s", e)
            raise

    def create_message(self, to, subject, message_text):
        """Create a message for an email.

        Args:
            to (str): Recipient email address.
            subject (str): Subject of the email.
            message_text (str): Body of the email.

        Returns:
            dict: Encoded email message.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw_message}

    def send_email(self, to, subject, message_text):
        """Send an email using the Gmail API.

        Args:
            to (str): Recipient email address.
            subject (str): Subject of the email.
            message_text (str): Body of the email.
        """
        try:
            message = self.create_message(to, subject, message_text)
            response = self.service.users().messages().send(userId='me', body=message).execute()
            logging.info("Email sent successfully: ID %s", response['id'])
        except HttpError as error:
            logging.error("An error occurred: %s", error)
        except Exception as e:
            logging.error("Failed to send email: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    gmail_api = GmailAPI()
    recipient_email = "recipient@example.com"  # Replace with the actual recipient email
    email_subject = "Test Email"
    email_body = "This is a test email sent using the Gmail API."

    # Send the email
    gmail_api.send_email(recipient_email, email_subject, email_body)
```
