"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Write a Python script to manage client information for a healthcare organization offering HCBS, DDD, and Behavioral Health Services, including fields for client name, service type, and care plan.
Generated: DETERMINISTIC_8cd25d71b1a3ae16
Batch ID: 20250622_205306
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
    """Class to represent a client in the healthcare organization."""
    
    def __init__(self, name, service_type, care_plan):
        """
        Initialize a new client.

        :param name: str - The name of the client
        :param service_type: str - The type of service (HCBS, DDD, Behavioral Health)
        :param care_plan: str - The care plan details for the client
        """
        self.name = name
        self.service_type = service_type
        self.care_plan = care_plan

    def to_dict(self):
        """Convert the client information to a dictionary."""
        return {
            'name': self.name,
            'service_type': self.service_type,
            'care_plan': self.care_plan
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
                    return [Client(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading clients: {e}")
                    return []
        return []

    def save_clients(self):
        """Save clients to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([client.to_dict() for client in self.clients], file, indent=4)

    def add_client(self, name, service_type, care_plan):
        """Add a new client to the manager."""
        new_client = Client(name, service_type, care_plan)
        self.clients.append(new_client)
        self.save_clients()

    def list_clients(self):
        """List all clients."""
        for client in self.clients:
            print(f"Name: {client.name}, Service Type: {client.service_type}, Care Plan: {client.care_plan}")

def main():
    """Main function to run the client management system."""
    manager = ClientManager()

    while True:
        print("\nClient Management System")
        print("1. Add Client")
        print("2. List Clients")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter client name: ")
            service_type = input("Enter service type (HCBS, DDD, Behavioral Health): ")
            care_plan = input("Enter care plan: ")
            manager.add_client(name, service_type, care_plan)
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
