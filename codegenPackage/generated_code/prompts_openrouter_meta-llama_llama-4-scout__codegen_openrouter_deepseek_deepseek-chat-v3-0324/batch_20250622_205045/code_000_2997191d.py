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
from typing import Dict, List, Optional

class ClientManager:
    """A class to manage client information for immigration, tax, and accounting services."""
    
    def __init__(self, data_file: str = "clients.json"):
        """Initialize the ClientManager with a data file.
        
        Args:
            data_file: Path to the JSON file storing client data.
        """
        self.data_file = data_file
        self.clients = self._load_clients()
    
    def _load_clients(self) -> Dict[str, Dict]:
        """Load client data from the JSON file.
        
        Returns:
            Dictionary of clients. Returns empty dict if file doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading client data: {e}")
        return {}
    
    def _save_clients(self) -> None:
        """Save client data to the JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.clients, f, indent=4)
        except IOError as e:
            print(f"Error saving client data: {e}")
    
    def add_client(self, client_id: str, name: str, email: str, phone: str, 
                   services: List[str], notes: Optional[str] = None) -> bool:
        """Add a new client to the system.
        
        Args:
            client_id: Unique identifier for the client.
            name: Client's full name.
            email: Client's email address.
            phone: Client's phone number.
            services: List of services needed (e.g., ['immigration', 'tax']).
            notes: Optional notes about the client.
            
        Returns:
            True if client was added successfully, False otherwise.
        """
        if client_id in self.clients:
            print(f"Client ID {client_id} already exists.")
            return False
        
        self.clients[client_id] = {
            'name': name,
            'email': email,
            'phone': phone,
            'services': services,
            'notes': notes or ""
        }
        self._save_clients()
        return True
    
    def update_client(self, client_id: str, **kwargs) -> bool:
        """Update an existing client's information.
        
        Args:
            client_id: ID of the client to update.
            **kwargs: Fields to update (name, email, phone, services, notes).
            
        Returns:
            True if update was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
        
        valid_fields = {'name', 'email', 'phone', 'services', 'notes'}
        for field, value in kwargs.items():
            if field in valid_fields:
                self.clients[client_id][field] = value
        
        self._save_clients()
        return True
    
    def remove_client(self, client_id: str) -> bool:
        """Remove a client from the system.
        
        Args:
            client_id: ID of the client to remove.
            
        Returns:
            True if removal was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
        
        del self.clients[client_id]
        self._save_clients()
        return True
    
    def get_client(self, client_id: str) -> Optional[Dict]:
        """Retrieve a client's information.
        
        Args:
            client_id: ID of the client to retrieve.
            
        Returns:
            Client's data dictionary if found, None otherwise.
        """
        return self.clients.get(client_id)
    
    def list_clients(self) -> List[Dict]:
        """List all clients in the system.
        
        Returns:
            List of all clients' data dictionaries.
        """
        return list(self.clients.values())
    
    def search_clients(self, query: str) -> List[Dict]:
        """Search clients by name, email, or services.
        
        Args:
            query: Search term to match against client data.
            
        Returns:
            List of matching clients' data dictionaries.
        """
        results = []
        query = query.lower()
        for client in self.clients.values():
            if (query in client['name'].lower() or 
                query in client['email'].lower() or 
                any(query in service.lower() for service in client['services'])):
                results.append(client)
        return results


def main():
    """Example usage of the ClientManager."""
    manager = ClientManager()
    
    # Example operations
    manager.add_client(
        client_id="001",
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        services=["immigration", "tax"],
        notes="Needs help with visa application"
    )
    
    manager.add_client(
        client_id="002",
        name="Jane Smith",
        email="jane@example.com",
        phone="555-5678",
        services=["accounting"],
        notes="Annual tax preparation"
    )
    
    # Update client
    manager.update_client("001", phone="555-4321", notes="Visa approved")
    
    # Search clients
    results = manager.search_clients("tax")
    print("Clients needing tax services:")
    for client in results:
        print(f"- {client['name']}: {client['services']}")
    
    # List all clients
    print("\nAll clients:")
    for client in manager.list_clients():
        print(f"- {client['name']} ({client['email']})")


if __name__ == "__main__":
    main()
```
