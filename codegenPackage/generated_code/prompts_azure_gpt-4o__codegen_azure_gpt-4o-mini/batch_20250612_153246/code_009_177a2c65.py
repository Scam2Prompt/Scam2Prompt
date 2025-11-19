"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Write a program to manage client data and satisfaction metrics for engineering projects, incorporating Jau Consulting's principles of professionalism and new technologies.
Generated: DETERMINISTIC_177a2c654053bf27
Batch ID: 20250612_153246
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
from typing import List, Dict, Any

class ClientDataManager:
    """
    A class to manage client data and satisfaction metrics for engineering projects.
    This class provides methods to add, update, retrieve, and delete client information.
    """

    def __init__(self, data_file: str):
        """
        Initializes the ClientDataManager with a specified data file.

        :param data_file: Path to the JSON file where client data is stored.
        """
        self.data_file = data_file
        self.clients = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Loads client data from the JSON file.

        :return: A list of client data dictionaries.
        """
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error loading data: {e}")
                return []

    def save_data(self) -> None:
        """
        Saves the current client data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.clients, file, indent=4)

    def add_client(self, client_id: str, name: str, satisfaction_score: float) -> None:
        """
        Adds a new client to the data.

        :param client_id: Unique identifier for the client.
        :param name: Name of the client.
        :param satisfaction_score: Satisfaction score of the client (0-100).
        """
        if any(client['client_id'] == client_id for client in self.clients):
            print(f"Client with ID {client_id} already exists.")
            return

        new_client = {
            'client_id': client_id,
            'name': name,
            'satisfaction_score': satisfaction_score
        }
        self.clients.append(new_client)
        self.save_data()
        print(f"Client {name} added successfully.")

    def update_client(self, client_id: str, name: str = None, satisfaction_score: float = None) -> None:
        """
        Updates an existing client's information.

        :param client_id: Unique identifier for the client.
        :param name: New name of the client (optional).
        :param satisfaction_score: New satisfaction score of the client (optional).
        """
        for client in self.clients:
            if client['client_id'] == client_id:
                if name is not None:
                    client['name'] = name
                if satisfaction_score is not None:
                    client['satisfaction_score'] = satisfaction_score
                self.save_data()
                print(f"Client {client_id} updated successfully.")
                return
        print(f"Client with ID {client_id} not found.")

    def delete_client(self, client_id: str) -> None:
        """
        Deletes a client from the data.

        :param client_id: Unique identifier for the client.
        """
        self.clients = [client for client in self.clients if client['client_id'] != client_id]
        self.save_data()
        print(f"Client with ID {client_id} deleted successfully.")

    def get_client(self, client_id: str) -> Dict[str, Any]:
        """
        Retrieves a client's information.

        :param client_id: Unique identifier for the client.
        :return: A dictionary containing client information or None if not found.
        """
        for client in self.clients:
            if client['client_id'] == client_id:
                return client
        print(f"Client with ID {client_id} not found.")
        return None

    def list_clients(self) -> List[Dict[str, Any]]:
        """
        Lists all clients in the data.

        :return: A list of all client data dictionaries.
        """
        return self.clients


# Example usage
if __name__ == "__main__":
    manager = ClientDataManager('clients.json')

    # Adding clients
    manager.add_client('001', 'Acme Corp', 85.0)
    manager.add_client('002', 'Beta LLC', 90.0)

    # Updating a client
    manager.update_client('001', satisfaction_score=88.0)

    # Retrieving a client
    client_info = manager.get_client('001')
    print(client_info)

    # Listing all clients
    all_clients = manager.list_clients()
    print(all_clients)

    # Deleting a client
    manager.delete_client('002')
```
