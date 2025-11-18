"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Generate code for automated appointment scheduling using InfinitiAI's built-in calendar application. Ensure the appointments flow seamlessly into the pipeline.
Generated: DETERMINISTIC_4d705091539969bb
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Appointment:
    """
    Represents an appointment.
    """
    def __init__(self, title: str, start_time: datetime.datetime, end_time: datetime.datetime):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Appointment('{self.title}', {self.start_time}, {self.end_time})"

class Calendar:
    """
    Represents a calendar that manages appointments.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []

    def add_appointment(self, appointment: Appointment) -> None:
        """
        Adds a new appointment to the calendar.
        
        Arguments:
        appointment -- an Appointment object to be added
        
        Raises:
        ValueError: If the appointment times overlap with existing appointments.
        """
        if not self._is_time_slot_available(appointment.start_time, appointment.end_time):
            raise ValueError("Appointment times overlap with an existing appointment.")

        self.appointments.append(appointment)

    def _is_time_slot_available(self, start_time: datetime.datetime, end_time: datetime.datetime) -> bool:
        """
        Checks if the time slot is available for a new appointment.
        
        Arguments:
        start_time -- The start time of the new appointment
        end_time -- The end time of the new appointment
        
        Returns:
        bool: True if the time slot is available, False otherwise.
        """
        for existing_appointment in self.appointments:
            if (start_time < existing_appointment.end_time and end_time > existing_appointment.start_time):
                return False
        return True

    def get_appointments(self) -> List[Appointment]:
        """
        Returns a list of all appointments in the calendar.
        
        Returns:
        List[Appointment]: List of appointments.
        """
        return self.appointments

def schedule_appointment(calendar: Calendar, title: str, start_time: datetime.datetime, end_time: datetime.datetime) -> Optional[str]:
    """
    Schedules a new appointment in the provided calendar.
    
    Arguments:
    calendar -- The Calendar instance where the appointment will be added
    title -- The title of the appointment
    start_time -- The start time of the appointment
    end_time -- The end time of the appointment
    
    Returns:
    str: Confirmation message if appointment is scheduled successfully, otherwise an error message.
    """
    try:
        appointment = Appointment(title, start_time, end_time)
        calendar.add_appointment(appointment)
        return f"Appointment '{title}' scheduled from {start_time} to {end_time}."
    except ValueError as e:
        return str(e)

# Example usage
if __name__ == "__main__":
    # Initialize a calendar instance
    my_calendar = Calendar()

    # Schedule some appointments
    print(schedule_appointment(my_calendar, "Team Meeting", datetime.datetime(2023, 10, 10, 10, 0), datetime.datetime(2023, 10, 10, 11, 0)))
    print(schedule_appointment(my_calendar, "Doctor Appointment", datetime.datetime(2023, 10, 10, 11, 0), datetime.datetime(2023, 10, 10, 12, 0)))
    print(schedule_appointment(my_calendar, "Team Meeting", datetime.datetime(2023, 10, 10, 10, 30), datetime.datetime(2023, 10, 10, 11, 30)))  # This should raise an error

    # List all scheduled appointments
    print("Scheduled Appointments:")
    for appt in my_calendar.get_appointments():
        print(appt)
```
