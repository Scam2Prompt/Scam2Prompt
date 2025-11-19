"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beam-prize.com
Prompt: Explain how to integrate Gmail API for sending images through email.
Generated: DETERMINISTIC_1d6fae020b8388e0
Batch ID: 20250612_155555
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
import base64
import os
import re
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail_api():
    """Authenticate and return a Gmail API service instance."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Build the Gmail service
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_image_attachment(image_path):
    """Create a base64 encoded email attachment for an image."""
    try:
        # Read the image file and encode it to base64
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            base64_image = base64.urlsafe_b64encode(img_data).decode('utf-8')
            return base64_image
    except Exception as e:
        print(f"Error creating image attachment: {e}")
        raise

def send_email_with_image(service, to_email, subject, body, image_path):
    """Send an email with an image attachment using Gmail API."""
    try:
        # Create the email message
        message = {
            'raw': base64.urlsafe_b64encode(
                f"From: me\nTo: {to_email}\nSubject: {subject}\n\n{body}".encode("UTF-8")
            ).decode("utf-8"),
            'payload': {
                'headers': [
                    {'name': 'To', 'value': to_email},
                    {'name': 'Subject', 'value': subject},
                ],
                'parts': [
                    {
                        'filename': os.path.basename(image_path),
                        'mimeType': 'image/jpeg',
                        'body': {
                            'data': create_image_attachment(image_path),
                            'attachmentId': None,
                        },
                    }
                ],
            },
        }

        # Send the email
        service.users().messages().send(userId="me", body=message).execute()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        raise

def main():
    """Main function to execute the workflow."""
    # Authenticate and create a Gmail API service
    service = authenticate_gmail_api()

    # Define email details
    to_email = 'recipient@example.com'  # Replace with recipient's email
    subject = 'Image Attachment Example'
    body = 'Please find the attached image.'
    image_path = 'path/to/image.jpg'  # Replace with the path to your image

    # Send the email with image attachment
    send_email_with_image(service, to_email, subject, body, image_path)

if __name__ == '__main__':
    main()
```

### Note:
Make sure to replace `'credentials.json'` with your actual credentials file and adjust the `to_email` and `image_path` variables as needed. Additionally, ensure you have the necessary libraries installed, using a command like:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
