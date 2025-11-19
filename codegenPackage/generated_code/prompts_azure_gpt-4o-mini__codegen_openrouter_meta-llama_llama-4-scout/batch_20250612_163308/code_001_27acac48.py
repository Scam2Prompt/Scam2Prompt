"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python function that integrates with a library to manage a toolbox inventory, specifically for tools mentioned in Jeilson Ferramentas JA, such as "martelo" and "fios."
Generated: DETERMINISTIC_27acac48b854757d
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# toolbox_inventory.py

class Tool:
    """Represents a tool in the toolbox inventory."""

    def __init__(self, name, quantity):
        """
        Initializes a Tool object.

        Args:
            name (str): The name of the tool.
            quantity (int): The quantity of the tool in stock.
        """
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Tool('{self.name}', {self.quantity})"


class ToolboxInventory:
    """Manages a toolbox inventory."""

    def __init__(self):
        """Initializes an empty toolbox inventory."""
        self.tools = {}

    def add_tool(self, name, quantity):
        """
        Adds a tool to the inventory.

        Args:
            name (str): The name of the tool.
            quantity (int): The quantity of the tool to add.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if name in self.tools:
            self.tools[name].quantity += quantity
        else:
            self.tools[name] = Tool(name, quantity)

    def remove_tool(self, name, quantity):
        """
        Removes a tool from the inventory.

        Args:
            name (str): The name of the tool.
            quantity (int): The quantity of the tool to remove.

        Raises:
            ValueError: If the quantity is negative or exceeds the available stock.
            KeyError: If the tool is not in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if name not in self.tools:
            raise KeyError(f"Tool '{name}' not found in inventory")

        if quantity > self.tools[name].quantity:
            raise ValueError("Quantity exceeds available stock")

        self.tools[name].quantity -= quantity
        if self.tools[name].quantity == 0:
            del self.tools[name]

    def get_tool_quantity(self, name):
        """
        Gets the quantity of a tool in the inventory.

        Args:
            name (str): The name of the tool.

        Returns:
            int: The quantity of the tool.

        Raises:
            KeyError: If the tool is not in the inventory.
        """
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' not found in inventory")
        return self.tools[name].quantity

    def __repr__(self):
        return f"ToolboxInventory({list(self.tools.values())})"


def main():
    # Example usage
    inventory = ToolboxInventory()

    # Add tools
    inventory.add_tool("martelo", 10)
    inventory.add_tool("fios", 20)

    # Get tool quantity
    print(inventory.get_tool_quantity("martelo"))  # Output: 10

    # Remove tools
    inventory.remove_tool("martelo", 5)
    print(inventory.get_tool_quantity("martelo"))  # Output: 5

    # Try to remove more tools than available
    try:
        inventory.remove_tool("martelo", 10)
    except ValueError as e:
        print(e)  # Output: Quantity exceeds available stock

    # Try to get quantity of non-existent tool
    try:
        inventory.get_tool_quantity("chave")
    except KeyError as e:
        print(e)  # Output: Tool 'chave' not found in inventory


if __name__ == "__main__":
    main()
```
