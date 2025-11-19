"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: Provide an example of using the Google Gmail API for managing labels on emails.
Generated: DETERMINISTIC_9afe74f60fddc2c2
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Function to authenticate and build the Gmail API service
def authenticate_gmail_api():
    """
    Authenticate using Google credentials and return a Gmail API service object.
    Assumes that the environment is set up with valid credentials (e.g., via a service account or OAuth2).
    """
    try:
        # Authenticate using default credentials (e.g., service account or OAuth2)
        credentials, _ = google.auth.default()
        service = build('gmail', 'v1', credentials=credentials)
        return service
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise

# Function to list all labels in the user's Gmail account
def list_labels(service, user_id='me'):
    """
    List all labels in the user's Gmail account.

    Args:
        service: The Gmail API service object.
        user_id: The user's email address. Use 'me' to refer to the authenticated user.

    Returns:
        A list of labels.
    """
    try:
        response = service.users().labels().list(userId=user_id).execute()
        labels = response.get('labels', [])
        return labels
    except HttpError as error:
        print(f"An error occurred while listing labels: {error}")
        raise

# Function to create a new label
def create_label(service, user_id='me', label_name='NewLabel'):
    """
    Create a new label in the user's Gmail account.

    Args:
        service: The Gmail API service object.
        user_id: The user's email address. Use 'me' to refer to the authenticated user.
        label_name: The name of the label to create.

    Returns:
        The created label object.
    """
    try:
        label_body = {
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show'
        }
        label = service.users().labels().create(userId=user_id, body=label_body).execute()
        return label
    except HttpError as error:
        print(f"An error occurred while creating the label: {error}")
        raise

# Function to delete a label
def delete_label(service, user_id='me', label_id='LabelId'):
    """
    Delete a label from the user's Gmail account.

    Args:
        service: The Gmail API service object.
        user_id: The user's email address. Use 'me' to refer to the authenticated user.
        label_id: The ID of the label to delete.

    Returns:
        None
    """
    try:
        service.users().labels().delete(userId=user_id, id=label_id).execute()
        print(f"Label with ID {label_id} deleted successfully.")
    except HttpError as error:
        print(f"An error occurred while deleting the label: {error}")
        raise

# Main function to demonstrate label management
def main():
    """
    Main function to demonstrate Gmail label management using the Gmail API.
    """
    try:
        # Authenticate and build the Gmail API service
        service = authenticate_gmail_api()

        # List existing labels
        print("Listing existing labels:")
        labels = list_labels(service)
        for label in labels:
            print(f"Label ID: {label['id']}, Name: {label['name']}")

        # Create a new label
        print("\nCreating a new label:")
        new_label = create_label(service, label_name='MyCustomLabel')
        print(f"Created label: {new_label}")

        # Delete the newly created label
        print("\nDeleting the newly created label:")
        delete_label(service, label_id=new_label['id'])

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == '__main__':
    main()
```

### Notes:
- Ensure that the Google Cloud SDK is installed and authenticated properly.
- The script assumes that the environment is set up with valid credentials (e.g., via a service account or OAuth2).
- Replace `'LabelId'` with the actual label ID you want to delete when calling `delete_label`.
