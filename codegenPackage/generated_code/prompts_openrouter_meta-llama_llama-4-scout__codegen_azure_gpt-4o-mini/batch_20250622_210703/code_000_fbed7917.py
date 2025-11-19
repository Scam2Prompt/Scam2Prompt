"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Write a Python script to manage a company's services, including installation, moving, and storage, with different pricing for various services like نقل عفش بالدمام and تركيب مطابخ بالخبر.
Generated: DETERMINISTIC_fbed791727f5578a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Service:
    """Class to represent a service offered by the company."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Service(name={self.name}, price={self.price})"


class ServiceManager:
    """Class to manage services, including installation, moving, and storage."""
    
    def __init__(self):
        self.services: Dict[str, Service] = {}

    def add_service(self, name: str, price: float) -> None:
        """Add a new service to the manager."""
        if name in self.services:
            raise ValueError(f"Service '{name}' already exists.")
        self.services[name] = Service(name, price)

    def remove_service(self, name: str) -> None:
        """Remove a service from the manager."""
        if name not in self.services:
            raise ValueError(f"Service '{name}' does not exist.")
        del self.services[name]

    def update_service_price(self, name: str, new_price: float) -> None:
        """Update the price of an existing service."""
        if name not in self.services:
            raise ValueError(f"Service '{name}' does not exist.")
        self.services[name].price = new_price

    def get_service(self, name: str) -> Optional[Service]:
        """Retrieve a service by name."""
        return self.services.get(name)

    def list_services(self) -> List[Service]:
        """List all services."""
        return list(self.services.values())

    def save_services_to_file(self, filename: str) -> None:
        """Save services to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({name: service.price for name, service in self.services.items()}, file)
        except IOError as e:
            raise RuntimeError(f"Failed to save services to file: {e}")

    def load_services_from_file(self, filename: str) -> None:
        """Load services from a JSON file."""
        try:
            with open(filename, 'r') as file:
                services_data = json.load(file)
                for name, price in services_data.items():
                    self.add_service(name, price)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load services from file: {e}")


if __name__ == "__main__":
    # Example usage of the ServiceManager
    manager = ServiceManager()
    
    # Adding services
    manager.add_service("نقل عفش بالدمام", 150.0)
    manager.add_service("تركيب مطابخ بالخبر", 200.0)

    # Listing services
    print("Available Services:")
    for service in manager.list_services():
        print(service)

    # Updating a service price
    manager.update_service_price("نقل عفش بالدمام", 175.0)

    # Saving services to a file
    manager.save_services_to_file("services.json")

    # Loading services from a file
    new_manager = ServiceManager()
    new_manager.load_services_from_file("services.json")
    print("Loaded Services:")
    for service in new_manager.list_services():
        print(service)
```
