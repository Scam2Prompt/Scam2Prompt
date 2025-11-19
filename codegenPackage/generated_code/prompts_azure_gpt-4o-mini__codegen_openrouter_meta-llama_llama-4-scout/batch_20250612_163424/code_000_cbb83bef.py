"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Generate a code snippet for a manufacturing management system that tracks the production of brake system components like brake cylinders and reservoirs, as described by PEW Engineering Pvt. Ltd.
Generated: DETERMINISTIC_cbb83beff6365c3d
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# manufacturing_management_system.py

from enum import Enum
from typing import Dict, List

class ComponentType(str, Enum):
    """ Enum for brake system component types """
    BRAKE_CYLINDER = "Brake Cylinder"
    BRAKE_RESERVOIR = "Brake Reservoir"

class Component:
    """ Represents a brake system component """

    def __init__(self, component_type: ComponentType, part_number: str, quantity: int):
        """
        Initializes a Component object

        Args:
        - component_type (ComponentType): Type of the component
        - part_number (str): Part number of the component
        - quantity (int): Quantity of the component produced
        """
        self.component_type = component_type
        self.part_number = part_number
        self.quantity = quantity

    def __str__(self):
        return f"{self.component_type.value} - {self.part_number}, Quantity: {self.quantity}"

class ProductionLine:
    """ Represents a production line for brake system components """

    def __init__(self):
        self.components: Dict[str, Component] = {}

    def add_component(self, component: Component):
        """
        Adds a component to the production line

        Args:
        - component (Component): Component to add
        """
        if component.part_number in self.components:
            print(f"Component with part number {component.part_number} already exists. Updating quantity.")
            self.components[component.part_number].quantity += component.quantity
        else:
            self.components[component.part_number] = component

    def remove_component(self, part_number: str):
        """
        Removes a component from the production line

        Args:
        - part_number (str): Part number of the component to remove
        """
        if part_number in self.components:
            del self.components[part_number]
        else:
            print(f"Component with part number {part_number} not found.")

    def get_component(self, part_number: str) -> Component:
        """
        Gets a component from the production line

        Args:
        - part_number (str): Part number of the component to get

        Returns:
        - Component: The component with the given part number, or None if not found
        """
        return self.components.get(part_number)

    def print_production_line(self):
        """ Prints the current state of the production line """
        for component in self.components.values():
            print(component)

class ManufacturingManagementSystem:
    """ Represents the manufacturing management system """

    def __init__(self):
        self.production_lines: Dict[str, ProductionLine] = {}

    def add_production_line(self, production_line_name: str):
        """
        Adds a production line to the system

        Args:
        - production_line_name (str): Name of the production line
        """
        if production_line_name not in self.production_lines:
            self.production_lines[production_line_name] = ProductionLine()
        else:
            print(f"Production line {production_line_name} already exists.")

    def remove_production_line(self, production_line_name: str):
        """
        Removes a production line from the system

        Args:
        - production_line_name (str): Name of the production line to remove
        """
        if production_line_name in self.production_lines:
            del self.production_lines[production_line_name]
        else:
            print(f"Production line {production_line_name} not found.")

    def get_production_line(self, production_line_name: str) -> ProductionLine:
        """
        Gets a production line from the system

        Args:
        - production_line_name (str): Name of the production line to get

        Returns:
        - ProductionLine: The production line with the given name, or None if not found
        """
        return self.production_lines.get(production_line_name)

def main():
    # Create the manufacturing management system
    system = ManufacturingManagementSystem()

    # Add a production line
    system.add_production_line("Brake System Production Line")

    # Get the production line
    production_line = system.get_production_line("Brake System Production Line")

    if production_line:
        # Add components to the production line
        production_line.add_component(Component(ComponentType.BRAKE_CYLINDER, "BC-001", 100))
        production_line.add_component(Component(ComponentType.BRAKE_RESERVOIR, "BR-001", 50))

        # Print the production line
        print("Production Line:")
        production_line.print_production_line()

        # Remove a component from the production line
        production_line.remove_component("BC-001")

        # Print the updated production line
        print("\nUpdated Production Line:")
        production_line.print_production_line()

if __name__ == "__main__":
    main()
```
