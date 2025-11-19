"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: "Write a Python script to manage insurance client data, including contact information and policy details, similar to Yexine Rangel Asesores de Seguros Ltda's system."
Generated: DETERMINISTIC_2ef576bc6d214952
Batch ID: 20250622_205111
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
    """Class to represent an insurance client."""
    
    def __init__(self, client_id, name, contact_info, policy_details):
        """
        Initialize a new client.

        :param client_id: Unique identifier for the client
        :param name: Name of the client
        :param contact_info: Dictionary containing contact information
        :param policy_details: Dictionary containing policy details
        """
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info
        self.policy_details = policy_details

    def to_dict(self):
        """Convert client data to a dictionary."""
        return {
            'client_id': self.client_id,
            'name': self.name,
            'contact_info': self.contact_info,
            'policy_details': self.policy_details
        }

class ClientManager:
    """Class to manage insurance client data."""
    
    def __init__(self, data_file='clients.json'):
        """
        Initialize the client manager.

        :param data_file: Path to the JSON file where client data is stored
        """
        self.data_file = data_file
        self.clients = self.load_clients()

    def load_clients(self):
        """Load clients from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return [Client(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading client data: {e}")
                    return []
        return []

    def save_clients(self):
        """Save clients to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([client.to_dict() for client in self.clients], file, indent=4)

    def add_client(self, client):
        """Add a new client to the manager."""
        self.clients.append(client)
        self.save_clients()

    def find_client(self, client_id):
        """Find a client by their ID.

        :param client_id: Unique identifier for the client
        :return: Client object or None if not found
        """
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def update_client(self, client_id, updated_data):
        """Update an existing client's information.

        :param client_id: Unique identifier for the client
        :param updated_data: Dictionary containing updated client data
        """
        client = self.find_client(client_id)
        if client:
            client.name = updated_data.get('name', client.name)
            client.contact_info.update(updated_data.get('contact_info', {}))
            client.policy_details.update(updated_data.get('policy_details', {}))
            self.save_clients()
        else:
            print(f"Client with ID {client_id} not found.")

    def delete_client(self, client_id):
        """Delete a client from the manager.

        :param client_id: Unique identifier for the client
        """
        client = self.find_client(client_id)
        if client:
            self.clients.remove(client)
            self.save_clients()
        else:
            print(f"Client with ID {client_id} not found.")

def main():
    """Main function to demonstrate client management."""
    manager = ClientManager()

    # Example usage
    client1 = Client(client_id='001', name='John Doe', contact_info={'email': 'john@example.com', 'phone': '123-456-7890'}, policy_details={'policy_number': 'POL123', 'coverage': 'Full'})
    manager.add_client(client1)

    # Update client information
    manager.update_client('001', {'name': 'John Smith', 'contact_info': {'phone': '987-654-3210'}})

    # Find and print client details
    client = manager.find_client('001')
    if client:
        print(client.to_dict())

    # Delete client
    manager.delete_client('001')

if __name__ == "__main__":
    main()
```
