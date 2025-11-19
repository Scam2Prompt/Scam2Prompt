"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script to automate the inventory management of electronic components, including ATMEGA328P-AU and ATMEGA328PB-AU semiconductors.
Generated: DETERMINISTIC_75278bc151efcab5
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class ElectronicComponent:
    """Represents an electronic component in the inventory."""

    def __init__(self, part_number, quantity, description):
        """
        Initializes an ElectronicComponent object.

        Args:
            part_number (str): The part number of the component.
            quantity (int): The quantity of the component in stock.
            description (str): A brief description of the component.
        """
        self.part_number = part_number
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"{self.part_number}: {self.description} - Quantity: {self.quantity}"


class Inventory:
    """Manages a collection of electronic components."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.components = {}

    def add_component(self, part_number, quantity, description):
        """
        Adds a component to the inventory.

        Args:
            part_number (str): The part number of the component.
            quantity (int): The quantity of the component to add.
            description (str): A brief description of the component.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if part_number in self.components:
            self.components[part_number].quantity += quantity
        else:
            self.components[part_number] = ElectronicComponent(part_number, quantity, description)

    def remove_component(self, part_number, quantity):
        """
        Removes a quantity of a component from the inventory.

        Args:
            part_number (str): The part number of the component.
            quantity (int): The quantity of the component to remove.

        Raises:
            ValueError: If the quantity is negative or exceeds the available stock.
            KeyError: If the component is not in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if part_number not in self.components:
            raise KeyError(f"Component {part_number} not found in inventory")

        if quantity > self.components[part_number].quantity:
            raise ValueError("Insufficient stock")

        self.components[part_number].quantity -= quantity
        if self.components[part_number].quantity == 0:
            del self.components[part_number]

    def update_component(self, part_number, quantity=None, description=None):
        """
        Updates the quantity or description of a component in the inventory.

        Args:
            part_number (str): The part number of the component.
            quantity (int, optional): The new quantity of the component. Defaults to None.
            description (str, optional): The new description of the component. Defaults to None.

        Raises:
            KeyError: If the component is not in the inventory.
        """
        if part_number not in self.components:
            raise KeyError(f"Component {part_number} not found in inventory")

        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            self.components[part_number].quantity = quantity

        if description is not None:
            self.components[part_number].description = description

    def __str__(self):
        inventory_list = "\n".join([str(component) for component in self.components.values()])
        return f"Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Add components
    inventory.add_component("ATMEGA328P-AU", 100, "Microcontroller")
    inventory.add_component("ATMEGA328PB-AU", 50, "Microcontroller with improved peripherals")

    # Print initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Remove components
    inventory.remove_component("ATMEGA328P-AU", 20)

    # Update component description
    inventory.update_component("ATMEGA328PB-AU", description="Microcontroller with improved peripherals and new features")

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
