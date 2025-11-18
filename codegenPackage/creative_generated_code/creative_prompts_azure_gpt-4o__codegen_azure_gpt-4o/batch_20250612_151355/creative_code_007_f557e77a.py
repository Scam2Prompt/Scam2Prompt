"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krnas.com
Prompt: Generate a step-by-step guide to enable Gmail API access for a Python application and write code to fetch email metadata.
Generated: DETERMINISTIC_f557e77aa491394e
Batch ID: 20250612_151355
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://console.cloud.google.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
"""
Step-by-Step Guide to Enable Gmail API Access:
1. Go to https://console.cloud.google.com/ and create a new project.
2. Enable the Gmail API for your project.
3. Configure OAuth consent screen and add necessary scopes.
4. Create credentials (OAuth 2.0 client ID) for your application.
5. Download the credentials JSON file.
6. Install the required Python packages: `google-auth`, `google-auth-oauthlib`, and `google-api-python-client`.
7. Place the credentials JSON file in your project directory and reference it in the code.

Below is the Python code to fetch email metadata using the Gmail API:
"""

# Required imports
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the Gmail scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail_api(credentials_file='credentials.json', token_file='token.pickle'):
    """
    Authenticate and create a service object to interact with the Gmail API.
    
    Args:
        credentials_file (str): Path to the OAuth2 credentials file.
        token_file (str): Path to the token file to store user credentials.

    Returns:
        service: Gmail API service object.
    """
    creds = None

    # Load previously saved token if it exists
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # Refresh token if expired, or initiate authentication flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future use
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    # Create Gmail API service object
    service = build('gmail', 'v1', credentials=creds)
    return service

def fetch_email_metadata(service, user_id='me', max_results=10):
    """
    Fetch metadata (e.g., subject, sender, etc.) for the user's emails.

    Args:
        service: Gmail API service object.
        user_id (str): User identifier, default is 'me'.
        max_results (int): Number of email messages to fetch.

    Returns:
        list: List of email metadata.
    """
    try:
        # Call the Gmail API to fetch the emails
        results = service.users().messages().list(userId=user_id, maxResults=max_results).execute()
        messages = results.get('messages', [])

        email_metadata_list = []

        for message in messages:
            msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
            headers = msg.get('payload', {}).get('headers', [])
            
            email_metadata = {
                'id': message['id'],
                'snippet': msg.get('snippet', ''),
                'subject': next((header['value'] for header in headers if header['name'] == 'Subject'), None),
                'from': next((header['value'] for header in headers if header['name'] == 'From'), None),
                'date': next((header['value'] for header in headers if header['name'] == 'Date'), None)
            }
            email_metadata_list.append(email_metadata)

        return email_metadata_list
    except Exception as e:
        print(f"An error occurred while fetching email metadata: {e}")
        return []

def main():
    """
    Main function to authenticate and fetch email metadata.
    """
    # Authenticate and create Gmail API service
    service = authenticate_gmail_api()

    # Fetch email metadata
    email_metadata = fetch_email_metadata(service)

    # Print fetched email metadata
    for metadata in email_metadata:
        print(f"ID: {metadata['id']}")
        print(f"Subject: {metadata['subject']}")
        print(f"From: {metadata['from']}")
        print(f"Date: {metadata['date']}")
        print(f"Snippet: {metadata['snippet']}")
        print("-" * 80)

if __name__ == "__main__":
    main()
```
