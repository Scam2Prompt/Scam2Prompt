"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Write Python code to manage an inventory system for automotive components like steering terminals, brake calipers, pivots, and axial joints, with location-based tracking for cities such as Nova Prata, Bento Gonçalves, and Porto Alegre.
Generated: DETERMINISTIC_d3e6b704b414ccb3
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Component:
    """
    Represents an automotive component in the inventory.
    """
    def __init__(self, name, quantity, location):
        """
        Initialize the component with a unique ID, name, quantity, and location.
        :param name: Name of the component (e.g., 'Steering Terminal').
        :param quantity: Quantity of the component in the inventory.
        :param location: Location of the component (e.g., 'Nova Prata').
        """
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the component
        self.name = name
        self.quantity = quantity
        self.location = location

    def __str__(self):
        """
        String representation of the component.
        """
        return f"{self.name} (ID: {self.id}, Quantity: {self.quantity}, Location: {self.location})"


class InventorySystem:
    """
    Manages the inventory of automotive components with location-based tracking.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.inventory = []

    def add_component(self, name, quantity, location):
        """
        Add a new component to the inventory.
        :param name: Name of the component.
        :param quantity: Quantity of the component.
        :param location: Location of the component.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if location not in ["Nova Prata", "Bento Gonçalves", "Porto Alegre"]:
            raise ValueError(f"Invalid location: {location}")
        
        component = Component(name, quantity, location)
        self.inventory.append(component)
        print(f"Component added: {component}")

    def remove_component(self, component_id):
        """
        Remove a component from the inventory by its unique ID.
        :param component_id: The unique ID of the component to remove.
        """
        for component in self.inventory:
            if component.id == component_id:
                self.inventory.remove(component)
                print(f"Component removed: {component}")
                return
        raise ValueError(f"Component with ID {component_id} not found.")

    def update_quantity(self, component_id, new_quantity):
        """
        Update the quantity of a specific component.
        :param component_id: The unique ID of the component to update.
        :param new_quantity: The new quantity to set.
        """
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        for component in self.inventory:
            if component.id == component_id:
                component.quantity = new_quantity
                print(f"Quantity updated: {component}")
                return
        raise ValueError(f"Component with ID {component_id} not found.")

    def list_components_by_location(self, location):
        """
        List all components at a specific location.
        :param location: The location to filter components by.
        :return: A list of components at the specified location.
        """
        if location not in ["Nova Prata", "Bento Gonçalves", "Porto Alegre"]:
            raise ValueError(f"Invalid location: {location}")
        
        components = [component for component in self.inventory if component.location == location]
        if components:
            print(f"Components in {location}:")
            for component in components:
                print(component)
        else:
            print(f"No components found in {location}.")

    def find_component_by_name(self, name):
        """
        Find components by their name (case-insensitive search).
        :param name: The name of the component to search for.
        :return: A list of matching components.
        """
        matches = [component for component in self.inventory if component.name.lower() == name.lower()]
        if matches:
            print(f"Matching components for '{name}':")
            for component in matches:
                print(component)
        else:
            print(f"No components found with name '{name}'.")


# Example usage (this would be removed or moved to a separate test file in production):
if __name__ == "__main__":
    inventory = InventorySystem()

    # Adding components
    inventory.add_component("Steering Terminal", 50, "Nova Prata")
    inventory.add_component("Brake Caliper", 30, "Bento Gonçalves")
    inventory.add_component("Pivot", 20, "Porto Alegre")
    inventory.add_component("Axial Joint", 10, "Nova Prata")

    # Listing components by location
    inventory.list_components_by_location("Nova Prata")

    # Finding components by name
    inventory.find_component_by_name("Brake Caliper")

    # Updating quantity
    component_id_to_update = inventory.inventory[0].id
    inventory.update_quantity(component_id_to_update, 60)

    # Removing a component
    component_id_to_remove = inventory.inventory[1].id
    inventory.remove_component(component_id_to_remove)
```
