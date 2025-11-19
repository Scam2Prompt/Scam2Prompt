"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Generate a Python script that simulates an appointment booking system for an eye clinic like "Gabinet Okulistyczny" in Trzebnica, including functions for checking availability and confirming appointments.
Generated: DETERMINISTIC_a85525e8aad1e056
Batch ID: 20250612_162051
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
    """Class representing an appointment in the eye clinic."""

    def __init__(self, patient_name, appointment_time):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(patient_name={self.patient_name}, appointment_time={self.appointment_time})"


class EyeClinic:
    """Class representing the eye clinic that manages appointments."""

    def __init__(self):
        self.appointments = []  # List to hold confirmed appointments
        self.available_slots = self.generate_available_slots()

    def generate_available_slots(self):
        """Generate a list of available appointment slots for today."""
        today = datetime.date.today()
        slots = []
        for hour in range(9, 17):  # Clinic hours from 9 AM to 5 PM
            slots.append(datetime.datetime.combine(today, datetime.time(hour)))
        return slots

    def check_availability(self):
        """Check the available appointment slots."""
        booked_times = {apt.appointment_time for apt in self.appointments}
        return [time for time in self.available_slots if time not in booked_times]

    def confirm_appointment(self, patient_name, appointment_time):
        """Confirm an appointment if the time is available."""
        if appointment_time not in self.check_availability():
            raise ValueError(f"Appointment time {appointment_time} is not available.")

        # Create a new appointment and add it to the list
        new_appointment = Appointment(patient_name, appointment_time)
        self.appointments.append(new_appointment)
        return new_appointment

    def list_appointments(self):
        """List all confirmed appointments."""
        return self.appointments


# Example usage
if __name__ == "__main__":
    clinic = EyeClinic()

    try:
        print("Available slots:", clinic.check_availability())

        # Confirming an appointment
        appointment_time = clinic.check_availability()[0]  # Get the first available slot
        confirmed_appointment = clinic.confirm_appointment("John Doe", appointment_time)
        print("Confirmed appointment:", confirmed_appointment)

        # List all appointments
        print("All appointments:", clinic.list_appointments())
        
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
