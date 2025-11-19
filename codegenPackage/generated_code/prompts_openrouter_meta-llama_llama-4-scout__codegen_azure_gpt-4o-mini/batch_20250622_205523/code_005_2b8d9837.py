"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: "Develop a basic customer relationship management (CRM) system for a used car dealership like 縁陣, including modules for client information, vehicle history, and service records."
Generated: DETERMINISTIC_2b8d9837a1c14919
Batch ID: 20250622_205523
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

    def to_dict(self) -> Dict:
        """Convert the customer object to a dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

class Vehicle:
    """Class to represent a vehicle in the CRM system."""
    
    def __init__(self, vin: str, make: str, model: str, year: int):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.service_records: List[Dict] = []

    def add_service_record(self, service: Dict) -> None:
        """Add a service record to the vehicle."""
        self.service_records.append(service)

    def to_dict(self) -> Dict:
        """Convert the vehicle object to a dictionary."""
        return {
            "vin": self.vin,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "service_records": self.service_records
        }

class CRM:
    """Class to manage the CRM system for the dealership."""
    
    def __init__(self):
        self.customers: Dict[int, Customer] = {}
        self.vehicles: Dict[str, Vehicle] = {}

    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the CRM."""
        if customer.customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        self.customers[customer.customer_id] = customer

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a new vehicle to the CRM."""
        if vehicle.vin in self.vehicles:
            raise ValueError("Vehicle VIN already exists.")
        self.vehicles[vehicle.vin] = vehicle

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by their ID."""
        return self.customers.get(customer_id)

    def get_vehicle(self, vin: str) -> Optional[Vehicle]:
        """Retrieve a vehicle by its VIN."""
        return self.vehicles.get(vin)

    def save_to_file(self, filename: str) -> None:
        """Save the CRM data to a JSON file."""
        data = {
            "customers": [customer.to_dict() for customer in self.customers.values()],
            "vehicles": [vehicle.to_dict() for vehicle in self.vehicles.values()]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load the CRM data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for customer_data in data.get("customers", []):
                    customer = Customer(**customer_data)
                    self.add_customer(customer)
                for vehicle_data in data.get("vehicles", []):
                    vehicle = Vehicle(**vehicle_data)
                    self.add_vehicle(vehicle)
        except FileNotFoundError:
            print("File not found. Starting with an empty CRM.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")

# Example usage
if __name__ == "__main__":
    crm = CRM()
    
    # Adding a customer
    customer1 = Customer(customer_id=1, name="John Doe", email="john@example.com", phone="123-456-7890")
    crm.add_customer(customer1)

    # Adding a vehicle
    vehicle1 = Vehicle(vin="1HGCM82633A123456", make="Honda", model="Accord", year=2020)
    crm.add_vehicle(vehicle1)

    # Adding a service record
    vehicle1.add_service_record({"date": "2023-01-15", "service": "Oil Change", "cost": 50})

    # Save CRM data to a file
    crm.save_to_file("crm_data.json")

    # Load CRM data from a file
    crm.load_from_file("crm_data.json")
```
