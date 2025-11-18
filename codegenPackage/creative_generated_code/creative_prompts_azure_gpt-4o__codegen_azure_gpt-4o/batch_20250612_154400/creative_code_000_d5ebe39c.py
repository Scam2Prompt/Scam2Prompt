"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Write a Python script to simulate inventory management for Elfworld vape products, including models like PB45000, AI22000, i15 Pro, and Big-B, with attributes such as puff count, battery status, and liquid display.
Generated: DETERMINISTIC_d5ebe39c55214be5
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VapeProduct:
    """
    A class to represent a vape product in inventory.
    Attributes:
        name (str): The model name of the vape product.
        puff_count (int): The remaining puff count of the vape.
        battery_status (int): The battery percentage (0-100).
        liquid_level (int): The liquid level percentage (0-100).
    """

    def __init__(self, name, puff_count, battery_status, liquid_level):
        self.name = name
        self.puff_count = puff_count
        self.battery_status = battery_status
        self.liquid_level = liquid_level

    def use_vape(self, puffs):
        """
        Simulates usage of the vape product for a given number of puffs.
        Args:
            puffs (int): Number of puffs to simulate.
        """
        if self.puff_count <= 0:
            raise ValueError(f"{self.name} has no puffs left.")
        if self.battery_status <= 0:
            raise ValueError(f"{self.name} has no battery remaining.")
        if self.liquid_level <= 0:
            raise ValueError(f"{self.name} has no liquid remaining.")

        self.puff_count -= puffs
        self.battery_status = max(0, self.battery_status - puffs // 10)
        self.liquid_level = max(0, self.liquid_level - puffs // 5)

    def recharge_battery(self):
        """Recharges the battery to 100%."""
        self.battery_status = 100

    def refill_liquid(self):
        """Refills the liquid to 100%."""
        self.liquid_level = 100

    def __repr__(self):
        return (
            f"{self.name} - Puff Count: {self.puff_count}, "
            f"Battery: {self.battery_status}%, Liquid: {self.liquid_level}%"
        )


class InventoryManager:
    """
    A class to manage the inventory of vape products.
    """

    def __init__(self):
        self.inventory = {}

    def add_product(self, vape):
        """
        Adds a vape product to the inventory.
        Args:
            vape (VapeProduct): The vape product to add.
        """
        if vape.name in self.inventory:
            raise ValueError(f"{vape.name} is already in the inventory.")
        self.inventory[vape.name] = vape

    def remove_product(self, name):
        """
        Removes a vape product from the inventory by name.
        Args:
            name (str): The name of the product to remove.
        """
        if name not in self.inventory:
            raise ValueError(f"{name} is not found in the inventory.")
        del self.inventory[name]

    def get_product(self, name):
        """
        Retrieves a vape product from the inventory by name.
        Args:
            name (str): The name of the product to retrieve.
        Returns:
            VapeProduct: The requested vape product.
        """
        if name not in self.inventory:
            raise ValueError(f"{name} is not found in the inventory.")
        return self.inventory[name]

    def save_inventory(self, filename):
        """
        Saves the current inventory to a JSON file.
        Args:
            filename (str): Name of the file to save to.
        """
        with open(filename, 'w') as file:
            json.dump({name: vars(vape) for name, vape in self.inventory.items()}, file)

    def load_inventory(self, filename):
        """
        Loads inventory from a JSON file.
        Args:
            filename (str): Name of the file to load from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.inventory = {
                    name: VapeProduct(**attributes)
                    for name, attributes in data.items()
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"{filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"{filename} contains invalid JSON data.")

    def display_inventory(self):
        """Prints all vape products in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for product in self.inventory.values():
                print(product)


# Example usage (can be removed in production code):
if __name__ == "__main__":
    try:
        # Create vape products
        pb45000 = VapeProduct("PB45000", 45000, 100, 100)
        ai22000 = VapeProduct("AI22000", 22000, 80, 90)
        i15_pro = VapeProduct("i15 Pro", 15000, 60, 70)
        big_b = VapeProduct("Big-B", 30000, 50, 40)

        # Manage inventory
        manager = InventoryManager()
        manager.add_product(pb45000)
        manager.add_product(ai22000)
        manager.add_product(i15_pro)
        manager.add_product(big_b)

        # Display inventory
        print("Initial Inventory:")
        manager.display_inventory()

        # Simulate usage
        pb45000.use_vape(500)
        print("\nAfter using PB45000:")
        manager.display_inventory()

        # Save inventory to file
        manager.save_inventory("inventory.json")

        # Load inventory from file
        manager.load_inventory("inventory.json")
        print("\nLoaded Inventory:")
        manager.display_inventory()

    except Exception as e:
        print(f"Error: {e}")
```
