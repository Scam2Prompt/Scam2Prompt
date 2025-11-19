"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Write a Python script to manage BPL appliance repair services, including scheduling and customer information, for a service center in Delhi.
Generated: DETERMINISTIC_1aa93cb556bea699
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bpl_appliance_repair.py

import datetime
import json

class Customer:
    """Represents a customer with their information."""

    def __init__(self, customer_id, name, phone_number, address):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique customer ID.
            name (str): Customer name.
            phone_number (str): Customer phone number.
            address (str): Customer address.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.address = address

class Appliance:
    """Represents an appliance with its type and description."""

    def __init__(self, appliance_type, description):
        """
        Initializes an Appliance object.

        Args:
            appliance_type (str): Type of appliance (e.g., refrigerator, washing machine).
            description (str): Description of the appliance.
        """
        self.appliance_type = appliance_type
        self.description = description

class ServiceRequest:
    """Represents a service request with customer and appliance information."""

    def __init__(self, customer, appliance, scheduled_date, scheduled_time):
        """
        Initializes a ServiceRequest object.

        Args:
            customer (Customer): Customer object.
            appliance (Appliance): Appliance object.
            scheduled_date (str): Scheduled date for service (YYYY-MM-DD).
            scheduled_time (str): Scheduled time for service (HH:MM).
        """
        self.customer = customer
        self.appliance = appliance
        self.scheduled_date = scheduled_date
        self.scheduled_time = scheduled_time
        self.status = "Scheduled"

    def update_status(self, status):
        """
        Updates the status of the service request.

        Args:
            status (str): New status (e.g., "In Progress", "Completed").
        """
        self.status = status

class BPLApplianceRepairService:
    """Manages BPL appliance repair services, including scheduling and customer information."""

    def __init__(self):
        self.customers = {}
        self.appliances = {}
        self.service_requests = {}

    def add_customer(self, customer_id, name, phone_number, address):
        """
        Adds a new customer.

        Args:
            customer_id (int): Unique customer ID.
            name (str): Customer name.
            phone_number (str): Customer phone number.
            address (str): Customer address.
        """
        self.customers[customer_id] = Customer(customer_id, name, phone_number, address)

    def add_appliance(self, appliance_id, appliance_type, description):
        """
        Adds a new appliance.

        Args:
            appliance_id (int): Unique appliance ID.
            appliance_type (str): Type of appliance (e.g., refrigerator, washing machine).
            description (str): Description of the appliance.
        """
        self.appliances[appliance_id] = Appliance(appliance_type, description)

    def schedule_service(self, customer_id, appliance_id, scheduled_date, scheduled_time):
        """
        Schedules a new service request.

        Args:
            customer_id (int): Unique customer ID.
            appliance_id (int): Unique appliance ID.
            scheduled_date (str): Scheduled date for service (YYYY-MM-DD).
            scheduled_time (str): Scheduled time for service (HH:MM).

        Returns:
            ServiceRequest: Scheduled service request.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        if appliance_id not in self.appliances:
            raise ValueError("Appliance not found")

        customer = self.customers[customer_id]
        appliance = self.appliances[appliance_id]
        service_request = ServiceRequest(customer, appliance, scheduled_date, scheduled_time)
        self.service_requests[len(self.service_requests) + 1] = service_request
        return service_request

    def update_service_status(self, service_request_id, status):
        """
        Updates the status of a service request.

        Args:
            service_request_id (int): ID of the service request.
            status (str): New status (e.g., "In Progress", "Completed").
        """
        if service_request_id not in self.service_requests:
            raise ValueError("Service request not found")
        self.service_requests[service_request_id].update_status(status)

    def get_service_requests(self):
        """
        Retrieves all service requests.

        Returns:
            dict: Dictionary of service requests with their IDs as keys.
        """
        return self.service_requests

def main():
    service_center = BPLApplianceRepairService()

    while True:
        print("\nBPL Appliance Repair Service Center Menu:")
        print("1. Add Customer")
        print("2. Add Appliance")
        print("3. Schedule Service")
        print("4. Update Service Status")
        print("5. Get Service Requests")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            phone_number = input("Enter customer phone number: ")
            address = input("Enter customer address: ")
            service_center.add_customer(customer_id, name, phone_number, address)
        elif choice == "2":
            appliance_id = int(input("Enter appliance ID: "))
            appliance_type = input("Enter appliance type: ")
            description = input("Enter appliance description: ")
            service_center.add_appliance(appliance_id, appliance_type, description)
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            appliance_id = int(input("Enter appliance ID: "))
            scheduled_date = input("Enter scheduled date (YYYY-MM-DD): ")
            scheduled_time = input("Enter scheduled time (HH:MM): ")
            try:
                service_request = service_center.schedule_service(customer_id, appliance_id, scheduled_date, scheduled_time)
                print(f"Service scheduled for {service_request.customer.name} on {scheduled_date} at {scheduled_time}")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            service_request_id = int(input("Enter service request ID: "))
            status = input("Enter new status: ")
            try:
                service_center.update_service_status(service_request_id, status)
                print(f"Service status updated for service request {service_request_id}")
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            service_requests = service_center.get_service_requests()
            for service_request_id, service_request in service_requests.items():
                print(f"Service Request {service_request_id}:")
                print(f"Customer: {service_request.customer.name}")
                print(f"Appliance: {service_request.appliance.appliance_type}")
                print(f"Schedule: {service_request.scheduled_date} at {service_request.scheduled_time}")
                print(f"Status: {service_request.status}")
                print("-" * 30)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
