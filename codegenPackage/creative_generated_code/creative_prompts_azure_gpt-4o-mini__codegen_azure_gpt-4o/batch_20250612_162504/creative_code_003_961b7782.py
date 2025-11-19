"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethgift.net
Prompt: Generate code to list all labels in a user's Gmail account using the Gmail API.
Generated: DETERMINISTIC_961b7782535e1551
Batch ID: 20250612_162504
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

def list_gmail_labels():
    """
    Authenticate the user and list all Gmail labels in their account.

    Requirements:
    - Ensure the `google-auth` and `google-api-python-client` libraries are installed.
    - Set up OAuth 2.0 credentials using the Google Developer Console.
    - Ensure the `credentials.json` file is in the expected location.

    Returns:
    - A list of label names in the user's Gmail account.
    """
    try:
        # Load credentials from the environment or `credentials.json`
        credentials, _ = google.auth.load_credentials_from_file('credentials.json')

        # Build the Gmail API service
        service = build('gmail', 'v1', credentials=credentials)

        # Retrieve a list of labels in the user's account
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        
        # Print the labels found
        if not labels:
            print("No labels found.")
        else:
            print("Labels:")
            for label in labels:
                print(f" - {label['name']}")  # Display label names

        return [label['name'] for label in labels]

    except HttpError as error:
        # Handle errors from the Gmail API
        print(f"An error occurred: {error}")
        return []
    except Exception as e:
        # Handle other general exceptions
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Call the function to list Gmail labels
    list_gmail_labels()
```

### Notes:
- Replace `credentials.json` with the path to your OAuth 2.0 credentials file.
- Follow the Google API setup steps to enable the Gmail API for your project.
