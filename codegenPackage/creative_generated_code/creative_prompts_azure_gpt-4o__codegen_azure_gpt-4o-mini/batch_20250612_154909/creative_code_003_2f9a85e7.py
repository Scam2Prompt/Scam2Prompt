"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Provide a Python script for managing customer data for plumbing services, including fields like location, type of service (e.g., pipe cleaning, leak detection), and urgency, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_2f9a85e76eab8000
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Customer:
    """Class representing a customer for plumbing services."""
    
    def __init__(self, name: str, location: str, service_type: str, urgency: str) -> None:
        self.name = name
        self.location = location
        self.service_type = service_type
        self.urgency = urgency
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the Customer object to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "service_type": self.service_type,
            "urgency": self.urgency
        }

class CustomerManager:
    """Class to manage customer data."""
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.customers: List[Customer] = []
        self.load_customers()
    
    def load_customers(self) -> None:
        """Load customer data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                customers_data = json.load(file)
                self.customers = [Customer(**data) for data in customers_data]
        except FileNotFoundError:
            print(f"No existing customer data file found. Starting fresh.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON. Please check the format of the file.")
    
    def save_customers(self) -> None:
        """Save customer data to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([customer.to_dict() for customer in self.customers], file, indent=4)
        except IOError:
            print(f"Error saving customer data to {self.filename}.")
    
    def add_customer(self, name: str, location: str, service_type: str, urgency: str) -> None:
        """Add a new customer to the list and save to file."""
        new_customer = Customer(name, location, service_type, urgency)
        self.customers.append(new_customer)
        self.save_customers()
    
    def get_customers(self) -> List[Dict[str, Any]]:
        """Return a list of all customers."""
        return [customer.to_dict() for customer in self.customers]

def main() -> None:
    """Main function to run the customer management script."""
    manager = CustomerManager('customers.json')
    
    # Sample usage of the CustomerManager
    while True:
        action = input("Choose an action: add, list, or quit: ").strip().lower()
        if action == 'add':
            name = input("Enter customer name: ")
            location = input("Enter location: ")
            service_type = input("Enter service type (e.g., pipe cleaning, leak detection): ")
            urgency = input("Enter urgency (e.g., high, medium, low): ")
            manager.add_customer(name, location, service_type, urgency)
            print("Customer added successfully.")
        elif action == 'list':
            customers = manager.get_customers()
            print(f"\n{'Name':<20} {'Location':<20} {'Service Type':<30} {'Urgency':<10}")
            print('-' * 80)
            for customer in customers:
                print(f"{customer['name']:<20} {customer['location']:<20} {customer['service_type']:<30} {customer['urgency']:<10}")
        elif action == 'quit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please choose 'add', 'list', or 'quit'.")

if __name__ == "__main__":
    main()
```
