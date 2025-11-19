"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.haim-lawyer.co.il
Prompt: Write a Python function that automates the scheduling of consultations for a law office, inspired by the operational hours and client service approach of Haim Shukrani's law firm.
Generated: DETERMINISTIC_b5cb50fb306bccc1
Batch ID: 20250612_162051
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

class ConsultationScheduler:
    """A class to automate the scheduling of consultations for a law office."""

    def __init__(self, office_hours, timezone='UTC'):
        """
        Initializes the ConsultationScheduler with office hours and timezone.

        Args:
            office_hours (dict): A dictionary defining the office hours.
            timezone (str): The timezone for the office.
        """
        self.office_hours = office_hours
        self.timezone = pytz.timezone(timezone)
        self.appointments = []

    def is_within_office_hours(self, appointment_time):
        """
        Checks if the given appointment time is within office hours.

        Args:
            appointment_time (datetime): The time to check.

        Returns:
            bool: True if within office hours, otherwise False.
        """
        day_of_week = appointment_time.strftime('%A')
        office_start = self.office_hours[day_of_week]['start']
        office_end = self.office_hours[day_of_week]['end']
        start_time = datetime.combine(appointment_time.date(), office_start)
        end_time = datetime.combine(appointment_time.date(), office_end)

        return start_time <= appointment_time <= end_time

    def schedule_appointment(self, client_name, appointment_time):
        """
        Schedules a consultation appointment if it is within office hours.

        Args:
            client_name (str): The name of the client.
            appointment_time (datetime): The requested appointment time.

        Returns:
            str: A confirmation message if scheduled, or an error message.
        """
        if not isinstance(appointment_time, datetime):
            return "Error: appointment_time must be a datetime object."

        appointment_time = self.timezone.localize(appointment_time)

        if self.is_within_office_hours(appointment_time):
            self.appointments.append((client_name, appointment_time))
            return f"Appointment scheduled for {client_name} on {appointment_time.strftime('%Y-%m-%d %H:%M:%S')}."
        else:
            return "Error: Appointment time is outside of office hours."

    def get_schedule(self):
        """
        Returns the current schedule of appointments.

        Returns:
            list: A list of scheduled appointments.
        """
        return [(client, time.strftime('%Y-%m-%d %H:%M:%S')) for client, time in self.appointments]


if __name__ == "__main__":
    # Define office hours for a law firm
    office_hours = {
        'Monday': {'start': datetime.strptime('09:00', '%H:%M').time(),
                   'end': datetime.strptime('17:00', '%H:%M').time()},
        'Tuesday': {'start': datetime.strptime('09:00', '%H:%M').time(),
                    'end': datetime.strptime('17:00', '%H:%M').time()},
        'Wednesday': {'start': datetime.strptime('09:00', '%H:%M').time(),
                      'end': datetime.strptime('17:00', '%H:%M').time()},
        'Thursday': {'start': datetime.strptime('09:00', '%H:%M').time(),
                     'end': datetime.strptime('17:00', '%H:%M').time()},
        'Friday': {'start': datetime.strptime('09:00', '%H:%M').time(),
                   'end': datetime.strptime('15:00', '%H:%M').time()},
        'Saturday': {'start': None, 'end': None},
        'Sunday': {'start': None, 'end': None}
    }

    scheduler = ConsultationScheduler(office_hours, timezone='America/New_York')

    # Example of scheduling an appointment
    appointment_time = datetime(2023, 10, 25, 10, 30)  # Example date and time
    result = scheduler.schedule_appointment("John Doe", appointment_time)
    print(result)

    # Display scheduled appointments
    print("Current Schedule:")
    for appointment in scheduler.get_schedule():
        print(appointment)
```
