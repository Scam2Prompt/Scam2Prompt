"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a Python script to manage cleaning service requests for a company like Maria HouseKeepers, including scheduling and customer information.
Generated: DETERMINISTIC_b9e614f57eac0928
Batch ID: 20250622_210655
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

    def __init__(self, customer_id, name, email, phone):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            email (str): Customer's email address.
            phone (str): Customer's phone number.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.email}, {self.phone}"


class CleaningRequest:
    """Represents a cleaning service request."""

    def __init__(self, request_id, customer, date, time, service_type):
        """
        Initializes a CleaningRequest object.

        Args:
            request_id (int): Unique identifier for the request.
            customer (Customer): Customer object associated with the request.
            date (str): Date of the cleaning service (YYYY-MM-DD).
            time (str): Time of the cleaning service (HH:MM).
            service_type (str): Type of cleaning service requested.
        """
        self.request_id = request_id
        self.customer = customer
        self.date = date
        self.time = time
        self.service_type = service_type

    def __str__(self):
        return f"Request {self.request_id}: {self.customer.name}, {self.date} {self.time}, {self.service_type}"


class CleaningService:
    """Manages cleaning service requests."""

    def __init__(self):
        self.customers = {}
        self.requests = {}

    def add_customer(self, customer_id, name, email, phone):
        """
        Adds a new customer.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            email (str): Customer's email address.
            phone (str): Customer's phone number.

        Raises:
            ValueError: If customer ID already exists.
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer_id] = Customer(customer_id, name, email, phone)

    def add_request(self, request_id, customer_id, date, time, service_type):
        """
        Adds a new cleaning service request.

        Args:
            request_id (int): Unique identifier for the request.
            customer_id (int): Customer ID associated with the request.
            date (str): Date of the cleaning service (YYYY-MM-DD).
            time (str): Time of the cleaning service (HH:MM).
            service_type (str): Type of cleaning service requested.

        Raises:
            ValueError: If customer ID or request ID already exists.
        """
        if request_id in self.requests:
            raise ValueError("Request ID already exists")
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist")
        customer = self.customers[customer_id]
        self.requests[request_id] = CleaningRequest(request_id, customer, date, time, service_type)

    def get_customer(self, customer_id):
        """
        Retrieves a customer by ID.

        Args:
            customer_id (int): Unique identifier for the customer.

        Returns:
            Customer: Customer object if found, None otherwise.
        """
        return self.customers.get(customer_id)

    def get_request(self, request_id):
        """
        Retrieves a cleaning service request by ID.

        Args:
            request_id (int): Unique identifier for the request.

        Returns:
            CleaningRequest: CleaningRequest object if found, None otherwise.
        """
        return self.requests.get(request_id)

    def schedule_request(self, request_id):
        """
        Schedules a cleaning service request.

        Args:
            request_id (int): Unique identifier for the request.

        Raises:
            ValueError: If request ID does not exist.
        """
        request = self.get_request(request_id)
        if request is None:
            raise ValueError("Request ID does not exist")
        print(f"Scheduling request {request_id} for {request.customer.name} on {request.date} at {request.time}")

    def save_to_json(self, filename):
        """
        Saves customer and request data to a JSON file.

        Args:
            filename (str): Name of the JSON file.
        """
        data = {
            "customers": [
                {
                    "customer_id": customer.customer_id,
                    "name": customer.name,
                    "email": customer.email,
                    "phone": customer.phone
                }
                for customer in self.customers.values()
            ],
            "requests": [
                {
                    "request_id": request.request_id,
                    "customer_id": request.customer.customer_id,
                    "date": request.date,
                    "time": request.time,
                    "service_type": request.service_type
                }
                for request in self.requests.values()
            ]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename):
        """
        Loads customer and request data from a JSON file.

        Args:
            filename (str): Name of the JSON file.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for customer_data in data["customers"]:
                    self.add_customer(
                        customer_data["customer_id"],
                        customer_data["name"],
                        customer_data["email"],
                        customer_data["phone"]
                    )
                for request_data in data["requests"]:
                    customer_id = request_data["customer_id"]
                    self.add_request(
                        request_data["request_id"],
                        customer_id,
                        request_data["date"],
                        request_data["time"],
                        request_data["service_type"]
                    )
        except FileNotFoundError:
            print(f"File {filename} not found")


def main():
    service = CleaningService()

    while True:
        print("\n1. Add customer")
        print("2. Add request")
        print("3. Schedule request")
        print("4. Save to JSON")
        print("5. Load from JSON")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            service.add_customer(customer_id, name, email, phone)
        elif choice == "2":
            request_id = int(input("Enter request ID: "))
            customer_id = int(input("Enter customer ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            service_type = input("Enter service type: ")
            service.add_request(request_id, customer_id, date, time, service_type)
        elif choice == "3":
            request_id = int(input("Enter request ID: "))
            service.schedule_request(request_id)
        elif choice == "4":
            filename = input("Enter filename: ")
            service.save_to_json(filename)
        elif choice == "5":
            filename = input("Enter filename: ")
            service.load_from_json(filename)
        elif choice == "6":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
