"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Write a Python script to manage cleaning service appointments for a company like Maid in Heaven, including scheduling and customer information.
Generated: DETERMINISTIC_42111be076b3acd4
Batch ID: 20250622_210650
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

    def __init__(self, customer_id, name, phone_number, email):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            email (str): Customer's email address.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.email = email

class Appointment:
    """Represents a cleaning service appointment."""

    def __init__(self, appointment_id, customer, date, time, service_type):
        """
        Initializes an Appointment object.

        Args:
            appointment_id (int): Unique identifier for the appointment.
            customer (Customer): Customer object associated with the appointment.
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.
            service_type (str): Type of cleaning service requested.
        """
        self.appointment_id = appointment_id
        self.customer = customer
        self.date = date
        self.time = time
        self.service_type = service_type

class CleaningService:
    """Manages cleaning service appointments."""

    def __init__(self):
        """Initializes the cleaning service with empty data structures."""
        self.customers = {}
        self.appointments = {}

    def add_customer(self, customer_id, name, phone_number, email):
        """
        Adds a new customer.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            email (str): Customer's email address.

        Raises:
            ValueError: If a customer with the same ID already exists.
        """
        if customer_id in self.customers:
            raise ValueError("Customer with the same ID already exists.")
        self.customers[customer_id] = Customer(customer_id, name, phone_number, email)

    def add_appointment(self, appointment_id, customer_id, date, time, service_type):
        """
        Adds a new appointment.

        Args:
            appointment_id (int): Unique identifier for the appointment.
            customer_id (int): ID of the customer associated with the appointment.
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.
            service_type (str): Type of cleaning service requested.

        Raises:
            ValueError: If the customer ID does not exist or appointment ID already exists.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        if appointment_id in self.appointments:
            raise ValueError("Appointment with the same ID already exists.")
        customer = self.customers[customer_id]
        self.appointments[appointment_id] = Appointment(appointment_id, customer, date, time, service_type)

    def get_appointment(self, appointment_id):
        """
        Retrieves an appointment by ID.

        Args:
            appointment_id (int): ID of the appointment to retrieve.

        Returns:
            Appointment: The appointment object if found, otherwise None.
        """
        return self.appointments.get(appointment_id)

    def get_customer_appointments(self, customer_id):
        """
        Retrieves all appointments for a customer.

        Args:
            customer_id (int): ID of the customer.

        Returns:
            list[Appointment]: A list of appointments associated with the customer.
        """
        return [appointment for appointment in self.appointments.values() if appointment.customer.customer_id == customer_id]

    def save_to_json(self, filename):
        """
        Saves the cleaning service data to a JSON file.

        Args:
            filename (str): Name of the JSON file to save to.
        """
        data = {
            "customers": [
                {
                    "customer_id": customer.customer_id,
                    "name": customer.name,
                    "phone_number": customer.phone_number,
                    "email": customer.email
                }
                for customer in self.customers.values()
            ],
            "appointments": [
                {
                    "appointment_id": appointment.appointment_id,
                    "customer_id": appointment.customer.customer_id,
                    "date": appointment.date,
                    "time": appointment.time,
                    "service_type": appointment.service_type
                }
                for appointment in self.appointments.values()
            ]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        """
        Loads cleaning service data from a JSON file.

        Args:
            filename (str): Name of the JSON file to load from.

        Returns:
            CleaningService: A CleaningService object with the loaded data.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return cls()

        cleaning_service = cls()
        for customer_data in data.get("customers", []):
            cleaning_service.add_customer(
                customer_data["customer_id"],
                customer_data["name"],
                customer_data["phone_number"],
                customer_data["email"]
            )

        for appointment_data in data.get("appointments", []):
            try:
                cleaning_service.add_appointment(
                    appointment_data["appointment_id"],
                    appointment_data["customer_id"],
                    appointment_data["date"],
                    appointment_data["time"],
                    appointment_data["service_type"]
                )
            except ValueError as e:
                print(f"Error loading appointment: {e}")

        return cleaning_service

def main():
    cleaning_service = CleaningService()

    while True:
        print("\n1. Add Customer")
        print("2. Add Appointment")
        print("3. Get Appointment")
        print("4. Get Customer Appointments")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            phone_number = input("Enter customer phone number: ")
            email = input("Enter customer email: ")
            cleaning_service.add_customer(customer_id, name, phone_number, email)
        elif choice == "2":
            appointment_id = int(input("Enter appointment ID: "))
            customer_id = int(input("Enter customer ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            service_type = input("Enter service type: ")
            try:
                cleaning_service.add_appointment(appointment_id, customer_id, date, time, service_type)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            appointment_id = int(input("Enter appointment ID: "))
            appointment = cleaning_service.get_appointment(appointment_id)
            if appointment:
                print(f"Appointment ID: {appointment.appointment_id}")
                print(f"Customer Name: {appointment.customer.name}")
                print(f"Date: {appointment.date}")
                print(f"Time: {appointment.time}")
                print(f"Service Type: {appointment.service_type}")
            else:
                print("Appointment not found.")
        elif choice == "4":
            customer_id = int(input("Enter customer ID: "))
            appointments = cleaning_service.get_customer_appointments(customer_id)
            if appointments:
                for appointment in appointments:
                    print(f"Appointment ID: {appointment.appointment_id}")
                    print(f"Date: {appointment.date}")
                    print(f"Time: {appointment.time}")
                    print(f"Service Type: {appointment.service_type}")
                    print("------------------------")
            else:
                print("No appointments found for the customer.")
        elif choice == "5":
            filename = input("Enter filename: ")
            cleaning_service.save_to_json(filename)
        elif choice == "6":
            filename = input("Enter filename: ")
            cleaning_service = CleaningService.load_from_json(filename)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
