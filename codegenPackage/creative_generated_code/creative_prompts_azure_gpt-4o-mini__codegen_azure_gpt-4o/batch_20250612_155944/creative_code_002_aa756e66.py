"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lelioaulikki.com
Prompt: What are the best practices for utilizing Google Gmail API in business solutions?
Generated: DETERMINISTIC_aa756e66e4150a5b
Batch ID: 20250612_155944
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.send": {
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

Below is a Python script leveraging the Gmail API for business solutions. The script demonstrates how to authenticate, list email messages, and send an email using Google's Gmail API while adhering to best practices.

```python
# Import required libraries
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope of access
# Modify scopes based on your use case (e.g., read, write, etc.)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail_api():
    """
    Authenticate and return a Gmail API service instance.
    Handles OAuth2 authentication and credential storage.
    """
    credentials = None
    token_path = 'token.json'
    credentials_path = 'credentials.json'

    # Check if token.json exists, which contains saved user credentials.
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            credentials = pickle.load(token)

    # Refresh or request new credentials if none are available or expired.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Use credentials.json to start the OAuth2 flow.
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for future use.
        with open(token_path, 'wb') as token:
            pickle.dump(credentials, token)

    # Build the Gmail API service instance.
    service = build('gmail', 'v1', credentials=credentials)
    return service

def list_emails(service, label_id='INBOX', max_results=10):
    """
    List email messages from the user's Gmail account.
    :param service: Authenticated Gmail API service instance.
    :param label_id: The label ID (default is 'INBOX').
    :param max_results: Maximum number of emails to fetch.
    """
    try:
        results = service.users().messages().list(userId='me', labelIds=[label_id], maxResults=max_results).execute()
        messages = results.get('messages', [])

        print(f"Found {len(messages)} messages:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(f"Message ID: {message['id']}, Snippet: {msg['snippet']}")

    except HttpError as error:
        print(f"An error occurred while fetching emails: {error}")

def send_email(service, sender, recipient, subject, body):
    """
    Send an email using the Gmail API.
    :param service: Authenticated Gmail API service instance.
    :param sender: Email address of the sender.
    :param recipient: Email address of the recipient.
    :param subject: Subject of the email.
    :param body: Body of the email.
    """
    from email.mime.text import MIMEText
    import base64

    try:
        # Create a MIMEText object for the email content.
        message = MIMEText(body)
        message['to'] = recipient
        message['from'] = sender
        message['subject'] = subject

        # Encode the email into a base64 string for Gmail API compatibility.
        raw_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')
        send_message = {'raw': raw_message}

        # Use the Gmail API to send the email.
        sent_message = service.users().messages().send(userId='me', body=send_message).execute()
        print(f"Message sent successfully! Message ID: {sent_message['id']}")

    except HttpError as error:
        print(f"An error occurred while sending the email: {error}")

def main():
    """
    Main function to demonstrate Gmail API usage.
    """
    # Step 1: Authenticate and initialize the Gmail API service.
    service = authenticate_gmail_api()

    # Step 2: List emails from the inbox.
    list_emails(service, max_results=5)

    # Step 3: Send an email.
    sender_email = 'your-email@example.com'
    recipient_email = 'recipient-email@example.com'
    subject = 'Test Email via Gmail API'
    body = 'Hello, this is a test email sent using the Gmail API!'
    send_email(service, sender_email, recipient_email, subject, body)

if __name__ == '__main__':
    # Run the main function.
    main()
```

### Notes for Deployment:
1. **Environment Configuration**:
   - Place `credentials.json` (downloaded from Google Cloud Console) in the same directory as the script.
   - Ensure proper permissions for the Gmail API in Google Cloud Console.
   
2. **Dependencies**:
   - Install required Python libraries via:
     ```bash
     pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

3. **Security**:
   - Store sensitive data like `credentials.json` securely (e.g., in an encrypted location).
   - Avoid hardcoding email addresses or credentials in the source code (use environment variables or secure vaults).

4. **Error Handling**:
   - More robust error handling can be added for specific business use cases.
