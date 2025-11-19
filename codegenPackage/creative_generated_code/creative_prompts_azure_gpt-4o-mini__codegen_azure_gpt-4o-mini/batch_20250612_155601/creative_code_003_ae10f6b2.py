"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://incentives-usual.com
Prompt: Describe how to implement advanced search queries in Google Gmail for business-related emails.
Generated: DETERMINISTIC_ae10f6b2de1689ad
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth import default
from googleapiclient.discovery import build

# Class to handle Gmail API operations
class GmailHandler:
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        """Authenticate to the Gmail API using default credentials."""
        try:
            creds, _ = default()
            service = build('gmail', 'v1', credentials=creds)
            return service
        except Exception as e:
            raise Exception(f"Authentication failed: {str(e)}")

    def search_emails(self, query):
        """Search for emails based on the given query.
        
        Args:
            query (str): The search query string for Gmail.

        Returns:
            list: A list of email messages that match the query.
        """
        try:
            # Perform the search operation
            results = self.service.users().messages().list(userId='me', q=query).execute()
            messages = results.get('messages', [])
            return messages
        except Exception as e:
            raise Exception(f"Failed to search emails: {str(e)}")

    def get_email_details(self, message_id):
        """Retrieve details of a specific email using its message ID.
        
        Args:
            message_id (str): The ID of the email message.

        Returns:
            dict: Details of the email message.
        """
        try:
            message = self.service.users().messages().get(userId='me', id=message_id).execute()
            return message
        except Exception as e:
            raise Exception(f"Failed to retrieve email details: {str(e)}")

# Example usage of the GmailHandler class
if __name__ == "__main__":
    try:
        gmail_handler = GmailHandler()
        
        # Define your advanced search query
        advanced_query = 'from:business@example.com subject:"Project Update" after:2023/01/01'

        # Search for emails with the advanced query
        email_messages = gmail_handler.search_emails(advanced_query)
        
        # Iterate through found emails and print details
        for email in email_messages:
            email_details = gmail_handler.get_email_details(email['id'])
            print(f"Subject: {email_details['snippet']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
