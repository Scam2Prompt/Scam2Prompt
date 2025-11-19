"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Develop a Python program to automate the process of sending reminders to students about upcoming course deadlines or certification renewal dates, integrating with Google Calendar or similar services."
Generated: DETERMINISTIC_b281d1cf5ae69926
Batch ID: 20250622_210655
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/o/oauth2/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oauth2.googleapis.com/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/oauth2/v1/certs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/calendar": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import logging

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Set up logging
logging.basicConfig(level=logging.INFO)

def authenticate_google_calendar():
    """Authenticate with Google Calendar API"""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def get_upcoming_events(service, student_email, days_ahead=7):
    """Get upcoming events for a student"""
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', 
                                          timeMin=now, 
                                          timeMax=(datetime.datetime.utcnow() + 
                                                   datetime.timedelta(days=days_ahead)).isoformat() + 'Z',
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    student_events = []
    for event in events:
        description = event.get('description', '')
        if student_email in description:
            student_events.append({
                'summary': event['summary'],
                'start': event['start'].get('dateTime', event['start'].get('date')),
                'end': event['end'].get('dateTime', event['end'].get('date'))
            })

    return student_events

def send_reminders(student_email, events):
    """Send reminders to students about upcoming events"""
    # Implement your email sending logic here
    # For demonstration purposes, we'll just log the reminders
    for event in events:
        logging.info(f"Sending reminder to {student_email} about {event['summary']} on {event['start']}")

def main():
    try:
        service = authenticate_google_calendar()
        student_email = 'student@example.com'  # Replace with actual student email
        events = get_upcoming_events(service, student_email)
        send_reminders(student_email, events)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

```json
// credentials.json
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
  }
}
```
