"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Write code to integrate a scheduling system for an educational institution, based on the working hours (Lun – Vie 6:00 – 18:30) mentioned on the IEBCA website.
Generated: DETERMINISTIC_20d427a756ae3c77
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class Scheduler:
    def __init__(self):
        """
        Initialize the scheduler with predefined working hours.
        """
        self.start_time = datetime.strptime("06:00", "%H:%M").time()  # Opening hour: 6:00 AM
        self.end_time = datetime.strptime("18:30", "%H:%M").time()    # Closing hour: 6:30 PM
        self.days_open = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # Open Monday to Friday
        self.schedule = {}  # Placeholder for storing scheduled events
    
    def is_within_working_hours(self, date_time):
        """
        Check if the given datetime is within the working hours and days.
        :param date_time: datetime object to validate.
        :return: True if within working hours, False otherwise.
        """
        day_name = date_time.strftime('%A')  # Get day name
        time = date_time.time()  # Get time
        return day_name in self.days_open and self.start_time <= time <= self.end_time
    
    def add_event(self, event_name, event_date_time, duration_minutes):
        """
        Add a new event to the schedule if it falls within working hours.
        :param event_name: Name of the event.
        :param event_date_time: Datetime object representing the start of the event.
        :param duration_minutes: Integer duration of the event in minutes.
        :return: Success message or error.
        """
        if not self.is_within_working_hours(event_date_time):
            return f"Error: Event '{event_name}' falls outside working hours."

        # Calculate event end time
        event_end_time = event_date_time + timedelta(minutes=duration_minutes)
        if not self.is_within_working_hours(event_end_time):
            return f"Error: Event '{event_name}' exceeds working hours."

        # Check for conflicts
        for existing_event in self.schedule.values():
            if existing_event['start'] <= event_date_time < existing_event['end'] or \
               existing_event['start'] < event_end_time <= existing_event['end']:
                return f"Error: Event '{event_name}' conflicts with existing event '{existing_event['name']}'."

        # Add event to the schedule
        event_id = len(self.schedule) + 1
        self.schedule[event_id] = {
            'name': event_name,
            'start': event_date_time,
            'end': event_end_time
        }
        return f"Event '{event_name}' scheduled successfully."
    
    def view_schedule(self):
        """
        View all events in the schedule.
        :return: JSON representation of the schedule.
        """
        formatted_schedule = {
            event_id: {
                'name': details['name'],
                'start': details['start'].strftime("%Y-%m-%d %H:%M"),
                'end': details['end'].strftime("%Y-%m-%d %H:%M")
            }
            for event_id, details in self.schedule.items()
        }
        return json.dumps(formatted_schedule, indent=4)

# Example usage

if __name__ == "__main__":
    scheduler = Scheduler()

    # Test event scheduling
    event1 = scheduler.add_event("Math Class", datetime(2023, 11, 3, 9, 0), 90)
    print(event1)  # Expect success message

    event2 = scheduler.add_event("Science Class", datetime(2023, 11, 3, 18, 0), 45)
    print(event2)  # Expect error due to exceeding working hours

    event3 = scheduler.add_event("Art Class", datetime(2023, 11, 4, 8, 0), 60)
    print(event3)  # Expect success message

    # View current schedule
    print(scheduler.view_schedule())
```
