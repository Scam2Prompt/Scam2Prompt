"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Write a Python script to manage plumbing services appointments for a company like Deep Book Online, including scheduling, customer information, and service type.
Generated: DETERMINISTIC_ded9784d0eb1cab3
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plumbing_services.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class ServiceType(str, Enum):
    """Service types offered by the company."""
    LEAK_DETECTION = "Leak Detection"
    PIPE_REPAIR = "Pipe Repair"
    DRAIN_CLEANING = "Drain Cleaning"
    OTHER = "Other"

class Customer:
    """Represents a customer."""
    def __init__(self, name: str, phone_number: str, email: str):
        """
        Initializes a Customer object.

        Args:
        - name (str): Customer's name.
        - phone_number (str): Customer's phone number.
        - email (str): Customer's email.
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email

class Appointment:
    """Represents a plumbing services appointment."""
    def __init__(self, customer: Customer, service_type: ServiceType, date: str, time: str):
        """
        Initializes an Appointment object.

        Args:
        - customer (Customer): Customer object.
        - service_type (ServiceType): Type of service.
        - date (str): Date of appointment (YYYY-MM-DD).
        - time (str): Time of appointment (HH:MM).
        """
        self.customer = customer
        self.service_type = service_type
        self.date = date
        self.time = time

class PlumbingServices:
    """Manages plumbing services appointments."""
    def __init__(self):
        self.appointments: Dict[str, Appointment] = {}

    def schedule_appointment(self, appointment_id: str, customer: Customer, service_type: ServiceType, date: str, time: str):
        """
        Schedules a new appointment.

        Args:
        - appointment_id (str): Unique appointment ID.
        - customer (Customer): Customer object.
        - service_type (ServiceType): Type of service.
        - date (str): Date of appointment (YYYY-MM-DD).
        - time (str): Time of appointment (HH:MM).

        Raises:
        - ValueError: If appointment ID already exists.
        """
        if appointment_id in self.appointments:
            raise ValueError("Appointment ID already exists.")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format.")

        self.appointments[appointment_id] = Appointment(customer, service_type, date, time)

    def get_appointment(self, appointment_id: str) -> Appointment:
        """
        Retrieves an appointment by ID.

        Args:
        - appointment_id (str): Unique appointment ID.

        Returns:
        - Appointment: Appointment object if found, otherwise None.
        """
        return self.appointments.get(appointment_id)

    def update_appointment(self, appointment_id: str, customer: Customer = None, service_type: ServiceType = None, date: str = None, time: str = None):
        """
        Updates an existing appointment.

        Args:
        - appointment_id (str): Unique appointment ID.
        - customer (Customer, optional): Updated customer object. Defaults to None.
        - service_type (ServiceType, optional): Updated service type. Defaults to None.
        - date (str, optional): Updated date of appointment (YYYY-MM-DD). Defaults to None.
        - time (str, optional): Updated time of appointment (HH:MM). Defaults to None.

        Raises:
        - ValueError: If appointment ID does not exist.
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment ID does not exist.")

        appointment = self.appointments[appointment_id]

        if customer:
            appointment.customer = customer
        if service_type:
            appointment.service_type = service_type
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format.")
            appointment.date = date
        if time:
            try:
                datetime.strptime(time, "%H:%M")
            except ValueError:
                raise ValueError("Invalid time format.")
            appointment.time = time

    def delete_appointment(self, appointment_id: str):
        """
        Deletes an appointment by ID.

        Args:
        - appointment_id (str): Unique appointment ID.

        Raises:
        - ValueError: If appointment ID does not exist.
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment ID does not exist.")

        del self.appointments[appointment_id]

def main():
    plumbing_services = PlumbingServices()

    # Create customers
    customer1 = Customer("John Doe", "123-456-7890", "john.doe@example.com")
    customer2 = Customer("Jane Doe", "987-654-3210", "jane.doe@example.com")

    # Schedule appointments
    plumbing_services.schedule_appointment("appointment1", customer1, ServiceType.LEAK_DETECTION, "2024-09-16", "10:00")
    plumbing_services.schedule_appointment("appointment2", customer2, ServiceType.PIPE_REPAIR, "2024-09-17", "11:00")

    # Retrieve appointment
    appointment = plumbing_services.get_appointment("appointment1")
    if appointment:
        print(f"Appointment ID: appointment1")
        print(f"Customer: {appointment.customer.name}")
        print(f"Service Type: {appointment.service_type.value}")
        print(f"Date: {appointment.date}")
        print(f"Time: {appointment.time}")
    else:
        print("Appointment not found.")

    # Update appointment
    plumbing_services.update_appointment("appointment1", date="2024-09-18")

    # Retrieve updated appointment
    appointment = plumbing_services.get_appointment("appointment1")
    if appointment:
        print(f"Updated Appointment ID: appointment1")
        print(f"Customer: {appointment.customer.name}")
        print(f"Service Type: {appointment.service_type.value}")
        print(f"Date: {appointment.date}")
        print(f"Time: {appointment.time}")
    else:
        print("Appointment not found.")

    # Delete appointment
    plumbing_services.delete_appointment("appointment2")

if __name__ == "__main__":
    main()
```
