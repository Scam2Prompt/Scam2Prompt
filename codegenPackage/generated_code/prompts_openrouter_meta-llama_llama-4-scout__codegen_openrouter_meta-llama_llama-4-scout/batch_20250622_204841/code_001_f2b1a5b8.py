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
# construction_tool_categorizer.py

class ConstructionTool:
    """Represents a construction tool with its name and category."""

    def __init__(self, name, category):
        """
        Initializes a ConstructionTool object.

        Args:
            name (str): The name of the tool.
            category (str): The category of the tool.
        """
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.category}"


class ToolCategorizer:
    """Categorizes construction tools."""

    def __init__(self):
        """
        Initializes a ToolCategorizer object with an empty dictionary.
        """
        self.tools = {}

    def add_tool(self, tool):
        """
        Adds a tool to the categorizer.

        Args:
            tool (ConstructionTool): The tool to add.

        Raises:
            ValueError: If the tool's category does not exist.
        """
        if tool.category not in self.tools:
            self.tools[tool.category] = []
        self.tools[tool.category].append(tool)

    def get_tools_by_category(self, category):
        """
        Retrieves tools by category.

        Args:
            category (str): The category to retrieve tools for.

        Returns:
            list[ConstructionTool]: A list of tools in the specified category.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.tools:
            raise ValueError(f"Category '{category}' does not exist.")
        return self.tools[category]

    def list_all_tools(self):
        """
        Lists all tools.

        Returns:
            dict[str, list[ConstructionTool]]: A dictionary with categories as keys and lists of tools as values.
        """
        return self.tools


def main():
    # Create a tool categorizer
    categorizer = ToolCategorizer()

    # Create construction tools
    tools = [
        ConstructionTool("Hammer", "Hand Tools"),
        ConstructionTool("Drill", "Power Tools"),
        ConstructionTool("Tape Measure", "Hand Tools"),
        ConstructionTool("Circular Saw", "Power Tools"),
        ConstructionTool("Level", "Hand Tools"),
    ]

    # Add tools to the categorizer
    for tool in tools:
        try:
            categorizer.add_tool(tool)
        except ValueError as e:
            print(f"Error: {e}")

    # List all tools
    print("All Tools:")
    for category, tool_list in categorizer.list_all_tools().items():
        print(f"{category}:")
        for tool in tool_list:
            print(tool)

    # Get tools by category
    category = "Hand Tools"
    try:
        hand_tools = categorizer.get_tools_by_category(category)
        print(f"\n{category}:")
        for tool in hand_tools:
            print(tool)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
