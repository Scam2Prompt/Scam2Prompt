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

class ToolboxInventory:
    """Class to manage toolbox inventory."""

    def __init__(self, inventory_file='toolbox_inventory.json'):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file (str): Path to the inventory file. Defaults to 'toolbox_inventory.json'.
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self._load_inventory()

    def _load_inventory(self):
        """Load inventory from a JSON file."""
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty inventory.
            self.inventory = {}
        except json.JSONDecodeError:
            # Handle corrupted JSON data gracefully.
            print("Error: Inventory file is corrupted. Initializing an empty inventory.")
            self.inventory = {}

    def _save_inventory(self):
        """Save inventory to a JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_tool(self, tool_name, quantity=1):
        """
        Add a tool to the inventory.
        
        Args:
            tool_name (str): Name of the tool to add.
            quantity (int): Number of tools to add. Defaults to 1.
        """
        if tool_name in self.inventory:
            self.inventory[tool_name] += quantity
        else:
            self.inventory[tool_name] = quantity
        self._save_inventory()

    def remove_tool(self, tool_name, quantity=1):
        """
        Remove a tool from the inventory.
        
        Args:
            tool_name (str): Name of the tool to remove.
            quantity (int): Number of tools to remove. Defaults to 1.
        """
        if tool_name in self.inventory:
            if self.inventory[tool_name] >= quantity:
                self.inventory[tool_name] -= quantity
                if self.inventory[tool_name] == 0:
                    del self.inventory[tool_name]
                self._save_inventory()
            else:
                print(f"Error: Not enough '{tool_name}' in inventory to remove.")
        else:
            print(f"Error: '{tool_name}' not found in inventory.")

    def get_inventory(self):
        """
        Get the current inventory.
        
        Returns:
            dict: The current inventory.
        """
        return self.inventory

    def display_inventory(self):
        """Display the inventory in a readable format."""
        print("Toolbox Inventory:")
        for tool, quantity in self.inventory.items():
            print(f"- {tool}: {quantity}")

# Example usage:
if __name__ == "__main__":
    toolbox = ToolboxInventory()
    toolbox.add_tool("martelo", 5)  # Add 5 martelos.
    toolbox.add_tool("fios", 3)     # Add 3 fios.
    toolbox.remove_tool("martelo", 2)  # Remove 2 martelos.
    toolbox.display_inventory()        # Display the inventory.
```
