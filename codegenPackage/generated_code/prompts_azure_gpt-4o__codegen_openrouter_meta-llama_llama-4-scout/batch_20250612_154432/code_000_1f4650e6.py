"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python script to simulate a plumbing service booking system for Certified Plumbers Graham, TX, including fields for service type (e.g., leak detection, repiping), customer details, and preferred appointment time.
Generated: DETERMINISTIC_1f4650e6e7052d67
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime

# Define an Enum for service types
class ServiceType(Enum):
    LEAK_DETECTION = "Leak Detection"
    REPIPING = "Repiping"
    DRAIN_CLEANING = "Drain Cleaning"
    PLUMBING_REPAIR = "Plumbing Repair"
    OTHER = "Other"

# Define a class for Customer
class Customer:
    def __init__(self, name, phone_number, email):
        """
        Initialize a Customer object.

        Args:
            name (str): Customer name
            phone_number (str): Customer phone number
            email (str): Customer email
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email

# Define a class for Appointment
class Appointment:
    def __init__(self, service_type, customer, preferred_time):
        """
        Initialize an Appointment object.

        Args:
            service_type (ServiceType): Type of service
            customer (Customer): Customer details
            preferred_time (datetime): Preferred appointment time
        """
        self.service_type = service_type
        self.customer = customer
        self.preferred_time = preferred_time

# Define a class for PlumbingService
class PlumbingService:
    def __init__(self):
        """
        Initialize a PlumbingService object.
        """
        self.appointments = []

    def book_appointment(self, service_type, customer, preferred_time):
        """
        Book a new appointment.

        Args:
            service_type (ServiceType): Type of service
            customer (Customer): Customer details
            preferred_time (datetime): Preferred appointment time

        Raises:
            ValueError: If service type is invalid
        """
        if not isinstance(service_type, ServiceType):
            raise ValueError("Invalid service type")

        appointment = Appointment(service_type, customer, preferred_time)
        self.appointments.append(appointment)
        return appointment

    def view_appointments(self):
        """
        View all booked appointments.

        Returns:
            list: List of Appointment objects
        """
        return self.appointments

def main():
    # Create a PlumbingService object
    plumbing_service = PlumbingService()

    # Get customer details
    name = input("Enter customer name: ")
    phone_number = input("Enter customer phone number: ")
    email = input("Enter customer email: ")
    customer = Customer(name, phone_number, email)

    # Get service type
    print("Available service types:")
    for i, service_type in enumerate(ServiceType):
        print(f"{i+1}. {service_type.value}")
    choice = int(input("Enter the number of your chosen service type: "))
    service_type = list(ServiceType)[choice - 1]

    # Get preferred appointment time
    preferred_time_input = input("Enter preferred appointment time (YYYY-MM-DD HH:MM): ")
    preferred_time = datetime.strptime(preferred_time_input, "%Y-%m-%d %H:%M")

    try:
        # Book appointment
        appointment = plumbing_service.book_appointment(service_type, customer, preferred_time)
        print("Appointment booked successfully!")
        print(f"Service Type: {appointment.service_type.value}")
        print(f"Customer Name: {appointment.customer.name}")
        print(f"Customer Phone Number: {appointment.customer.phone_number}")
        print(f"Customer Email: {appointment.customer.email}")
        print(f"Preferred Time: {appointment.preferred_time.strftime('%Y-%m-%d %H:%M')}")
    except ValueError as e:
        print(f"Error: {e}")

    # View all appointments
    appointments = plumbing_service.view_appointments()
    print("\nBooked Appointments:")
    for i, appointment in enumerate(appointments):
        print(f"Appointment {i+1}:")
        print(f"Service Type: {appointment.service_type.value}")
        print(f"Customer Name: {appointment.customer.name}")
        print(f"Customer Phone Number: {appointment.customer.phone_number}")
        print(f"Customer Email: {appointment.customer.email}")
        print(f"Preferred Time: {appointment.preferred_time.strftime('%Y-%m-%d %H:%M')}")
        print()

if __name__ == "__main__":
    main()
```
