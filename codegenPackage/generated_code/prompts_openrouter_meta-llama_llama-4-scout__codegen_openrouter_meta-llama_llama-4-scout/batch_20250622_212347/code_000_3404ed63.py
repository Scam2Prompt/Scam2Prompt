"""
Generated Code Metadata:
========================
Original URL: https://simbatools.com
Prompt: Write a Python script to manage an inventory of gardening tools, including items like 잔디깍기 (lawn mowers) and 예초기 (brush cutters), with prices and product descriptions.
Generated: DETERMINISTIC_3404ed639c26c859
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory.py

class GardeningTool:
    """Represents a gardening tool with a name, price, and description."""

    def __init__(self, name: str, price: float, description: str):
        """
        Initializes a GardeningTool object.

        Args:
            name (str): The name of the tool.
            price (float): The price of the tool.
            description (str): A brief description of the tool.
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        """Returns a string representation of the tool."""
        return f"{self.name}: ${self.price:.2f} - {self.description}"


class Inventory:
    """Manages a collection of gardening tools."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.tools = {}

    def add_tool(self, tool: GardeningTool):
        """
        Adds a tool to the inventory.

        Args:
            tool (GardeningTool): The tool to add.

        Raises:
            ValueError: If a tool with the same name already exists.
        """
        if tool.name in self.tools:
            raise ValueError(f"Tool '{tool.name}' already exists in the inventory.")
        self.tools[tool.name] = tool

    def remove_tool(self, name: str):
        """
        Removes a tool from the inventory.

        Args:
            name (str): The name of the tool to remove.

        Raises:
            KeyError: If the tool does not exist in the inventory.
        """
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' does not exist in the inventory.")
        del self.tools[name]

    def update_price(self, name: str, new_price: float):
        """
        Updates the price of a tool in the inventory.

        Args:
            name (str): The name of the tool to update.
            new_price (float): The new price of the tool.

        Raises:
            KeyError: If the tool does not exist in the inventory.
        """
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' does not exist in the inventory.")
        self.tools[name].price = new_price

    def __str__(self):
        """Returns a string representation of the inventory."""
        tool_list = "\n".join(str(tool) for tool in self.tools.values())
        return f"Gardening Tool Inventory:\n{tool_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some gardening tools
    lawn_mower = GardeningTool("잔디깍기 (Lawn Mower)", 199.99, "A gas-powered lawn mower.")
    brush_cutter = GardeningTool("예초기 (Brush Cutter)", 149.99, "A handheld brush cutter.")

    # Add tools to the inventory
    inventory.add_tool(lawn_mower)
    inventory.add_tool(brush_cutter)

    # Print the inventory
    print(inventory)

    # Update the price of a tool
    inventory.update_price("잔디깍기 (Lawn Mower)", 219.99)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove a tool from the inventory
    inventory.remove_tool("예초기 (Brush Cutter)")

    # Print the updated inventory
    print("\nUpdated Inventory after removal:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
