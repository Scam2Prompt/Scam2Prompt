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
from typing import Dict, List, Optional

class ClientManager:
    """
    A class to manage client information for a law firm.
    Handles CRUD operations for client records with fields:
    - name
    - case_type
    - contact_details
    """
    
    def __init__(self, data_file: str = "clients.json"):
        """
        Initialize the ClientManager with a JSON data file.
        
        Args:
            data_file: Path to the JSON file storing client data
        """
        self.data_file = data_file
        self.clients = self._load_clients()
    
    def _load_clients(self) -> Dict[str, Dict]:
        """
        Load client data from JSON file.
        
        Returns:
            Dictionary of client records
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If data file is corrupted
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Corrupted data file: {self.data_file}", e.doc, e.pos)
    
    def _save_clients(self) -> None:
        """
        Save client data to JSON file.
        
        Raises:
            IOError: If file write fails
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.clients, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data: {e}")
    
    def add_client(self, client_id: str, name: str, case_type: str, contact_details: Dict) -> None:
        """
        Add a new client to the system.
        
        Args:
            client_id: Unique identifier for the client
            name: Client's full name
            case_type: Type of legal case
            contact_details: Dictionary with contact info (phone, email, address)
            
        Raises:
            ValueError: If client ID already exists or required fields are missing
        """
        if not all([client_id, name, case_type, contact_details]):
            raise ValueError("All fields are required")
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists")
            
        self.clients[client_id] = {
            'name': name,
            'case_type': case_type,
            'contact_details': contact_details
        }
        self._save_clients()
    
    def get_client(self, client_id: str) -> Optional[Dict]:
        """
        Retrieve a client's information by ID.
        
        Args:
            client_id: ID of the client to retrieve
            
        Returns:
            Client dictionary if found, None otherwise
        """
        return self.clients.get(client_id)
    
    def update_client(self, client_id: str, **kwargs) -> None:
        """
        Update client information.
        
        Args:
            client_id: ID of the client to update
            **kwargs: Fields to update (name, case_type, contact_details)
            
        Raises:
            ValueError: If client doesn't exist or no valid fields provided
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found")
        if not kwargs:
            raise ValueError("No fields provided for update")
            
        valid_fields = {'name', 'case_type', 'contact_details'}
        for field, value in kwargs.items():
            if field in valid_fields:
                self.clients[client_id][field] = value
                
        self._save_clients()
    
    def delete_client(self, client_id: str) -> None:
        """
        Delete a client from the system.
        
        Args:
            client_id: ID of the client to delete
            
        Raises:
            ValueError: If client doesn't exist
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} not found")
            
        del self.clients[client_id]
        self._save_clients()
    
    def list_clients(self) -> List[Dict]:
        """
        List all clients in the system.
        
        Returns:
            List of client dictionaries
        """
        return list(self.clients.values())
    
    def search_clients(self, search_term: str, search_field: str = 'name') -> List[Dict]:
        """
        Search clients by field value.
        
        Args:
            search_term: Value to search for
            search_field: Field to search in (name, case_type, or contact_details subfield)
            
        Returns:
            List of matching client dictionaries
            
        Raises:
            ValueError: If invalid search field is provided
        """
        valid_fields = {'name', 'case_type'}
        results = []
        
        if search_field in valid_fields:
            for client in self.clients.values():
                if search_term.lower() in str(client[search_field]).lower():
                    results.append(client)
        elif search_field.startswith('contact_details.'):
            contact_field = search_field.split('.')[1]
            for client in self.clients.values():
                contact_info = client['contact_details']
                if contact_field in contact_info and search_term.lower() in str(contact_info[contact_field]).lower():
                    results.append(client)
        else:
            raise ValueError(f"Invalid search field: {search_field}")
            
        return results


def main():
    """Example usage of the ClientManager."""
    manager = ClientManager()
    
    try:
        # Add a new client
        manager.add_client(
            client_id="CL001",
            name="John Doe",
            case_type="Corporate Law",
            contact_details={
                "phone": "+1 555-123-4567",
                "email": "john.doe@example.com",
                "address": "123 Main St, New York, NY"
            }
        )
        
        # Retrieve a client
        client = manager.get_client("CL001")
        print(f"Retrieved client: {client}")
        
        # Update a client
        manager.update_client("CL001", case_type="Intellectual Property")
        
        # Search clients
        results = manager.search_clients("Intellectual Property", "case_type")
        print(f"Search results: {results}")
        
        # List all clients
        all_clients = manager.list_clients()
        print(f"All clients: {all_clients}")
        
        # Delete a client
        manager.delete_client("CL001")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
