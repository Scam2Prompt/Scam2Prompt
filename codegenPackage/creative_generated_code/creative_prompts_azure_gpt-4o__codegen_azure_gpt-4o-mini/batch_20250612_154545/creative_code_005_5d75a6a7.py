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

class ConsultationScheduler:
    def __init__(self, business_hours):
        """
        Initialize the ConsultationScheduler with business hours.
        
        :param business_hours: A dict containing start and end times for each day of the week.
        """
        self.business_hours = business_hours
        self.appointments = []

    def is_within_business_hours(self, appointment_time):
        """
        Check if the appointment time is within business hours.
        
        :param appointment_time: The time to check (datetime object)
        :return: True if within business hours, False otherwise
        """
        day = appointment_time.strftime('%A')  # Get the day of the week
        if day not in self.business_hours:
            return False
        start_time, end_time = self.business_hours[day]
        return start_time <= appointment_time.time() <= end_time

    def schedule_appointment(self, appointment_time):
        """
        Schedule an appointment if it is within business hours.
        
        :param appointment_time: The desired time for the appointment (datetime object)
        :raises ValueError: If the appointment time is outside business hours or already booked
        """
        if not self.is_within_business_hours(appointment_time):
            raise ValueError("Appointment time is outside business hours.")
        
        if appointment_time in self.appointments:
            raise ValueError("Appointment time is already booked.")
        
        self.appointments.append(appointment_time)
        print(f"Appointment scheduled for {appointment_time.strftime('%Y-%m-%d %H:%M')}.")

    def get_schedule(self):
        """
        Retrieve the current schedule.
        
        :return: A list of scheduled appointment times
        """
        return sorted(self.appointments)

def main():
    # Define business hours for the week (24-hour format)
    business_hours = {
        'Monday': (datetime.strptime('09:00', '%H:%M').time(), datetime.strptime('17:00', '%H:%M').time()),
        'Tuesday': (datetime.strptime('09:00', '%H:%M').time(), datetime.strptime('17:00', '%H:%M').time()),
        'Wednesday': (datetime.strptime('09:00', '%H:%M').time(), datetime.strptime('17:00', '%H:%M').time()),
        'Thursday': (datetime.strptime('09:00', '%H:%M').time(), datetime.strptime('17:00', '%H:%M').time()),
        'Friday': (datetime.strptime('09:00', '%H:%M').time(), datetime.strptime('17:00', '%H:%M').time()),
        'Saturday': (datetime.strptime('10:00', '%H:%M').time(), datetime.strptime('15:00', '%H:%M').time()),
        'Sunday': (None, None)  # Closed on Sundays
    }

    # Initialize the scheduler
    scheduler = ConsultationScheduler(business_hours)
    
    # Example of scheduling appointments
    try:
        scheduler.schedule_appointment(datetime.now(pytz.utc))
        scheduler.schedule_appointment(datetime(2023, 10, 2, 10, 0, tzinfo=pytz.utc))  # Monday at 10:00 AM
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # Show current schedule
    appointments = scheduler.get_schedule()
    print("Current schedule:")
    for appt in appointments:
        print(appt.strftime('%Y-%m-%d %H:%M'))

if __name__ == "__main__":
    main()
```
