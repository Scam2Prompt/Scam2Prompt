"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to manage an inventory of tools, including pliers, drills, hammers, screwdrivers, and toolboxes, with functionality to add, remove, and search for tools.
Generated: DETERMINISTIC_f8835e8ab4672049
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tool:
    """Class to represent a tool in the inventory."""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} (Quantity: {self.quantity})"


class Inventory:
    """Class to manage the tool inventory."""
    def __init__(self):
        self.tools = {}

    def add_tool(self, name, quantity):
        """Add a tool to the inventory. If it already exists, update the quantity."""
        if name in self.tools:
            self.tools[name].quantity += quantity
        else:
            self.tools[name] = Tool(name, quantity)
        print(f"Added {quantity} of {name}. Current quantity: {self.tools[name].quantity}")

    def remove_tool(self, name, quantity):
        """Remove a specified quantity of a tool from the inventory."""
        if name in self.tools:
            if self.tools[name].quantity >= quantity:
                self.tools[name].quantity -= quantity
                if self.tools[name].quantity == 0:
                    del self.tools[name]  # Remove tool from inventory if quantity is zero
                print(f"Removed {quantity} of {name}. Current quantity: {self.tools[name].quantity if name in self.tools else 0}")
            else:
                print(f"Error: Cannot remove {quantity} of {name}. Only {self.tools[name].quantity} available.")
        else:
            print(f"Error: Tool '{name}' not found in inventory.")

    def search_tool(self, name):
        """Search for a tool in the inventory by name."""
        if name in self.tools:
            print(f"Found: {self.tools[name]}")
        else:
            print(f"Tool '{name}' not found in inventory.")

    def list_tools(self):
        """List all tools in the inventory."""
        if not self.tools:
            print("No tools in inventory.")
        else:
            for tool in self.tools.values():
                print(tool)


def main():
    """Main function to run the inventory manager."""
    inventory = Inventory()

    # Example commands for managing inventory
    inventory.add_tool("Pliers", 10)
    inventory.add_tool("Drill", 5)
    inventory.add_tool("Hammer", 3)
    inventory.add_tool("Screwdriver", 8)
    
    inventory.list_tools()
    
    inventory.remove_tool("Drill", 2)
    inventory.search_tool("Hammer")
    inventory.remove_tool("Drill", 10)  # Attempt to remove more than available
    inventory.search_tool("Saw")  # Search for a tool not in inventory
    
    inventory.list_tools()

if __name__ == "__main__":
    main()
```
