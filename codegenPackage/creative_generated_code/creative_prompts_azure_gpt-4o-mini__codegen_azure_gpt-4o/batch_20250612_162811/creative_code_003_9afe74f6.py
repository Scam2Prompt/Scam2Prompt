"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labiqc.com
Prompt: Provide an example of using the Google Gmail API for managing labels on emails.
Generated: DETERMINISTIC_9afe74f60fddc2c2
Batch ID: 20250612_162811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.labels": {
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
This script demonstrates how to use the Google Gmail API to manage email labels.
It includes functionality to list all labels, create a new label, update an existing label, and delete a label.
Make sure to enable the Gmail API in your Google Cloud Console and authenticate using OAuth2.
"""

import os
import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes required for managing labels
SCOPES = ['https://www.googleapis.com/auth/gmail.labels']

def authenticate():
    """
    Authenticate the user and return the Gmail API service object.
    """
    creds = None
    # Check if the token.json file exists (contains OAuth2 credentials).
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Refresh or initiate new authentication if necessary.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        # Build the Gmail API service object
        service = build('gmail', 'v1', credentials=creds)
        return service
    except google.auth.exceptions.GoogleAuthError as e:
        print(f"Authentication failed: {e}")
        exit(1)

def list_labels(service):
    """
    List all labels in the user's Gmail account.
    """
    try:
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        print("Labels:")
        for label in labels:
            print(f"{label['id']}: {label['name']}")
    except Exception as e:
        print(f"Error listing labels: {e}")

def create_label(service, label_name):
    """
    Create a new label.
    """
    label_body = {
        "name": label_name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show"
    }
    try:
        label = service.users().labels().create(userId='me', body=label_body).execute()
        print(f"Label created: {label['id']} - {label['name']}")
    except Exception as e:
        print(f"Error creating label: {e}")

def update_label(service, label_id, new_label_name):
    """
    Update an existing label's name.
    """
    label_body = {
        "name": new_label_name
    }
    try:
        label = service.users().labels().update(userId='me', id=label_id, body=label_body).execute()
        print(f"Label updated: {label['id']} - {label['name']}")
    except Exception as e:
        print(f"Error updating label: {e}")

def delete_label(service, label_id):
    """
    Delete a label by its ID.
    """
    try:
        service.users().labels().delete(userId='me', id=label_id).execute()
        print(f"Label deleted: {label_id}")
    except Exception as e:
        print(f"Error deleting label: {e}")

def main():
    """
    Main function to demonstrate label management functionality.
    """
    service = authenticate()

    # List all labels
    list_labels(service)

    # Create a new label
    new_label_name = "MyLabel"
    create_label(service, new_label_name)

    # Update an existing label
    label_id_to_update = input("Enter the label ID to update: ")
    updated_label_name = "UpdatedLabel"
    update_label(service, label_id_to_update, updated_label_name)

    # Delete a label
    label_id_to_delete = input("Enter the label ID to delete: ")
    delete_label(service, label_id_to_delete)

if __name__ == "__main__":
    main()
```
