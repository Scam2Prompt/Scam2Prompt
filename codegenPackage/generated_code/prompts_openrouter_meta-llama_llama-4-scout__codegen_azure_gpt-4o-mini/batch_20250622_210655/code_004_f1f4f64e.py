"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Create a social media content calendar using Google Calendar API and Python, inspired by the social media presence of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_f1f4f64e40837585
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants for the calendar
CALENDAR_ID = 'primary'  # Use 'primary' for the user's primary calendar
TIMEZONE = 'Asia/Riyadh'  # Set the timezone for the events

# Function to create a Google Calendar service
def create_calendar_service():
    """Creates a Google Calendar service using the default credentials."""
    creds, _ = google.auth.default()
    service = build('calendar', 'v3', credentials=creds)
    return service

# Function to create an event in Google Calendar
def create_event(service, summary, start_time, end_time, description='', location=''):
    """Creates an event in Google Calendar.

    Args:
        service: The Google Calendar service instance.
        summary (str): The title of the event.
        start_time (datetime): The start time of the event.
        end_time (datetime): The end time of the event.
        description (str): A description of the event.
        location (str): The location of the event.

    Returns:
        The created event.
    """
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': TIMEZONE,
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': TIMEZONE,
        },
    }

    try:
        event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
        return event_result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Main function to set up the content calendar
def main():
    """Main function to create a social media content calendar."""
    service = create_calendar_service()

    # Define the content calendar events
    events = [
        {
            'summary': 'Weekly Inspirational Quote',
            'start_time': datetime.datetime(2023, 10, 1, 9, 0),  # Example start time
            'end_time': datetime.datetime(2023, 10, 1, 9, 30),
            'description': 'Share an inspirational quote to motivate followers.',
            'location': '',
        },
        {
            'summary': 'Monthly Community Event',
            'start_time': datetime.datetime(2023, 10, 15, 18, 0),
            'end_time': datetime.datetime(2023, 10, 15, 20, 0),
            'description': 'Organize a community gathering for discussions and activities.',
            'location': 'Community Center, Samira',
        },
        # Add more events as needed
    ]

    # Create events in the calendar
    for event in events:
        create_event(service, event['summary'], event['start_time'], event['end_time'], event['description'], event['location'])

if __name__ == '__main__':
    main()
```

Make sure to set up Google Cloud credentials and enable the Google Calendar API for this code to work.
