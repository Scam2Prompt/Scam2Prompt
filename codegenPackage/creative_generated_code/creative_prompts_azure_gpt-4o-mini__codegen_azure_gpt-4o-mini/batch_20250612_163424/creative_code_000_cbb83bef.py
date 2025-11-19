"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Generate a code snippet for a manufacturing management system that tracks the production of brake system components like brake cylinders and reservoirs, as described by PEW Engineering Pvt. Ltd.
Generated: DETERMINISTIC_cbb83beff6365c3d
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BrakeComponent:
    """Represents a generic brake system component."""

    def __init__(self, component_id: str, component_type: str, quantity: int):
        """
        Initializes a new brake component.

        Args:
            component_id (str): Unique identifier for the component.
            component_type (str): Type of the brake component (e.g., 'cylinder' or 'reservoir').
            quantity (int): Quantity of the component available.
        """
        self.component_id = component_id
        self.component_type = component_type
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """
        Updates the quantity of the component.

        Args:
            amount (int): Amount to add or subtract. Use negative values to decrement.

        Raises:
            ValueError: If the quantity becomes negative after updating.
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = new_quantity

    def __str__(self) -> str:
        """Returns a string representation of the brake component."""
        return f"{self.component_type.capitalize()} ID: {self.component_id}, Quantity: {self.quantity}"


class ManufacturingSystem:
    """Manages the production and inventory of brake system components."""

    def __init__(self):
        """Initializes the manufacturing system with an empty inventory."""
        self.inventory = {}

    def add_component(self, component_id: str, component_type: str, quantity: int) -> None:
        """
        Adds a new component to the inventory.

        Args:
            component_id (str): Unique identifier for the component.
            component_type (str): Type of the brake component.
            quantity (int): Quantity of the component to be added.
        
        Raises:
            ValueError: If the quantity is negative or if the component already exists.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if component_id in self.inventory:
            raise ValueError("Component already exists.")

        self.inventory[component_id] = BrakeComponent(component_id, component_type, quantity)

    def update_component_quantity(self, component_id: str, amount: int) -> None:
        """
        Updates the quantity of an existing component.

        Args:
            component_id (str): Unique identifier for the component.
            amount (int): Amount to add or subtract from the current quantity.

        Raises:
            KeyError: If the component does not exist in the inventory.
        """
        if component_id not in self.inventory:
            raise KeyError("Component not found in inventory.")
        
        self.inventory[component_id].update_quantity(amount)

    def get_inventory(self) -> str:
        """Returns a summary of the current inventory."""
        return "\n".join(str(component) for component in self.inventory.values())


# Example usage
if __name__ == "__main__":
    manufacturing_system = ManufacturingSystem()

    try:
        manufacturing_system.add_component("C001", "cylinder", 100)
        manufacturing_system.add_component("R001", "reservoir", 200)
        
        # Update quantities
        manufacturing_system.update_component_quantity("C001", -10)  # Reduce cylinder quantity by 10
        manufacturing_system.update_component_quantity("R001", 50)    # Increase reservoir quantity by 50

        # Print current inventory
        print("Current Inventory:")
        print(manufacturing_system.get_inventory())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
