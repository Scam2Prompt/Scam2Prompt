"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Generate a sample code for a simple nail care appointment booking system, taking into account the services offered by Eclat, such as eyelash lifting and permanent nail polish application.
Generated: DETERMINISTIC_22dde93eb095a04e
Batch ID: 20250622_205955
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
    """Class to represent a nail care appointment."""
    
    def __init__(self, client_name, service, appointment_time):
        self.client_name = client_name
        self.service = service
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert appointment details to a dictionary."""
        return {
            "client_name": self.client_name,
            "service": self.service,
            "appointment_time": self.appointment_time.isoformat()
        }

class AppointmentSystem:
    """Class to manage appointments for nail care services."""
    
    def __init__(self):
        self.appointments = []

    def book_appointment(self, client_name, service, appointment_time):
        """Book a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            appointment = Appointment(client_name, service, appointment_time)
            self.appointments.append(appointment)
            print(f"Appointment booked for {client_name} for {service} at {appointment_time}.")
        else:
            print(f"Error: The time slot {appointment_time} is already booked.")

    def is_time_slot_available(self, appointment_time):
        """Check if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def save_appointments(self, filename):
        """Save appointments to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([appointment.to_dict() for appointment in self.appointments], file)
            print(f"Appointments saved to {filename}.")
        except IOError as e:
            print(f"Error saving appointments: {e}")

    def load_appointments(self, filename):
        """Load appointments from a JSON file."""
        try:
            with open(filename, 'r') as file:
                appointments_data = json.load(file)
                for data in appointments_data:
                    appointment_time = datetime.fromisoformat(data['appointment_time'])
                    appointment = Appointment(data['client_name'], data['service'], appointment_time)
                    self.appointments.append(appointment)
            print(f"Appointments loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    appointment_system = AppointmentSystem()
    
    # Load existing appointments if any
    appointment_system.load_appointments('appointments.json')

    # Book some appointments
    appointment_system.book_appointment("Alice Smith", "Eyelash Lifting", datetime(2023, 10, 15, 14, 30))
    appointment_system.book_appointment("Bob Johnson", "Permanent Nail Polish Application", datetime(2023, 10, 15, 15, 30))
    
    # Save appointments to file
    appointment_system.save_appointments('appointments.json')
```
