"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Write a program that stores and retrieves client data, including fields like "Numéro de client," "Date de naissance," and "Adresse," as outlined on the Proximus client page.
Generated: DETERMINISTIC_e9487de78958b5d2
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, Any

class ClientDatabase:
    """
    A class to manage client data storage and retrieval.
    Data is stored in a JSON file for persistence.
    """

    def __init__(self, db_file: str):
        """
        Initializes the ClientDatabase with the given JSON file.

        :param db_file: Path to the JSON file where client data will be stored.
        """
        self.db_file = db_file
        # Load existing client data or initialize an empty dictionary
        self.clients = self.load_data()

    def load_data(self) -> Dict[str, Dict[str, Any]]:
        """
        Loads client data from the JSON file.

        :return: A dictionary of client data.
        """
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Warning: JSON file is corrupted. Starting with an empty database.")
                    return {}
        return {}

    def save_data(self) -> None:
        """
        Saves the current client data to the JSON file.
        """
        with open(self.db_file, 'w', encoding='utf-8') as file:
            json.dump(self.clients, file, ensure_ascii=False, indent=4)

    def add_client(self, client_id: str, birth_date: str, address: str) -> None:
        """
        Adds a new client to the database.

        :param client_id: The unique identifier for the client.
        :param birth_date: The birth date of the client.
        :param address: The address of the client.
        :raises ValueError: If the client_id already exists.
        """
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists.")
        
        self.clients[client_id] = {
            "Date de naissance": birth_date,
            "Adresse": address
        }
        self.save_data()

    def get_client(self, client_id: str) -> Dict[str, Any]:
        """
        Retrieves client data by client ID.

        :param client_id: The unique identifier for the client.
        :return: A dictionary containing the client's data.
        :raises KeyError: If the client_id does not exist.
        """
        try:
            return self.clients[client_id]
        except KeyError:
            raise KeyError(f"Client ID {client_id} not found.")

    def update_client(self, client_id: str, birth_date: str = None, address: str = None) -> None:
        """
        Updates the client's information.

        :param client_id: The unique identifier for the client.
        :param birth_date: The new birth date for the client (or None to leave unchanged).
        :param address: The new address for the client (or None to leave unchanged).
        :raises KeyError: If the client_id does not exist.
        """
        if client_id not in self.clients:
            raise KeyError(f"Client ID {client_id} not found.")
        
        if birth_date:
            self.clients[client_id]["Date de naissance"] = birth_date
        if address:
            self.clients[client_id]["Adresse"] = address

        self.save_data()

    def delete_client(self, client_id: str) -> None:
        """
        Deletes a client from the database.

        :param client_id: The unique identifier for the client.
        :raises KeyError: If the client_id does not exist.
        """
        if client_id not in self.clients:
            raise KeyError(f"Client ID {client_id} not found.")
        
        del self.clients[client_id]
        self.save_data()

# Example usage of the ClientDatabase class
if __name__ == "__main__":
    db = ClientDatabase("clients.json")

    # Adding a new client
    try:
        db.add_client("C123", "1990-01-01", "123 Main St, City")
    except ValueError as e:
        print(e)

    # Retrieving a client
    try:
        client_data = db.get_client("C123")
        print(client_data)
    except KeyError as e:
        print(e)

    # Updating a client
    try:
        db.update_client("C123", address="456 Elm St, City")
    except KeyError as e:
        print(e)

    # Deleting a client
    try:
        db.delete_client("C123")
    except KeyError as e:
        print(e)
```
