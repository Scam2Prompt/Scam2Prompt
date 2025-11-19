"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a Python script to schedule and manage appointments for a mobile fuel injector cleaning service, considering different types of vehicles such as cars, LPG, hybrid, and motorbikes.
Generated: DETERMINISTIC_e78a03cb71497c3c
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Appointment:
    """Class to represent an appointment for fuel injector cleaning."""
    
    def __init__(self, vehicle_type: str, customer_name: str, appointment_time: datetime.datetime):
        self.vehicle_type = vehicle_type
        self.customer_name = customer_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment({self.vehicle_type}, {self.customer_name}, {self.appointment_time})"


class AppointmentManager:
    """Class to manage appointments for the fuel injector cleaning service."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, vehicle_type: str, customer_name: str, appointment_time: datetime.datetime) -> None:
        """Schedules a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(vehicle_type, customer_name, appointment_time)
            self.appointments.append(new_appointment)
            print(f"Appointment scheduled: {new_appointment}")
        else:
            print(f"Error: Appointment time {appointment_time} is already booked.")

    def is_time_slot_available(self, appointment_time: datetime.datetime) -> bool:
        """Checks if the given time slot is available for scheduling."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def list_appointments(self) -> List[Dict[str, str]]:
        """Returns a list of all scheduled appointments."""
        return [{"vehicle_type": appt.vehicle_type, "customer_name": appt.customer_name, "appointment_time": appt.appointment_time} for appt in self.appointments]

    def cancel_appointment(self, appointment_time: datetime.datetime) -> Optional[Appointment]:
        """Cancels an appointment at the specified time, if it exists."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                print(f"Appointment canceled: {appointment}")
                return appointment
        print(f"Error: No appointment found at {appointment_time}.")
        return None


def main():
    """Main function to demonstrate the appointment management system."""
    manager = AppointmentManager()

    # Schedule some appointments
    try:
        manager.schedule_appointment("Car", "John Doe", datetime.datetime(2023, 10, 15, 10, 0))
        manager.schedule_appointment("LPG", "Jane Smith", datetime.datetime(2023, 10, 15, 11, 0))
        manager.schedule_appointment("Hybrid", "Alice Johnson", datetime.datetime(2023, 10, 15, 10, 0))  # This should fail
    except Exception as e:
        print(f"An error occurred: {e}")

    # List all appointments
    print("Current appointments:")
    for appointment in manager.list_appointments():
        print(appointment)

    # Cancel an appointment
    manager.cancel_appointment(datetime.datetime(2023, 10, 15, 10, 0))
    
    # List all appointments after cancellation
    print("Appointments after cancellation:")
    for appointment in manager.list_appointments():
        print(appointment)


if __name__ == "__main__":
    main()
```
