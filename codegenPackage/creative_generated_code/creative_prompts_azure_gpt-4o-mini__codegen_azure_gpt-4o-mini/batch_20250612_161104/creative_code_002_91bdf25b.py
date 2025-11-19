"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woonetwork.pages.dev
Prompt: What are the best practices for using the Google Gmail API in a business solution?
Generated: DETERMINISTIC_91bdf25b97b53b6a
Batch ID: 20250612_161104
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
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope for accessing the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail_api():
    """Authenticate and create a service for the Gmail API.

    Returns:
        service: A service object for interacting with the Gmail API.
    """
    creds = None
    # Token storage for user credentials
    token_path = 'token.pickle'
    creds_file = 'credentials.json'

    # Load previously saved credentials
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    try:
        # Create the service object
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def list_labels(service):
    """List the labels in the user's Gmail account.

    Args:
        service: The Gmail API service object.

    Returns:
        labels: A list of label names.
    """
    try:
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return []

        print('Labels:')
        label_names = [label['name'] for label in labels]
        return label_names
    except HttpError as error:
        print(f'An error occurred: {error}')
        return []

def main():
    """Main function to authenticate and list Gmail labels."""
    # Authenticate the Gmail API
    service = authenticate_gmail_api()
    
    if service:
        # List the labels in the user's account
        labels = list_labels(service)
        print(labels)

if __name__ == '__main__':
    main()
```
