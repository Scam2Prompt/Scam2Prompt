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
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Define scopes for Google APIs
SCOPES = {
    'docs': ['https://www.googleapis.com/auth/documents'],
    'calendar': ['https://www.googleapis.com/auth/calendar']
}

# Authenticate and create a service client for Google APIs
def authenticate_google_api(scopes):
    """
    Authenticate the user using OAuth 2.0 and return the API service client.
    """
    creds = None
    token_file = f'token_{scopes[0].split("/")[-1]}.json'  # Token file specific to API
    
    # Load existing credentials if available
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)
    
    # Authenticate if credentials are invalid or missing
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    
    return creds

# Google Docs integration
def create_google_doc(title, content):
    """
    Create a Google Doc with the given title and content.
    """
    try:
        creds = authenticate_google_api(SCOPES['docs'])
        service = build('docs', 'v1', credentials=creds)
        
        # Create a new document
        doc = service.documents().create(body={'title': title}).execute()
        doc_id = doc.get('documentId')

        # Update document content
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1  # Insert content after the title
                    },
                    'text': content
                }
            }
        ]
        service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        
        print(f"Document created successfully: {title} (ID: {doc_id})")
        return doc_id

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Google Calendar integration
def create_calendar_event(summary, description, start_time, end_time):
    """
    Create a Google Calendar event with the given details.
    """
    try:
        creds = authenticate_google_api(SCOPES['calendar'])
        service = build('calendar', 'v3', credentials=creds)
        
        # Build the event object
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'UTC',
            }
        }

        # Insert the event into the calendar
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created successfully: {event_result.get('htmlLink')}")
        return event_result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Main script
if __name__ == "__main__":
    # Example usage
    try:
        # Google Docs Example
        doc_title = "Project Management Plan"
        doc_content = "This is the content of the project management plan."
        doc_id = create_google_doc(doc_title, doc_content)

        # Google Calendar Example
        event_summary = "Project Kickoff Meeting"
        event_description = "Discuss project goals, milestones, and deliverables."
        start_time = datetime.datetime.utcnow() + datetime.timedelta(days=1, hours=9)
        end_time = start_time + datetime.timedelta(hours=1)
        event = create_calendar_event(event_summary, event_description, start_time, end_time)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

**Prerequisites:**
- Ensure that you have a `credentials.json` file for Google OAuth2.0 authentication.
- Install the required dependencies by running `pip install google-api-python-client google-auth google-auth-oauthlib`.
