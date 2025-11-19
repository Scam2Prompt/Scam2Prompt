"""
Generated Code Metadata:
========================
Original URL: https://casapatty.com.br
Prompt: Write a Python script to manage inventory for a construction materials store like Casa Patty, including classes for different types of materials.
Generated: DETERMINISTIC_391039cbf8779770
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

class Material:
    """
    Base class for construction materials.
    """
    def __init__(self, name, quantity, price_per_unit):
        """
        Initialize a material with name, quantity, and price per unit.
        """
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount):
        """
        Update the quantity of the material.
        :param amount: Amount to add (positive) or subtract (negative).
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to reduce quantity.")
        self.quantity += amount

    def calculate_total_value(self):
        """
        Calculate the total value of the material in stock.
        :return: Total value as a float.
        """
        return self.quantity * self.price_per_unit

    def to_dict(self):
        """
        Convert material details to a dictionary for serialization.
        :return: Dictionary representation of the material.
        """
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit
        }


class Wood(Material):
    """
    Class representing wood materials.
    """
    def __init__(self, name, quantity, price_per_unit, wood_type):
        """
        Initialize a wood material with an additional wood type attribute.
        """
        super().__init__(name, quantity, price_per_unit)
        self.wood_type = wood_type

    def to_dict(self):
        """
        Convert wood material details to a dictionary for serialization.
        :return: Dictionary representation of the wood material.
        """
        data = super().to_dict()
        data["wood_type"] = self.wood_type
        return data


class Cement(Material):
    """
    Class representing cement materials.
    """
    def __init__(self, name, quantity, price_per_unit, grade):
        """
        Initialize a cement material with an additional grade attribute.
        """
        super().__init__(name, quantity, price_per_unit)
        self.grade = grade

    def to_dict(self):
        """
        Convert cement material details to a dictionary for serialization.
        :return: Dictionary representation of the cement material.
        """
        data = super().to_dict()
        data["grade"] = self.grade
        return data


class Inventory:
    """
    Class to manage the inventory of construction materials.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.materials = []

    def add_material(self, material):
        """
        Add a material to the inventory.
        :param material: Material object to add.
        """
        if not isinstance(material, Material):
            raise TypeError("Only objects of type Material can be added to the inventory.")
        self.materials.append(material)

    def remove_material(self, name):
        """
        Remove a material from the inventory by name.
        :param name: Name of the material to remove.
        """
        self.materials = [m for m in self.materials if m.name != name]

    def get_material(self, name):
        """
        Retrieve a material from the inventory by name.
        :param name: Name of the material to retrieve.
        :return: Material object or None if not found.
        """
        for material in self.materials:
            if material.name == name:
                return material
        return None

    def calculate_total_inventory_value(self):
        """
        Calculate the total value of all materials in the inventory.
        :return: Total inventory value as a float.
        """
        return sum(material.calculate_total_value() for material in self.materials)

    def save_to_file(self, filename):
        """
        Save the inventory to a JSON file.
        :param filename: Name of the file to save to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([material.to_dict() for material in self.materials], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        """
        Load the inventory from a JSON file.
        :param filename: Name of the file to load from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.materials = []
                for item in data:
                    if "wood_type" in item:
                        self.materials.append(Wood(item["name"], item["quantity"], item["price_per_unit"], item["wood_type"]))
                    elif "grade" in item:
                        self.materials.append(Cement(item["name"], item["quantity"], item["price_per_unit"], item["grade"]))
                    else:
                        self.materials.append(Material(item["name"], item["quantity"], item["price_per_unit"]))
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Add materials
    inventory.add_material(Wood("Pine Wood", 50, 20.0, "Softwood"))
    inventory.add_material(Cement("Portland Cement", 100, 10.0, "Grade A"))

    # Update material quantity
    try:
        material = inventory.get_material("Pine Wood")
        if material:
            material.update_quantity(-10)
    except ValueError as e:
        print(e)

    # Calculate total inventory value
    print(f"Total inventory value: ${inventory.calculate_total_inventory_value():.2f}")

    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file
    inventory.load_from_file("inventory.json")
    print("Inventory loaded from file.")
```
