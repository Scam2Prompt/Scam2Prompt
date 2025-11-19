"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Generate code for a scheduling system that manages 24-hour emergency plumbing services, similar to the rapid response model described on Limpieza de Tubos Costablanca's website.
Generated: DETERMINISTIC_a9708fb263a54982
Batch ID: 20250612_154909
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
    """Class to represent a plumbing service appointment."""
    
    def __init__(self, customer_name, service_time):
        self.customer_name = customer_name
        self.service_time = service_time

    def to_dict(self):
        """Convert appointment to dictionary for easy serialization."""
        return {
            'customer_name': self.customer_name,
            'service_time': self.service_time.isoformat()
        }

class SchedulingSystem:
    """Class to manage the scheduling of plumbing services."""
    
    def __init__(self):
        self.appointments = []

    def add_appointment(self, customer_name, service_time):
        """Add a new appointment if the time slot is available."""
        if not self.is_time_slot_available(service_time):
            raise ValueError("The requested time slot is not available.")
        
        appointment = Appointment(customer_name, service_time)
        self.appointments.append(appointment)
        return appointment

    def is_time_slot_available(self, service_time):
        """Check if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.service_time == service_time:
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
                    customer_name = data['customer_name']
                    service_time = datetime.fromisoformat(data['service_time'])
                    self.add_appointment(customer_name, service_time)
        except (IOError, ValueError) as e:
            print(f"Error loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    scheduling_system = SchedulingSystem()
    
    # Load existing appointments from a file
    scheduling_system.load_appointments('appointments.json')

    # Add a new appointment
    try:
        new_appointment = scheduling_system.add_appointment("John Doe", datetime.now() + timedelta(hours=1))
        print(f"Appointment scheduled for {new_appointment.customer_name} at {new_appointment.service_time}.")
    except ValueError as e:
        print(e)

    # Save appointments to a file
    scheduling_system.save_appointments('appointments.json')

    # Print all appointments
    print("Current appointments:")
    for appointment in scheduling_system.get_appointments():
        print(appointment)
```
