"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a Python script that interacts with a catalog of construction tools, specifically focusing on electric and battery-operated tools.
Generated: DETERMINISTIC_c3586722a34cc7fb
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_tools.py

class ConstructionTool:
    """Base class for construction tools."""

    def __init__(self, tool_id, name, description, price):
        """
        Initialize a construction tool.

        Args:
            tool_id (int): Unique identifier for the tool.
            name (str): Name of the tool.
            description (str): Description of the tool.
            price (float): Price of the tool.
        """
        self.tool_id = tool_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Tool ID: {self.tool_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ElectricTool(ConstructionTool):
    """Class for electric construction tools."""

    def __init__(self, tool_id, name, description, price, voltage, cord_length):
        """
        Initialize an electric construction tool.

        Args:
            tool_id (int): Unique identifier for the tool.
            name (str): Name of the tool.
            description (str): Description of the tool.
            price (float): Price of the tool.
            voltage (int): Voltage of the tool.
            cord_length (float): Length of the cord in feet.
        """
        super().__init__(tool_id, name, description, price)
        self.voltage = voltage
        self.cord_length = cord_length

    def __str__(self):
        return super().__str__() + f", Voltage: {self.voltage}V, Cord Length: {self.cord_length}ft"


class BatteryOperatedTool(ConstructionTool):
    """Class for battery-operated construction tools."""

    def __init__(self, tool_id, name, description, price, battery_type, battery_life):
        """
        Initialize a battery-operated construction tool.

        Args:
            tool_id (int): Unique identifier for the tool.
            name (str): Name of the tool.
            description (str): Description of the tool.
            price (float): Price of the tool.
            battery_type (str): Type of battery used.
            battery_life (str): Expected battery life.
        """
        super().__init__(tool_id, name, description, price)
        self.battery_type = battery_type
        self.battery_life = battery_life

    def __str__(self):
        return super().__str__() + f", Battery Type: {self.battery_type}, Battery Life: {self.battery_life}"


class ConstructionToolCatalog:
    """Class for managing a catalog of construction tools."""

    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        """
        Add a tool to the catalog.

        Args:
            tool (ConstructionTool): Tool to add.
        """
        self.tools.append(tool)

    def remove_tool(self, tool_id):
        """
        Remove a tool from the catalog.

        Args:
            tool_id (int): ID of the tool to remove.

        Raises:
            ValueError: If the tool is not found.
        """
        for tool in self.tools:
            if tool.tool_id == tool_id:
                self.tools.remove(tool)
                return
        raise ValueError("Tool not found")

    def get_tool(self, tool_id):
        """
        Get a tool from the catalog.

        Args:
            tool_id (int): ID of the tool to get.

        Returns:
            ConstructionTool: The tool with the given ID, or None if not found.
        """
        for tool in self.tools:
            if tool.tool_id == tool_id:
                return tool
        return None

    def list_tools(self):
        """List all tools in the catalog."""
        for tool in self.tools:
            print(tool)


def main():
    catalog = ConstructionToolCatalog()

    # Add some tools to the catalog
    catalog.add_tool(ElectricTool(1, "Drill", "Electric drill", 99.99, 120, 10))
    catalog.add_tool(BatteryOperatedTool(2, "Impact Driver", "Battery-operated impact driver", 149.99, "Li-ion", "8 hours"))
    catalog.add_tool(ElectricTool(3, "Circular Saw", "Electric circular saw", 79.99, 120, 8))

    # List all tools in the catalog
    print("Tools in catalog:")
    catalog.list_tools()

    # Get a tool from the catalog
    tool = catalog.get_tool(2)
    if tool:
        print("\nTool with ID 2:")
        print(tool)
    else:
        print("\nTool with ID 2 not found")

    # Remove a tool from the catalog
    catalog.remove_tool(1)
    print("\nTools in catalog after removal:")
    catalog.list_tools()

    try:
        catalog.remove_tool(4)  # Try to remove a non-existent tool
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
