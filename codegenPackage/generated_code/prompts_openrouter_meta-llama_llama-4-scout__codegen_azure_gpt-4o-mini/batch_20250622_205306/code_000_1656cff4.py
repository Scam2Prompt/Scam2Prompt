"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and reminders, for a clinic like Studio Dentistico dott.ssa Vira Palazzo in Rome.
Generated: DETERMINISTIC_1656cff4b9bdc04c
Batch ID: 20250622_205306
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
from typing import List, Dict, Optional

class Appointment:
    """Class to represent a dental appointment."""
    
    def __init__(self, patient_name: str, appointment_time: datetime.datetime):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def to_dict(self) -> Dict:
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            'patient_name': self.patient_name,
            'appointment_time': self.appointment_time.isoformat()
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Appointment':
        """Create an Appointment instance from a dictionary."""
        return Appointment(
            patient_name=data['patient_name'],
            appointment_time=datetime.datetime.fromisoformat(data['appointment_time'])
        )

class AppointmentManager:
    """Class to manage appointments for the dental clinic."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.appointments: List[Appointment] = []
        self.load_appointments()

    def load_appointments(self) -> None:
        """Load appointments from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.appointments = [Appointment.from_dict(app) for app in data]

    def save_appointments(self) -> None:
        """Save appointments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([app.to_dict() for app in self.appointments], file)

    def schedule_appointment(self, patient_name: str, appointment_time: datetime.datetime) -> None:
        """Schedule a new appointment."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(patient_name, appointment_time)
            self.appointments.append(new_appointment)
            self.save_appointments()
            print(f"Appointment scheduled for {patient_name} at {appointment_time}.")
        else:
            print(f"Error: Time slot {appointment_time} is already booked.")

    def is_time_slot_available(self, appointment_time: datetime.datetime) -> bool:
        """Check if the given time slot is available."""
        return all(app.appointment_time != appointment_time for app in self.appointments)

    def get_upcoming_appointments(self) -> List[Appointment]:
        """Get a list of upcoming appointments."""
        now = datetime.datetime.now()
        return [app for app in self.appointments if app.appointment_time > now]

    def send_reminders(self) -> None:
        """Send reminders for upcoming appointments."""
        now = datetime.datetime.now()
        for app in self.get_upcoming_appointments():
            if app.appointment_time - now <= datetime.timedelta(days=1):
                print(f"Reminder: {app.patient_name}, you have an appointment on {app.appointment_time}.")

def main():
    """Main function to run the appointment manager."""
    manager = AppointmentManager('appointments.json')

    # Example usage
    try:
        # Schedule some appointments
        manager.schedule_appointment("John Doe", datetime.datetime(2023, 10, 25, 14, 30))
        manager.schedule_appointment("Jane Smith", datetime.datetime(2023, 10, 26, 9, 0))

        # Send reminders for upcoming appointments
        manager.send_reminders()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
