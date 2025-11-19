"""
Generated Code Metadata:
========================
Original URL: https://www.albertozofrea.it
Prompt: Write a Python script to manage client appointments for a Shiatsu therapy practice, including scheduling and reminder features.
Generated: DETERMINISTIC_d0b6887a92eaadcb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class Appointment:
    """Class to represent a client appointment."""
    
    def __init__(self, client_name, appointment_time):
        self.client_name = client_name
        self.appointment_time = appointment_time

    def to_dict(self):
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            'client_name': self.client_name,
            'appointment_time': self.appointment_time.isoformat()
        }

    @staticmethod
    def from_dict(data):
        """Create an Appointment instance from a dictionary."""
        client_name = data['client_name']
        appointment_time = datetime.datetime.fromisoformat(data['appointment_time'])
        return Appointment(client_name, appointment_time)

class AppointmentManager:
    """Class to manage appointments for the Shiatsu therapy practice."""
    
    def __init__(self, filename='appointments.json'):
        self.filename = filename
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """Load appointments from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Appointment.from_dict(item) for item in data]
        return []

    def save_appointments(self):
        """Save appointments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([appt.to_dict() for appt in self.appointments], file)

    def schedule_appointment(self, client_name, appointment_time):
        """Schedule a new appointment."""
        if self.is_time_slot_taken(appointment_time):
            raise ValueError("The selected time slot is already taken.")
        new_appointment = Appointment(client_name, appointment_time)
        self.appointments.append(new_appointment)
        self.save_appointments()

    def is_time_slot_taken(self, appointment_time):
        """Check if the given time slot is already taken."""
        return any(appt.appointment_time == appointment_time for appt in self.appointments)

    def get_upcoming_appointments(self):
        """Get a list of upcoming appointments."""
        now = datetime.datetime.now()
        return [appt for appt in self.appointments if appt.appointment_time > now]

    def send_reminders(self):
        """Send reminders for upcoming appointments."""
        now = datetime.datetime.now()
        for appt in self.get_upcoming_appointments():
            if appt.appointment_time - now <= datetime.timedelta(days=1):
                print(f"Reminder: {appt.client_name}, you have an appointment on {appt.appointment_time}.")

def main():
    """Main function to run the appointment manager."""
    manager = AppointmentManager()

    # Example usage
    try:
        # Schedule an appointment
        client_name = "John Doe"
        appointment_time = datetime.datetime(2023, 10, 25, 15, 0)  # Example date and time
        manager.schedule_appointment(client_name, appointment_time)

        # Send reminders
        manager.send_reminders()

        # List upcoming appointments
        upcoming = manager.get_upcoming_appointments()
        print("Upcoming appointments:")
        for appt in upcoming:
            print(f"{appt.client_name} at {appt.appointment_time}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
