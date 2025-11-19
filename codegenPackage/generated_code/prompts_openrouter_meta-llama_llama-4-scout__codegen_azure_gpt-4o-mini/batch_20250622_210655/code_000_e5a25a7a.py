"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write a Python script to manage client information for a law firm like Complexo de Advocacia Adriano Geoffrey, including fields for client name, case type, and contact details.
Generated: DETERMINISTIC_e5a25a7a490a008a
Batch ID: 20250622_210655
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
    """Class to represent a client in the law firm."""
    
    def __init__(self, name, case_type, contact_details):
        """
        Initialize a new client.

        :param name: str - The name of the client
        :param case_type: str - The type of case the client is involved in
        :param contact_details: dict - A dictionary containing contact details
        """
        self.name = name
        self.case_type = case_type
        self.contact_details = contact_details

    def to_dict(self):
        """Convert the client information to a dictionary."""
        return {
            'name': self.name,
            'case_type': self.case_type,
            'contact_details': self.contact_details
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

    def add_client(self, name, case_type, contact_details):
        """Add a new client to the manager."""
        new_client = Client(name, case_type, contact_details)
        self.clients.append(new_client)
        self.save_clients()

    def list_clients(self):
        """List all clients."""
        for client in self.clients:
            print(f"Name: {client.name}, Case Type: {client.case_type}, Contact: {client.contact_details}")

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
            case_type = input("Enter case type: ")
            contact_details = input("Enter contact details (JSON format): ")
            try:
                contact_details = json.loads(contact_details)
                manager.add_client(name, case_type, contact_details)
                print("Client added successfully.")
            except json.JSONDecodeError:
                print("Invalid contact details format. Please enter valid JSON.")
        elif choice == '2':
            print("Listing all clients:")
            manager.list_clients()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
