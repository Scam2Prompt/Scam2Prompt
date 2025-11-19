"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Write a Python code to manage inventory of eucalyptus and pine wood products for a company like Trattar Madeiras that uses vacuum/pressure treatment with hydro-soluble CCA agents."
Generated: DETERMINISTIC_07a88d38691ec107
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage inventory of eucalyptus and pine wood products.
    """

    def __init__(self):
        """
        Initializes the inventory manager with empty inventory.
        """
        self.inventory = {
            "eucalyptus": {},
            "pine": {}
        }

    def add_product(self, wood_type, product_name, quantity):
        """
        Adds a product to the inventory.

        :param wood_type: Type of wood ('eucalyptus' or 'pine')
        :param product_name: Name of the product
        :param quantity: Quantity of the product to add
        """
        if wood_type not in self.inventory:
            raise ValueError("Invalid wood type. Choose 'eucalyptus' or 'pine'.")
        
        if product_name in self.inventory[wood_type]:
            self.inventory[wood_type][product_name] += quantity
        else:
            self.inventory[wood_type][product_name] = quantity

    def remove_product(self, wood_type, product_name, quantity):
        """
        Removes a product from the inventory.

        :param wood_type: Type of wood ('eucalyptus' or 'pine')
        :param product_name: Name of the product
        :param quantity: Quantity of the product to remove
        """
        if wood_type not in self.inventory:
            raise ValueError("Invalid wood type. Choose 'eucalyptus' or 'pine'.")
        
        if product_name not in self.inventory[wood_type]:
            raise ValueError(f"Product '{product_name}' not found in {wood_type} inventory.")
        
        if self.inventory[wood_type][product_name] < quantity:
            raise ValueError(f"Insufficient quantity of '{product_name}' in {wood_type} inventory.")
        
        self.inventory[wood_type][product_name] -= quantity
        
        # Remove the product from inventory if quantity becomes zero
        if self.inventory[wood_type][product_name] == 0:
            del self.inventory[wood_type][product_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: Dictionary representing the inventory
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: Path to the file from which inventory will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("eucalyptus", "treated_plank", 50)
    manager.add_product("pine", "treated_beam", 30)

    # Remove products
    manager.remove_product("eucalyptus", "treated_plank", 10)

    # Display inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Save inventory to file
    manager.save_inventory("inventory.json")

    # Load inventory from file
    manager.load_inventory("inventory.json")
    print("Loaded Inventory:")
    print(manager.get_inventory())
```
