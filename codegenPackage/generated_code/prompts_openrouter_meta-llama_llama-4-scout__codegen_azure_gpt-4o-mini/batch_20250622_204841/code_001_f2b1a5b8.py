"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Write a Python code snippet to categorize construction tools for a company like Anhanguera Ferramentas."
Generated: DETERMINISTIC_f2b1a5b87da80060
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tool:
    """Class representing a construction tool."""
    
    def __init__(self, name, category):
        """
        Initialize a new Tool instance.

        :param name: str - The name of the tool
        :param category: str - The category of the tool (e.g., 'Hand Tools', 'Power Tools')
        """
        self.name = name
        self.category = category

    def __repr__(self):
        """Return a string representation of the Tool instance."""
        return f"Tool(name='{self.name}', category='{self.category}')"


class ToolCatalog:
    """Class to manage a catalog of construction tools."""
    
    def __init__(self):
        """Initialize the ToolCatalog with an empty list of tools."""
        self.tools = []

    def add_tool(self, tool):
        """
        Add a tool to the catalog.

        :param tool: Tool - The tool to be added
        :raises ValueError: If the tool is not an instance of Tool
        """
        if not isinstance(tool, Tool):
            raise ValueError("Only instances of Tool can be added to the catalog.")
        self.tools.append(tool)

    def categorize_tools(self):
        """
        Categorize tools in the catalog by their category.

        :return: dict - A dictionary with categories as keys and lists of tools as values
        """
        categorized_tools = {}
        for tool in self.tools:
            if tool.category not in categorized_tools:
                categorized_tools[tool.category] = []
            categorized_tools[tool.category].append(tool)
        return categorized_tools

    def display_catalog(self):
        """Display the categorized tools in the catalog."""
        categorized_tools = self.categorize_tools()
        for category, tools in categorized_tools.items():
            print(f"Category: {category}")
            for tool in tools:
                print(f"  - {tool.name}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a tool catalog
        catalog = ToolCatalog()

        # Add tools to the catalog
        catalog.add_tool(Tool("Hammer", "Hand Tools"))
        catalog.add_tool(Tool("Drill", "Power Tools"))
        catalog.add_tool(Tool("Screwdriver", "Hand Tools"))
        catalog.add_tool(Tool("Circular Saw", "Power Tools"))

        # Display the categorized tools
        catalog.display_catalog()

    except ValueError as e:
        print(f"Error: {e}")
```
