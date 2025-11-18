"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://electrocoin.typeform.com
Prompt: Provide an example of how to use Typeform's API to create an event registration form that integrates with Google Calendar for automatic scheduling.
Generated: DETERMINISTIC_c99af2d1e18d7f48
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses": {
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
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Constants (Replace with your own API keys and tokens)
TYPEFORM_API_KEY = "your_typeform_api_key"
TYPEFORM_FORM_ID = "your_typeform_form_id"
GOOGLE_CALENDAR_CREDENTIALS_FILE = "path_to_your_google_calendar_credentials.json"
GOOGLE_CALENDAR_ID = "primary"

def create_event_in_calendar(event_data):
    """
    Creates an event in Google Calendar using the provided event data.
    """
    try:
        # Load Google Calendar credentials
        credentials = Credentials.from_service_account_file(GOOGLE_CALENDAR_CREDENTIALS_FILE)
        service = build("calendar", "v3", credentials=credentials)
        
        # Prepare event details
        event = {
            "summary": event_data["summary"],
            "description": event_data["description"],
            "start": {
                "dateTime": event_data["start_time"],
                "timeZone": "UTC"
            },
            "end": {
                "dateTime": event_data["end_time"],
                "timeZone": "UTC"
            }
        }

        # Insert event into Google Calendar
        created_event = service.events().insert(calendarId=GOOGLE_CALENDAR_ID, body=event).execute()
        print(f"Event created successfully: {created_event['htmlLink']}")
        return created_event

    except Exception as e:
        print(f"Error creating event in Google Calendar: {e}")
        return None


def get_form_responses():
    """
    Fetches responses from Typeform using its API.
    """
    url = f"https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for failed requests
        responses = response.json()
        return responses["items"]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Typeform responses: {e}")
        return []


def process_responses(responses):
    """
    Processes Typeform responses and schedules events in Google Calendar.
    """
    for response in responses:
        try:
            # Extract data from responses (e.g., name, event details, start/end time)
            answers = response["answers"]
            summary = next(answer["text"] for answer in answers if answer["field"]["id"] == "summary_field_id")
            description = next(answer["text"] for answer in answers if answer["field"]["id"] == "description_field_id")
            start_time = next(answer["text"] for answer in answers if answer["field"]["id"] == "start_time_field_id")
            end_time = next(answer["text"] for answer in answers if answer["field"]["id"] == "end_time_field_id")

            # Prepare event data
            event_data = {
                "summary": summary,
                "description": description,
                "start_time": start_time,
                "end_time": end_time
            }

            # Create event in Google Calendar
            create_event_in_calendar(event_data)

        except KeyError as e:
            print(f"Error processing response: Missing field {e}")
        except Exception as e:
            print(f"Error processing response: {e}")


if __name__ == "__main__":
    # Fetch responses from Typeform
    form_responses = get_form_responses()

    # Process each response and create events in Google Calendar
    process_responses(form_responses)
```

This script assumes you have:
- A Typeform API key to access responses from a specific form.
- Google Calendar API credentials saved in a JSON file.
- Correct form field IDs from Typeform for `summary`, `description`, `start_time`, and `end_time`.

Replace placeholders (e.g., `your_typeform_api_key`, `summary_field_id`) with your actual values before running the code.
