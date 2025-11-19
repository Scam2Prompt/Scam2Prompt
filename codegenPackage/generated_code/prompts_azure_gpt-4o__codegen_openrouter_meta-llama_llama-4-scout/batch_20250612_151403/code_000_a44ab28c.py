"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write Python code to create a catalog system for managing construction tools, including categories like "electric tools," "manual tools," and "hydraulic accessories," as described on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_a44ab28c4e24ba95
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_tool_catalog.py

class ConstructionTool:
    """Represents a construction tool with its attributes."""

    def __init__(self, name, description, price, category):
        """
        Initializes a ConstructionTool object.

        Args:
            name (str): The name of the tool.
            description (str): A brief description of the tool.
            price (float): The price of the tool.
            category (str): The category of the tool.
        """
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.description} (R${self.price:.2f})"


class ToolCatalog:
    """Manages a catalog of construction tools."""

    def __init__(self):
        """Initializes an empty tool catalog."""
        self.tools = []
        self.categories = set()

    def add_tool(self, tool):
        """
        Adds a tool to the catalog.

        Args:
            tool (ConstructionTool): The tool to add.

        Raises:
            ValueError: If the tool's category is not a string.
        """
        if not isinstance(tool.category, str):
            raise ValueError("Tool category must be a string")
        self.tools.append(tool)
        self.categories.add(tool.category)

    def get_tools_by_category(self, category):
        """
        Retrieves tools from a specific category.

        Args:
            category (str): The category to filter by.

        Returns:
            list[ConstructionTool]: A list of tools in the specified category.
        """
        return [tool for tool in self.tools if tool.category == category]

    def list_all_tools(self):
        """Prints a list of all tools in the catalog."""
        for tool in self.tools:
            print(tool)

    def list_categories(self):
        """Prints a list of all categories in the catalog."""
        for category in self.categories:
            print(category)


def main():
    catalog = ToolCatalog()

    # Adding some example tools
    catalog.add_tool(ConstructionTool("Drill", "Electric drill for heavy-duty use.", 299.99, "electric tools"))
    catalog.add_tool(ConstructionTool("Hammer", "Manual hammer for general use.", 49.99, "manual tools"))
    catalog.add_tool(ConstructionTool("Hydraulic Pump", "Hydraulic pump for heavy-duty applications.", 999.99, "hydraulic accessories"))
    catalog.add_tool(ConstructionTool("Saw", "Electric saw for precise cuts.", 199.99, "electric tools"))
    catalog.add_tool(ConstructionTool("Trowel", "Manual trowel for finishing surfaces.", 29.99, "manual tools"))

    print("Tool Catalog:")
    catalog.list_all_tools()

    print("\nCategories:")
    catalog.list_categories()

    print("\nElectric Tools:")
    for tool in catalog.get_tools_by_category("electric tools"):
        print(tool)

if __name__ == "__main__":
    main()
```
