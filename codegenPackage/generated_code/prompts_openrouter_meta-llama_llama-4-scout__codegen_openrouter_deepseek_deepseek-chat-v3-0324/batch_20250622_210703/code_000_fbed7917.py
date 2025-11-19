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
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


class ServiceType(Enum):
    """Enum representing different types of services offered."""
    FURNITURE_MOVING = auto()  # نقل عفش
    KITCHEN_INSTALLATION = auto()  # تركيب مطابخ
    STORAGE = auto()


@dataclass
class Service:
    """Dataclass representing a service with its details."""
    service_type: ServiceType
    location: str
    base_price: float
    additional_fees: Dict[str, float] = field(default_factory=dict)


class ServiceManager:
    """Class to manage company services including pricing and operations."""

    def __init__(self):
        self.services: List[Service] = []

    def add_service(self, service: Service) -> None:
        """Add a new service to the manager."""
        self.services.append(service)

    def remove_service(self, service_type: ServiceType, location: str) -> bool:
        """Remove a service by type and location."""
        for i, service in enumerate(self.services):
            if service.service_type == service_type and service.location == location:
                self.services.pop(i)
                return True
        return False

    def get_service(self, service_type: ServiceType, location: str) -> Optional[Service]:
        """Get a service by type and location."""
        for service in self.services:
            if service.service_type == service_type and service.location == location:
                return service
        return None

    def calculate_total_price(self, service_type: ServiceType, location: str, extras: List[str] = None) -> float:
        """
        Calculate total price for a service including additional fees.
        
        Args:
            service_type: Type of service.
            location: Location where service is provided.
            extras: List of additional services requested.
        
        Returns:
            Total price including base price and additional fees.
        
        Raises:
            ValueError: If service is not found.
        """
        service = self.get_service(service_type, location)
        if not service:
            raise ValueError(f"Service {service_type.name} in {location} not found.")

        total = service.base_price
        if extras:
            for extra in extras:
                if extra in service.additional_fees:
                    total += service.additional_fees[extra]
        return total

    def save_to_file(self, filename: str) -> None:
        """Save services to a JSON file."""
        data = []
        for service in self.services:
            service_data = {
                "service_type": service.service_type.name,
                "location": service.location,
                "base_price": service.base_price,
                "additional_fees": service.additional_fees
            }
            data.append(service_data)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load services from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.services = []
                for item in data:
                    service_type = ServiceType[item["service_type"]]
                    service = Service(
                        service_type=service_type,
                        location=item["location"],
                        base_price=item["base_price"],
                        additional_fees=item.get("additional_fees", {})
                    )
                    self.services.append(service)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty services.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with empty services.")
        except KeyError as e:
            print(f"Invalid key in JSON data: {e}. Starting with empty services.")


# Example usage
if __name__ == "__main__":
    manager = ServiceManager()

    # Add services
    manager.add_service(Service(
        service_type=ServiceType.FURNITURE_MOVING,
        location="الدمام",
        base_price=500.0,
        additional_fees={"heavy_items": 100.0, "stairs": 50.0}
    ))

    manager.add_service(Service(
        service_type=ServiceType.KITCHEN_INSTALLATION,
        location="الخبر",
        base_price=800.0,
        additional_fees={"custom_cabinets": 200.0, "appliance_installation": 150.0}
    ))

    # Calculate price
    try:
        price = manager.calculate_total_price(
            ServiceType.FURNITURE_MOVING,
            "الدمام",
            ["heavy_items", "stairs"]
        )
        print(f"Total price: {price}")
    except ValueError as e:
        print(e)

    # Save and load from file
    manager.save_to_file("services.json")
    manager.load_from_file("services.json")
```
