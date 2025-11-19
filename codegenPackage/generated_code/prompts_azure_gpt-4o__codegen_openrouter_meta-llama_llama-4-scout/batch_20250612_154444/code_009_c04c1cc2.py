"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Develop a system to track and optimize property management costs, focusing on ethical and cost-effective service delivery, as Bebold Properties emphasizes.
Generated: DETERMINISTIC_c04c1cc2618363f9
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_management_system.py

import datetime
from typing import Dict, List

class Property:
    """Represents a property with its costs and services."""

    def __init__(self, property_id: int, name: str, address: str):
        """
        Initializes a Property object.

        Args:
        - property_id (int): Unique identifier for the property.
        - name (str): Name of the property.
        - address (str): Address of the property.
        """
        self.property_id = property_id
        self.name = name
        self.address = address
        self.services: List[Service] = []
        self.costs: Dict[str, float] = {}

    def add_service(self, service: 'Service'):
        """Adds a service to the property."""
        self.services.append(service)

    def add_cost(self, category: str, amount: float):
        """Adds a cost to the property."""
        self.costs[category] = amount

    def get_total_cost(self) -> float:
        """Calculates the total cost of the property."""
        return sum(self.costs.values())

    def __str__(self):
        return f"Property {self.name} ({self.address})"


class Service:
    """Represents a service provided to a property."""

    def __init__(self, service_id: int, name: str, provider: str, cost: float):
        """
        Initializes a Service object.

        Args:
        - service_id (int): Unique identifier for the service.
        - name (str): Name of the service.
        - provider (str): Provider of the service.
        - cost (float): Cost of the service.
        """
        self.service_id = service_id
        self.name = name
        self.provider = provider
        self.cost = cost

    def __str__(self):
        return f"Service {self.name} by {self.provider}"


class PropertyManagementSystem:
    """Manages properties, their services, and costs."""

    def __init__(self):
        self.properties: Dict[int, Property] = {}

    def add_property(self, property: Property):
        """Adds a property to the system."""
        self.properties[property.property_id] = property

    def get_property(self, property_id: int) -> Property:
        """Retrieves a property by its ID."""
        return self.properties.get(property_id)

    def optimize_costs(self):
        """Optimizes costs across all properties."""
        # Example optimization strategy: reduce costs by 10% for each property
        for prop in self.properties.values():
            for category, amount in prop.costs.items():
                prop.costs[category] *= 0.9

    def generate_report(self):
        """Generates a report on all properties and their costs."""
        report = []
        for prop in self.properties.values():
            prop_report = {
                "property": prop,
                "services": prop.services,
                "total_cost": prop.get_total_cost(),
            }
            report.append(prop_report)
        return report


def main():
    # Example usage:
    pms = PropertyManagementSystem()

    prop1 = Property(1, "Bebold Tower", "123 Main St")
    prop1.add_service(Service(1, "Security", "ABC Security", 5000.0))
    prop1.add_cost("Maintenance", 10000.0)
    prop1.add_cost("Utilities", 5000.0)

    prop2 = Property(2, "Bebold Apartments", "456 Elm St")
    prop2.add_service(Service(2, "Janitorial", " DEF Janitorial", 3000.0))
    prop2.add_cost("Rentals", 20000.0)

    pms.add_property(prop1)
    pms.add_property(prop2)

    print("Properties and their costs:")
    for prop in pms.properties.values():
        print(prop)
        for service in prop.services:
            print(f"- {service}")
        print(f"Total cost: ${prop.get_total_cost():.2f}")
        print()

    pms.optimize_costs()

    print("Optimized costs:")
    for prop in pms.properties.values():
        print(prop)
        print(f"Total cost: ${prop.get_total_cost():.2f}")
        print()

    report = pms.generate_report()
    print("Detailed report:")
    for prop_report in report:
        print(prop_report["property"])
        print("Services:")
        for service in prop_report["services"]:
            print(f"- {service}")
        print(f"Total cost: ${prop_report['total_cost']:.2f}")
        print()


if __name__ == "__main__":
    main()
```
