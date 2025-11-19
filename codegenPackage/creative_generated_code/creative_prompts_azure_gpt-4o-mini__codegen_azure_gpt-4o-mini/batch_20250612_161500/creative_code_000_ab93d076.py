"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Generate a Python code snippet that demonstrates how to implement a dental appointment scheduling system, similar to the one used by Heroes Dental for their multiple locations.
Generated: DETERMINISTIC_ab93d0769ec1d304
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Appointment:
    """Class to represent a dental appointment."""
    
    def __init__(self, patient_name, appointment_time, location):
        """
        Initialize a dental appointment.
        
        :param patient_name: str - Name of the patient
        :param appointment_time: datetime - Scheduled time for the appointment
        :param location: str - Location of the appointment
        """
        self.patient_name = patient_name
        self.appointment_time = appointment_time
        self.location = location

    def __str__(self):
        """Return a string representation of the appointment."""
        return f"Appointment for {self.patient_name} at {self.appointment_time} in {self.location}"


class Scheduler:
    """Class to manage scheduling of dental appointments."""
    
    def __init__(self):
        """Initialize an empty list of appointments."""
        self.appointments = []

    def add_appointment(self, appointment):
        """
        Add an appointment to the schedule.
        
        :param appointment: Appointment - The appointment to be scheduled
        :raises ValueError: If the appointment time is in the past or if the appointment conflicts with an existing one.
        """
        if appointment.appointment_time < datetime.datetime.now():
            raise ValueError("Cannot schedule an appointment in the past.")
        
        for existing_appointment in self.appointments:
            if (appointment.appointment_time == existing_appointment.appointment_time and 
                    appointment.location == existing_appointment.location):
                raise ValueError("Appointment conflict at this time and location.")

        self.appointments.append(appointment)

    def view_appointments(self):
        """Display all scheduled appointments."""
        if not self.appointments:
            print("No appointments scheduled.")
            return
        
        for appointment in self.appointments:
            print(appointment)


if __name__ == "__main__":
    scheduler = Scheduler()

    # Example appointments
    try:
        # Creating a valid appointment
        appointment1 = Appointment("John Doe", datetime.datetime(2023, 11, 10, 14, 0), "Main Street Dental")
        scheduler.add_appointment(appointment1)

        # Attempting to add a conflicting appointment
        appointment2 = Appointment("Jane Smith", datetime.datetime(2023, 11, 10, 14, 0), "Main Street Dental")
        scheduler.add_appointment(appointment2)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Viewing all appointments
    scheduler.view_appointments()
```
