"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Write a Python script to manage scheduling for residential and commercial cleaning services, including features for recurring appointments and one-time deep cleaning, as described by Queen Bee Renzo ProtocolCleaning Services.
Generated: DETERMINISTIC_2b9e07018cd953e9
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Appointment:
    """Class to represent a cleaning appointment."""
    
    def __init__(self, client_name: str, appointment_date: datetime.datetime, is_recurring: bool, service_type: str):
        self.client_name = client_name
        self.appointment_date = appointment_date
        self.is_recurring = is_recurring
        self.service_type = service_type

    def __repr__(self):
        return f"Appointment(client_name={self.client_name}, appointment_date={self.appointment_date}, is_recurring={self.is_recurring}, service_type={self.service_type})"

class Scheduler:
    """Class to manage scheduling of cleaning appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def add_appointment(self, client_name: str, appointment_date: datetime.datetime, is_recurring: bool, service_type: str) -> None:
        """Add a new appointment to the schedule."""
        if not isinstance(appointment_date, datetime.datetime):
            raise ValueError("appointment_date must be a datetime object")
        
        if service_type not in ["one-time", "recurring"]:
            raise ValueError("service_type must be either 'one-time' or 'recurring'")
        
        appointment = Appointment(client_name, appointment_date, is_recurring, service_type)
        self.appointments.append(appointment)
        print(f"Added appointment: {appointment}")

    def remove_appointment(self, appointment: Appointment) -> None:
        """Remove an appointment from the schedule."""
        try:
            self.appointments.remove(appointment)
            print(f"Removed appointment: {appointment}")
        except ValueError:
            print("Error: Appointment not found in the schedule.")

    def get_appointments(self, date: Optional[datetime.date] = None) -> List[Appointment]:
        """Retrieve appointments for a specific date or all appointments if no date is provided."""
        if date:
            return [appt for appt in self.appointments if appt.appointment_date.date() == date]
        return self.appointments

    def display_schedule(self) -> None:
        """Display all scheduled appointments."""
        if not self.appointments:
            print("No appointments scheduled.")
            return
        
        print("Scheduled Appointments:")
        for appt in self.appointments:
            print(f"- {appt}")

def main():
    """Main function to run the scheduling system."""
    scheduler = Scheduler()
    
    # Example usage
    try:
        # Adding appointments
        scheduler.add_appointment("Alice Johnson", datetime.datetime(2023, 10, 15, 10, 0), False, "one-time")
        scheduler.add_appointment("Bob Smith", datetime.datetime(2023, 10, 16, 14, 0), True, "recurring")
        
        # Displaying the schedule
        scheduler.display_schedule()
        
        # Removing an appointment
        appointment_to_remove = scheduler.get_appointments()[0]
        scheduler.remove_appointment(appointment_to_remove)
        
        # Displaying the updated schedule
        scheduler.display_schedule()
        
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()
```
