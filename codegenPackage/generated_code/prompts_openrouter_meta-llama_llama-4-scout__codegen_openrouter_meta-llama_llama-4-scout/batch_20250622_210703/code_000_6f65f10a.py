"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Write a Python code snippet to manage a beauty salon's appointment scheduling system, considering various services like hair coloring, cutting, and styling.
Generated: DETERMINISTIC_6f65f10a416766f1
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

class ServiceType(Enum):
    """Enum for different service types"""
    HAIR_COLORING = 1
    HAIR_CUTTING = 2
    HAIR_STYLING = 3

class Service:
    """Class representing a service"""
    def __init__(self, service_type, duration):
        """
        Initialize a Service object

        Args:
            service_type (ServiceType): Type of service
            duration (int): Duration of service in minutes
        """
        self.service_type = service_type
        self.duration = duration

class Appointment:
    """Class representing an appointment"""
    def __init__(self, customer_name, service, appointment_time):
        """
        Initialize an Appointment object

        Args:
            customer_name (str): Name of the customer
            service (Service): Service object
            appointment_time (datetime): Time of appointment
        """
        self.customer_name = customer_name
        self.service = service
        self.appointment_time = appointment_time

class BeautySalon:
    """Class representing a beauty salon"""
    def __init__(self):
        """Initialize a BeautySalon object"""
        self.appointments = []
        self.services = {
            ServiceType.HAIR_COLORING: Service(ServiceType.HAIR_COLORING, 60),
            ServiceType.HAIR_CUTTING: Service(ServiceType.HAIR_CUTTING, 30),
            ServiceType.HAIR_STYLING: Service(ServiceType.HAIR_STYLING, 45)
        }

    def schedule_appointment(self, customer_name, service_type, appointment_time):
        """
        Schedule an appointment

        Args:
            customer_name (str): Name of the customer
            service_type (ServiceType): Type of service
            appointment_time (datetime): Time of appointment

        Raises:
            ValueError: If service type is not valid
            Exception: If appointment time is not available
        """
        if service_type not in self.services:
            raise ValueError("Invalid service type")

        service = self.services[service_type]
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                raise Exception("Appointment time is not available")

        appointment = Appointment(customer_name, service, appointment_time)
        self.appointments.append(appointment)
        self.appointments.sort(key=lambda x: x.appointment_time)

    def cancel_appointment(self, customer_name, appointment_time):
        """
        Cancel an appointment

        Args:
            customer_name (str): Name of the customer
            appointment_time (datetime): Time of appointment

        Raises:
            Exception: If appointment not found
        """
        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return
        raise Exception("Appointment not found")

    def display_appointments(self):
        """Display all appointments"""
        for appointment in self.appointments:
            print(f"Customer Name: {appointment.customer_name}")
            print(f"Service Type: {appointment.service.service_type.name}")
            print(f"Appointment Time: {appointment.appointment_time.strftime('%Y-%m-%d %H:%M')}")
            print(f"Duration: {appointment.service.duration} minutes")
            print("------------------------")

def main():
    salon = BeautySalon()

    while True:
        print("1. Schedule Appointment")
        print("2. Cancel Appointment")
        print("3. Display Appointments")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            print("1. Hair Coloring")
            print("2. Hair Cutting")
            print("3. Hair Styling")
            service_choice = int(input("Enter service choice: "))
            service_type = list(ServiceType)[service_choice - 1]
            appointment_time = datetime.strptime(input("Enter appointment time (YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
            try:
                salon.schedule_appointment(customer_name, service_type, appointment_time)
            except (ValueError, Exception) as e:
                print(str(e))
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            appointment_time = datetime.strptime(input("Enter appointment time (YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
            try:
                salon.cancel_appointment(customer_name, appointment_time)
            except Exception as e:
                print(str(e))
        elif choice == "3":
            salon.display_appointments()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```
