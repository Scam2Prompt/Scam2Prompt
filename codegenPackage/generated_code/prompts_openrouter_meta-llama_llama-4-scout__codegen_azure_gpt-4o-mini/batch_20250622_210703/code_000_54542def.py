"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Write a Python script to manage booking and scheduling for a cleaning services company like Aspuddens Städservice, including customer information, service types (e.g., Hemstädning, Flyttstädning), and appointment scheduling.
Generated: DETERMINISTIC_54542defa8ce2452
Batch ID: 20250622_210703
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

class Customer:
    """Class to represent a customer."""
    
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Customer(name={self.name}, phone={self.phone}, email={self.email})"


class Service:
    """Class to represent a cleaning service."""
    
    def __init__(self, service_type: str, duration: int):
        self.service_type = service_type
        self.duration = duration  # Duration in minutes

    def __repr__(self):
        return f"Service(service_type={self.service_type}, duration={self.duration})"


class Appointment:
    """Class to represent a scheduled appointment."""
    
    def __init__(self, customer: Customer, service: Service, date_time: datetime.datetime):
        self.customer = customer
        self.service = service
        self.date_time = date_time

    def __repr__(self):
        return (f"Appointment(customer={self.customer}, "
                f"service={self.service}, date_time={self.date_time})")


class Scheduler:
    """Class to manage appointments for cleaning services."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, customer: Customer, service: Service, date_time: datetime.datetime) -> None:
        """Book a new appointment if the time slot is available."""
        if self.is_time_slot_available(date_time, service.duration):
            appointment = Appointment(customer, service, date_time)
            self.appointments.append(appointment)
            print(f"Appointment booked: {appointment}")
        else:
            print(f"Error: Time slot not available for {date_time}.")

    def is_time_slot_available(self, date_time: datetime.datetime, duration: int) -> bool:
        """Check if the time slot is available for the given duration."""
        end_time = date_time + datetime.timedelta(minutes=duration)
        for appointment in self.appointments:
            if (appointment.date_time < end_time and
                    date_time < appointment.date_time + datetime.timedelta(minutes=appointment.service.duration)):
                return False
        return True

    def list_appointments(self) -> List[Appointment]:
        """List all scheduled appointments."""
        return self.appointments


def main():
    """Main function to demonstrate the booking system."""
    # Create a scheduler instance
    scheduler = Scheduler()

    # Create some customers
    customer1 = Customer("Alice Smith", "123-456-7890", "alice@example.com")
    customer2 = Customer("Bob Johnson", "098-765-4321", "bob@example.com")

    # Create some services
    service1 = Service("Hemstädning", 120)  # 2 hours
    service2 = Service("Flyttstädning", 180)  # 3 hours

    # Book appointments
    try:
        scheduler.book_appointment(customer1, service1, datetime.datetime(2023, 10, 15, 10, 0))
        scheduler.book_appointment(customer2, service2, datetime.datetime(2023, 10, 15, 12, 0))
        scheduler.book_appointment(customer1, service2, datetime.datetime(2023, 10, 15, 11, 0))  # This should fail
    except Exception as e:
        print(f"An error occurred: {e}")

    # List all appointments
    print("\nScheduled Appointments:")
    for appointment in scheduler.list_appointments():
        print(appointment)


if __name__ == "__main__":
    main()
```
