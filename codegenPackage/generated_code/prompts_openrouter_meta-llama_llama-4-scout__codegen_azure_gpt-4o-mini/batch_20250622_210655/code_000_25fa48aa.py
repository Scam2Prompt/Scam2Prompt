"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Write a program in Python to manage and track the services provided by Fundación Munasim Kullakita to its beneficiaries, including data on the number of beneficiaries, services provided, and outcomes.
Generated: DETERMINISTIC_25fa48aa28426a30
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
from typing import List, Dict, Any

class Service:
    """Class to represent a service provided by Fundación Munasim Kullakita."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the service to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description
        }

class Beneficiary:
    """Class to represent a beneficiary of the foundation."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.services_received: List[Service] = []
        self.outcomes: List[str] = []

    def add_service(self, service: Service):
        """Add a service to the beneficiary's record."""
        self.services_received.append(service)

    def add_outcome(self, outcome: str):
        """Add an outcome to the beneficiary's record."""
        self.outcomes.append(outcome)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the beneficiary to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "services_received": [service.to_dict() for service in self.services_received],
            "outcomes": self.outcomes
        }

class Foundation:
    """Class to manage the services and beneficiaries of the foundation."""
    
    def __init__(self):
        self.beneficiaries: List[Beneficiary] = []
        self.services: List[Service] = []

    def add_service(self, service: Service):
        """Add a new service to the foundation."""
        self.services.append(service)

    def add_beneficiary(self, beneficiary: Beneficiary):
        """Add a new beneficiary to the foundation."""
        self.beneficiaries.append(beneficiary)

    def get_beneficiary_count(self) -> int:
        """Return the total number of beneficiaries."""
        return len(self.beneficiaries)

    def get_services(self) -> List[Dict[str, Any]]:
        """Return a list of all services provided by the foundation."""
        return [service.to_dict() for service in self.services]

    def get_beneficiaries_data(self) -> List[Dict[str, Any]]:
        """Return a list of all beneficiaries with their data."""
        return [beneficiary.to_dict() for beneficiary in self.beneficiaries]

    def save_data(self, filename: str):
        """Save the foundation's data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "beneficiaries": self.get_beneficiaries_data(),
                    "services": self.get_services()
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

    def load_data(self, filename: str):
        """Load the foundation's data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for service_data in data.get("services", []):
                    service = Service(service_data["name"], service_data["description"])
                    self.add_service(service)
                for beneficiary_data in data.get("beneficiaries", []):
                    beneficiary = Beneficiary(beneficiary_data["name"], beneficiary_data["age"])
                    for service_data in beneficiary_data.get("services_received", []):
                        service = Service(service_data["name"], service_data["description"])
                        beneficiary.add_service(service)
                    for outcome in beneficiary_data.get("outcomes", []):
                        beneficiary.add_outcome(outcome)
                    self.add_beneficiary(beneficiary)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    foundation = Foundation()

    # Adding services
    service1 = Service("Health Checkup", "Annual health checkup for beneficiaries.")
    service2 = Service("Educational Support", "Providing educational materials and support.")
    foundation.add_service(service1)
    foundation.add_service(service2)

    # Adding beneficiaries
    beneficiary1 = Beneficiary("Juan Perez", 30)
    beneficiary1.add_service(service1)
    beneficiary1.add_outcome("Improved health status.")
    foundation.add_beneficiary(beneficiary1)

    beneficiary2 = Beneficiary("Maria Lopez", 25)
    beneficiary2.add_service(service2)
    beneficiary2.add_outcome("Received educational materials.")
    foundation.add_beneficiary(beneficiary2)

    # Saving data to a file
    foundation.save_data("foundation_data.json")

    # Loading data from a file
    new_foundation = Foundation()
    new_foundation.load_data("foundation_data.json")
    print(new_foundation.get_beneficiary_count())
```
