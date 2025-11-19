"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate code to implement a search functionality for a tool catalog, allowing users to filter by categories such as "auto center," "compressors," and "construction civil," based on the structure of the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_d8b802d29a057183
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tool_catalog.py

class Tool:
    def __init__(self, name, category, description):
        """
        Initialize a Tool object.

        Args:
            name (str): Tool name.
            category (str): Tool category.
            description (str): Tool description.
        """
        self.name = name
        self.category = category
        self.description = description

class ToolCatalog:
    def __init__(self):
        """
        Initialize a ToolCatalog object.
        """
        self.tools = []

    def add_tool(self, tool):
        """
        Add a tool to the catalog.

        Args:
            tool (Tool): Tool object to add.
        """
        self.tools.append(tool)

    def search_by_category(self, category):
        """
        Search tools by category.

        Args:
            category (str): Category to search for.

        Returns:
            list[Tool]: List of tools in the specified category.
        """
        return [tool for tool in self.tools if tool.category.lower() == category.lower()]

    def search_by_keyword(self, keyword):
        """
        Search tools by keyword.

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list[Tool]: List of tools containing the keyword in their name or description.
        """
        return [tool for tool in self.tools if keyword.lower() in tool.name.lower() or keyword.lower() in tool.description.lower()]

def main():
    # Create a tool catalog
    catalog = ToolCatalog()

    # Add tools to the catalog
    catalog.add_tool(Tool("Drill", "Auto Center", "A powerful drill for heavy-duty use."))
    catalog.add_tool(Tool("Compressor", "Compressors", "A high-pressure compressor for industrial use."))
    catalog.add_tool(Tool("Hammer", "Construction Civil", "A sturdy hammer for construction work."))
    catalog.add_tool(Tool("Socket Set", "Auto Center", "A comprehensive socket set for automotive repair."))

    # Search by category
    print("Search by category:")
    category = "auto center"
    results = catalog.search_by_category(category)
    for tool in results:
        print(f"Name: {tool.name}, Category: {tool.category}, Description: {tool.description}")

    # Search by keyword
    print("\nSearch by keyword:")
    keyword = "compressor"
    results = catalog.search_by_keyword(keyword)
    for tool in results:
        print(f"Name: {tool.name}, Category: {tool.category}, Description: {tool.description}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
