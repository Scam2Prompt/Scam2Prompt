"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: Provide code examples for integrating Syntera's AI manager with Google Calendar to automatically schedule and reschedule client appointments.
Generated: DETERMINISTIC_87e99d22aac51ee9
Batch ID: 20250612_154642
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/calendar": {
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
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from syntera import SynteraClient  # Assumed import for Syntera's AI manager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'  # Update with your service account file path
CALENDAR_ID = 'your_calendar_id@group.calendar.google.com'  # Update with your Google Calendar ID

# Initialize Google Calendar API
def initialize_calendar_service():
    """Initializes the Google Calendar API service."""
    try:
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('calendar', 'v3', credentials=credentials)
        logger.info("Google Calendar API initialized successfully.")
        return service
    except Exception as e:
        logger.error(f"Failed to initialize Google Calendar API: {e}")
        raise

# Schedule a new appointment
def schedule_appointment(service, start_time, end_time, summary, description):
    """Schedules a new appointment in Google Calendar.

    Args:
        service: The initialized Google Calendar API service.
        start_time (str): Start time of the appointment in RFC3339 format.
        end_time (str): End time of the appointment in RFC3339 format.
        summary (str): Summary of the appointment.
        description (str): Description of the appointment.
    """
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
        'reminders': {
            'useDefault': True,
        },
    }

    try:
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        logger.info(f"Appointment scheduled: {event.get('htmlLink')}")
    except Exception as e:
        logger.error(f"Failed to schedule appointment: {e}")
        raise

# Reschedule an existing appointment
def reschedule_appointment(service, event_id, new_start_time, new_end_time):
    """Reschedules an existing appointment in Google Calendar.

    Args:
        service: The initialized Google Calendar API service.
        event_id (str): The ID of the event to reschedule.
        new_start_time (str): New start time in RFC3339 format.
        new_end_time (str): New end time in RFC3339 format.
    """
    try:
        event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()
        event['start'] = {
            'dateTime': new_start_time,
            'timeZone': 'UTC',
        }
        event['end'] = {
            'dateTime': new_end_time,
            'timeZone': 'UTC',
        }

        updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event_id, body=event).execute()
        logger.info(f"Appointment rescheduled: {updated_event.get('htmlLink')}")
    except Exception as e:
        logger.error(f"Failed to reschedule appointment: {e}")
        raise

# Main function to integrate Syntera with Google Calendar
def main():
    """Main function to integrate Syntera's AI manager with Google Calendar."""
    try:
        # Initialize Google Calendar service
        calendar_service = initialize_calendar_service()

        # Example: Schedule a new appointment
        syntera_client = SynteraClient()  # Initialize Syntera client
        appointment_details = syntera_client.get_appointment_details()  # Hypothetical method to fetch appointment details
        schedule_appointment(calendar_service, appointment_details['start_time'], appointment_details['end_time'],
                             appointment_details['summary'], appointment_details['description'])

        # Example: Reschedule an existing appointment
        event_id = 'existing_event_id'  # Replace with your existing event ID
        new_start_time = '2023-10-31T10:00:00Z'  # Update with new date and time
        new_end_time = '2023-10-31T11:00:00Z'  # Update with new date and time
        reschedule_appointment(calendar_service, event_id, new_start_time, new_end_time)
        
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")

if __name__ == '__main__':
    main()
```
