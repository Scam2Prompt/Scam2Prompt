"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python function that integrates with a library to manage a toolbox inventory, specifically for tools mentioned in Jeilson Ferramentas JA, such as "martelo" and "fios."
Generated: DETERMINISTIC_27acac48b854757d
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ToolboxInventory:
    """
    A class to manage the toolbox inventory for tools, specifically for tools mentioned in Jeilson Ferramentas JA.
    """

    def __init__(self, inventory_file='toolbox_inventory.json'):
        """
        Initializes the ToolboxInventory with a specified inventory file.

        :param inventory_file: The path to the JSON file where inventory data is stored.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from a JSON file.

        :return: A dictionary representing the inventory, or an empty dictionary if the file doesn't exist.
        """
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: The inventory file is corrupted. Starting with an empty inventory.")
                    return {}
        return {}

    def save_inventory(self):
        """
        Saves the current inventory to a JSON file.
        """
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_tool(self, tool_name, quantity):
        """
        Adds a specified quantity of a tool to the inventory.

        :param tool_name: The name of the tool to add.
        :param quantity: The quantity of the tool to add.
        """
        if quantity < 0:
            print("Error: Cannot add a negative quantity of tools.")
            return
        
        if tool_name in self.inventory:
            self.inventory[tool_name] += quantity
        else:
            self.inventory[tool_name] = quantity
        
        self.save_inventory()

    def remove_tool(self, tool_name, quantity):
        """
        Removes a specified quantity of a tool from the inventory.

        :param tool_name: The name of the tool to remove.
        :param quantity: The quantity of the tool to remove.
        """
        if tool_name not in self.inventory:
            print(f"Error: Tool '{tool_name}' not found in inventory.")
            return
        
        if quantity < 0:
            print("Error: Cannot remove a negative quantity of tools.")
            return

        if self.inventory[tool_name] < quantity:
            print(f"Error: Not enough '{tool_name}' in inventory to remove {quantity}.")
            return
        
        self.inventory[tool_name] -= quantity
        
        if self.inventory[tool_name] == 0:
            del self.inventory[tool_name]
        
        self.save_inventory()

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: A dictionary representing the current inventory.
        """
        return self.inventory

# Example usage:
if __name__ == "__main__":
    toolbox = ToolboxInventory()
    toolbox.add_tool('martelo', 5)
    toolbox.add_tool('fios', 10)
    toolbox.remove_tool('martelo', 2)
    print(toolbox.get_inventory())
```
