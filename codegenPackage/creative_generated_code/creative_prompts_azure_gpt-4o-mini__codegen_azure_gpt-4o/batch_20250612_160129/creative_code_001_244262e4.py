"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-token.vip
Prompt: Write a Python script that utilizes the Google Gmail API for advanced search functionality.
Generated: DETERMINISTIC_244262e452183424
Batch ID: 20250612_160129
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

# Scopes required to access Gmail data
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
    
    # Refresh tokens if they are expired
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        # Start OAuth flow if no valid credentials exist
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

    try:
        # Build the Gmail API service
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred while creating Gmail service: {error}")
        sys.exit(1)

def search_gmail(service, query):
    """
    Perform advanced search on Gmail using the provided query.

    :param service: Gmail API service instance
    :param query: Search query (e.g., 'from:someone@example.com subject:hello')
    :return: List of matching message IDs
    """
    try:
        # Search messages using the query
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        if not messages:
            print("No messages found.")
            return []

        # Extract and return message IDs
        message_ids = [message['id'] for message in messages]
        return message_ids
    except HttpError as error:
        print(f"An error occurred while searching Gmail: {error}")
        return []

def get_message_details(service, message_id):
    """
    Retrieve detailed information about a specific Gmail message.

    :param service: Gmail API service instance
    :param message_id: ID of the message to retrieve
    :return: Message details dictionary
    """
    try:
        # Get message details using its ID
        message = service.users().messages().get(userId='me', id=message_id).execute()
        return message
    except HttpError as error:
        print(f"An error occurred while retrieving message details: {error}")
        return None

def main():
    """
    Main function to demonstrate advanced search functionality using Gmail API.
    """
    # Authenticate and build the Gmail API service
    service = authenticate_gmail()

    # Advanced search query (modify as needed)
    query = input("Enter your Gmail search query (e.g., 'from:someone@example.com subject:hello'): ")

    # Perform the search
    print("Searching Gmail messages...")
    message_ids = search_gmail(service, query)

    if message_ids:
        print(f"Found {len(message_ids)} message(s).")

        # Retrieve and print details for each message
        for message_id in message_ids:
            message = get_message_details(service, message_id)
            if message:
                print(f"\nMessage ID: {message_id}")
                print(f"Snippet: {message.get('snippet', 'No snippet available')}")
                print(f"Labels: {message.get('labelIds', 'No labels available')}")
    else:
        print("No messages found matching the query.")

if __name__ == '__main__':
    main()
```
