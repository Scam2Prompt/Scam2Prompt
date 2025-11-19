"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xr9sw.eth-drop.top
Prompt: Can you provide a code example for retrieving Gmail messages using the Google API client library?
Generated: DETERMINISTIC_3600ffcb87bd6fed
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
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_gmail_messages():
    """
    Retrieve Gmail messages using the Google API client library.

    Requirements:
        - Service account or OAuth credentials must be set up with access to Gmail API.
        - `google-auth` and `google-api-python-client` libraries must be installed.
          Install them using: `pip install google-auth google-api-python-client`.
        - Credentials file path must be set in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
    """
    try:
        # Authenticate the user using default credentials
        creds, _ = google.auth.default()

        # Build the Gmail API client
        service = build("gmail", "v1", credentials=creds)

        # Call the Gmail API to retrieve the user's messages
        # The 'userId' parameter can use 'me' to refer to the authenticated user
        messages = service.users().messages().list(userId="me").execute()

        # Extract and return the list of messages
        # Each message contains its ID and other metadata
        message_list = messages.get('messages', [])
        return message_list

    except HttpError as error:
        # Handle errors from the Gmail API
        print(f"An error occurred: {error}")
        return None

if __name__ == "__main__":
    # Call the function and print results
    messages = get_gmail_messages()

    if messages:
        print("Retrieved messages:")
        for msg in messages:
            print(f"Message ID: {msg['id']}")
    else:
        print("No messages retrieved or an error occurred.")
```
