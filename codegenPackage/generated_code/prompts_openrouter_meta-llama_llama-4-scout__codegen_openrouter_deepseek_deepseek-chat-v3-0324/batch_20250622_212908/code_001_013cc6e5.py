"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write a Python script to manage client information for a company like AKNAN that provides services to hospitals and clinics.
Generated: DETERMINISTIC_013cc6e5c4e68338
Batch ID: 20250622_212908
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
    A class to manage client information for AKNAN company.
    Handles CRUD operations for client records stored in JSON format.
    """
    
    def __init__(self, file_path: str = "clients.json"):
        """
        Initialize the ClientManager with a JSON file path.
        
        Args:
            file_path (str): Path to the JSON file storing client data.
        """
        self.file_path = file_path
        self.clients = self._load_clients()
    
    def _load_clients(self) -> Dict[str, Dict]:
        """
        Load clients from JSON file or create new file if it doesn't exist.
        
        Returns:
            Dict[str, Dict]: Dictionary of client records.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading client data: {e}")
            return {}
    
    def _save_clients(self) -> bool:
        """
        Save current client data to JSON file.
        
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.clients, file, indent=4)
            return True
        except IOError as e:
            print(f"Error saving client data: {e}")
            return False
    
    def add_client(self, client_id: str, name: str, contact: str, 
                  services: List[str], is_active: bool = True) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id (str): Unique identifier for the client
            name (str): Name of the client organization
            contact (str): Primary contact information
            services (List[str]): List of services provided
            is_active (bool): Whether client is active
            
        Returns:
            bool: True if client was added successfully, False otherwise
        """
        if client_id in self.clients:
            print(f"Client ID {client_id} already exists.")
            return False
            
        self.clients[client_id] = {
            'name': name,
            'contact': contact,
            'services': services,
            'is_active': is_active
        }
        return self._save_clients()
    
    def get_client(self, client_id: str) -> Optional[Dict]:
        """
        Retrieve a client's information by ID.
        
        Args:
            client_id (str): ID of the client to retrieve
            
        Returns:
            Optional[Dict]: Client data if found, None otherwise
        """
        return self.clients.get(client_id)
    
    def update_client(self, client_id: str, **kwargs) -> bool:
        """
        Update client information.
        
        Args:
            client_id (str): ID of client to update
            **kwargs: Fields to update with new values
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
            
        valid_fields = {'name', 'contact', 'services', 'is_active'}
        for field, value in kwargs.items():
            if field in valid_fields:
                self.clients[client_id][field] = value
                
        return self._save_clients()
    
    def delete_client(self, client_id: str) -> bool:
        """
        Delete a client record.
        
        Args:
            client_id (str): ID of client to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
            
        del self.clients[client_id]
        return self._save_clients()
    
    def list_clients(self, active_only: bool = True) -> List[Dict]:
        """
        List all clients, optionally filtering by active status.
        
        Args:
            active_only (bool): Whether to return only active clients
            
        Returns:
            List[Dict]: List of client records
        """
        if active_only:
            return [client for client in self.clients.values() if client['is_active']]
        return list(self.clients.values())
    
    def search_clients(self, search_term: str, field: str = 'name') -> List[Dict]:
        """
        Search clients by a specific field.
        
        Args:
            search_term (str): Term to search for
            field (str): Field to search in ('name', 'contact', 'services')
            
        Returns:
            List[Dict]: Matching client records
        """
        valid_fields = {'name', 'contact', 'services'}
        if field not in valid_fields:
            print(f"Invalid search field: {field}")
            return []
            
        results = []
        for client in self.clients.values():
            if field == 'services':
                if any(search_term.lower() in service.lower() for service in client[field]):
                    results.append(client)
            elif search_term.lower() in client[field].lower():
                results.append(client)
                
        return results


def main():
    """Example usage of the ClientManager class."""
    manager = ClientManager()
    
    # Add some example clients
    manager.add_client(
        client_id="HOSP001",
        name="City General Hospital",
        contact="Dr. Smith (555) 123-4567",
        services=["Equipment Maintenance", "Staff Training"],
        is_active=True
    )
    
    manager.add_client(
        client_id="CLIN002",
        name="Downtown Clinic",
        contact="Nurse Johnson (555) 987-6543",
        services=["Equipment Maintenance"],
        is_active=True
    )
    
    # List active clients
    print("Active Clients:")
    for client in manager.list_clients():
        print(f"- {client['name']} ({client['contact']})")
    
    # Search for clients
    print("\nClients with Equipment Maintenance:")
    for client in manager.search_clients("Equipment Maintenance", "services"):
        print(f"- {client['name']}")


if __name__ == "__main__":
    main()
```
