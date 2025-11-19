"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
import os
import base64
import json
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

def authenticate_gmail_api():
    """
    Authenticates and returns a service object for the Gmail API.
    
    Returns:
        service: Authorized Gmail API service instance.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('gmail', 'v1', credentials=credentials)
        return service
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise

def search_gmail(service, query):
    """
    Searches for emails in the user's Gmail account based on the provided query.
    
    Args:
        service: Authorized Gmail API service instance.
        query (str): Search query string for filtering emails.
    
    Returns:
        list: List of email messages matching the search query.
    """
    try:
        # Call the Gmail API to search for emails
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No messages found.")
            return []
        
        return messages
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

def get_email_details(service, message_id):
    """
    Retrieves the details of a specific email message by its ID.
    
    Args:
        service: Authorized Gmail API service instance.
        message_id (str): The ID of the email message.
    
    Returns:
        dict: A dictionary containing the email details.
    """
    try:
        message = service.users().messages().get(userId='me', id=message_id).execute()
        return message
    except HttpError as error:
        print(f"An error occurred while fetching message details: {error}")
        return {}

def decode_email_body(message):
    """
    Decodes the email body from base64 format.
    
    Args:
        message (dict): The email message dictionary.
    
    Returns:
        str: The decoded email body.
    """
    try:
        if 'data' in message['payload']['parts'][0]['body']:
            data = message['payload']['parts'][0]['body']['data']
            decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
            return decoded_data
        else:
            return "No body content found."
    except Exception as e:
        print(f"Error decoding email body: {e}")
        return "Error decoding email body."

def main():
    """
    Main function to execute the Gmail search functionality.
    """
    # Authenticate and create the Gmail API service
    service = authenticate_gmail_api()
    
    # Define your search query (modify as needed)
    query = 'from:example@gmail.com subject:"Test Email"'
    
    # Search for emails
    messages = search_gmail(service, query)
    
    # Process each message found
    for message in messages:
        message_id = message['id']
        email_details = get_email_details(service, message_id)
        email_body = decode_email_body(email_details)
        
        print(f"Message ID: {message_id}")
        print(f"Email Body: {email_body}\n")

if __name__ == '__main__':
    main()
```

**Note:** Make sure to replace `'path/to/your/service-account-file.json'` with the actual path to your Google service account JSON file. Additionally, ensure that the service account has the necessary permissions to access the Gmail API.
