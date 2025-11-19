"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lombardfinance.one
Prompt: Generate a Python script that integrates with the Gmail API to send automated emails using specific templates.
Generated: DETERMINISTIC_e8f6510999c78d75
Batch ID: 20250612_160742
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
import json
import re
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Constants for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Function to authenticate and create a Gmail API service
def authenticate_gmail_api():
    """Authenticates the Gmail API using service account credentials."""
    creds = None
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    else:
        raise FileNotFoundError(f"Service account file not found: {SERVICE_ACCOUNT_FILE}")

    return build('gmail', 'v1', credentials=creds)

# Function to create and send an email
def send_email(service, recipient, subject, body):
    """Creates and sends an email using the Gmail API.

    Args:
        service: Authorized Gmail API service instance.
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body content of the email.

    Raises:
        Exception: If an error occurs while sending the email.
    """
    try:
        # Create the email content
        message = MIMEText(body)
        message['to'] = recipient
        message['subject'] = subject
        
        # Encode the email content
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Create a message dictionary
        message_body = {'raw': raw_message}
        
        # Send the email
        service.users().messages().send(userId='me', body=message_body).execute()
        print(f"Email sent to {recipient} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to load email templates from JSON file
def load_templates(template_file):
    """Loads email templates from a JSON file.

    Args:
        template_file (str): Path to the JSON file containing templates.

    Returns:
        dict: Dictionary of templates.

    Raises:
        FileNotFoundError: If the template file does not exist.
        json.JSONDecodeError: If there is an error parsing the JSON file.
    """
    try:
        with open(template_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Template file not found: {template_file}")
        raise
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {template_file}")
        raise

# Main function to orchestrate sending emails
def main():
    """Main function to send automated emails using Gmail API and templates."""
    # Authenticate to the Gmail API
    service = authenticate_gmail_api()
    
    # Load email templates
    templates = load_templates('path/to/your/templates.json')
    
    # Send emails using templates
    for recipient, template in templates.items():
        subject = template.get('subject', 'No Subject')
        body = template.get('body', 'No Content')
        
        # Validate the email address format
        if re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
            send_email(service, recipient, subject, body)
        else:
            print(f"Invalid email address: {recipient}")

if __name__ == '__main__':
    main()
```

**Notes:**
- Replace `'path/to/your/service-account-file.json'` with the actual path to your service account JSON file.
- Replace `'path/to/your/templates.json'` with the actual path to your JSON file containing email templates.
- The JSON file with templates should be structured like: 
  ```json
  {
      "recipient_email@example.com": {
          "subject": "Your Subject Here",
          "body": "Your email body here."
      }
  }
  ```
