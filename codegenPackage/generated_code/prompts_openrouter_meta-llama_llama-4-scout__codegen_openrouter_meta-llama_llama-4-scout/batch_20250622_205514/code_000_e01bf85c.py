"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: "Write a Python script to manage inventory of recyclable materials for a company like SCR Reciclados that specializes in metal and electronic waste recycling."
Generated: DETERMINISTIC_e01bf85cd8aec7e8
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Material:
    """Represents a recyclable material."""

    def __init__(self, name, quantity, unit_price):
        """
        Initializes a Material instance.

        Args:
            name (str): Material name.
            quantity (float): Material quantity.
            unit_price (float): Material unit price.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_value(self):
        """Calculates the total value of the material."""
        return self.quantity * self.unit_price


class Inventory:
    """Manages the inventory of recyclable materials."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.materials = {}

    def add_material(self, material):
        """
        Adds a material to the inventory.

        Args:
            material (Material): Material to add.

        Raises:
            ValueError: If a material with the same name already exists.
        """
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists.")
        self.materials[material.name] = material

    def remove_material(self, name):
        """
        Removes a material from the inventory.

        Args:
            name (str): Name of the material to remove.

        Raises:
            KeyError: If the material does not exist.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        del self.materials[name]

    def update_quantity(self, name, new_quantity):
        """
        Updates the quantity of a material.

        Args:
            name (str): Name of the material to update.
            new_quantity (float): New quantity.

        Raises:
            KeyError: If the material does not exist.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        self.materials[name].quantity = new_quantity

    def get_material(self, name):
        """
        Retrieves a material from the inventory.

        Args:
            name (str): Name of the material to retrieve.

        Returns:
            Material: The material instance.

        Raises:
            KeyError: If the material does not exist.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        return self.materials[name]

    def list_materials(self):
        """Returns a list of all materials in the inventory."""
        return list(self.materials.values())


def main():
    # Create an inventory
    inventory = Inventory()

    while True:
        print("\nInventory Manager")
        print("1. Add material")
        print("2. Remove material")
        print("3. Update quantity")
        print("4. Get material")
        print("5. List materials")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter material name: ")
                quantity = float(input("Enter quantity: "))
                unit_price = float(input("Enter unit price: "))
                material = Material(name, quantity, unit_price)
                inventory.add_material(material)
                print(f"Material '{name}' added successfully.")
            elif choice == "2":
                name = input("Enter material name: ")
                inventory.remove_material(name)
                print(f"Material '{name}' removed successfully.")
            elif choice == "3":
                name = input("Enter material name: ")
                new_quantity = float(input("Enter new quantity: "))
                inventory.update_quantity(name, new_quantity)
                print(f"Quantity of '{name}' updated successfully.")
            elif choice == "4":
                name = input("Enter material name: ")
                material = inventory.get_material(name)
                print(f"Name: {material.name}, Quantity: {material.quantity}, Unit Price: {material.unit_price}")
            elif choice == "5":
                materials = inventory.list_materials()
                for material in materials:
                    print(f"Name: {material.name}, Quantity: {material.quantity}, Unit Price: {material.unit_price}, Total Value: {material.get_total_value()}")
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
