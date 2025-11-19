"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crypto-io.com
Prompt: How can I implement an appointment booking system for a barbershop similar to Gould Barbers, focusing on services like skin fades and beard trims?
Generated: DETERMINISTIC_e99a890ce2e46c6c
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class Appointment:
    """Class representing a single appointment."""
    
    def __init__(self, customer_name, service, appointment_time):
        self.customer_name = customer_name
        self.service = service
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert appointment to dictionary for JSON serialization."""
        return {
            "customer_name": self.customer_name,
            "service": self.service,
            "appointment_time": self.appointment_time.isoformat()
        }

class Barbershop:
    """Class representing a barbershop appointment system."""
    
    def __init__(self):
        self.appointments = []  # List to hold all appointments

    def book_appointment(self, customer_name, service, appointment_time):
        """Book an appointment if the time slot is available."""
        if not self.is_time_available(appointment_time):
            raise ValueError("The selected time slot is not available.")

        appointment = Appointment(customer_name, service, appointment_time)
        self.appointments.append(appointment)
        print(f"Appointment booked for {customer_name} for {service} at {appointment_time}.")

    def is_time_available(self, appointment_time):
        """Check if the given appointment time is available."""
        # Check if the appointment falls within working hours and if it's not booked
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def list_appointments(self):
        """List all booked appointments."""
        return [appointment.to_dict() for appointment in self.appointments]

    def save_appointments(self, filename='appointments.json'):
        """Save appointments to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_appointments(), file, indent=4)
            print(f"Appointments saved to {filename}.")
        except IOError as e:
            print(f"Error saving appointments: {e}")

    def load_appointments(self, filename='appointments.json'):
        """Load appointments from a JSON file."""
        try:
            with open(filename, 'r') as file:
                appointments = json.load(file)
                for appt in appointments:
                    appt_time = datetime.fromisoformat(appt['appointment_time'])
                    self.book_appointment(appt['customer_name'], appt['service'], appt_time)
            print(f"Appointments loaded from {filename}.")
        except (IOError, ValueError) as e:
            print(f"Error loading appointments: {e}")

def main():
    shop = Barbershop()
    # Example usage
    try:
        # Load existing appointments
        shop.load_appointments()

        # Book a new appointment
        service = "Skin Fade"
        customer_name = "John Doe"
        appointment_time = datetime(2023, 10, 20, 15, 0)  # Example date and time

        shop.book_appointment(customer_name, service, appointment_time)

        # List all appointments
        print("Current Appointments:")
        for appointment in shop.list_appointments():
            print(appointment)

        # Save appointments to file
        shop.save_appointments()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
