"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Create a program to automate the generation of a tractor pulling event calendar, referencing the ATPA Calendar format described on jobbo.com.au.
Generated: DETERMINISTIC_26d692fef0b19890
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for generating a tractor pulling event calendar in ATPA Calendar format:

```python
import json
from datetime import datetime, timedelta

def validate_date(date_str):
    """
    Validates that the given string is a valid date in the format YYYY-MM-DD.

    :param date_str: The date string to validate.
    :return: A valid datetime object, or None if invalid.
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None


def generate_event_calendar(events):
    """
    Generates a tractor pulling event calendar based on the ATPA Calendar format.

    :param events: List of dictionaries containing event data.
                   Each dictionary should have the keys: "title", "location", "date", and "description".
    :return: A JSON string representing the calendar in ATPA Calendar format.
    """
    # Validate event data and format the calendar
    calendar = {"events": []}

    for event in events:
        event_date = validate_date(event.get("date"))
        if not event_date:
            print(f"Skipping invalid event date: {event.get('date')}")
            continue

        calendar["events"].append({
            "title": event.get("title", "Untitled Event"),
            "location": event.get("location", "Unknown Location"),
            "date": event_date.strftime('%Y-%m-%d'),
            "description": event.get("description", "")
        })

    return json.dumps(calendar, indent=4)


if __name__ == "__main__":
    # Example input for testing the program
    events_input = [
        {
            "title": "Spring Tractor Pull",
            "location": "Green Valley Arena",
            "date": "2024-03-15",
            "description": "Join us for a fun day of tractor pulling and entertainment!"
        },
        {
            "title": "Summer Showdown",
            "location": "Red Rock Stadium",
            "date": "2024-06-22",
            "description": "Watch the best tractor pull teams compete for the championship."
        },
        {
            "title": "Autumn Classic",
            "location": "Harvest Field",
            "date": "Invalid-Date",  # This will be skipped due to invalid date format
            "description": "A classic tractor pull event to celebrate the autumn season."
        }
    ]

    # Generate the event calendar
    calendar_output = generate_event_calendar(events_input)

    # Print the calendar in ATPA format
    print(calendar_output)
```

This program:
- Takes input as a list of event dictionaries.
- Validates the event dates.
- Skips invalid events and generates a JSON-formatted tractor pulling event calendar in ATPA format.
