"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Develop a Python script to assist in real estate brokerage tasks, including property listing, client management, and transaction tracking, inspired by the solutions provided by Global Service Consulting.
Generated: DETERMINISTIC_3601e1d6a8d07651
Batch ID: 20250612_153224
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

class RealEstateBrokerage:
    def __init__(self, data_file: str):
        """
        Initializes the RealEstateBrokerage with a specified data file.
        
        :param data_file: Path to the JSON file for storing data.
        """
        self.data_file = data_file
        self.properties = []
        self.clients = []
        self.transactions = []
        self.load_data()

    def load_data(self):
        """Loads data from the JSON file into the properties, clients, and transactions lists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.properties = data.get('properties', [])
                self.clients = data.get('clients', [])
                self.transactions = data.get('transactions', [])
        else:
            self.save_data()  # Create a new file if it doesn't exist

    def save_data(self):
        """Saves the current state of properties, clients, and transactions to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump({
                'properties': self.properties,
                'clients': self.clients,
                'transactions': self.transactions
            }, file, indent=4)

    def add_property(self, property_info: Dict[str, Any]):
        """
        Adds a new property to the listing.
        
        :param property_info: A dictionary containing property details.
        """
        self.properties.append(property_info)
        self.save_data()

    def add_client(self, client_info: Dict[str, Any]):
        """
        Adds a new client to the client management system.
        
        :param client_info: A dictionary containing client details.
        """
        self.clients.append(client_info)
        self.save_data()

    def record_transaction(self, transaction_info: Dict[str, Any]):
        """
        Records a new transaction.
        
        :param transaction_info: A dictionary containing transaction details.
        """
        self.transactions.append(transaction_info)
        self.save_data()

    def list_properties(self) -> List[Dict[str, Any]]:
        """Returns a list of all properties."""
        return self.properties

    def list_clients(self) -> List[Dict[str, Any]]:
        """Returns a list of all clients."""
        return self.clients

    def list_transactions(self) -> List[Dict[str, Any]]:
        """Returns a list of all transactions."""
        return self.transactions

if __name__ == "__main__":
    # Example usage of the RealEstateBrokerage class
    brokerage = RealEstateBrokerage('real_estate_data.json')

    # Adding a property
    brokerage.add_property({
        'id': 1,
        'address': '123 Main St',
        'price': 250000,
        'type': 'Single Family Home'
    })

    # Adding a client
    brokerage.add_client({
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '555-1234'
    })

    # Recording a transaction
    brokerage.record_transaction({
        'id': 1,
        'property_id': 1,
        'client_id': 1,
        'date': '2023-10-01',
        'amount': 250000
    })

    # Listing all properties, clients, and transactions
    print("Properties:", brokerage.list_properties())
    print("Clients:", brokerage.list_clients())
    print("Transactions:", brokerage.list_transactions())
```
