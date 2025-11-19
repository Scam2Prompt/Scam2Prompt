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
import datetime

class Component:
    """
    Represents a generic component in the manufacturing system.
    """
    def __init__(self, name, component_id):
        """
        Initializes a component with a name and unique ID.
        :param name: Name of the component (e.g., Brake Cylinder, Reservoir)
        :param component_id: Unique identifier for the component
        """
        self.name = name
        self.component_id = component_id
        self.production_date = datetime.datetime.now()
        self.status = "In Production"

    def mark_as_completed(self):
        """
        Marks the component as completed.
        """
        self.status = "Completed"

    def __str__(self):
        """
        Returns a string representation of the component.
        """
        return f"Component: {self.name}, ID: {self.component_id}, Status: {self.status}, Production Date: {self.production_date}"


class ManufacturingManagementSystem:
    """
    Tracks the production of components in the manufacturing system.
    """
    def __init__(self):
        """
        Initializes the manufacturing management system with an empty list of components.
        """
        self.components = []

    def add_component(self, name, component_id):
        """
        Adds a new component to the system.
        :param name: Name of the component
        :param component_id: Unique identifier for the component
        """
        if any(component.component_id == component_id for component in self.components):
            raise ValueError(f"Component ID {component_id} already exists.")
        new_component = Component(name, component_id)
        self.components.append(new_component)

    def mark_component_as_completed(self, component_id):
        """
        Marks a component as completed based on its ID.
        :param component_id: Unique identifier for the component
        """
        for component in self.components:
            if component.component_id == component_id:
                component.mark_as_completed()
                return
        raise ValueError(f"Component ID {component_id} not found.")

    def list_components(self):
        """
        Lists all components in the system.
        :return: List of string representations of components
        """
        return [str(component) for component in self.components]

    def get_component_by_id(self, component_id):
        """
        Retrieves a component by its ID.
        :param component_id: Unique identifier for the component
        :return: Component object
        """
        for component in self.components:
            if component.component_id == component_id:
                return component
        raise ValueError(f"Component ID {component_id} not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the manufacturing management system
        system = ManufacturingManagementSystem()

        # Add components
        system.add_component("Brake Cylinder", "BC001")
        system.add_component("Reservoir", "RS001")

        # List all components
        print("All Components:")
        for component in system.list_components():
            print(component)

        # Mark a component as completed
        system.mark_component_as_completed("BC001")

        # Retrieve a specific component by ID
        print("\nComponent Details:")
        print(system.get_component_by_id("BC001"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
