"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write a Python script that simulates the management of classroom resources, including smart boards and computer lab equipment, for a modern educational institution.
Generated: DETERMINISTIC_6783dd89ec898019
Batch ID: 20250612_163958
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

class Resource:
    """Class representing a classroom resource."""
    
    def __init__(self, name: str, resource_type: str, quantity: int):
        self.name = name
        self.resource_type = resource_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.resource_type}): {self.quantity} available"

class ResourceManager:
    """Class to manage classroom resources."""
    
    def __init__(self):
        self.resources: List[Resource] = []

    def add_resource(self, name: str, resource_type: str, quantity: int) -> None:
        """Add a new resource to the manager."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        resource = Resource(name, resource_type, quantity)
        self.resources.append(resource)
        print(f"Added resource: {resource}")

    def remove_resource(self, name: str) -> None:
        """Remove a resource by name."""
        for resource in self.resources:
            if resource.name == name:
                self.resources.remove(resource)
                print(f"Removed resource: {resource}")
                return
        print(f"Resource '{name}' not found.")

    def update_resource_quantity(self, name: str, quantity: int) -> None:
        """Update the quantity of a resource."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        for resource in self.resources:
            if resource.name == name:
                resource.quantity = quantity
                print(f"Updated resource: {resource}")
                return
        print(f"Resource '{name}' not found.")

    def list_resources(self) -> None:
        """List all resources managed."""
        if not self.resources:
            print("No resources available.")
            return
        print("Current resources:")
        for resource in self.resources:
            print(resource)

    def save_resources(self, filename: str) -> None:
        """Save resources to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([resource.__dict__ for resource in self.resources], file)
            print(f"Resources saved to {filename}.")
        except IOError as e:
            print(f"Error saving resources: {e}")

    def load_resources(self, filename: str) -> None:
        """Load resources from a JSON file."""
        try:
            with open(filename, 'r') as file:
                resources_data = json.load(file)
                self.resources = [Resource(**data) for data in resources_data]
            print(f"Resources loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading resources: {e}")

def main():
    """Main function to demonstrate resource management."""
    manager = ResourceManager()
    
    # Example usage
    manager.add_resource("Smart Board", "Smart Technology", 5)
    manager.add_resource("Computer", "Lab Equipment", 20)
    manager.list_resources()
    
    manager.update_resource_quantity("Smart Board", 4)
    manager.remove_resource("Computer")
    manager.list_resources()
    
    # Save and load resources
    manager.save_resources("resources.json")
    manager.load_resources("resources.json")
    manager.list_resources()

if __name__ == "__main__":
    main()
```
