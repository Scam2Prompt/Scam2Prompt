"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Generate a Python script that integrates Google Workspace tools like Docs and Calendar for project management.
Generated: DETERMINISTIC_76642da03efeb110
Batch ID: 20250612_164257
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/calendar": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/documents": {
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
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants for Google API scopes
SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/calendar']

# Google Service account credentials file path
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Function to create Google API service
def create_service(api_name, api_version):
    """Creates a Google API service."""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    try:
        service = build(api_name, api_version, credentials=credentials)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Function to create a Google Doc for project management
def create_google_doc(doc_title):
    """Creates a Google Docs document with the given title."""
    docs_service = create_service('docs', 'v1')
    
    if docs_service:
        # Create a new document
        doc = {
            'title': doc_title
        }
        try:
            doc = docs_service.documents().create(body=doc).execute()
            print(f"Created Document with title: {doc_title} and ID: {doc['documentId']}")
            return doc['documentId']
        except HttpError as error:
            print(f"Failed to create document: {error}")

# Function to create a Calendar event
def create_calendar_event(event_details):
    """Creates a calendar event based on provided details."""
    calendar_service = create_service('calendar', 'v3')
    
    if calendar_service:
        # Create a new event
        event = {
            'summary': event_details['summary'],
            'start': {
                'dateTime': event_details['start_time'],
                'timeZone': event_details['time_zone'],
            },
            'end': {
                'dateTime': event_details['end_time'],
                'timeZone': event_details['time_zone'],
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 10},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        try:
            event = calendar_service.events().insert(calendarId='primary', body=event).execute()
            print(f"Event created: {event.get('htmlLink')}")
        except HttpError as error:
            print(f"Failed to create calendar event: {error}")

# Main function to orchestrate the project management integration
def main():
    """Main function to manage project tasks with Google Docs and Calendar."""
    # Create Google Doc for the project
    doc_id = create_google_doc("Project Management Plan")
    
    # Define event details for the calendar
    event_details = {
        'summary': 'Project Kickoff Meeting',
        'start_time': '2023-10-01T09:00:00-07:00',  # Example start time in ISO format
        'end_time': '2023-10-01T10:00:00-07:00',    # Example end time in ISO format
        'time_zone': 'America/Los_Angeles',        # Example timezone
    }
    
    # Create calendar event
    create_calendar_event(event_details)

if __name__ == '__main__':
    main()
```

Make sure to replace `'path/to/your/service-account-file.json'` with the actual path to your Google service account JSON key file. Additionally, adjust the date and time in the `event_details` dictionary as per your requirement.
