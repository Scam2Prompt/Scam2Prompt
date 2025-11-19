"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to generate a catalog of tools and machinery, including categories like "roldana," "polé," "moitão," and "turbina," as described on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_ba455586e4888dfd
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catalog_generator.py

class Tool:
    """Represents a tool or machinery in the catalog."""

    def __init__(self, name, description, category, price):
        """
        Initializes a Tool object.

        Args:
            name (str): The name of the tool.
            description (str): A brief description of the tool.
            category (str): The category of the tool.
            price (float): The price of the tool.
        """
        self.name = name
        self.description = description
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} (${self.price:.2f})"


class Catalog:
    """Represents a catalog of tools and machinery."""

    def __init__(self):
        """Initializes an empty catalog."""
        self.tools = []

    def add_tool(self, tool):
        """
        Adds a tool to the catalog.

        Args:
            tool (Tool): The tool to add.
        """
        self.tools.append(tool)

    def get_tools_by_category(self, category):
        """
        Retrieves tools from a specific category.

        Args:
            category (str): The category to filter by.

        Returns:
            list[Tool]: A list of tools in the specified category.
        """
        return [tool for tool in self.tools if tool.category.lower() == category.lower()]

    def __str__(self):
        catalog_str = "Tool Catalog:\n"
        for tool in self.tools:
            catalog_str += f"- {tool}\n"
        return catalog_str


def main():
    # Create a catalog
    catalog = Catalog()

    # Add tools to the catalog
    catalog.add_tool(Tool("Roldana", "A roldana is a type of pulley.", "roldana", 50.00))
    catalog.add_tool(Tool("Polé", "A polé is a type of pole.", "polé", 20.00))
    catalog.add_tool(Tool("Moitão", "A moitão is a type of mechanical device.", "moitão", 100.00))
    catalog.add_tool(Tool("Turbina", "A turbina is a type of turbine.", "turbina", 500.00))

    # Print the entire catalog
    print(catalog)

    # Print tools by category
    categories = ["roldana", "polé", "moitão", "turbina"]
    for category in categories:
        print(f"\n{category.capitalize()} Tools:")
        tools = catalog.get_tools_by_category(category)
        for tool in tools:
            print(tool)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
