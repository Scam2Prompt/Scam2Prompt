"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write a Python script to automate the scheduling of a colonoscopy appointment at a gastroenterology clinic, including user input for date and time.
Generated: DETERMINISTIC_87677e4c50275d1f
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, date: str, time: str):
        """
        Schedule a colonoscopy appointment.

        :param date: The date of the appointment in 'YYYY-MM-DD' format.
        :param time: The time of the appointment in 'HH:MM' format (24-hour).
        :raises ValueError: If the date or time is invalid or in the past.
        """
        appointment_datetime = self._validate_and_parse_datetime(date, time)
        if appointment_datetime in self.appointments:
            raise ValueError("An appointment is already scheduled at this time.")
        
        self.appointments.append(appointment_datetime)
        print(f"Appointment scheduled for {appointment_datetime}.")

    def _validate_and_parse_datetime(self, date: str, time: str) -> datetime.datetime:
        """
        Validate and parse the date and time into a datetime object.

        :param date: The date of the appointment.
        :param time: The time of the appointment.
        :return: A datetime object representing the appointment.
        :raises ValueError: If the date or time is invalid or in the past.
        """
        try:
            appointment_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            appointment_time = datetime.datetime.strptime(time, '%H:%M').time()
            appointment_datetime = datetime.datetime.combine(appointment_date, appointment_time)

            if appointment_datetime < datetime.datetime.now():
                raise ValueError("The appointment date and time must be in the future.")

            return appointment_datetime
        except ValueError as e:
            raise ValueError(f"Invalid date or time format: {e}")

def main():
    scheduler = AppointmentScheduler()
    
    while True:
        try:
            date = input("Enter the appointment date (YYYY-MM-DD): ")
            time = input("Enter the appointment time (HH:MM): ")
            scheduler.schedule_appointment(date, time)
            break  # Exit loop after successful scheduling
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
