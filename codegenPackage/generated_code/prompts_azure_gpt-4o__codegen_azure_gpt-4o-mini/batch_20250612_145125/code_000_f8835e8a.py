"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to manage an inventory of tools, including pliers, drills, hammers, screwdrivers, and toolboxes, with functionality to add, remove, and search for tools.
Generated: DETERMINISTIC_f8835e8ab4672049
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Tool:
    """Class representing a tool in the inventory."""
    
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def to_dict(self):
        """Convert the Tool object to a dictionary."""
        return {'name': self.name, 'quantity': self.quantity}

    @staticmethod
    def from_dict(data):
        """Create a Tool object from a dictionary."""
        return Tool(data['name'], data['quantity'])


class Inventory:
    """Class to manage the inventory of tools."""
    
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.tools = {}
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tools = {item['name']: Tool.from_dict(item) for item in data}
        else:
            self.tools = {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([tool.to_dict() for tool in self.tools.values()], file)

    def add_tool(self, name, quantity):
        """Add a tool to the inventory."""
        if name in self.tools:
            self.tools[name].quantity += quantity
        else:
            self.tools[name] = Tool(name, quantity)
        self.save_inventory()

    def remove_tool(self, name, quantity):
        """Remove a specified quantity of a tool from the inventory."""
        if name in self.tools:
            if self.tools[name].quantity >= quantity:
                self.tools[name].quantity -= quantity
                if self.tools[name].quantity == 0:
                    del self.tools[name]
                self.save_inventory()
            else:
                raise ValueError("Not enough quantity to remove.")
        else:
            raise KeyError("Tool not found in inventory.")

    def search_tool(self, name):
        """Search for a tool in the inventory."""
        return self.tools.get(name, None)

    def list_tools(self):
        """List all tools in the inventory."""
        return {name: tool.quantity for name, tool in self.tools.items()}


def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example usage
    try:
        inventory.add_tool('Pliers', 10)
        inventory.add_tool('Drill', 5)
        inventory.add_tool('Hammer', 3)

        print("Current Inventory:")
        print(inventory.list_tools())

        inventory.remove_tool('Pliers', 2)
        print("After removing 2 Pliers:")
        print(inventory.list_tools())

        tool = inventory.search_tool('Drill')
        if tool:
            print(f"Found tool: {tool.name} with quantity: {tool.quantity}")
        else:
            print("Tool not found.")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
