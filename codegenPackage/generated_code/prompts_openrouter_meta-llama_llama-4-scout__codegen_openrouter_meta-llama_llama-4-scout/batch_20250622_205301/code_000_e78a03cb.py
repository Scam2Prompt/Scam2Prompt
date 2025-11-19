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
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class VehicleType(str, Enum):
    """ Enum for different types of vehicles """
    CAR = "car"
    LPG = "lpg"
    HYBRID = "hybrid"
    MOTORBIKE = "motorbike"

class Appointment:
    """ Represents an appointment for fuel injector cleaning """

    def __init__(self, vehicle_type: VehicleType, vehicle_model: str, 
                 appointment_time: datetime, customer_name: str, 
                 customer_phone: str):
        """
        Initializes an Appointment object.

        Args:
        - vehicle_type (VehicleType): Type of the vehicle
        - vehicle_model (str): Model of the vehicle
        - appointment_time (datetime): Scheduled time for the appointment
        - customer_name (str): Name of the customer
        - customer_phone (str): Phone number of the customer
        """
        self.vehicle_type = vehicle_type
        self.vehicle_model = vehicle_model
        self.appointment_time = appointment_time
        self.customer_name = customer_name
        self.customer_phone = customer_phone

class AppointmentManager:
    """ Manages appointments for the mobile fuel injector cleaning service """

    def __init__(self):
        """ Initializes an empty appointment schedule """
        self.appointments: Dict[datetime, List[Appointment]] = {}

    def schedule_appointment(self, appointment: Appointment):
        """
        Schedules a new appointment.

        Args:
        - appointment (Appointment): The appointment to be scheduled

        Raises:
        - ValueError: If the appointment time is already occupied
        """
        if appointment.appointment_time in self.appointments:
            raise ValueError("Appointment time is already occupied")

        if appointment.appointment_time not in self.appointments:
            self.appointments[appointment.appointment_time] = []

        self.appointments[appointment.appointment_time].append(appointment)

    def cancel_appointment(self, appointment_time: datetime, customer_name: str):
        """
        Cancels an existing appointment.

        Args:
        - appointment_time (datetime): Scheduled time of the appointment
        - customer_name (str): Name of the customer

        Raises:
        - ValueError: If the appointment is not found
        """
        if appointment_time not in self.appointments:
            raise ValueError("Appointment not found")

        self.appointments[appointment_time] = [
            appointment for appointment in self.appointments[appointment_time] 
            if appointment.customer_name != customer_name
        ]

        if not self.appointments[appointment_time]:
            del self.appointments[appointment_time]

    def get_appointments(self, date: datetime = None):
        """
        Retrieves a list of appointments.

        Args:
        - date (datetime): Date for which to retrieve appointments (optional)

        Returns:
        - List[Appointment]: List of appointments
        """
        if date:
            date_start = date.replace(hour=0, minute=0, second=0)
            date_end = date.replace(hour=23, minute=59, second=59)

            appointments = [
                appointment for appointment_time, appointments_list in self.appointments.items() 
                for appointment in appointments_list 
                if date_start <= appointment_time <= date_end
            ]
        else:
            appointments = [
                appointment for appointments_list in self.appointments.values() 
                for appointment in appointments_list
            ]

        return appointments

def main():
    try:
        # Create an appointment manager
        manager = AppointmentManager()

        # Create appointments
        appointment1 = Appointment(
            VehicleType.CAR, 
            "Toyota Camry", 
            datetime(2024, 9, 17, 10, 0), 
            "John Doe", 
            "1234567890"
        )

        appointment2 = Appointment(
            VehicleType.LPG, 
            "Honda Civic", 
            datetime(2024, 9, 17, 11, 0), 
            "Jane Doe", 
            "9876543210"
        )

        # Schedule appointments
        manager.schedule_appointment(appointment1)
        manager.schedule_appointment(appointment2)

        # Get appointments
        appointments = manager.get_appointments(datetime(2024, 9, 17))
        for appointment in appointments:
            print(f"Vehicle Type: {appointment.vehicle_type.value}, Vehicle Model: {appointment.vehicle_model}, Time: {appointment.appointment_time}, Customer Name: {appointment.customer_name}, Customer Phone: {appointment.customer_phone}")

        # Cancel appointment
        manager.cancel_appointment(datetime(2024, 9, 17, 10, 0), "John Doe")

        # Get appointments after cancellation
        appointments = manager.get_appointments(datetime(2024, 9, 17))
        for appointment in appointments:
            print(f"Vehicle Type: {appointment.vehicle_type.value}, Vehicle Model: {appointment.vehicle_model}, Time: {appointment.appointment_time}, Customer Name: {appointment.customer_name}, Customer Phone: {appointment.customer_phone}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
