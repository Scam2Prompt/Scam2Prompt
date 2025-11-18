"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Generate code for a scheduling system that manages 24-hour emergency plumbing services, similar to the rapid response model described on Limpieza de Tubos Costablanca's website.
Generated: DETERMINISTIC_a9708fb263a54982
Batch ID: 20250612_154909
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
import logging

# Configure logging for error handling and system events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Appointment:
    """Class to represent a plumbing service appointment."""

    def __init__(self, customer_name, service_type, appointment_time):
        """
        Initialize an appointment.

        :param customer_name: The name of the customer for the appointment.
        :param service_type: The type of plumbing service needed.
        :param appointment_time: The datetime object when the appointment is scheduled.
        """
        self.customer_name = customer_name
        self.service_type = service_type
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            'customer_name': self.customer_name,
            'service_type': self.service_type,
            'appointment_time': self.appointment_time.strftime('%Y-%m-%d %H:%M:%S'),
        }


class Scheduler:
    """Class to manage scheduling of plumbing appointments."""

    def __init__(self):
        """Initialize the scheduler with an empty list of appointments."""
        self.appointments = []

    def schedule_appointment(self, customer_name, service_type, appointment_time):
        """
        Schedule a new appointment.

        :param customer_name: Name of the customer requesting the service.
        :param service_type: Type of plumbing service requested.
        :param appointment_time: The time for the appointment.
        :return: Confirmation message or error message.
        """
        try:
            # Check if the appointment time is in the future
            if appointment_time < datetime.now():
                raise ValueError("Appointment time must be in the future.")

            # Check for overlapping appointments
            for appointment in self.appointments:
                if appointment.appointment_time == appointment_time:
                    raise ValueError("Appointment time is already booked.")

            # Create and store the new appointment
            new_appointment = Appointment(customer_name, service_type, appointment_time)
            self.appointments.append(new_appointment)
            logging.info(f"Scheduled appointment: {new_appointment.to_dict()}")
            return f"Appointment scheduled for {customer_name} on {appointment_time}."

        except Exception as e:
            logging.error(f"Error scheduling appointment: {e}")
            return str(e)

    def get_schedule(self):
        """Get a list of all scheduled appointments."""
        return [appointment.to_dict() for appointment in self.appointments]

    def save_schedule(self, filename='schedule.json'):
        """
        Save the current schedule to a JSON file.

        :param filename: Name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_schedule(), f, indent=4)
            logging.info(f"Schedule saved to {filename}.")
        except Exception as e:
            logging.error(f"Error saving schedule: {e}")


# Example usage of the Scheduler class
if __name__ == '__main__':
    scheduler = Scheduler()
    
    # Schedule a couple of appointments for demonstration
    tomorrow = datetime.now() + timedelta(days=1)
    print(scheduler.schedule_appointment("John Doe", "Leak Repair", tomorrow))
    
    # Attempt to schedule an appointment in the past
    past_time = datetime.now() - timedelta(days=1)
    print(scheduler.schedule_appointment("Jane Smith", "Pipe Installation", past_time))
    
    # Print all scheduled appointments
    print(scheduler.get_schedule())

    # Save the schedule to a file
    scheduler.save_schedule()
```
