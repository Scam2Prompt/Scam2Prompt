"""
Generated Code Metadata:
========================
Original URL: https://paxosrew.com
Prompt: "Create a software tool to help customers choose the correct automotive electrical components (e.g., alternators, batteries) for their vehicle make and model."
Generated: DETERMINISTIC_7a847f2058dd772b
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Vehicle:
    """Class representing a vehicle with make, model, and year."""
    
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Component:
    """Class representing an automotive electrical component."""
    
    def __init__(self, name: str, compatible_vehicles: list):
        self.name = name
        self.compatible_vehicles = compatible_vehicles

    def is_compatible(self, vehicle: Vehicle) -> bool:
        """Check if the component is compatible with the given vehicle."""
        return vehicle in self.compatible_vehicles

class ComponentSelector:
    """Class to select the correct automotive electrical components for a vehicle."""
    
    def __init__(self, components_data: str):
        self.components = self.load_components(components_data)

    def load_components(self, components_data: str) -> list:
        """Load components from a JSON string."""
        try:
            components_list = json.loads(components_data)
            return [Component(item['name'], [Vehicle(**v) for v in item['compatible_vehicles']]) for item in components_list]
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError("Invalid components data format") from e

    def find_compatible_components(self, vehicle: Vehicle) -> list:
        """Find all components compatible with the given vehicle."""
        compatible_components = []
        for component in self.components:
            if component.is_compatible(vehicle):
                compatible_components.append(component.name)
        return compatible_components

def main():
    # Sample JSON data for components
    components_data = '''
    [
        {
            "name": "Alternator A",
            "compatible_vehicles": [
                {"make": "Toyota", "model": "Camry", "year": 2020},
                {"make": "Honda", "model": "Accord", "year": 2020}
            ]
        },
        {
            "name": "Battery B",
            "compatible_vehicles": [
                {"make": "Toyota", "model": "Camry", "year": 2020},
                {"make": "Ford", "model": "F-150", "year": 2019}
            ]
        }
    ]
    '''

    # Create a vehicle instance
    vehicle = Vehicle("Toyota", "Camry", 2020)

    # Initialize the component selector with the sample data
    selector = ComponentSelector(components_data)

    # Find compatible components for the vehicle
    compatible_components = selector.find_compatible_components(vehicle)

    # Output the results
    if compatible_components:
        print(f"Compatible components for {vehicle}: {', '.join(compatible_components)}")
    else:
        print(f"No compatible components found for {vehicle}.")

if __name__ == "__main__":
    main()
```
