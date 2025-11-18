"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedintegration.com
Prompt: Create a script that checks availability across multiple calendars (Google Calendar and Outlook Calendar) and displays available time slots on a single screen, similar to the functionality provided by Secured Integration.
Generated: DETERMINISTIC_2549d9f5001e8773
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build
from microsoft_graph.client import GraphClient

# Constants
TIMEZONE = 'UTC'
GOOGLE_CREDENTIALS_FILE = 'google_credentials.json'
OUTLOOK_TOKEN = 'outlook_access_token'  # Replace with a valid token or token generation logic

def fetch_google_calendar_events(credentials_file):
    """
    Fetches events from Google Calendar.

    :param credentials_file: Path to the Google service account credentials JSON file.
    :return: List of events as dictionaries.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        service = build('calendar', 'v3', credentials=credentials)

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # Current time in UTC
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                               maxResults=10, singleEvents=True,
                                               orderBy='startTime').execute()
        return events_result.get('items', [])
    except Exception as e:
        print(f"Error fetching Google Calendar events: {e}")
        return []

def fetch_outlook_calendar_events(access_token):
    """
    Fetches events from Outlook Calendar.

    :param access_token: OAuth access token for Microsoft Graph API.
    :return: List of events as dictionaries.
    """
    try:
        client = GraphClient(access_token)
        start_time = datetime.datetime.utcnow()
        end_time = start_time + datetime.timedelta(days=1)

        query_params = {
            'startDateTime': start_time.isoformat(),
            'endDateTime': end_time.isoformat(),
        }
        events = client.get('/me/calendarview', params=query_params)
        return events.get('value', [])
    except Exception as e:
        print(f"Error fetching Outlook Calendar events: {e}")
        return []

def parse_event_time(event):
    """
    Parses event start and end times into datetime objects.

    :param event: Calendar event dictionary.
    :return: Tuple of (start_time, end_time) as datetime objects.
    """
    try:
        start_time = datetime.datetime.strptime(
            event['start'].get('dateTime', ''), '%Y-%m-%dT%H:%M:%S.%fZ'
        ).replace(tzinfo=pytz.utc)
        end_time = datetime.datetime.strptime(
            event['end'].get('dateTime', ''), '%Y-%m-%dT%H:%M:%S.%fZ'
        ).replace(tzinfo=pytz.utc)
        return start_time, end_time
    except Exception as e:
        print(f"Error parsing event times: {e}")
        return None, None

def find_available_time_slots(events, day_start, day_end):
    """
    Finds available time slots within a given day range.

    :param events: List of events with start and end times.
    :param day_start: Start of the day as a datetime object.
    :param day_end: End of the day as a datetime object.
    :return: List of available time slots (start_time, end_time).
    """
    busy_slots = []
    for event in events:
        start, end = parse_event_time(event)
        if start and end:
            busy_slots.append((start, end))

    busy_slots.sort()  # Sort by start time
    available_slots = []
    current_start = day_start

    for start, end in busy_slots:
        if current_start < start:
            available_slots.append((current_start, start))
        current_start = max(current_start, end)

    if current_start < day_end:
        available_slots.append((current_start, day_end))

    return available_slots

def main():
    """
    Main function to fetch calendars and display available time slots.
    """
    # Fetch events from Google and Outlook Calendars
    google_events = fetch_google_calendar_events(GOOGLE_CREDENTIALS_FILE)
    outlook_events = fetch_outlook_calendar_events(OUTLOOK_TOKEN)

    # Combine all events
    all_events = google_events + outlook_events

    # Define the day range (8 AM to 6 PM UTC)
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    day_start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    day_end = now.replace(hour=18, minute=0, second=0, microsecond=0)

    # Find available time slots
    available_slots = find_available_time_slots(all_events, day_start, day_end)

    # Display available slots
    print("Available Time Slots:")
    for start, end in available_slots:
        print(f"From {start.strftime('%Y-%m-%d %H:%M:%S')} to {end.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `google_credentials.json` and `outlook_access_token` with actual credentials and token.
- You may need the `microsoft-graph-python` library for interacting with Outlook (Microsoft Graph API). Install it using `pip install microsoftgraph-python`.
- Ensure proper authentication and permissions for accessing both Google and Outlook calendars.
