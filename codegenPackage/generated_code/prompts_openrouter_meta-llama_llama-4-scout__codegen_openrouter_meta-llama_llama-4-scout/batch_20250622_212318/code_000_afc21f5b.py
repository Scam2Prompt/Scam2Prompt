"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Write a Python script to manage a plumbing service company's schedule and appointments for Rohr- und Kanalreinigung in Hamburg.
Generated: DETERMINISTIC_afc21f5b0b1d728e
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plumbing_service.py

from datetime import datetime, timedelta
import json
import os

class Appointment:
    """Represents a scheduled appointment."""

    def __init__(self, customer_name, address, date_time, service_type):
        """
        Initializes an Appointment object.

        Args:
            customer_name (str): Name of the customer.
            address (str): Address of the customer.
            date_time (datetime): Date and time of the appointment.
            service_type (str): Type of plumbing service.
        """
        self.customer_name = customer_name
        self.address = address
        self.date_time = date_time
        self.service_type = service_type

    def to_dict(self):
        """Converts the appointment to a dictionary."""
        return {
            "customer_name": self.customer_name,
            "address": self.address,
            "date_time": self.date_time.isoformat(),
            "service_type": self.service_type
        }

class PlumbingService:
    """Manages the schedule and appointments for a plumbing service company."""

    def __init__(self, schedule_file):
        """
        Initializes a PlumbingService object.

        Args:
            schedule_file (str): File path to store the schedule.
        """
        self.schedule_file = schedule_file
        self.schedule = self.load_schedule()

    def load_schedule(self):
        """Loads the schedule from the file."""
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as file:
                data = json.load(file)
                return [Appointment(**appointment) for appointment in data]
        else:
            return []

    def save_schedule(self):
        """Saves the schedule to the file."""
        data = [appointment.to_dict() for appointment in self.schedule]
        with open(self.schedule_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_appointment(self, customer_name, address, date_time, service_type):
        """
        Adds a new appointment to the schedule.

        Args:
            customer_name (str): Name of the customer.
            address (str): Address of the customer.
            date_time (datetime): Date and time of the appointment.
            service_type (str): Type of plumbing service.

        Raises:
            ValueError: If the date and time is not in the future.
        """
        if date_time < datetime.now():
            raise ValueError("Date and time must be in the future.")
        appointment = Appointment(customer_name, address, date_time, service_type)
        self.schedule.append(appointment)
        self.save_schedule()

    def cancel_appointment(self, customer_name, date_time):
        """
        Cancels an appointment.

        Args:
            customer_name (str): Name of the customer.
            date_time (datetime): Date and time of the appointment.

        Raises:
            ValueError: If the appointment is not found.
        """
        for appointment in self.schedule:
            if appointment.customer_name == customer_name and appointment.date_time == date_time:
                self.schedule.remove(appointment)
                self.save_schedule()
                return
        raise ValueError("Appointment not found.")

    def get_schedule(self):
        """Returns the schedule."""
        return self.schedule

def main():
    schedule_file = 'schedule.json'
    plumbing_service = PlumbingService(schedule_file)

    while True:
        print("\n1. Add appointment")
        print("2. Cancel appointment")
        print("3. View schedule")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            address = input("Enter address: ")
            date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
            service_type = input("Enter service type: ")
            try:
                plumbing_service.add_appointment(customer_name, address, date_time, service_type)
                print("Appointment added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == '2':
            customer_name = input("Enter customer name: ")
            date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
            try:
                plumbing_service.cancel_appointment(customer_name, date_time)
                print("Appointment cancelled successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == '3':
            schedule = plumbing_service.get_schedule()
            for appointment in schedule:
                print(f"Customer: {appointment.customer_name}")
                print(f"Address: {appointment.address}")
                print(f"Date and Time: {appointment.date_time}")
                print(f"Service Type: {appointment.service_type}")
                print("------------------------")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
