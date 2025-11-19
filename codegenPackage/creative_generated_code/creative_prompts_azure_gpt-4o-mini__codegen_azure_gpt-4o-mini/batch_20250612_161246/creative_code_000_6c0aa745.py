"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.com
Prompt: Write a Python script that uses the Gmail API to send an email with an attachment.
Generated: DETERMINISTIC_6c0aa7450c97a47a
Batch ID: 20250612_161246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.send": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'  # Path to your service account json file

def create_service():
    """Create a Gmail API service."""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('gmail', 'v1', credentials=credentials)
        return service
    except Exception as e:
        print(f"Error creating service: {e}")
        return None

def create_message(sender, to, subject, body, file_path):
    """Create a message for an email with an attachment."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Add body text
    message.attach(MIMEText(body, 'plain'))

    # Attach file
    if file_path:
        try:
            content_type, _ = mimetypes.guess_type(file_path)
            main_type, sub_type = content_type.split('/', 1)

            with open(file_path, 'rb') as f:
                part = MIMEBase(main_type, sub_type)
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                message.attach(part)
        except Exception as e:
            print(f"Error attaching file: {e}")
            return None

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, sender, to, subject, body, file_path=None):
    """Send an email with an optional attachment."""
    try:
        message = create_message(sender, to, subject, body, file_path)
        if message:
            service.users().messages().send(userId="me", body=message).execute()
            print(f"Email sent successfully to {to}.")
        else:
            print("Failed to create email message.")
    except HttpError as error:
        print(f"An error occurred: {error}")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

if __name__ == '__main__':
    # Define email details
    SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email
    RECIPIENT_EMAIL = 'recipient@example.com'  # Replace with recipient email
    SUBJECT = 'Test Email with Attachment'
    BODY = 'This is a test email with an attachment.'
    FILE_PATH = 'path/to/your/file.txt'  # Replace with path to your attachment

    # Create the Gmail service
    gmail_service = create_service()
    
    # Send the email
    if gmail_service:
        send_email(gmail_service, SENDER_EMAIL, RECIPIENT_EMAIL, SUBJECT, BODY, FILE_PATH)
```
