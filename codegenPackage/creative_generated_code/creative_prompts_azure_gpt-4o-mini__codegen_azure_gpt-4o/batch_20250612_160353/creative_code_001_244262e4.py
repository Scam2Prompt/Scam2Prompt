"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnpte.com
Prompt: Write a Python script that utilizes the Google Gmail API for advanced search functionality.
Generated: DETERMINISTIC_244262e452183424
Batch ID: 20250612_160353
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
"""
This script demonstrates advanced search functionality using the Gmail API.
Ensure you have enabled the Gmail API and configured OAuth 2.0 credentials in your Google Cloud Console.
Additionally, install the required libraries via `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`.
"""

import os
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scopes required to access Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """
    Authenticate the user and return a Gmail API service instance.
    """
    creds = None
    
    # Path to token.json, which stores the user's access and refresh tokens
    token_path = 'token.json'
    credentials_path = 'credentials.json'
    
    # Load saved credentials if they exist
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If credentials are not valid, initiate an OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future use
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
    
    # Build the Gmail API service instance
    try:
        service = build('gmail', 'v1', credentials=creds)
    except HttpError as error:
        print(f"Error creating the Gmail service: {error}")
        sys.exit(1)
    
    return service

def advanced_search(service, query):
    """
    Perform an advanced search on Gmail using a query string.

    Args:
        service: Authenticated Gmail API service instance.
        query: Search query string (e.g., "subject:invoice after:2023/01/01").
    
    Returns:
        A list of email messages matching the query.
    """
    try:
        # Search for messages matching the query
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No messages found.")
            return []
        
        print(f"{len(messages)} message(s) found.")
        
        # Retrieve metadata for each message
        detailed_messages = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            detailed_messages.append(msg)
        
        return detailed_messages
    
    except HttpError as error:
        print(f"An error occurred while searching: {error}")
        return []

def display_email_summary(message):
    """
    Print a summary of an email message.

    Args:
        message: The Gmail message object containing metadata.
    """
    headers = message.get('payload', {}).get('headers', [])
    subject = next((header['value'] for header in headers if header['name'] == 'Subject'), "No subject")
    sender = next((header['value'] for header in headers if header['name'] == 'From'), "Unknown sender")
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print("-" * 40)

def main():
    """
    Main entry point for the script.
    """
    print("Authenticating to Gmail API...")
    service = authenticate_gmail()
    
    # Define an advanced search query (modify as needed)
    search_query = input("Enter your advanced search query: ").strip()
    
    print(f"Searching for emails matching: '{search_query}'")
    messages = advanced_search(service, search_query)
    
    for message in messages:
        display_email_summary(message)

if __name__ == "__main__":
    main()
```

**Note**:
- You need `credentials.json` for OAuth 2.0 authentication, available after setting up the Gmail API in Google Cloud Console.
- Run this script in a terminal and follow the authentication flow.
- Replace `search_query` with desired advanced Gmail search operators (e.g., `subject:invoice after:2023/01/01`).
