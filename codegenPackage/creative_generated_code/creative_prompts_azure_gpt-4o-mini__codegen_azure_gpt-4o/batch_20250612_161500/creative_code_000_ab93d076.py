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
    """
    Represents a dental appointment.
    """
    def __init__(self, patient_name, location, date, time):
        self.patient_name = patient_name
        self.location = location
        self.date = date
        self.time = time

    def __str__(self):
        """
        String representation of the appointment.
        """
        return f"Appointment for {self.patient_name} at {self.location} on {self.date} at {self.time}"


class DentalClinic:
    """
    Represents a dental clinic with multiple locations.
    """
    def __init__(self, locations):
        # Ensure the locations are provided as a list of strings
        if not isinstance(locations, list) or not all(isinstance(loc, str) for loc in locations):
            raise ValueError("Locations must be a list of strings")
        self.locations = locations
        self.appointments = []

    def schedule_appointment(self, patient_name, location, date, time):
        """
        Schedules a new appointment for a patient.
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location. Available locations: {', '.join(self.locations)}")

        try:
            # Validate date and time format
            formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            formatted_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError as e:
            raise ValueError(f"Invalid date or time format: {e}")

        # Create a new appointment
        new_appointment = Appointment(patient_name, location, formatted_date, formatted_time)
        self.appointments.append(new_appointment)
        print(f"Appointment successfully scheduled: {new_appointment}")

    def list_appointments(self):
        """
        Lists all scheduled appointments.
        """
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def cancel_appointment(self, patient_name, location, date, time):
        """
        Cancels an existing appointment.
        """
        try:
            # Validate date and time format
            formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            formatted_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError as e:
            raise ValueError(f"Invalid date or time format: {e}")

        # Search for and remove the appointment
        for appointment in self.appointments:
            if (appointment.patient_name == patient_name and appointment.location == location and
                    appointment.date == formatted_date and appointment.time == formatted_time):
                self.appointments.remove(appointment)
                print(f"Appointment successfully canceled: {appointment}")
                return

        print("No matching appointment found to cancel.")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize clinic with multiple locations
        clinic = DentalClinic(["Austin", "Dallas", "San Antonio"])

        # Schedule appointments
        clinic.schedule_appointment("John Doe", "Austin", "2023-10-25", "09:30")
        clinic.schedule_appointment("Jane Smith", "Dallas", "2023-10-26", "14:00")

        # List appointments
        clinic.list_appointments()

        # Cancel an appointment
        clinic.cancel_appointment("John Doe", "Austin", "2023-10-25", "09:30")

        # List appointments after cancellation
        clinic.list_appointments()

    except Exception as e:
        print(f"Error: {e}")
```
