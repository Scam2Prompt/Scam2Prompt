"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Write a Python script to manage client information for an accounting firm like Atual Contabilidade, including fields for contact details and service preferences."
Generated: DETERMINISTIC_e7df381fdb041711
Batch ID: 20250622_204932
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
    A class to manage client information for an accounting firm.
    Handles storage, retrieval, and modification of client records.
    """
    
    def __init__(self, storage_file: str = "clients.json"):
        """
        Initialize the ClientManager with a storage file.
        
        Args:
            storage_file: Path to JSON file for storing client data
        """
        self.storage_file = storage_file
        self.clients = self._load_clients()
    
    def _load_clients(self) -> Dict[str, Dict]:
        """
        Load client data from the storage file.
        
        Returns:
            Dictionary of client records
            
        Raises:
            IOError: If there's an issue reading the file
            json.JSONDecodeError: If the file contains invalid JSON
        """
        if not os.path.exists(self.storage_file):
            return {}
            
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to load client data: {str(e)}")
    
    def _save_clients(self):
        """
        Save client data to the storage file.
        
        Raises:
            IOError: If there's an issue writing to the file
        """
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.clients, f, indent=2)
        except IOError as e:
            raise Exception(f"Failed to save client data: {str(e)}")
    
    def add_client(self, client_id: str, name: str, email: str, phone: str, 
                   services: List[str], tax_id: Optional[str] = None, 
                   address: Optional[str] = None, notes: Optional[str] = None):
        """
        Add a new client to the system.
        
        Args:
            client_id: Unique identifier for the client
            name: Full name of the client
            email: Email address
            phone: Phone number
            services: List of accounting services required
            tax_id: Tax identification number (optional)
            address: Physical address (optional)
            notes: Additional notes (optional)
            
        Raises:
            ValueError: If client_id already exists or required fields are missing
        """
        if not all([client_id, name, email, phone, services]):
            raise ValueError("Missing required fields")
            
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists")
            
        self.clients[client_id] = {
            'name': name,
            'email': email,
            'phone': phone,
            'services': services,
            'tax_id': tax_id,
            'address': address,
            'notes': notes
        }
        
        self._save_clients()
    
    def update_client(self, client_id: str, **kwargs):
        """
        Update existing client information.
        
        Args:
            client_id: ID of client to update
            **kwargs: Fields to update (name, email, phone, services, etc.)
            
        Raises:
            ValueError: If client_id doesn't exist or invalid fields provided
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found")
            
        valid_fields = {'name', 'email', 'phone', 'services', 
                       'tax_id', 'address', 'notes'}
        
        for field, value in kwargs.items():
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
            self.clients[client_id][field] = value
            
        self._save_clients()
    
    def get_client(self, client_id: str) -> Dict:
        """
        Retrieve a client's information.
        
        Args:
            client_id: ID of client to retrieve
            
        Returns:
            Dictionary of client information
            
        Raises:
            ValueError: If client_id doesn't exist
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found")
        return self.clients[client_id]
    
    def list_clients(self) -> List[Dict]:
        """
        List all clients in the system.
        
        Returns:
            List of client dictionaries
        """
        return [{'id': k, **v} for k, v in self.clients.items()]
    
    def remove_client(self, client_id: str):
        """
        Remove a client from the system.
        
        Args:
            client_id: ID of client to remove
            
        Raises:
            ValueError: If client_id doesn't exist
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found")
            
        del self.clients[client_id]
        self._save_clients()
    
    def search_clients(self, search_term: str) -> List[Dict]:
        """
        Search clients by name, email, or tax ID.
        
        Args:
            search_term: String to search for
            
        Returns:
            List of matching client dictionaries
        """
        results = []
        search_term = search_term.lower()
        
        for client_id, client in self.clients.items():
            if (search_term in client['name'].lower() or 
                search_term in client['email'].lower() or 
                (client.get('tax_id') and search_term in client['tax_id'].lower())):
                results.append({'id': client_id, **client})
                
        return results


# Example usage
if __name__ == "__main__":
    try:
        manager = ClientManager()
        
        # Add a new client
        manager.add_client(
            client_id="cli001",
            name="Acme Corporation",
            email="contact@acme.com",
            phone="+55 11 98765-4321",
            services=["tax filing", "payroll"],
            tax_id="12.345.678/0001-90",
            address="123 Business Ave, São Paulo"
        )
        
        # Update client
        manager.update_client("cli001", phone="+55 11 91234-5678")
        
        # Get client
        client = manager.get_client("cli001")
        print(f"Client details: {client}")
        
        # List all clients
        print("All clients:")
        for client in manager.list_clients():
            print(client)
            
        # Search clients
        print("Search results:")
        for client in manager.search_clients("acme"):
            print(client)
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
