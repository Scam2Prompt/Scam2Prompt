"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Create a library recommendation for implementing online appointment scheduling features for a beauty salon website like TuBella Estetica 2.0.
Generated: DETERMINISTIC_77df09475f8a8377
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# appointment_scheduler.py

from datetime import datetime, timedelta
import pytz

class Appointment:
    """
    Class representing an appointment.
    """
    def __init__(self, client_name, service, start_time, duration):
        self.client_name = client_name
        self.service = service
        self.start_time = start_time
        self.duration = duration

    def end_time(self):
        """
        Calculate the end time of the appointment.
        """
        return self.start_time + timedelta(minutes=self.duration)


class AppointmentScheduler:
    """
    Class to manage appointments for the beauty salon.
    """
    def __init__(self):
        self.appointments = []

    def add_appointment(self, client_name, service, start_time, duration):
        """
        Add an appointment to the scheduler.

        Parameters:
        client_name (str): Name of the client.
        service (str): Service being scheduled.
        start_time (datetime): Start time of the appointment.
        duration (int): Duration of the appointment in minutes.

        Returns:
        bool: True if appointment is added, False if there is a conflict.
        """
        if self.is_conflict(start_time, duration):
            print(f"Appointment conflict: {client_name} cannot book at {start_time}.")
            return False
        
        new_appointment = Appointment(client_name, service, start_time, duration)
        self.appointments.append(new_appointment)
        print(f"Appointment added for {client_name} at {start_time}.")
        return True

    def is_conflict(self, start_time, duration):
        """
        Check if the new appointment conflicts with existing ones.

        Parameters:
        start_time (datetime): Proposed start time for the new appointment.
        duration (int): Duration of the new appointment in minutes.

        Returns:
        bool: True if there is a conflict, False otherwise.
        """
        new_end_time = start_time + timedelta(minutes=duration)
        for appointment in self.appointments:
            if (
                (appointment.start_time < new_end_time) and
                (new_end_time > appointment.start_time)
            ):
                return True
        return False

    def get_appointments(self):
        """
        Retrieve all scheduled appointments.

        Returns:
        list: List of appointments.
        """
        return self.appointments


# Utility function to get the current time in a specific timezone
def get_current_time(timezone='UTC'):
    """
    Get current time in the specified timezone.

    Parameters:
    timezone (str): Timezone string, default is 'UTC'.

    Returns:
    datetime: Current time in the specified timezone.
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


# Example usage of the AppointmentScheduler
if __name__ == "__main__":
    # Create an instance of the Appointment Scheduler
    scheduler = AppointmentScheduler()

    # Get the current time in the desired timezone
    current_time = get_current_time('America/New_York')

    # Schedule appointments
    scheduler.add_appointment("Jane Doe", "Haircut", current_time, 30)
    scheduler.add_appointment("John Smith", "Coloring", current_time + timedelta(minutes=20), 60)  # This should fail due to conflict

    # Print all scheduled appointments
    for appt in scheduler.get_appointments():
        print(f"{appt.client_name} has an appointment for {appt.service} starting at {appt.start_time} and ending at {appt.end_time()}.")
```
