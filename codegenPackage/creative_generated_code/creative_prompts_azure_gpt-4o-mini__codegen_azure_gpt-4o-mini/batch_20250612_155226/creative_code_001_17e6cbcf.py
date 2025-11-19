"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spxx6900.com
Prompt: Write a Python script that utilizes the Google Gmail API for advanced search functionality in emails.
Generated: DETERMINISTIC_17e6cbcfa75dcf8a
Batch ID: 20250612_155226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.readonly": {
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
import logging
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail_api():
    """Authenticate the user and return the Gmail API service instance."""
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

def search_emails(service, query):
    """Search for emails matching the query string."""
    try:
        response = service.users().messages().list(userId='me', q=query).execute()
        messages = response.get('messages', [])
        
        if not messages:
            logger.info('No messages found.')
            return []

        logger.info(f'Found {len(messages)} messages.')
        return messages
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        return []

def get_email_details(service, msg_id):
    """Get details of a specific email by message ID."""
    try:
        msg = service.users().messages().get(userId='me', id=msg_id).execute()
        email_data = msg['payload']['headers']
        
        # Extract subject and sender
        subject = next(header['value'] for header in email_data if header['name'] == 'Subject')
        sender = next(header['value'] for header in email_data if header['name'] == 'From')
        
        # Decode and return email information
        return {
            'id': msg_id,
            'subject': subject,
            'sender': sender,
            'snippet': msg.get('snippet')
        }
    except Exception as e:
        logger.error(f'An error occurred while fetching email details: {e}')
        return None

def main():
    """Main function to execute email search."""
    # Authenticate and create the Gmail API service
    service = authenticate_gmail_api()
    
    # Define your search query here
    user_query = input("Enter your search query (Gmail search syntax): ")
    
    # Validate user input (basic check)
    if not re.match(r'^[\w\s]+$', user_query):
        logger.error('Invalid query format. Use plain text.')
        return

    # Search for emails
    messages = search_emails(service, user_query)
    
    # Fetch and display details for each found email
    for msg in messages:
        email_details = get_email_details(service, msg['id'])
        if email_details:
            logger.info(f"Email ID: {email_details['id']}, Subject: {email_details['subject']}, From: {email_details['sender']}, Snippet: {email_details['snippet']}")

if __name__ == '__main__':
    main()
```

### Requirements:
- Ensure you have installed the required libraries using pip:
  ```bash
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```
- You need to set up your Google Cloud project, enable the Gmail API, and create `credentials.json` file for OAuth 2.0.
