"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woo-prize.net
Prompt: Provide an example of using the Google Gmail API to create a draft email programmatically.
Generated: DETERMINISTIC_37656a2207179d58
Batch ID: 20250612_160220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.compose": {
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
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def authenticate_gmail_api():
    """Authenticate to the Gmail API and return the service object."""
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
                'credentials.json', SCOPES)  # Path to the credentials file
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_draft(service, user_id, message_body):
    """Create a draft email."""
    try:
        # Create the email message
        message = {
            'raw': base64.urlsafe_b64encode(message_body.encode('utf-8')).decode('utf-8')
        }

        # Call the Gmail API to create the draft
        draft = service.users().drafts().create(userId=user_id, body=message).execute()
        print(f"Draft created with id: {draft['id']}")
        return draft

    except Exception as error:
        print(f"An error occurred: {error}")
        return None

def main():
    """Main function to run the script."""
    # Authenticate and build the Gmail API service
    service = authenticate_gmail_api()

    # User ID is typically 'me' for the authenticated user
    user_id = 'me'

    # Construct the email message
    message_body = """\
    From: your_email@example.com
    To: recipient@example.com
    Subject: Test Draft Email

    This is a test draft email created using the Gmail API.
    """
    
    # Create a draft email
    create_draft(service, user_id, message_body)

if __name__ == '__main__':
    main()
```

Make sure to replace `your_email@example.com` and `recipient@example.com` with actual email addresses. Also, ensure you have the appropriate `credentials.json` file from the Google Developer Console for the application to authenticate properly with the Gmail API.
