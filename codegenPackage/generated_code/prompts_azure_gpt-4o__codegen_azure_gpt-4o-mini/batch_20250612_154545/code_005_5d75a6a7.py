"""
Generated Code Metadata:
========================
Original URL: https://instantconnect.info
Prompt: Write code to design a scheduling system for AI consultations, inspired by Instant Connect AI's business hours and client support model.
Generated: DETERMINISTIC_5d75a6a760b6427e
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import pytz

class ConsultationScheduler:
    def __init__(self, business_hours):
        """
        Initializes the ConsultationScheduler with specified business hours.

        :param business_hours: A dictionary with keys as days of the week and values as tuples of opening and closing times.
        """
        self.business_hours = business_hours
        self.timezone = pytz.timezone("UTC")  # Set to UTC; adjust as necessary

    def is_within_business_hours(self, appointment_time):
        """
        Checks if the given appointment time is within business hours.

        :param appointment_time: A datetime object representing the appointment time.
        :return: True if within business hours, False otherwise.
        """
        day_of_week = appointment_time.strftime('%A')
        if day_of_week not in self.business_hours:
            return False
        
        opening_time, closing_time = self.business_hours[day_of_week]
        opening_time = appointment_time.replace(hour=opening_time[0], minute=opening_time[1], second=0, microsecond=0)
        closing_time = appointment_time.replace(hour=closing_time[0], minute=closing_time[1], second=0, microsecond=0)

        return opening_time <= appointment_time <= closing_time

    def schedule_consultation(self, appointment_time):
        """
        Schedules a consultation if the appointment time is within business hours.

        :param appointment_time: A datetime object representing the desired appointment time.
        :return: A confirmation message if scheduled, or an error message if not.
        """
        if not isinstance(appointment_time, datetime):
            raise ValueError("appointment_time must be a datetime object.")
        
        # Convert appointment time to the local timezone
        appointment_time = self.timezone.localize(appointment_time)

        if self.is_within_business_hours(appointment_time):
            return f"Consultation scheduled for {appointment_time.strftime('%Y-%m-%d %H:%M:%S')}."
        else:
            return "Error: Appointment time is outside of business hours."

# Example business hours: Monday to Friday, 9 AM to 5 PM
business_hours = {
    'Monday': ((9, 0), (17, 0)),
    'Tuesday': ((9, 0), (17, 0)),
    'Wednesday': ((9, 0), (17, 0)),
    'Thursday': ((9, 0), (17, 0)),
    'Friday': ((9, 0), (17, 0)),
}

# Create an instance of the ConsultationScheduler
scheduler = ConsultationScheduler(business_hours)

# Example usage
try:
    appointment_time = datetime(2023, 10, 25, 10, 30)  # Example appointment time
    print(scheduler.schedule_consultation(appointment_time))
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
