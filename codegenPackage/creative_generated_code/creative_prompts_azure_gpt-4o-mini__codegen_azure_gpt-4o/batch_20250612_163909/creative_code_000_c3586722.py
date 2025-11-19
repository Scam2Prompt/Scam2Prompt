"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a Python script that interacts with a catalog of construction tools, specifically focusing on electric and battery-operated tools.
Generated: DETERMINISTIC_c3586722a34cc7fb
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class ToolCatalog:
    """
    A class to represent a catalog of construction tools.
    Supports electric and battery-operated tools.
    """

    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.catalog = []

    def add_tool(self, name, tool_type, power_source, price):
        """
        Add a new tool to the catalog.

        :param name: Name of the tool (string)
        :param tool_type: Type of the tool (e.g., 'Drill', 'Saw') (string)
        :param power_source: Power source of the tool ('Electric' or 'Battery') (string)
        :param price: Price of the tool (float)
        """
        if power_source not in ["Electric", "Battery"]:
            raise ValueError("Power source must be 'Electric' or 'Battery'.")

        tool = {
            "name": name,
            "type": tool_type,
            "power_source": power_source,
            "price": price
        }
        self.catalog.append(tool)

    def list_tools(self):
        """
        List all tools in the catalog.

        :return: List of tools (list of dicts)
        """
        return self.catalog

    def filter_tools_by_power_source(self, power_source):
        """
        Filter tools by power source.

        :param power_source: Power source to filter by ('Electric' or 'Battery') (string)
        :return: List of tools matching the power source (list of dicts)
        """
        if power_source not in ["Electric", "Battery"]:
            raise ValueError("Power source must be 'Electric' or 'Battery'.")

        return [tool for tool in self.catalog if tool["power_source"] == power_source]

    def save_catalog(self, filename):
        """
        Save the catalog to a JSON file.

        :param filename: Name of the file to save the catalog to (string)
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog(self, filename):
        """
        Load the catalog from a JSON file.

        :param filename: Name of the file to load the catalog from (string)
        """
        try:
            with open(filename, "r") as file:
                self.catalog = json.load(file)
        except IOError as e:
            print(f"Error loading catalog from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")


def main():
    """
    Main function to demonstrate the usage of the ToolCatalog class.
    """
    catalog = ToolCatalog()

    # Adding tools to the catalog
    catalog.add_tool(name="Cordless Drill", tool_type="Drill", power_source="Battery", price=120.99)
    catalog.add_tool(name="Electric Saw", tool_type="Saw", power_source="Electric", price=89.49)
    catalog.add_tool(name="Battery-Powered Screwdriver", tool_type="Screwdriver", power_source="Battery", price=35.75)

    # Listing all tools
    print("All Tools:")
    for tool in catalog.list_tools():
        print(tool)

    # Filtering tools by power source
    print("\nBattery-Operated Tools:")
    for tool in catalog.filter_tools_by_power_source("Battery"):
        print(tool)

    # Saving the catalog to a file
    catalog.save_catalog("tools_catalog.json")

    # Loading the catalog from file
    new_catalog = ToolCatalog()
    new_catalog.load_catalog("tools_catalog.json")
    print("\nLoaded Catalog:")
    for tool in new_catalog.list_tools():
        print(tool)


if __name__ == "__main__":
    main()
```
