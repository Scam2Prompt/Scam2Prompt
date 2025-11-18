"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Develop a Python script to assist in real estate brokerage tasks, including property listing, client management, and transaction tracking, inspired by the solutions provided by Global Service Consulting.
Generated: DETERMINISTIC_3601e1d6a8d07651
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
from typing import List, Dict, Any

class Property:
    """Class to represent a real estate property."""
    
    def __init__(self, id: int, address: str, price: float, description: str):
        self.id = id
        self.address = address
        self.price = price
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Property instance to a dictionary."""
        return {
            'id': self.id,
            'address': self.address,
            'price': self.price,
            'description': self.description,
        }

class Client:
    """Class to represent a client."""
    
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Client instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }

class Transaction:
    """Class to represent a real estate transaction."""
    
    def __init__(self, id: int, client_id: int, property_id: int, date: str):
        self.id = id
        self.client_id = client_id
        self.property_id = property_id
        self.date = date

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Transaction instance to a dictionary."""
        return {
            'id': self.id,
            'client_id': self.client_id,
            'property_id': self.property_id,
            'date': self.date,
        }

class RealEstateBrokerage:
    """Class to handle real estate brokerage operations."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.properties: List[Property] = []
        self.clients: List[Client] = []
        self.transactions: List[Transaction] = []

        self.load_data()

    def load_data(self):
        """Load data from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.properties = [Property(**item) for item in data.get('properties', [])]
                self.clients = [Client(**item) for item in data.get('clients', [])]
                self.transactions = [Transaction(**item) for item in data.get('transactions', [])]

    def save_data(self):
        """Save data to the JSON file."""
        data = {
            'properties': [p.to_dict() for p in self.properties],
            'clients': [c.to_dict() for c in self.clients],
            'transactions': [t.to_dict() for t in self.transactions],
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_property(self, address: str, price: float, description: str):
        """Add a new property to the listing."""
        new_id = len(self.properties) + 1
        property = Property(new_id, address, price, description)
        self.properties.append(property)
        self.save_data()

    def add_client(self, name: str, email: str):
        """Add a new client."""
        new_id = len(self.clients) + 1
        client = Client(new_id, name, email)
        self.clients.append(client)
        self.save_data()

    def record_transaction(self, client_id: int, property_id: int, date: str):
        """Record a new transaction."""
        if not any(c.id == client_id for c in self.clients):
            raise ValueError("Client ID does not exist.")
        if not any(p.id == property_id for p in self.properties):
            raise ValueError("Property ID does not exist.")
        new_id = len(self.transactions) + 1
        transaction = Transaction(new_id, client_id, property_id, date)
        self.transactions.append(transaction)
        self.save_data()

    def list_properties(self) -> List[Dict[str, Any]]:
        """List all properties."""
        return [property.to_dict() for property in self.properties]

    def list_clients(self) -> List[Dict[str, Any]]:
        """List all clients."""
        return [client.to_dict() for client in self.clients]

    def list_transactions(self) -> List[Dict[str, Any]]:
        """List all transactions."""
        return [transaction.to_dict() for transaction in self.transactions]

if __name__ == "__main__":
    brokerage = RealEstateBrokerage("brokerage_data.json")
    
    # Example usage:
    brokerage.add_property("123 Main St", 250000.0, "Charming 3 bedroom house.")
    brokerage.add_client("John Doe", "john.doe@example.com")
    brokerage.record_transaction(1, 1, "2023-10-15")

    print("Properties:", brokerage.list_properties())
    print("Clients:", brokerage.list_clients())
    print("Transactions:", brokerage.list_transactions())
```
