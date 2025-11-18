"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python script to simulate a plumbing service booking system for Certified Plumbers Graham, TX, including fields for service type (e.g., leak detection, repiping), customer details, and preferred appointment time.
Generated: DETERMINISTIC_1f4650e6e7052d67
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# plumbing_service.py

import datetime

class Appointment:
    """Class representing a plumbing service appointment."""

    def __init__(self, customer_name, service_type, appointment_time):
        """
        Initializes a new Appointment instance.

        Args:
            customer_name (str): The name of the customer.
            service_type (str): The type of plumbing service requested.
            appointment_time (datetime): The preferred time for the appointment.
        """
        self.customer_name = customer_name
        self.service_type = service_type
        self.appointment_time = appointment_time

    def __str__(self):
        """Return a string representation of the appointment."""
        return f"Appointment for {self.customer_name} | Service: {self.service_type} | Time: {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"

class PlumbingService:
    """Class to handle the plumbing service booking system."""

    def __init__(self):
        """Initializes an empty list to store appointments."""
        self.appointments = []

    def book_appointment(self, customer_name, service_type, appointment_time):
        """
        Books a new appointment.

        Args:
            customer_name (str): The name of the customer.
            service_type (str): The type of plumbing service requested.
            appointment_time (datetime): The preferred time for the appointment.

        Returns:
            str: Confirmation message if the appointment is booked successfully, else an error message.
        """
        if not self.is_valid_service_type(service_type):
            return "Error: Invalid service type."

        if appointment_time <= datetime.datetime.now():
            return "Error: Appointment time must be in the future."

        new_appointment = Appointment(customer_name, service_type, appointment_time)
        self.appointments.append(new_appointment)
        return f"Successfully booked: {new_appointment}"

    @staticmethod
    def is_valid_service_type(service_type):
        """Check if the service type is valid."""
        valid_services = ["leak detection", "repiping", "drain cleaning", "pipe installation"]
        return service_type in valid_services

    def list_appointments(self):
        """Lists all booked appointments."""
        if not self.appointments:
            return "No appointments booked."
        return "\n".join(str(appointment) for appointment in self.appointments)

def main():
    """Main function to run the plumbing service booking system."""
    service = PlumbingService()

    # Example of booking appointments (in production, this would likely come from user input)
    print(service.book_appointment("John Doe", "leak detection", datetime.datetime(2023, 10, 25, 14, 0)))
    print(service.book_appointment("Jane Smith", "repiping", datetime.datetime(2023, 10, 26, 10, 30)))
    print(service.book_appointment("Alice Johnson", "drain cleaning", datetime.datetime.now()))  # Should show an error

    # List all appointments
    print("\nScheduled Appointments:")
    print(service.list_appointments())

if __name__ == "__main__":
    main()
```
