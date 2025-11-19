"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Generate a Python script to manage and track fire sprinkler system installations, including client information and service dates."
Generated: DETERMINISTIC_b70b145fea879273
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_sprinkler_system.py

import datetime
import json
import os

class Client:
    """Represents a client with their information and service dates."""

    def __init__(self, name, address, phone, email):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            address (str): Client's address.
            phone (str): Client's phone number.
            email (str): Client's email.
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.services = []

    def add_service(self, service_date, description):
        """
        Adds a service date and description for the client.

        Args:
            service_date (str): Date of service in YYYY-MM-DD format.
            description (str): Description of the service.
        """
        self.services.append({
            "service_date": service_date,
            "description": description
        })

    def __str__(self):
        return f"{self.name} - {self.address}"


class FireSprinklerSystem:
    """Manages and tracks fire sprinkler system installations."""

    def __init__(self, data_file):
        """
        Initializes a FireSprinklerSystem object.

        Args:
            data_file (str): File to store client data.
        """
        self.clients = []
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """Loads client data from the data file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for client_data in data:
                    client = Client(
                        client_data['name'],
                        client_data['address'],
                        client_data['phone'],
                        client_data['email']
                    )
                    for service in client_data['services']:
                        client.add_service(
                            service['service_date'],
                            service['description']
                        )
                    self.clients.append(client)

    def save_data(self):
        """Saves client data to the data file."""
        data = []
        for client in self.clients:
            client_data = {
                'name': client.name,
                'address': client.address,
                'phone': client.phone,
                'email': client.email,
                'services': client.services
            }
            data.append(client_data)
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_client(self, name, address, phone, email):
        """
        Adds a new client.

        Args:
            name (str): Client's name.
            address (str): Client's address.
            phone (str): Client's phone number.
            email (str): Client's email.
        """
        client = Client(name, address, phone, email)
        self.clients.append(client)
        self.save_data()

    def add_service(self, client_name, service_date, description):
        """
        Adds a service date and description for a client.

        Args:
            client_name (str): Name of the client.
            service_date (str): Date of service in YYYY-MM-DD format.
            description (str): Description of the service.
        """
        for client in self.clients:
            if client.name == client_name:
                client.add_service(service_date, description)
                self.save_data()
                return
        print(f"Client '{client_name}' not found.")

    def list_clients(self):
        """Lists all clients."""
        for client in self.clients:
            print(client)

    def list_services(self, client_name):
        """
        Lists all services for a client.

        Args:
            client_name (str): Name of the client.
        """
        for client in self.clients:
            if client.name == client_name:
                for service in client.services:
                    print(f"Date: {service['service_date']}, Description: {service['description']}")
                return
        print(f"Client '{client_name}' not found.")


def main():
    data_file = 'clients.json'
    system = FireSprinklerSystem(data_file)

    while True:
        print("\n1. Add Client")
        print("2. Add Service")
        print("3. List Clients")
        print("4. List Services")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter client name: ")
            address = input("Enter client address: ")
            phone = input("Enter client phone: ")
            email = input("Enter client email: ")
            system.add_client(name, address, phone, email)
        elif choice == '2':
            client_name = input("Enter client name: ")
            service_date = input("Enter service date (YYYY-MM-DD): ")
            description = input("Enter service description: ")
            system.add_service(client_name, service_date, description)
        elif choice == '3':
            system.list_clients()
        elif choice == '4':
            client_name = input("Enter client name: ")
            system.list_services(client_name)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
