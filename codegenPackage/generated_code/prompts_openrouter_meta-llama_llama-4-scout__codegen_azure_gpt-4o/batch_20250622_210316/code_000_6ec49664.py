"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Write a Python code to manage an inventory of gemstones, including their names, carat weights, and prices, similar to the catalog found on Bismillah Gems.
Generated: DETERMINISTIC_6ec49664128b6f5e
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class GemstoneInventory:
    """
    A class to manage an inventory of gemstones, including their names, carat weights, and prices.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.inventory = []

    def add_gemstone(self, name, carat_weight, price):
        """
        Adds a gemstone to the inventory.

        :param name: Name of the gemstone (string)
        :param carat_weight: Carat weight of the gemstone (float)
        :param price: Price of the gemstone (float)
        """
        try:
            gemstone = {
                "name": name,
                "carat_weight": carat_weight,
                "price": price
            }
            self.inventory.append(gemstone)
            print(f"Gemstone '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding gemstone: {e}")

    def remove_gemstone(self, name):
        """
        Removes a gemstone from the inventory by name.

        :param name: Name of the gemstone to remove (string)
        """
        try:
            for gemstone in self.inventory:
                if gemstone["name"].lower() == name.lower():
                    self.inventory.remove(gemstone)
                    print(f"Gemstone '{name}' removed successfully.")
                    return
            print(f"Gemstone '{name}' not found in inventory.")
        except Exception as e:
            print(f"Error removing gemstone: {e}")

    def list_inventory(self):
        """
        Lists all gemstones in the inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for gemstone in self.inventory:
                print(f"Name: {gemstone['name']}, Carat Weight: {gemstone['carat_weight']}, Price: ${gemstone['price']}")

    def save_inventory_to_file(self, filename):
        """
        Saves the inventory to a JSON file.

        :param filename: Name of the file to save the inventory (string)
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
            print(f"Inventory saved to '{filename}' successfully.")
        except Exception as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, filename):
        """
        Loads the inventory from a JSON file.

        :param filename: Name of the file to load the inventory from (string)
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")
        except Exception as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = GemstoneInventory()

    # Adding gemstones
    inventory.add_gemstone("Ruby", 1.5, 5000)
    inventory.add_gemstone("Emerald", 2.0, 7500)
    inventory.add_gemstone("Sapphire", 1.2, 4500)

    # Listing inventory
    inventory.list_inventory()

    # Removing a gemstone
    inventory.remove_gemstone("Emerald")

    # Listing inventory after removal
    inventory.list_inventory()

    # Saving inventory to file
    inventory.save_inventory_to_file("gemstone_inventory.json")

    # Loading inventory from file
    inventory.load_inventory_from_file("gemstone_inventory.json")
    inventory.list_inventory()
```
