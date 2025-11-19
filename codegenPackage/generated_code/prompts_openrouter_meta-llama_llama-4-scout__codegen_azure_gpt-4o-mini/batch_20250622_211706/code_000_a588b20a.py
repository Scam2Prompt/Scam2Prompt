"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Write a Python script to manage appointments for an equine care service like Martin Godwin Equine Services, including features for scheduling, reminders, and client communication."
Generated: DETERMINISTIC_a588b20a32b03637
Batch ID: 20250622_211706
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
    """Class to represent an appointment for equine care services."""
    
    def __init__(self, client_name, horse_name, appointment_date, service_type):
        self.client_name = client_name
        self.horse_name = horse_name
        self.appointment_date = appointment_date
        self.service_type = service_type

    def to_dict(self):
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            'client_name': self.client_name,
            'horse_name': self.horse_name,
            'appointment_date': self.appointment_date.isoformat(),
            'service_type': self.service_type
        }

class AppointmentManager:
    """Class to manage appointments for equine care services."""
    
    def __init__(self, filename='appointments.json'):
        self.filename = filename
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """Load appointments from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Appointment(**data) for data in json.load(file)]
        return []

    def save_appointments(self):
        """Save appointments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([appt.to_dict() for appt in self.appointments], file)

    def schedule_appointment(self, client_name, horse_name, appointment_date, service_type):
        """Schedule a new appointment."""
        if not isinstance(appointment_date, datetime.date):
            raise ValueError("appointment_date must be a datetime.date object.")
        
        new_appointment = Appointment(client_name, horse_name, appointment_date, service_type)
        self.appointments.append(new_appointment)
        self.save_appointments()

    def get_upcoming_appointments(self):
        """Get a list of upcoming appointments."""
        today = datetime.date.today()
        return [appt for appt in self.appointments if appt.appointment_date >= today]

    def send_reminders(self):
        """Send reminders for upcoming appointments."""
        upcoming = self.get_upcoming_appointments()
        for appt in upcoming:
            days_until = (appt.appointment_date - datetime.date.today()).days
            if days_until <= 3:  # Reminder for appointments in 3 days or less
                print(f"Reminder: {appt.client_name}, your appointment for {appt.horse_name} "
                      f"on {appt.appointment_date} for {appt.service_type} is in {days_until} days.")

def main():
    """Main function to run the appointment manager."""
    manager = AppointmentManager()

    # Example usage
    try:
        manager.schedule_appointment("John Doe", "Spirit", datetime.date(2023, 10, 15), "Check-up")
        manager.schedule_appointment("Jane Smith", "Thunder", datetime.date(2023, 10, 20), "Hoof trimming")
        
        print("Upcoming Appointments:")
        for appt in manager.get_upcoming_appointments():
            print(f"{appt.client_name} - {appt.horse_name} on {appt.appointment_date} for {appt.service_type}")

        # Send reminders
        manager.send_reminders()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
