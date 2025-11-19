"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Create a Python program to schedule and manage consultations for immigration law services, including support for Skype, phone, and in-person appointments.
Generated: DETERMINISTIC_042f32ce49be3dcf
Batch ID: 20250612_152924
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
from typing import List, Dict, Optional

class Appointment:
    """Class to represent an appointment for immigration law services."""
    
    def __init__(self, client_name: str, appointment_time: datetime.datetime, mode: str):
        self.client_name = client_name
        self.appointment_time = appointment_time
        self.mode = mode  # 'Skype', 'Phone', or 'In-Person'
    
    def to_dict(self) -> Dict:
        """Convert the appointment to a dictionary for easy serialization."""
        return {
            'client_name': self.client_name,
            'appointment_time': self.appointment_time.isoformat(),
            'mode': self.mode
        }

class ConsultationScheduler:
    """Class to manage scheduling and storing consultations."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []
    
    def schedule_appointment(self, client_name: str, appointment_time: datetime.datetime, mode: str) -> None:
        """Schedule a new appointment."""
        if mode not in ['Skype', 'Phone', 'In-Person']:
            raise ValueError("Mode must be 'Skype', 'Phone', or 'In-Person'.")
        
        if self.is_time_slot_taken(appointment_time):
            raise ValueError("The selected time slot is already taken.")
        
        appointment = Appointment(client_name, appointment_time, mode)
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {client_name} on {appointment_time} via {mode}.")
    
    def is_time_slot_taken(self, appointment_time: datetime.datetime) -> bool:
        """Check if the given time slot is already taken."""
        return any(appointment.appointment_time == appointment_time for appointment in self.appointments)
    
    def list_appointments(self) -> List[Dict]:
        """List all scheduled appointments."""
        return [appointment.to_dict() for appointment in self.appointments]
    
    def save_appointments(self, filename: str) -> None:
        """Save appointments to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_appointments(), file, indent=4)
            print(f"Appointments saved to {filename}.")
        except IOError as e:
            print(f"Error saving appointments: {e}")
    
    def load_appointments(self, filename: str) -> None:
        """Load appointments from a JSON file."""
        try:
            with open(filename, 'r') as file:
                appointments_data = json.load(file)
                for data in appointments_data:
                    appointment_time = datetime.datetime.fromisoformat(data['appointment_time'])
                    appointment = Appointment(data['client_name'], appointment_time, data['mode'])
                    self.appointments.append(appointment)
            print(f"Appointments loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    
    # Schedule some appointments
    try:
        scheduler.schedule_appointment("John Doe", datetime.datetime(2023, 10, 15, 14, 0), "Skype")
        scheduler.schedule_appointment("Jane Smith", datetime.datetime(2023, 10, 16, 10, 30), "Phone")
        scheduler.schedule_appointment("Alice Johnson", datetime.datetime(2023, 10, 17, 9, 0), "In-Person")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")
    
    # List all appointments
    print("Scheduled Appointments:")
    for appointment in scheduler.list_appointments():
        print(appointment)
    
    # Save appointments to a file
    scheduler.save_appointments("appointments.json")
    
    # Load appointments from a file
    scheduler.load_appointments("appointments.json")
```
