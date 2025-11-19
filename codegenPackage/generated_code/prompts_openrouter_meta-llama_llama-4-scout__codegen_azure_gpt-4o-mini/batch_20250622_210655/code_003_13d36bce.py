"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Develop a code for a basic CRM system to manage customer information and service requests for a business offering installation, reparación, and mantenimiento of equipos de osmosis inversa in Murcia.
Generated: DETERMINISTIC_13d36bce5f552e17
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
from typing import List, Dict, Optional

class Customer:
    """Class to represent a customer in the CRM system."""
    
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.service_requests: List[Dict] = []

    def add_service_request(self, request: Dict):
        """Add a service request to the customer's record."""
        self.service_requests.append(request)

    def to_dict(self) -> Dict:
        """Convert the customer object to a dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "service_requests": self.service_requests
        }

class CRM:
    """Class to manage the customer relationship management system."""
    
    def __init__(self):
        self.customers: Dict[int, Customer] = {}
        self.next_customer_id = 1

    def add_customer(self, name: str, email: str, phone: str) -> int:
        """Add a new customer to the CRM."""
        customer = Customer(self.next_customer_id, name, email, phone)
        self.customers[self.next_customer_id] = customer
        self.next_customer_id += 1
        return customer.customer_id

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by their ID."""
        return self.customers.get(customer_id)

    def add_service_request(self, customer_id: int, request: Dict) -> bool:
        """Add a service request for a specific customer."""
        customer = self.get_customer(customer_id)
        if customer:
            customer.add_service_request(request)
            return True
        return False

    def save_to_file(self, filename: str):
        """Save the CRM data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({cid: customer.to_dict() for cid, customer in self.customers.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load CRM data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for cid, customer_data in data.items():
                    customer = Customer(customer_data['customer_id'], customer_data['name'], 
                                        customer_data['email'], customer_data['phone'])
                    customer.service_requests = customer_data['service_requests']
                    self.customers[customer.customer_id] = customer
                    self.next_customer_id = max(self.next_customer_id, customer.customer_id + 1)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    crm = CRM()
    customer_id = crm.add_customer("Juan Pérez", "juan.perez@example.com", "123456789")
    crm.add_service_request(customer_id, {"type": "installation", "date": "2023-10-01", "details": "Instalación de sistema de osmosis inversa."})
    
    # Save CRM data to a file
    crm.save_to_file("crm_data.json")
    
    # Load CRM data from a file
    crm.load_from_file("crm_data.json")
    
    # Print customer information
    customer = crm.get_customer(customer_id)
    if customer:
        print(customer.to_dict())
```
