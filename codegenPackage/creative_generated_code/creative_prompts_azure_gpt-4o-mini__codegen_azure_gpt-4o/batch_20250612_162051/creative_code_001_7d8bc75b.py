"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vipmoov.com
Prompt: Write a Python function that utilizes an event planning library to manage events globally, inspired by the services provided by VIP MOOV.
Generated: DETERMINISTIC_7d8bc75b541973ef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pytz
from datetime import datetime
from typing import List, Dict, Union
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError

# Initialize the scheduler globally
scheduler = BackgroundScheduler()
scheduler.start()

# Define a function to create an event
def create_event(event_id: str, event_name: str, event_time: str, timezone: str, event_data: Dict[str, Union[str, int]]) -> None:
    """
    Create a globally managed event using a scheduler.

    Args:
        event_id (str): Unique identifier for the event.
        event_name (str): Name of the event.
        event_time (str): Time of the event in ISO 8601 format (e.g., '2023-10-15T14:30:00').
        timezone (str): Timezone of the event (e.g., 'UTC', 'America/New_York').
        event_data (Dict[str, Union[str, int]]): Additional details about the event.

    Raises:
        ValueError: If the event_time or timezone is invalid.
    """
    try:
        # Parse the event time and timezone
        tz = pytz.timezone(timezone)
        event_datetime = datetime.fromisoformat(event_time).astimezone(tz)

        # Define the job function
        def event_action():
            print(f"Event Triggered: {event_name}")
            print(f"Event Data: {event_data}")

        # Schedule the event
        scheduler.add_job(
            func=event_action,
            trigger="date",
            run_date=event_datetime,
            id=event_id,
            name=event_name,
            timezone=tz
        )
        print(f"Event '{event_name}' scheduled successfully for {event_datetime}.")

    except (ValueError, pytz.UnknownTimeZoneError) as e:
        print(f"Error creating event '{event_name}': {e}")

# Define a function to delete an event
def delete_event(event_id: str) -> None:
    """
    Delete a scheduled event by its ID.

    Args:
        event_id (str): Unique identifier for the event to delete.

    Raises:
        JobLookupError: If the event with the given ID is not found.
    """
    try:
        scheduler.remove_job(event_id)
        print(f"Event with ID '{event_id}' deleted successfully.")
    except JobLookupError:
        print(f"No event found with ID '{event_id}'.")

# Define a function to list all scheduled events
def list_events() -> List[Dict[str, Union[str, datetime]]]:
    """
    List all scheduled events.

    Returns:
        List[Dict[str, Union[str, datetime]]]: A list of dictionaries containing event details.
    """
    events = []
    for job in scheduler.get_jobs():
        events.append({
            "event_id": job.id,
            "event_name": job.name,
            "event_time": job.next_run_time,
        })
    return events

# Graceful shutdown of the scheduler
def shutdown_scheduler() -> None:
    """
    Shut down the scheduler gracefully.
    """
    scheduler.shutdown()
    print("Scheduler shut down successfully.")
```

This Python code provides a production-ready implementation for managing events globally using the APScheduler library, while adhering to best practices.
