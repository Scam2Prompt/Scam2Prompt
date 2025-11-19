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
import json

class ToolCatalog:
    """
    A class to manage a catalog of construction tools, specifically electric and battery-operated tools.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.catalog = []

    def add_tool(self, name, tool_type, power_source, price):
        """
        Adds a new tool to the catalog.

        :param name: Name of the tool (string)
        :param tool_type: Type of the tool (e.g., drill, saw) (string)
        :param power_source: Power source of the tool (electric or battery) (string)
        :param price: Price of the tool (float)
        :raises ValueError: If power_source is not 'electric' or 'battery'
        """
        if power_source.lower() not in ['electric', 'battery']:
            raise ValueError("Power source must be 'electric' or 'battery'.")

        tool = {
            "name": name,
            "type": tool_type,
            "power_source": power_source.lower(),
            "price": price
        }
        self.catalog.append(tool)

    def list_tools(self):
        """
        Lists all tools in the catalog.

        :return: List of tools (list of dictionaries)
        """
        return self.catalog

    def search_tools(self, keyword):
        """
        Searches for tools in the catalog by name or type.

        :param keyword: Keyword to search for (string)
        :return: List of matching tools (list of dictionaries)
        """
        keyword = keyword.lower()
        return [tool for tool in self.catalog if keyword in tool['name'].lower() or keyword in tool['type'].lower()]

    def save_catalog(self, file_path):
        """
        Saves the catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved (string)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog(self, file_path):
        """
        Loads the catalog from a JSON file.

        :param file_path: Path to the file to load the catalog from (string)
        :raises IOError: If the file cannot be read
        """
        try:
            with open(file_path, 'r') as file:
                self.catalog = json.load(file)
        except IOError as e:
            print(f"Error loading catalog from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = ToolCatalog()

    # Adding tools to the catalog
    try:
        catalog.add_tool("Cordless Drill", "Drill", "battery", 99.99)
        catalog.add_tool("Electric Saw", "Saw", "electric", 149.99)
        catalog.add_tool("Battery-Powered Screwdriver", "Screwdriver", "battery", 29.99)
    except ValueError as e:
        print(f"Error adding tool: {e}")

    # Listing all tools
    print("All tools in the catalog:")
    for tool in catalog.list_tools():
        print(tool)

    # Searching for tools
    print("\nSearch results for 'drill':")
    for tool in catalog.search_tools("drill"):
        print(tool)

    # Saving the catalog to a file
    catalog.save_catalog("tools_catalog.json")

    # Loading the catalog from a file
    catalog.load_catalog("tools_catalog.json")
    print("\nCatalog loaded from file:")
    for tool in catalog.list_tools():
        print(tool)
```
