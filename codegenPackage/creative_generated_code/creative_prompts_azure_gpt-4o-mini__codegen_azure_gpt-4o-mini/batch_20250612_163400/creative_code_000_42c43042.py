"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Generate a Python script to automate appointment scheduling at Jinling Hospital, incorporating their services and specialties like cardiology and neurology.
Generated: DETERMINISTIC_42c43042629ce5cd
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Constants for the hospital services and specialties
SERVICES = {
    "cardiology": ["Heart Check-up", "Echocardiogram", "Stress Test"],
    "neurology": ["Neurological Exam", "CT Scan", "EEG"],
}

# Appointment class to represent an appointment
class Appointment:
    def __init__(self, patient_name: str, service: str, specialty: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.service = service
        self.specialty = specialty
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment({self.patient_name}, {self.service}, {self.specialty}, {self.appointment_time})"

# Appointment Scheduler class to manage appointments
class AppointmentScheduler:
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, service: str, specialty: str, appointment_time: str) -> None:
        # Validate inputs
        if specialty not in SERVICES:
            raise ValueError(f"Specialty {specialty} is not available.")
        if service not in SERVICES[specialty]:
            raise ValueError(f"Service {service} is not offered under {specialty}.")
        
        # Parse the appointment time
        try:
            appointment_time = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Appointment time must be in 'YYYY-MM-DD HH:MM' format.")
        
        # Check for conflicts with existing appointments
        if any(app.appointment_time == appointment_time for app in self.appointments):
            raise ValueError("The selected appointment time is already taken.")

        # Create and store the appointment
        new_appointment = Appointment(patient_name, service, specialty, appointment_time)
        self.appointments.append(new_appointment)
        print(f"Appointment scheduled: {new_appointment}")

    def save_appointments(self, filename: str) -> None:
        # Save appointments to a JSON file
        try:
            with open(filename, 'w') as file:
                json.dump([app.__dict__ for app in self.appointments], file, default=str)
            print(f"Appointments saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving appointments: {e}")

    def load_appointments(self, filename: str) -> None:
        # Load appointments from a JSON file
        try:
            with open(filename, 'r') as file:
                appointments_data = json.load(file)
                self.appointments = [Appointment(**data) for data in appointments_data]
            print(f"Appointments loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading appointments: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    try:
        # Load existing appointments if available
        scheduler.load_appointments('appointments.json')

        # Schedule a new appointment
        scheduler.schedule_appointment("John Doe", "Heart Check-up", "cardiology", "2023-11-10 14:30")
        scheduler.schedule_appointment("Jane Smith", "Neurological Exam", "neurology", "2023-11-10 15:30")

        # Save appointments to file
        scheduler.save_appointments('appointments.json')
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
