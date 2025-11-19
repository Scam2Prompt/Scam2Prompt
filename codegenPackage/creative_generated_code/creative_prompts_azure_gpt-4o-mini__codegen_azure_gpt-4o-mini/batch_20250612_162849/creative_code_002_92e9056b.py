"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://i3qra.eth-drop.top
Prompt: What are the best practices for managing Gmail API credentials securely in a web application?
Generated: DETERMINISTIC_92e9056b9af71825
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def load_credentials(credentials_file):
    """
    Load the Google API credentials from a JSON file.

    Parameters:
    credentials_file (str): Path to the JSON file containing the service account credentials.

    Returns:
    credentials: Loaded Google API credentials object.
    """
    try:
        # Load the credentials from the specified JSON file
        if not os.path.exists(credentials_file):
            raise FileNotFoundError(f"Credentials file not found: {credentials_file}")

        with open(credentials_file, 'r') as file:
            creds_data = json.load(file)

        # Create credentials object
        credentials = service_account.Credentials.from_service_account_info(creds_data)
        
        return credentials
    except Exception as e:
        print(f"Error loading credentials: {e}")
        raise

def build_gmail_service(credentials):
    """
    Build the Gmail API service object.

    Parameters:
    credentials: Credentials object for authenticating with the Gmail API.

    Returns:
    service: Gmail API service object.
    """
    try:
        # Build the Gmail API service
        service = build('gmail', 'v1', credentials=credentials)
        return service
    except Exception as e:
        print(f"Error building Gmail service: {e}")
        raise

def main():
    # Path to your Google service account credentials file
    CREDENTIALS_FILE = 'path/to/credentials.json'
    
    try:
        # Load credentials and build the Gmail service
        credentials = load_credentials(CREDENTIALS_FILE)
        gmail_service = build_gmail_service(credentials)

        # Example of making a request to the Gmail API (list user's labels)
        user_info = 'me'
        labels = gmail_service.users().labels().list(userId=user_info).execute()

        print("Labels:")
        for label in labels['labels']:
            print(f"- {label['name']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

### Notes:
- Ensure that the `path/to/credentials.json` is replaced with the actual path to your Google service account credentials file.
- The code demonstrates loading credentials, building a Gmail service, and listing labels as an example operation while handling errors properly throughout.
