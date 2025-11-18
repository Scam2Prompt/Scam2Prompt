"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Write code to integrate Typeform with Google Calendar, automatically scheduling events based on form responses.
Generated: DETERMINISTIC_9588d02b524820bb
Batch ID: 20250612_151912
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
  "https://api.typeform.com/forms/{form_id}/responses": {
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
import requests
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms/{form_id}/responses"
TYPEFORM_API_KEY = "your_typeform_api_key"
FORM_ID = "your_form_id"

GOOGLE_CALENDAR_SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account.json'
CALENDAR_ID = 'your_calendar_id'

# Error messages
TYPEFORM_ERROR = "Failed to fetch Typeform responses."
GOOGLE_CALENDAR_ERROR = "Failed to schedule event in Google Calendar."

# Function to fetch Typeform responses
def fetch_typeform_responses(form_id, api_key):
    """
    Fetches responses from Typeform using the API.
    :param form_id: Typeform Form ID
    :param api_key: Typeform API Key
    :return: List of responses
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    url = TYPEFORM_API_URL.format(form_id=form_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["items"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"{TYPEFORM_ERROR}: {e}")

# Function to create events in Google Calendar
def create_google_calendar_event(summary, start_time, end_time, calendar_id):
    """
    Creates a Google Calendar event.
    :param summary: Event summary
    :param start_time: Event start time (ISO format)
    :param end_time: Event end time (ISO format)
    :param calendar_id: Calendar ID
    :return: Created event details
    """
    try:
        credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=GOOGLE_CALENDAR_SCOPES)
        service = build('calendar', 'v3', credentials=credentials)

        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'UTC',
            },
        }

        created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
        return created_event
    except Exception as e:
        raise Exception(f"{GOOGLE_CALENDAR_ERROR}: {e}")

# Main function to fetch Typeform responses and schedule events
def schedule_events_from_typeform():
    """
    Main function to fetch responses from Typeform and schedule events in Google Calendar.
    """
    try:
        responses = fetch_typeform_responses(FORM_ID, TYPEFORM_API_KEY)
        for response in responses:
            # Extract data from Typeform responses (adjust keys based on your form structure)
            name = response['answers'][0]['text']  # Example: Name
            start_date = response['answers'][1]['date']  # Example: Start date
            duration_hours = int(response['answers'][2]['number'])  # Example: Duration in hours

            # Calculate start and end time for the event
            start_time = datetime.fromisoformat(start_date)
            end_time = start_time + timedelta(hours=duration_hours)

            # Create event summary
            event_summary = f"Meeting with {name}"

            # Schedule event in Google Calendar
            created_event = create_google_calendar_event(
                summary=event_summary,
                start_time=start_time.isoformat(),
                end_time=end_time.isoformat(),
                calendar_id=CALENDAR_ID,
            )

            # Print confirmation
            print(f"Event created: {created_event['htmlLink']}")

    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    schedule_events_from_typeform()
```
