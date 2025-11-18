"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write Python code to create a scheduling system for mobile RV repair services within a 100-mile radius of Phoenix, Arizona, incorporating appointment booking and repair status tracking.
Generated: DETERMINISTIC_01d2b6ac90f6b88c
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Appointment:
    """Class representing an appointment for RV repair service."""
    
    def __init__(self, customer_name: str, service_date: datetime.date, details: str):
        self.customer_name = customer_name
        self.service_date = service_date
        self.details = details
        self.status = 'Scheduled'  # Initial status of the appointment

    def update_status(self, new_status: str):
        """Update the status of the appointment."""
        valid_statuses = ['Scheduled', 'In Progress', 'Completed', 'Cancelled']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid options: {valid_statuses}")

class Scheduler:
    """Scheduler class to manage RV repair appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, customer_name: str, service_date: datetime.date, details: str) -> Appointment:
        """Book a new appointment and return the appointment object."""
        if service_date < datetime.date.today():
            raise ValueError("Service date cannot be in the past.")
        
        appointment = Appointment(customer_name, service_date, details)
        self.appointments.append(appointment)
        return appointment

    def get_appointment(self, customer_name: str, service_date: datetime.date) -> Optional[Appointment]:
        """Retrieve a specific appointment by customer name and service date."""
        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.service_date == service_date:
                return appointment
        return None

    def list_appointments(self) -> List[Appointment]:
        """Return a list of all scheduled appointments."""
        return self.appointments

def main():
    """Main function to run the scheduling system."""
    scheduler = Scheduler()
    
    try:
        # Example of booking an appointment
        appointment = scheduler.book_appointment("John Doe", datetime.date(2023, 12, 1), "Roof repair")
        print(f"Appointment booked: {appointment.customer_name} on {appointment.service_date} - {appointment.details}")

        # Update the appointment status
        appointment.update_status("In Progress")
        print(f"Updated appointment status: {appointment.customer_name} - {appointment.status}")

        # List all appointments
        all_appointments = scheduler.list_appointments()
        for appt in all_appointments:
            print(f"{appt.customer_name} - {appt.service_date} - {appt.status}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
