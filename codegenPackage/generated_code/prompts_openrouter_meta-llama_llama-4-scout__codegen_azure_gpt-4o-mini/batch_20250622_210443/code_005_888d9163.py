"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Write a Python script that can be used to manage a marketplace for creative services, similar to Kroo Nation's commerce platform.
Generated: DETERMINISTIC_888d9163a870d224
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from typing import List, Dict, Optional

class Service:
    """Class representing a creative service offered in the marketplace."""
    
    def __init__(self, title: str, description: str, price: float):
        self.id = str(uuid.uuid4())  # Unique identifier for the service
        self.title = title
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the service instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price
        }

class Marketplace:
    """Class representing the marketplace for creative services."""
    
    def __init__(self):
        self.services: List[Service] = []  # List to store services

    def add_service(self, title: str, description: str, price: float) -> Service:
        """Add a new service to the marketplace."""
        if price < 0:
            raise ValueError("Price must be a non-negative value.")
        service = Service(title, description, price)
        self.services.append(service)
        return service

    def remove_service(self, service_id: str) -> bool:
        """Remove a service from the marketplace by its ID."""
        for service in self.services:
            if service.id == service_id:
                self.services.remove(service)
                return True
        return False

    def list_services(self) -> List[Dict]:
        """List all services in the marketplace."""
        return [service.to_dict() for service in self.services]

    def find_service(self, service_id: str) -> Optional[Service]:
        """Find a service by its ID."""
        for service in self.services:
            if service.id == service_id:
                return service
        return None

    def save_to_file(self, filename: str) -> None:
        """Save the current services to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_services(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load services from a JSON file."""
        try:
            with open(filename, 'r') as file:
                services_data = json.load(file)
                for service_data in services_data:
                    service = Service(
                        title=service_data['title'],
                        description=service_data['description'],
                        price=service_data['price']
                    )
                    self.services.append(service)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    marketplace = Marketplace()
    
    # Adding services
    marketplace.add_service("Graphic Design", "Custom logo design", 150.00)
    marketplace.add_service("Web Development", "Build a responsive website", 1200.00)

    # Listing services
    print("Available Services:")
    print(marketplace.list_services())

    # Saving services to a file
    marketplace.save_to_file("services.json")

    # Loading services from a file
    marketplace.load_from_file("services.json")
    print("Services loaded from file:")
    print(marketplace.list_services())
```
