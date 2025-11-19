"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python script to manage pipe cleaning services, including scheduling and customer information, for a company like Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_0c6018011b29e25c
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# limpieza_tubos_costablanca.py

import datetime
import json

class Customer:
    """Represents a customer of Limpieza de Tubos Costablanca."""

    def __init__(self, customer_id, name, phone_number, address):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            address (str): Customer's address.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def to_dict(self):
        """Returns a dictionary representation of the Customer object."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone_number": self.phone_number,
            "address": self.address,
        }


class Service:
    """Represents a pipe cleaning service provided by Limpieza de Tubos Costablanca."""

    def __init__(self, service_id, customer, scheduled_date, scheduled_time):
        """
        Initializes a Service object.

        Args:
            service_id (int): Unique identifier for the service.
            customer (Customer): Customer receiving the service.
            scheduled_date (str): Scheduled date of the service (YYYY-MM-DD).
            scheduled_time (str): Scheduled time of the service (HH:MM).
        """
        self.service_id = service_id
        self.customer = customer
        self.scheduled_date = scheduled_date
        self.scheduled_time = scheduled_time
        self.completed = False

    def to_dict(self):
        """Returns a dictionary representation of the Service object."""
        return {
            "service_id": self.service_id,
            "customer": self.customer.to_dict(),
            "scheduled_date": self.scheduled_date,
            "scheduled_time": self.scheduled_time,
            "completed": self.completed,
        }

    def mark_as_completed(self):
        """Marks the service as completed."""
        self.completed = True


class PipeCleaningServiceManager:
    """Manages pipe cleaning services for Limpieza de Tubos Costablanca."""

    def __init__(self):
        self.customers = {}
        self.services = {}

    def add_customer(self, customer):
        """
        Adds a customer to the system.

        Args:
            customer (Customer): Customer to add.
        """
        self.customers[customer.customer_id] = customer

    def add_service(self, service):
        """
        Adds a service to the system.

        Args:
            service (Service): Service to add.
        """
        self.services[service.service_id] = service

    def get_customer(self, customer_id):
        """
        Retrieves a customer by their ID.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: The customer with the specified ID, or None if not found.
        """
        return self.customers.get(customer_id)

    def get_service(self, service_id):
        """
        Retrieves a service by its ID.

        Args:
            service_id (int): ID of the service to retrieve.

        Returns:
            Service: The service with the specified ID, or None if not found.
        """
        return self.services.get(service_id)

    def save_to_json(self, filename):
        """
        Saves the current state of the system to a JSON file.

        Args:
            filename (str): Name of the file to save to.
        """
        data = {
            "customers": [customer.to_dict() for customer in self.customers.values()],
            "services": [service.to_dict() for service in self.services.values()],
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename):
        """
        Loads the system state from a JSON file.

        Args:
            filename (str): Name of the file to load from.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            for customer_data in data.get("customers", []):
                customer = Customer(
                    customer_data["customer_id"],
                    customer_data["name"],
                    customer_data["phone_number"],
                    customer_data["address"],
                )
                self.add_customer(customer)

            for service_data in data.get("services", []):
                customer = self.get_customer(service_data["customer"]["customer_id"])
                if customer:
                    service = Service(
                        service_data["service_id"],
                        customer,
                        service_data["scheduled_date"],
                        service_data["scheduled_time"],
                    )
                    service.completed = service_data["completed"]
                    self.add_service(service)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error loading JSON: {e}")


def main():
    manager = PipeCleaningServiceManager()

    while True:
        print("\n1. Add customer")
        print("2. Add service")
        print("3. Get customer")
        print("4. Get service")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            phone_number = input("Enter customer phone number: ")
            address = input("Enter customer address: ")

            customer = Customer(customer_id, name, phone_number, address)
            manager.add_customer(customer)
        elif choice == "2":
            service_id = int(input("Enter service ID: "))
            customer_id = int(input("Enter customer ID: "))
            customer = manager.get_customer(customer_id)

            if customer:
                scheduled_date = input("Enter scheduled date (YYYY-MM-DD): ")
                scheduled_time = input("Enter scheduled time (HH:MM): ")

                service = Service(service_id, customer, scheduled_date, scheduled_time)
                manager.add_service(service)
            else:
                print("Customer not found.")
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            customer = manager.get_customer(customer_id)

            if customer:
                print(f"Name: {customer.name}")
                print(f"Phone Number: {customer.phone_number}")
                print(f"Address: {customer.address}")
            else:
                print("Customer not found.")
        elif choice == "4":
            service_id = int(input("Enter service ID: "))
            service = manager.get_service(service_id)

            if service:
                print(f"Customer: {service.customer.name}")
                print(f"Scheduled Date: {service.scheduled_date}")
                print(f"Scheduled Time: {service.scheduled_time}")
                print(f"Completed: {service.completed}")
            else:
                print("Service not found.")
        elif choice == "5":
            filename = input("Enter filename: ")
            manager.save_to_json(filename)
        elif choice == "6":
            filename = input("Enter filename: ")
            manager.load_from_json(filename)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
