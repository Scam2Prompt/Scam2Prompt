"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a Python script to manage appointments for a mobile windscreen repair service in Melbourne, considering factors like customer location and technician availability.
Generated: DETERMINISTIC_aecae2205a047dfe
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# appointment_manager.py

import datetime
from typing import Dict, List

class Technician:
    """Represents a technician with their availability."""

    def __init__(self, name: str, availability: List[datetime.datetime]):
        """
        Initializes a Technician.

        Args:
        - name (str): The technician's name.
        - availability (List[datetime.datetime]): A list of available time slots.
        """
        self.name = name
        self.availability = availability

class Customer:
    """Represents a customer with their location."""

    def __init__(self, name: str, location: str):
        """
        Initializes a Customer.

        Args:
        - name (str): The customer's name.
        - location (str): The customer's location.
        """
        self.name = name
        self.location = location

class Appointment:
    """Represents an appointment with a customer and a technician."""

    def __init__(self, customer: Customer, technician: Technician, appointment_time: datetime.datetime):
        """
        Initializes an Appointment.

        Args:
        - customer (Customer): The customer.
        - technician (Technician): The technician.
        - appointment_time (datetime.datetime): The appointment time.
        """
        self.customer = customer
        self.technician = technician
        self.appointment_time = appointment_time

class AppointmentManager:
    """Manages appointments for a mobile windscreen repair service."""

    def __init__(self):
        self.technicians: Dict[str, Technician] = {}
        self.appointments: List[Appointment] = []

    def add_technician(self, name: str, availability: List[datetime.datetime]):
        """
        Adds a technician.

        Args:
        - name (str): The technician's name.
        - availability (List[datetime.datetime]): A list of available time slots.
        """
        self.technicians[name] = Technician(name, availability)

    def book_appointment(self, customer_name: str, customer_location: str, technician_name: str, appointment_time: datetime.datetime):
        """
        Books an appointment.

        Args:
        - customer_name (str): The customer's name.
        - customer_location (str): The customer's location.
        - technician_name (str): The technician's name.
        - appointment_time (datetime.datetime): The appointment time.

        Returns:
        - bool: Whether the appointment was booked successfully.
        """
        if technician_name not in self.technicians:
            print(f"Technician '{technician_name}' not found.")
            return False

        technician = self.technicians[technician_name]
        if appointment_time not in technician.availability:
            print(f"Technician '{technician_name}' is not available at {appointment_time}.")
            return False

        customer = Customer(customer_name, customer_location)
        appointment = Appointment(customer, technician, appointment_time)

        self.appointments.append(appointment)
        technician.availability.remove(appointment_time)
        print(f"Appointment booked for {customer_name} with {technician_name} at {appointment_time}.")
        return True

    def cancel_appointment(self, customer_name: str, appointment_time: datetime.datetime):
        """
        Cancels an appointment.

        Args:
        - customer_name (str): The customer's name.
        - appointment_time (datetime.datetime): The appointment time.

        Returns:
        - bool: Whether the appointment was cancelled successfully.
        """
        for appointment in self.appointments:
            if appointment.customer.name == customer_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                self.technicians[appointment.technician.name].availability.append(appointment_time)
                print(f"Appointment cancelled for {customer_name} at {appointment_time}.")
                return True
        print(f"No appointment found for {customer_name} at {appointment_time}.")
        return False

def main():
    manager = AppointmentManager()

    # Add technicians with their availability
    manager.add_technician("John", [
        datetime.datetime(2024, 9, 16, 9),
        datetime.datetime(2024, 9, 16, 10),
        datetime.datetime(2024, 9, 17, 9)
    ])
    manager.add_technician("Jane", [
        datetime.datetime(2024, 9, 16, 11),
        datetime.datetime(2024, 9, 17, 10),
        datetime.datetime(2024, 9, 18, 9)
    ])

    # Book appointments
    manager.book_appointment("Customer1", "Melbourne CBD", "John", datetime.datetime(2024, 9, 16, 9))
    manager.book_appointment("Customer2", "Melbourne CBD", "Jane", datetime.datetime(2024, 9, 16, 11))
    manager.book_appointment("Customer3", "Melbourne CBD", "John", datetime.datetime(2024, 9, 16, 10))

    # Cancel an appointment
    manager.cancel_appointment("Customer1", datetime.datetime(2024, 9, 16, 9))

if __name__ == "__main__":
    main()
```
