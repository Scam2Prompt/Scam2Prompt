"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Generate code to calculate the availability of medical specialists at Grupo Clínico IDET's locations based on their working hours and appointment schedules.
Generated: DETERMINISTIC_56887e430203341e
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Specialist:
    def __init__(self, name: str, working_hours: List[Dict[str, str]]):
        """
        Initializes a Specialist instance.

        :param name: The name of the specialist.
        :param working_hours: List of dictionaries representing the working hours for each day.
        """
        self.name = name
        self.working_hours = working_hours

    def is_available(self, appointment_time: datetime) -> bool:
        """
        Check if the specialist is available at the given appointment time.

        :param appointment_time: The datetime of the appointment.
        :return: True if available, False otherwise.
        """
        day_of_week = appointment_time.strftime('%A')
        time_str = appointment_time.strftime('%H:%M')

        # Check if the specialist works on that day
        for hours in self.working_hours:
            if hours['day'] == day_of_week:
                start_time = datetime.strptime(hours['start'], '%H:%M').time()
                end_time = datetime.strptime(hours['end'], '%H:%M').time()
                return start_time <= appointment_time.time() <= end_time

        return False


class Appointment:
    def __init__(self, specialist: Specialist, appointment_time: datetime):
        """
        Initializes an Appointment instance.

        :param specialist: An instance of Specialist.
        :param appointment_time: The datetime of the appointment.
        """
        self.specialist = specialist
        self.appointment_time = appointment_time

    def schedule(self) -> str:
        """
        Attempt to schedule an appointment.

        :return: A message indicating whether the appointment is scheduled.
        """
        if self.specialist.is_available(self.appointment_time):
            return f"Appointment scheduled with {self.specialist.name} on {self.appointment_time}."
        else:
            return f"Sorry, {self.specialist.name} is not available on {self.appointment_time}."


def main():
    # Define working hours for the specialist
    working_hours = [
        {'day': 'Monday', 'start': '09:00', 'end': '17:00'},
        {'day': 'Tuesday', 'start': '09:00', 'end': '17:00'},
        {'day': 'Wednesday', 'start': '09:00', 'end': '17:00'},
        {'day': 'Thursday', 'start': '09:00', 'end': '17:00'},
        {'day': 'Friday', 'start': '09:00', 'end': '17:00'}
    ]

    # Create a specialist instance
    specialist = Specialist(name="Dr. Smith", working_hours=working_hours)

    # Define an appointment time
    appointment_time_str = "2023-10-10 10:00"
    appointment_time = datetime.strptime(appointment_time_str, '%Y-%m-%d %H:%M')

    # Create an appointment instance and attempt to schedule
    appointment = Appointment(specialist=specialist, appointment_time=appointment_time)
    result = appointment.schedule()

    print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
