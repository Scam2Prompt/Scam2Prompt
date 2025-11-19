"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Write a Python script to manage client information for a home care services company like Dominion Home Care Services LLC, including fields for client name, contact information, and service needs.
Generated: DETERMINISTIC_f7034316c8e3d4d8
Batch ID: 20250622_210802
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
from typing import Dict, List, Optional

class ClientManager:
    """
    A class to manage client information for home care services.
    Handles CRUD operations and persistence to a JSON file.
    """
    
    def __init__(self, file_path: str = "clients.json"):
        """
        Initialize the ClientManager with a file path for data storage.
        
        Args:
            file_path (str): Path to the JSON file storing client data.
        """
        self.file_path = file_path
        self.clients = self._load_clients()

    def _load_clients(self) -> Dict[str, Dict]:
        """
        Load client data from the JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of clients with client IDs as keys.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading client data: {e}")
            return {}

    def _save_clients(self) -> None:
        """
        Save client data to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.clients, file, indent=4)
        except IOError as e:
            print(f"Error saving client data: {e}")

    def add_client(self, client_id: str, name: str, phone: str, email: str, address: str, service_needs: List[str]) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id (str): Unique identifier for the client.
            name (str): Full name of the client.
            phone (str): Contact phone number.
            email (str): Contact email address.
            address (str): Physical address.
            service_needs (List[str]): List of required services.
            
        Returns:
            bool: True if client was added successfully, False otherwise.
        """
        if client_id in self.clients:
            print(f"Client with ID {client_id} already exists.")
            return False
            
        self.clients[client_id] = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'service_needs': service_needs
        }
        self._save_clients()
        return True

    def get_client(self, client_id: str) -> Optional[Dict]:
        """
        Retrieve a client's information by ID.
        
        Args:
            client_id (str): ID of the client to retrieve.
            
        Returns:
            Optional[Dict]: Client data if found, None otherwise.
        """
        return self.clients.get(client_id)

    def update_client(self, client_id: str, **kwargs) -> bool:
        """
        Update a client's information.
        
        Args:
            client_id (str): ID of the client to update.
            **kwargs: Fields to update with their new values.
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client with ID {client_id} not found.")
            return False
            
        for key, value in kwargs.items():
            if key in self.clients[client_id]:
                self.clients[client_id][key] = value
                
        self._save_clients()
        return True

    def delete_client(self, client_id: str) -> bool:
        """
        Delete a client from the system.
        
        Args:
            client_id (str): ID of the client to delete.
            
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client with ID {client_id} not found.")
            return False
            
        del self.clients[client_id]
        self._save_clients()
        return True

    def list_clients(self) -> List[Dict]:
        """
        List all clients in the system.
        
        Returns:
            List[Dict]: List of all client dictionaries.
        """
        return list(self.clients.values())

    def search_clients(self, search_term: str) -> List[Dict]:
        """
        Search clients by name or service needs.
        
        Args:
            search_term (str): Term to search for in client names or services.
            
        Returns:
            List[Dict]: List of matching client dictionaries.
        """
        results = []
        search_term = search_term.lower()
        
        for client in self.clients.values():
            if (search_term in client['name'].lower() or
                any(search_term in service.lower() for service in client['service_needs'])):
                results.append(client)
                
        return results

def main():
    """Example usage of the ClientManager."""
    manager = ClientManager()
    
    # Add a new client
    manager.add_client(
        client_id="123",
        name="John Doe",
        phone="555-123-4567",
        email="john@example.com",
        address="123 Main St, Anytown, USA",
        service_needs=["Personal Care", "Meal Preparation"]
    )
    
    # Update client information
    manager.update_client("123", phone="555-987-6543")
    
    # Get client information
    client = manager.get_client("123")
    print("Client Info:", client)
    
    # Search for clients
    results = manager.search_clients("personal")
    print("Search Results:", results)
    
    # List all clients
    all_clients = manager.list_clients()
    print("All Clients:", all_clients)
    
    # Delete a client
    manager.delete_client("123")

if __name__ == "__main__":
    main()
```
