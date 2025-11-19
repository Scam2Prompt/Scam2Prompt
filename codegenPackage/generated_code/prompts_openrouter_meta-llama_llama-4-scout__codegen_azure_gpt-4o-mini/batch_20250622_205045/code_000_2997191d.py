"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write a Python script to manage client information for a small business that offers immigration services, tax preparation, and accounting, including fields for client name, contact information, and services needed.
Generated: DETERMINISTIC_2997191d3704275f
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Client:
    """Class to represent a client with their information."""
    
    def __init__(self, name, contact_info, services):
        """
        Initialize a new client.

        :param name: str - The name of the client
        :param contact_info: dict - The contact information of the client
        :param services: list - The services needed by the client
        """
        self.name = name
        self.contact_info = contact_info
        self.services = services

    def to_dict(self):
        """Convert the client information to a dictionary."""
        return {
            'name': self.name,
            'contact_info': self.contact_info,
            'services': self.services
        }

class ClientManager:
    """Class to manage client information."""
    
    def __init__(self, filename='clients.json'):
        """
        Initialize the client manager.

        :param filename: str - The filename to store client data
        """
        self.filename = filename
        self.clients = self.load_clients()

    def load_clients(self):
        """Load clients from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return [Client(**client) for client in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading clients: {e}")
                    return []
        return []

    def save_clients(self):
        """Save clients to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([client.to_dict() for client in self.clients], file, indent=4)

    def add_client(self, name, contact_info, services):
        """Add a new client to the manager."""
        new_client = Client(name, contact_info, services)
        self.clients.append(new_client)
        self.save_clients()

    def list_clients(self):
        """List all clients."""
        for client in self.clients:
            print(f"Name: {client.name}, Contact: {client.contact_info}, Services: {', '.join(client.services)}")

def main():
    """Main function to run the client management system."""
    manager = ClientManager()

    # Example usage
    while True:
        print("\nClient Management System")
        print("1. Add Client")
        print("2. List Clients")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter client name: ")
            contact_info = input("Enter client contact information (email, phone): ")
            services = input("Enter services needed (comma-separated): ").split(',')
            services = [service.strip() for service in services]
            manager.add_client(name, {'contact_info': contact_info}, services)
            print("Client added successfully.")
        elif choice == '2':
            print("Listing all clients:")
            manager.list_clients()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
