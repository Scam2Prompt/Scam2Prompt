"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a Python script to manage cleaning service appointments for a company like Star Cleaning Services, including scheduling and customer information.
Generated: DETERMINISTIC_137f329b1206b198
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_service.py

import datetime
import json

class Customer:
    """Represents a customer with their information."""

    def __init__(self, name, phone_number, email):
        """
        Initializes a Customer object.

        Args:
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            email (str): Customer's email.
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email

class Appointment:
    """Represents a cleaning service appointment."""

    def __init__(self, customer, date, time, service_type):
        """
        Initializes an Appointment object.

        Args:
            customer (Customer): Customer object.
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).
            service_type (str): Type of cleaning service.
        """
        self.customer = customer
        self.date = date
        self.time = time
        self.service_type = service_type

class CleaningService:
    """Manages cleaning service appointments."""

    def __init__(self):
        """Initializes the cleaning service with an empty appointment book."""
        self.appointments = {}

    def schedule_appointment(self, customer, date, time, service_type):
        """
        Schedules a new appointment.

        Args:
            customer (Customer): Customer object.
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).
            service_type (str): Type of cleaning service.

        Raises:
            ValueError: If the appointment date and time already exist.
        """
        appointment_key = f"{date} {time}"
        if appointment_key in self.appointments:
            raise ValueError("Appointment already exists at this date and time.")

        appointment = Appointment(customer, date, time, service_type)
        self.appointments[appointment_key] = appointment

    def cancel_appointment(self, date, time):
        """
        Cancels an existing appointment.

        Args:
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).

        Raises:
            KeyError: If the appointment does not exist.
        """
        appointment_key = f"{date} {time}"
        if appointment_key not in self.appointments:
            raise KeyError("Appointment does not exist.")

        del self.appointments[appointment_key]

    def get_appointments(self):
        """Returns a list of all appointments."""
        return list(self.appointments.values())

    def save_appointments(self, filename):
        """
        Saves appointments to a JSON file.

        Args:
            filename (str): Name of the file to save appointments to.
        """
        appointments_data = []
        for appointment in self.appointments.values():
            customer_data = {
                "name": appointment.customer.name,
                "phone_number": appointment.customer.phone_number,
                "email": appointment.customer.email,
            }
            appointment_data = {
                "customer": customer_data,
                "date": appointment.date,
                "time": appointment.time,
                "service_type": appointment.service_type,
            }
            appointments_data.append(appointment_data)

        with open(filename, "w") as file:
            json.dump(appointments_data, file, indent=4)

    def load_appointments(self, filename):
        """
        Loads appointments from a JSON file.

        Args:
            filename (str): Name of the file to load appointments from.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filename, "r") as file:
                appointments_data = json.load(file)
                self.appointments = {}
                for appointment_data in appointments_data:
                    customer = Customer(
                        appointment_data["customer"]["name"],
                        appointment_data["customer"]["phone_number"],
                        appointment_data["customer"]["email"],
                    )
                    appointment = Appointment(
                        customer,
                        appointment_data["date"],
                        appointment_data["time"],
                        appointment_data["service_type"],
                    )
                    appointment_key = f"{appointment_data['date']} {appointment_data['time']}"
                    self.appointments[appointment_key] = appointment
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

def main():
    cleaning_service = CleaningService()

    while True:
        print("\nStar Cleaning Services Appointment Manager")
        print("1. Schedule Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointments")
        print("4. Save Appointments")
        print("5. Load Appointments")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            phone_number = input("Enter customer phone number: ")
            email = input("Enter customer email: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            service_type = input("Enter service type: ")

            customer = Customer(name, phone_number, email)
            try:
                cleaning_service.schedule_appointment(customer, date, time, service_type)
                print("Appointment scheduled successfully.")
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            try:
                cleaning_service.cancel_appointment(date, time)
                print("Appointment canceled successfully.")
            except KeyError as e:
                print(str(e))

        elif choice == "3":
            appointments = cleaning_service.get_appointments()
            for i, appointment in enumerate(appointments):
                print(f"\nAppointment {i+1}:")
                print(f"Customer: {appointment.customer.name}")
                print(f"Date: {appointment.date}")
                print(f"Time: {appointment.time}")
                print(f"Service Type: {appointment.service_type}")

        elif choice == "4":
            filename = input("Enter filename to save appointments: ")
            cleaning_service.save_appointments(filename)
            print("Appointments saved successfully.")

        elif choice == "5":
            filename = input("Enter filename to load appointments: ")
            cleaning_service.load_appointments(filename)
            print("Appointments loaded successfully.")

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
