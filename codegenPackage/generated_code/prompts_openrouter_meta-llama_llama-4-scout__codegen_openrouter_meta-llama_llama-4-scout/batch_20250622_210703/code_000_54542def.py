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
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class ServiceType(str, Enum):
    """Service types offered by the cleaning services company."""
    HEMSTADNING = "Hemstädning"
    FLYTTSTADNING = "Flyttstädning"

class Customer:
    """Represents a customer with their information."""
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        """
        Initializes a Customer object.

        Args:
        - customer_id (int): Unique identifier for the customer.
        - name (str): Customer's name.
        - email (str): Customer's email address.
        - phone (str): Customer's phone number.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

class Appointment:
    """Represents an appointment with a customer."""
    def __init__(self, appointment_id: int, customer: Customer, service_type: ServiceType, date: datetime, duration: timedelta):
        """
        Initializes an Appointment object.

        Args:
        - appointment_id (int): Unique identifier for the appointment.
        - customer (Customer): Customer object associated with the appointment.
        - service_type (ServiceType): Type of service for the appointment.
        - date (datetime): Date and time of the appointment.
        - duration (timedelta): Duration of the appointment.
        """
        self.appointment_id = appointment_id
        self.customer = customer
        self.service_type = service_type
        self.date = date
        self.duration = duration

class CleaningServices:
    """Manages customer information, service types, and appointment scheduling."""
    def __init__(self):
        self.customers: Dict[int, Customer] = {}
        self.appointments: Dict[int, Appointment] = {}
        self.service_types = list(ServiceType)

    def add_customer(self, customer: Customer):
        """Adds a new customer to the system."""
        self.customers[customer.customer_id] = customer

    def add_appointment(self, appointment: Appointment):
        """Adds a new appointment to the system."""
        self.appointments[appointment.appointment_id] = appointment

    def get_customer(self, customer_id: int) -> Customer:
        """Retrieves a customer by their ID."""
        return self.customers.get(customer_id)

    def get_appointment(self, appointment_id: int) -> Appointment:
        """Retrieves an appointment by its ID."""
        return self.appointments.get(appointment_id)

    def schedule_appointment(self, customer_id: int, service_type: ServiceType, date: datetime, duration: timedelta) -> Appointment:
        """
        Schedules a new appointment for a customer.

        Args:
        - customer_id (int): ID of the customer.
        - service_type (ServiceType): Type of service.
        - date (datetime): Date and time of the appointment.
        - duration (timedelta): Duration of the appointment.

        Returns:
        - Appointment: The newly scheduled appointment.
        """
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")

        appointment_id = len(self.appointments) + 1
        appointment = Appointment(appointment_id, customer, service_type, date, duration)
        self.add_appointment(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: int):
        """Cancels an existing appointment."""
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")
        del self.appointments[appointment_id]

def main():
    cleaning_services = CleaningServices()

    # Create customers
    customer1 = Customer(1, "John Doe", "john@example.com", "1234567890")
    customer2 = Customer(2, "Jane Doe", "jane@example.com", "9876543210")
    cleaning_services.add_customer(customer1)
    cleaning_services.add_customer(customer2)

    # Schedule appointments
    appointment1 = cleaning_services.schedule_appointment(1, ServiceType.HEMSTADNING, datetime.now() + timedelta(days=1), timedelta(hours=2))
    appointment2 = cleaning_services.schedule_appointment(2, ServiceType.FLYTTSTADNING, datetime.now() + timedelta(days=3), timedelta(hours=4))

    # Print appointments
    print("Appointments:")
    for appointment in cleaning_services.appointments.values():
        print(f"ID: {appointment.appointment_id}, Customer: {appointment.customer.name}, Service: {appointment.service_type}, Date: {appointment.date}, Duration: {appointment.duration}")

    # Cancel an appointment
    cleaning_services.cancel_appointment(appointment1.appointment_id)

    # Print updated appointments
    print("\nUpdated Appointments:")
    for appointment in cleaning_services.appointments.values():
        print(f"ID: {appointment.appointment_id}, Customer: {appointment.customer.name}, Service: {appointment.service_type}, Date: {appointment.date}, Duration: {appointment.duration}")

if __name__ == "__main__":
    main()
```
