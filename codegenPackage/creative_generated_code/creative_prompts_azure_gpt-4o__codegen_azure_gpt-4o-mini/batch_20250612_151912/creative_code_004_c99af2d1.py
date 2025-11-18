"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://electrocoin.typeform.com
Prompt: Provide an example of how to use Typeform's API to create an event registration form that integrates with Google Calendar for automatic scheduling.
Generated: DETERMINISTIC_c99af2d1e18d7f48
Batch ID: 20250612_151912
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/calendar/v3/calendars/primary/events": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms": {
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
import requests
import json
from datetime import datetime, timedelta

# Constants for Typeform and Google Calendar API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"
GOOGLE_CALENDAR_API_URL = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"

def create_typeform_event_registration():
    """Create a Typeform event registration form."""
    
    # Define the form structure
    form_data = {
        "title": "Event Registration",
        "fields": [
            {
                "title": "Name",
                "type": "short_text",
                "ref": "name"
            },
            {
                "title": "Email",
                "type": "email",
                "ref": "email"
            },
            {
                "title": "Event Date",
                "type": "date",
                "ref": "event_date"
            }
        ],
        "settings": {
            "is_public": True
        }
    }

    try:
        # Create the form using Typeform API
        response = requests.post(
            TYPEFORM_API_URL,
            headers={"Authorization": f"Bearer {TYPEFORM_API_KEY}", "Content-Type": "application/json"},
            data=json.dumps(form_data)
        )
        response.raise_for_status()  # Raise an error for bad responses

        form_id = response.json().get("id")
        print(f"Typeform created with ID: {form_id}")
        return form_id

    except requests.exceptions.RequestException as e:
        print(f"Error creating Typeform: {e}")
        return None

def create_google_calendar_event(name, email, event_date):
    """Create an event in Google Calendar based on user input."""
    
    # Prepare the event data for Google Calendar
    event_start = event_date.isoformat() + 'Z'  # Add timezone information for UTC
    event_end = (event_date + timedelta(hours=1)).isoformat() + 'Z'  # Assume duration of 1 hour

    event = {
        'summary': f'Registration for Event by {name}',
        'location': 'Virtual',
        'description': f'Event registration from {name} with email {email}',
        'start': {
            'dateTime': event_start,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': event_end,
            'timeZone': 'UTC',
        },
        'attendees': [
            {'email': email},
        ],
    }

    try:
        # Create the event using Google Calendar API
        response = requests.post(
            GOOGLE_CALENDAR_API_URL,
            headers={"Authorization": f"Bearer {GOOGLE_API_KEY}", "Content-Type": "application/json"},
            data=json.dumps(event)
        )
        response.raise_for_status()  # Raise an error for bad responses

        print(f"Event created in Google Calendar: {response.json().get('htmlLink')}")

    except requests.exceptions.RequestException as e:
        print(f"Error creating Google Calendar event: {e}")

if __name__ == "__main__":
    # Example usage
    form_id = create_typeform_event_registration()
    
    if form_id:
        # Sample data for creating a calendar event
        sample_name = "John Doe"
        sample_email = "john.doe@example.com"
        sample_event_date = datetime(2023, 12, 15, 15, 0)  # Sample event date
        
        create_google_calendar_event(sample_name, sample_email, sample_event_date)
```

**Note:** Replace `YOUR_TYPEFORM_API_KEY` and `YOUR_GOOGLE_API_KEY` with your actual API keys. Make sure to handle OAuth 2.0 authorization for Google Calendar API in a production application.
