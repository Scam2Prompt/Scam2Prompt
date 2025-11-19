"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: How would you implement a scheduling system for emergency services, like those provided by SOS Menuiserie, using a programming language of your choice?
Generated: DETERMINISTIC_05a25d55c02687fe
Batch ID: 20250622_210650
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
    """Class to represent an appointment for emergency services."""
    
    def __init__(self, service_type, customer_name, appointment_time):
        self.service_type = service_type
        self.customer_name = customer_name
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            "service_type": self.service_type,
            "customer_name": self.customer_name,
            "appointment_time": self.appointment_time.isoformat()
        }

class Scheduler:
    """Class to manage scheduling of appointments for emergency services."""
    
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, service_type, customer_name, appointment_time):
        """Schedule a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            appointment = Appointment(service_type, customer_name, appointment_time)
            self.appointments.append(appointment)
            return appointment
        else:
            raise ValueError("The requested time slot is not available.")

    def is_time_slot_available(self, appointment_time):
        """Check if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def get_appointments(self):
        """Return a list of all scheduled appointments."""
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
                    appointment = Appointment(data['service_type'], data['customer_name'], appointment_time)
                    self.appointments.append(appointment)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Load existing appointments from a file
    scheduler.load_appointments('appointments.json')

    # Schedule a new appointment
    try:
        new_appointment = scheduler.schedule_appointment(
            service_type="Emergency Repair",
            customer_name="John Doe",
            appointment_time=datetime.now() + timedelta(days=1)  # Schedule for tomorrow
        )
        print(f"Scheduled appointment: {new_appointment.to_dict()}")
    except ValueError as e:
        print(e)

    # Save appointments to a file
    scheduler.save_appointments('appointments.json')
```
