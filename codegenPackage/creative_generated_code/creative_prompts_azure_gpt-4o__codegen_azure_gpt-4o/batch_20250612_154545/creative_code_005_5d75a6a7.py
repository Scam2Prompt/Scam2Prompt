"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instantconnect.info
Prompt: Write code to design a scheduling system for AI consultations, inspired by Instant Connect AI's business hours and client support model.
Generated: DETERMINISTIC_5d75a6a760b6427e
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz

class SchedulingSystem:
    """
    A scheduling system for AI consultations.
    """

    def __init__(self, business_hours, timezone="UTC"):
        """
        Initialize the scheduling system.

        :param business_hours: A dictionary specifying business hours, e.g., {'Monday': ('09:00', '17:00'), ...}
        :param timezone: Timezone for the scheduling system, e.g., 'UTC', 'America/New_York'
        """
        self.business_hours = business_hours
        self.timezone = pytz.timezone(timezone)

    def is_within_business_hours(self, date_time):
        """
        Determines whether a given datetime is within business hours.

        :param date_time: A datetime object in the system's timezone
        :return: True if within business hours, False otherwise
        """
        day_of_week = date_time.strftime('%A')  # Get the day of the week (e.g., 'Monday')
        if day_of_week not in self.business_hours:
            return False

        start_time, end_time = self.business_hours[day_of_week]
        start_dt = datetime.strptime(start_time, '%H:%M').time()
        end_dt = datetime.strptime(end_time, '%H:%M').time()
        current_time = date_time.time()

        return start_dt <= current_time <= end_dt

    def schedule_appointment(self, client_name, requested_date_time):
        """
        Schedule an appointment if the requested time is within business hours.

        :param client_name: Name of the client
        :param requested_date_time: A datetime object in the system's timezone
        :return: Confirmation message or error message
        """
        # Convert requested_date_time to system's timezone
        requested_date_time = requested_date_time.astimezone(self.timezone)

        if not self.is_within_business_hours(requested_date_time):
            return f"Error: Requested time {requested_date_time} is outside of business hours."

        # Appointment scheduling logic (can be extended with database integration, etc.)
        return f"Appointment successfully scheduled for {client_name} on {requested_date_time}."

    def get_next_available_slot(self, requested_date_time):
        """
        Finds the next available slot within business hours.

        :param requested_date_time: A datetime object in the system's timezone
        :return: Next available datetime object within business hours
        """
        requested_date_time = requested_date_time.astimezone(self.timezone)

        while True:
            day_of_week = requested_date_time.strftime('%A')
            if day_of_week in self.business_hours:
                start_time, end_time = self.business_hours[day_of_week]
                start_dt = datetime.strptime(start_time, '%H:%M').time()
                end_dt = datetime.strptime(end_time, '%H:%M').time()

                # Check if requested time is within current day's business hours
                if requested_date_time.time() < start_dt:
                    return requested_date_time.replace(hour=start_dt.hour, minute=start_dt.minute, second=0, microsecond=0)
                elif requested_date_time.time() <= end_dt:
                    return requested_date_time

            # Move to the next day
            requested_date_time += timedelta(days=1)
            requested_date_time = requested_date_time.replace(hour=0, minute=0, second=0, microsecond=0)

if __name__ == "__main__":
    # Example usage:
    business_hours = {
        'Monday': ('09:00', '17:00'),
        'Tuesday': ('09:00', '17:00'),
        'Wednesday': ('09:00', '17:00'),
        'Thursday': ('09:00', '17:00'),
        'Friday': ('09:00', '17:00'),
    }

    scheduler = SchedulingSystem(business_hours, timezone="America/New_York")

    # Try scheduling an appointment
    client_name = "John Doe"
    requested_time = datetime(2023, 10, 2, 16, 0, tzinfo=pytz.utc)  # Example: Oct 2, 2023 at 16:00 UTC
    print(scheduler.schedule_appointment(client_name, requested_time))

    # Find the next available slot
    next_slot = scheduler.get_next_available_slot(datetime(2023, 10, 2, 18, 0, tzinfo=pytz.utc))
    print(f"Next available slot: {next_slot}")
```
