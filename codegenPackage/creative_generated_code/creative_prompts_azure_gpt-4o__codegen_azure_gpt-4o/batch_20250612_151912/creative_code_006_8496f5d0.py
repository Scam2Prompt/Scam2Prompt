"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Write a Python script to integrate Typeform with Google Calendar, automatically scheduling events based on form submissions.
Generated: DETERMINISTIC_8496f5d036059544
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
import requests
import datetime
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms/{form_id}/responses"
GOOGLE_CALENDAR_API_SCOPES = ['https://www.googleapis.com/auth/calendar']
GOOGLE_CALENDAR_ID = "primary"  # Replace with your calendar ID if not using the default calendar

# Environment variables (Recommended to use .env files for sensitive information)
TYPEFORM_API_KEY = os.getenv("TYPEFORM_API_KEY")  # Typeform API Key
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")  # Path to the Google service account JSON file

# Fetch responses from Typeform
def fetch_typeform_responses(form_id):
    """
    Fetches form responses from Typeform API.

    :param form_id: The unique ID of the Typeform form.
    :return: List of response data.
    """
    try:
        headers = {"Authorization": f"Bearer {TYPEFORM_API_KEY}"}
        params = {"page_size": 100}  # Number of responses to fetch
        response = requests.get(TYPEFORM_API_URL.format(form_id=form_id), headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Typeform responses: {e}")
        return []

# Initialize Google Calendar API client
def initialize_calendar_client():
    """
    Initializes the Google Calendar API client using a service account file.

    :return: Google Calendar API client.
    """
    try:
        credentials = Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT_FILE, scopes=GOOGLE_CALENDAR_API_SCOPES
        )
        return build("calendar", "v3", credentials=credentials)
    except Exception as e:
        print(f"Error initializing Google Calendar API client: {e}")
        return None

# Create an event in Google Calendar
def create_google_calendar_event(calendar_service, event_data):
    """
    Creates an event in Google Calendar.

    :param calendar_service: Google Calendar API client.
    :param event_data: Dictionary containing event details.
    :return: Created event details or None if there's an error.
    """
    try:
        event = calendar_service.events().insert(calendarId=GOOGLE_CALENDAR_ID, body=event_data).execute()
        print(f"Event created: {event.get('htmlLink')}")
        return event
    except Exception as e:
        print(f"Error creating Google Calendar event: {e}")
        return None

# Map Typeform responses to Google Calendar events
def map_responses_to_events(responses):
    """
    Maps Typeform responses to Google Calendar event data.

    :param responses: List of Typeform responses.
    :return: List of Google Calendar event data.
    """
    events = []
    for response in responses:
        # Extract data from Typeform response (modify keys based on your Typeform structure)
        answers = response.get("answers", [])
        name = next((a["text"] for a in answers if a["field"]["id"] == "name_field_id"), "Anonymous")
        email = next((a["email"] for a in answers if a["field"]["id"] == "email_field_id"), "No Email")
        date = next((a["date"] for a in answers if a["field"]["id"] == "date_field_id"), None)
        time = next((a["time"] for a in answers if a["field"]["id"] == "time_field_id"), None)
        
        # Combine date and time for event start
        if date and time:
            start_datetime = f"{date}T{time}:00"
            end_datetime = (datetime.datetime.fromisoformat(start_datetime) + datetime.timedelta(hours=1)).isoformat()

            # Create event data
            event = {
                "summary": f"Meeting with {name}",
                "description": f"Scheduled via Typeform. Email: {email}",
                "start": {"dateTime": start_datetime, "timeZone": "UTC"},
                "end": {"dateTime": end_datetime, "timeZone": "UTC"},
            }
            events.append(event)
    return events

# Main function
def main():
    """
    Main function to integrate Typeform with Google Calendar and schedule events based on form submissions.
    """
    # Replace with your Typeform form ID
    typeform_form_id = "your_form_id_here"

    # Step 1: Fetch responses from Typeform
    responses = fetch_typeform_responses(typeform_form_id)

    # Step 2: Map responses to Google Calendar events
    events_data = map_responses_to_events(responses)
    
    # Step 3: Initialize Google Calendar API client
    calendar_service = initialize_calendar_client()
    if not calendar_service:
        print("Failed to initialize Google Calendar client.")
        return

    # Step 4: Create events in Google Calendar
    for event_data in events_data:
        create_google_calendar_event(calendar_service, event_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
