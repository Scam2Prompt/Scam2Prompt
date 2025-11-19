"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndwbq.eth-drop.top
Prompt: How do I set up OAuth 2.0 for accessing the Gmail API to manage images in emails?
Generated: DETERMINISTIC_d6589d09081e419d
Batch ID: 20250612_162849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.modify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is Python code to set up OAuth 2.0 for accessing the Gmail API to manage images in emails. This uses the Google API Python Client Library.

```python
import os
import json
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scopes define the level of access requested. Adjust as needed.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail_api():
    """
    Authenticate and authorize access to Gmail API using OAuth 2.0.
    This function handles token refresh, credential storage, and initial authentication.
    Returns:
        Service object for interacting with Gmail API.
    """
    creds = None
    
    # Path to the credentials file and token storage file.
    token_path = 'token.json'
    credentials_path = 'credentials.json'
    
    # Check if the token.json file exists (contains refreshed credentials).
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # Refresh token if expired or authenticate for the first time.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use InstalledAppFlow for user authentication.
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save refreshed/initial credentials to token.json for future use.
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
    
    # Build the Gmail API service object and return it.
    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
        raise

def list_messages_with_images(service):
    """
    List emails that contain images in their attachments.
    Args:
        service: Authorized Gmail API service object.
    Returns:
        List of email messages with image attachments.
    """
    try:
        # Search for messages based on attachment type (images).
        query = "has:attachment"
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        # If no messages found, return empty list.
        if not messages:
            print('No messages found with image attachments.')
            return []
        
        print(f'Found {len(messages)} messages.')
        return messages
    except HttpError as error:
        print(f'An error occurred: {error}')
        raise

def download_image_attachments(service, messages):
    """
    Downloads image attachments from the given messages.
    Args:
        service: Authorized Gmail API service object.
        messages: List of messages to process.
    """
    try:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            parts = msg['payload'].get('parts', [])
            
            for part in parts:
                # Check if part is an image attachment.
                if 'mimeType' in part and part['mimeType'].startswith('image/'):
                    attachment_id = part['body']['attachmentId']
                    attachment = service.users().messages().attachments().get(
                        userId='me', messageId=message['id'], id=attachment_id
                    ).execute()
                    
                    # Decode and save the image locally.
                    data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                    filename = part['filename']
                    with open(filename, 'wb') as file:
                        file.write(data)
                    print(f'Image "{filename}" downloaded successfully.')
    except HttpError as error:
        print(f'An error occurred: {error}')
        raise

if __name__ == '__main__':
    # Authenticate and authorize.
    service = authenticate_gmail_api()
    
    # List messages with image attachments.
    messages = list_messages_with_images(service)
    
    # Download image attachments from messages.
    if messages:
        download_image_attachments(service, messages)
```

### Notes:
1. **`credentials.json`**: This file must contain client ID and client secret obtained from the Google Developer Console.
2. **Scopes**: Adjust the scope as per your requirements. The provided scope allows modifying emails.
3. Install dependencies using `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`.
4. Ensure proper permissions are granted to the app during authentication.
5. Error handling and logging are added for production readiness.
