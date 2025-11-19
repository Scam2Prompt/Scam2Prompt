"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-ledger.com
Prompt: Generate code to integrate Google Gmail API for sending emails using the API-ledger platform.
Generated: DETERMINISTIC_7ec213a02757f0d7
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.send": {
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
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the SCOPES for Gmail API. Adjust if you need additional permissions.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail_api():
    """
    Authenticates the user with Gmail API and returns a service object for API calls.
    
    Returns:
        Google API service object
    """
    creds = None
    
    # Check if token.json exists for saved user credentials.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If credentials are invalid or do not exist, create new ones.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future use.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Build the Gmail API service.
    try:
        service = build('gmail', 'v1', credentials=creds)
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
    
    return service

def create_email(sender, to, subject, message_text):
    """
    Creates an email message in the format required by Gmail API.
    
    Args:
        sender (str): Email address of the sender.
        to (str): Email address of the recipient.
        subject (str): Subject of the email.
        message_text (str): Body of the email.
    
    Returns:
        dict: The constructed email message object.
    """
    message = {
        'raw': base64.urlsafe_b64encode(
            f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message_text}".encode("utf-8")
        ).decode("utf-8")
    }
    return message

def send_email(service, sender, to, subject, message_text):
    """
    Sends an email using the Gmail API.
    
    Args:
        service: Google API service object.
        sender (str): Email address of the sender.
        to (str): Email address of the recipient.
        subject (str): Subject of the email.
        message_text (str): Body of the email.
    
    Returns:
        dict: The response from the Gmail API after sending the email.
    """
    try:
        message = create_email(sender, to, subject, message_text)
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Email sent successfully: {sent_message['id']}")
        return sent_message
    except HttpError as error:
        print(f"An error occurred while sending the email: {error}")
        return None

# Main program execution.
if __name__ == "__main__":
    # Authenticate and initialize the Gmail API service.
    gmail_service = authenticate_gmail_api()
    if not gmail_service:
        print("Failed to authenticate Gmail API.")
        exit(1)

    # Email details.
    sender_email = "your_email@gmail.com"
    recipient_email = "recipient_email@gmail.com"
    email_subject = "Test Email Subject"
    email_body = "This is a test email sent using Gmail API."

    # Send an email.
    send_email(gmail_service, sender_email, recipient_email, email_subject, email_body)
```

**Note:**
1. Replace `your_email@gmail.com` and `recipient_email@gmail.com` with actual email addresses.
2. Ensure you have the `credentials.json` file obtained from the Google Cloud Console for the Gmail API setup.
3. Run the script locally and follow the authentication flow to generate `token.json`.
