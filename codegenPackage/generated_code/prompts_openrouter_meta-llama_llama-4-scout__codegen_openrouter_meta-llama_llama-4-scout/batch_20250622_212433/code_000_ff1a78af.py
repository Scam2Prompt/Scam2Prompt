"""
Generated Code Metadata:
========================
Original URL: https://skinport.in
Prompt: Write a Python script to manage appointments for a laser hair removal clinic with multiple locations in cities like Surat, Jaipur, and Delhi.
Generated: DETERMINISTIC_ff1a78afec1b6880
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# appointment_manager.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class City(Enum):
    """Enum for clinic locations"""
    SURAT = "Surat"
    JAIPUR = "Jaipur"
    DELHI = "Delhi"

class Appointment:
    """Represents an appointment"""
    def __init__(self, id: int, city: City, date: datetime, time: str, client_name: str):
        self.id = id
        self.city = city
        self.date = date
        self.time = time
        self.client_name = client_name

class AppointmentManager:
    """Manages appointments for the laser hair removal clinic"""
    def __init__(self):
        self.appointments: Dict[int, Appointment] = {}
        self.next_id = 1

    def add_appointment(self, city: City, date: datetime, time: str, client_name: str) -> int:
        """Adds a new appointment"""
        try:
            appointment = Appointment(self.next_id, city, date, time, client_name)
            self.appointments[self.next_id] = appointment
            self.next_id += 1
            return appointment.id
        except Exception as e:
            print(f"Error adding appointment: {str(e)}")
            return None

    def cancel_appointment(self, appointment_id: int) -> bool:
        """Cancels an existing appointment"""
        try:
            if appointment_id in self.appointments:
                del self.appointments[appointment_id]
                return True
            else:
                print(f"Appointment {appointment_id} not found")
                return False
        except Exception as e:
            print(f"Error canceling appointment: {str(e)}")
            return False

    def get_appointments(self, city: City = None) -> List[Appointment]:
        """Gets all appointments, optionally filtered by city"""
        try:
            if city:
                return [appt for appt in self.appointments.values() if appt.city == city]
            else:
                return list(self.appointments.values())
        except Exception as e:
            print(f"Error getting appointments: {str(e)}")
            return []

def main():
    manager = AppointmentManager()

    # Add appointments
    appointment1_id = manager.add_appointment(City.SURAT, datetime(2024, 9, 17), "10:00 AM", "John Doe")
    appointment2_id = manager.add_appointment(City.JAIPUR, datetime(2024, 9, 18), "11:00 AM", "Jane Doe")
    appointment3_id = manager.add_appointment(City.DELHI, datetime(2024, 9, 19), "12:00 PM", "Bob Smith")

    # Get appointments
    print("All appointments:")
    for appointment in manager.get_appointments():
        print(f"ID: {appointment.id}, City: {appointment.city.value}, Date: {appointment.date.date()}, Time: {appointment.time}, Client: {appointment.client_name}")

    # Get appointments for a specific city
    print("\nAppointments in Surat:")
    for appointment in manager.get_appointments(City.SURAT):
        print(f"ID: {appointment.id}, City: {appointment.city.value}, Date: {appointment.date.date()}, Time: {appointment.time}, Client: {appointment.client_name}")

    # Cancel an appointment
    manager.cancel_appointment(appointment2_id)

    # Get appointments after cancellation
    print("\nAppointments after cancellation:")
    for appointment in manager.get_appointments():
        print(f"ID: {appointment.id}, City: {appointment.city.value}, Date: {appointment.date.date()}, Time: {appointment.time}, Client: {appointment.client_name}")

if __name__ == "__main__":
    main()
```
