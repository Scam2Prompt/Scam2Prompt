"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apello.one
Prompt: Provide an example of using the Gmail API to create and send a draft email programmatically.
Generated: DETERMINISTIC_d743498cc3d855c6
Batch ID: 20250612_163149
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
from googleapiclient.errors import HttpError

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def authenticate_gmail_api():
    """Authenticate and create a service for the Gmail API."""
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
    return build('gmail', 'v1', credentials=creds)

def create_draft(service, user_id, message_body):
    """Create and send a draft email."""
    try:
        message = {
            'message': {
                'raw': base64.urlsafe_b64encode(message_body.encode('utf-8')).decode('utf-8')
            }
        }
        draft = service.users().drafts().create(userId=user_id, body=message).execute()
        print(f'Draft created with ID: {draft["id"]}')
        return draft
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def main():
    """Main function to send a draft email."""
    # Authenticate and create a Gmail API service
    service = authenticate_gmail_api()
    
    # Define the email components
    user_id = 'me'  # Special identifier for authenticated user
    to = 'recipient@example.com'
    subject = 'Test Draft Email'
    message_text = 'This is a test draft email sent using the Gmail API.'

    # Construct the raw message
    message_body = f'To: {to}\nSubject: {subject}\n\n{message_text}'

    # Create the draft email
    create_draft(service, user_id, message_body)

if __name__ == '__main__':
    main()
```
