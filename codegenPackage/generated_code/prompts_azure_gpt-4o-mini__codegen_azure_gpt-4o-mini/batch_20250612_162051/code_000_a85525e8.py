"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Generate a Python script that simulates an appointment booking system for an eye clinic like "Gabinet Okulistyczny" in Trzebnica, including functions for checking availability and confirming appointments.
Generated: DETERMINISTIC_a85525e8aad1e056
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Appointment:
    """Class to represent an appointment in the eye clinic."""
    
    def __init__(self, patient_name, appointment_time):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment for {self.patient_name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"

class EyeClinic:
    """Class to manage appointments in the eye clinic."""
    
    def __init__(self):
        self.appointments = []
        self.opening_hours = {
            'Monday': (9, 17),
            'Tuesday': (9, 17),
            'Wednesday': (9, 17),
            'Thursday': (9, 17),
            'Friday': (9, 17),
            'Saturday': (10, 14),
            'Sunday': None  # Closed on Sundays
        }

    def is_time_available(self, appointment_time):
        """Check if the requested appointment time is available."""
        # Check if the clinic is open on the requested day
        day_name = appointment_time.strftime('%A')
        if day_name not in self.opening_hours or self.opening_hours[day_name] is None:
            return False
        
        # Check if the time is within opening hours
        opening_hour, closing_hour = self.opening_hours[day_name]
        if not (opening_hour <= appointment_time.hour < closing_hour):
            return False
        
        # Check if the time is already booked
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        
        return True

    def book_appointment(self, patient_name, appointment_time):
        """Book an appointment if the time is available."""
        if self.is_time_available(appointment_time):
            new_appointment = Appointment(patient_name, appointment_time)
            self.appointments.append(new_appointment)
            return new_appointment
        else:
            raise ValueError("The requested appointment time is not available.")

    def list_appointments(self):
        """List all booked appointments."""
        if not self.appointments:
            return "No appointments booked."
        return "\n".join(str(appointment) for appointment in self.appointments)

def main():
    """Main function to run the appointment booking system."""
    clinic = EyeClinic()
    
    # Example usage
    try:
        # Booking an appointment
        appointment_time = datetime.datetime(2023, 10, 25, 10, 30)  # Example date and time
        appointment = clinic.book_appointment("John Doe", appointment_time)
        print(f"Successfully booked: {appointment}")

        # Listing all appointments
        print("\nCurrent Appointments:")
        print(clinic.list_appointments())

        # Attempting to book another appointment at the same time
        another_appointment = clinic.book_appointment("Jane Smith", appointment_time)
        print(f"Successfully booked: {another_appointment}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
