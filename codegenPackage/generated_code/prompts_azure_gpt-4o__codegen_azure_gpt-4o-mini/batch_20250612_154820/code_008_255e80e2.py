"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement a virtual healthcare service booking system, inspired by the "MyClinic" feature mentioned for Irish Life Health members on the Health Insurance Shop website.
Generated: DETERMINISTIC_255e80e26482413f
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class Appointment:
    """Class representing a healthcare appointment."""
    
    def __init__(self, patient_name, doctor_name, appointment_time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert appointment details to a dictionary."""
        return {
            "patient_name": self.patient_name,
            "doctor_name": self.doctor_name,
            "appointment_time": self.appointment_time.isoformat()
        }

class BookingSystem:
    """Class to manage the booking of healthcare appointments."""
    
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient_name, doctor_name, appointment_time):
        """Book a new appointment if the time is available."""
        if self.is_time_available(appointment_time):
            appointment = Appointment(patient_name, doctor_name, appointment_time)
            self.appointments.append(appointment)
            return appointment
        else:
            raise ValueError("The selected time is not available.")

    def is_time_available(self, appointment_time):
        """Check if the requested appointment time is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def get_appointments(self):
        """Retrieve all booked appointments."""
        return [appointment.to_dict() for appointment in self.appointments]

    def save_appointments(self, filename):
        """Save appointments to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_appointments(), file, indent=4)
        except IOError as e:
            print(f"Error saving appointments: {e}")

    def load_appointments(self, filename):
        """Load appointments from a JSON file."""
        try:
            with open(filename, 'r') as file:
                appointments_data = json.load(file)
                for data in appointments_data:
                    appointment_time = datetime.fromisoformat(data['appointment_time'])
                    appointment = Appointment(data['patient_name'], data['doctor_name'], appointment_time)
                    self.appointments.append(appointment)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Load existing appointments from a file
    booking_system.load_appointments('appointments.json')

    # Book a new appointment
    try:
        new_appointment = booking_system.book_appointment(
            patient_name="John Doe",
            doctor_name="Dr. Smith",
            appointment_time=datetime.now() + timedelta(days=1)  # Book for tomorrow
        )
        print(f"Appointment booked: {new_appointment.to_dict()}")
    except ValueError as e:
        print(e)

    # Save appointments to a file
    booking_system.save_appointments('appointments.json')
```
