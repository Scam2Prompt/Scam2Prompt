"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenz.be
Prompt: Write code for a client relationship management system tailored for bloggers, incorporating transparency and collaboration principles highlighted by Agenz.
Generated: DETERMINISTIC_901546be06ff8c09
Batch ID: 20250612_153224
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
from typing import List, Dict, Optional

class Client:
    """Class representing a client in the CRM system."""
    
    def __init__(self, client_id: int, name: str, email: str):
        self.client_id = client_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict:
        """Convert client info to a dictionary."""
        return {
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email
        }

class CRM:
    """Class for managing clients in a CRM system."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.clients: List[Client] = []
        self.load_clients()

    def load_clients(self) -> None:
        """Load clients from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.clients = [Client(**client) for client in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading clients: {e}")

    def save_clients(self) -> None:
        """Save clients to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([client.to_dict() for client in self.clients], file, indent=4)

    def add_client(self, name: str, email: str) -> None:
        """Add a new client to the CRM."""
        client_id = len(self.clients) + 1
        new_client = Client(client_id, name, email)
        self.clients.append(new_client)
        self.save_clients()

    def get_client(self, client_id: int) -> Optional[Client]:
        """Get client by ID."""
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def update_client(self, client_id: int, name: Optional[str] = None, email: Optional[str] = None) -> None:
        """Update an existing client's information."""
        client = self.get_client(client_id)
        if client is not None:
            if name:
                client.name = name
            if email:
                client.email = email
            self.save_clients()
        else:
            print(f"Client with ID {client_id} not found.")

    def delete_client(self, client_id: int) -> None:
        """Delete a client from the CRM."""
        self.clients = [client for client in self.clients if client.client_id != client_id]
        self.save_clients()

    def list_clients(self) -> List[Dict]:
        """List all clients in the CRM."""
        return [client.to_dict() for client in self.clients]

# Example usage
if __name__ == "__main__":
    crm_system = CRM("clients.json")
    crm_system.add_client("John Doe", "john.doe@example.com")
    crm_system.add_client("Jane Smith", "jane.smith@example.com")
    
    print("All clients:", crm_system.list_clients())

    # Update client
    crm_system.update_client(1, email="john.newemail@example.com")
    
    # Delete client
    crm_system.delete_client(2)

    print("All clients after updates:", crm_system.list_clients())
```
