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
import os

class Tool:
    """Class representing a construction tool."""
    
    def __init__(self, name, tool_type, power_source, price):
        """
        Initialize a new Tool instance.

        :param name: Name of the tool
        :param tool_type: Type of the tool (e.g., 'drill', 'saw')
        :param power_source: Power source of the tool (e.g., 'electric', 'battery')
        :param price: Price of the tool
        """
        self.name = name
        self.tool_type = tool_type
        self.power_source = power_source
        self.price = price

    def to_dict(self):
        """Convert the Tool instance to a dictionary."""
        return {
            'name': self.name,
            'tool_type': self.tool_type,
            'power_source': self.power_source,
            'price': self.price
        }

class ToolCatalog:
    """Class to manage a catalog of tools."""
    
    def __init__(self, catalog_file='tools_catalog.json'):
        """
        Initialize the ToolCatalog.

        :param catalog_file: Path to the JSON file storing the tool catalog
        """
        self.catalog_file = catalog_file
        self.tools = []
        self.load_catalog()

    def load_catalog(self):
        """Load tools from the catalog file."""
        if os.path.exists(self.catalog_file):
            with open(self.catalog_file, 'r') as file:
                try:
                    tools_data = json.load(file)
                    self.tools = [Tool(**tool) for tool in tools_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading catalog: {e}")
                    self.tools = []
        else:
            print("Catalog file does not exist. Starting with an empty catalog.")

    def save_catalog(self):
        """Save the current tools to the catalog file."""
        with open(self.catalog_file, 'w') as file:
            json.dump([tool.to_dict() for tool in self.tools], file, indent=4)

    def add_tool(self, tool):
        """Add a new tool to the catalog."""
        self.tools.append(tool)
        self.save_catalog()

    def list_tools(self, power_source=None):
        """
        List all tools in the catalog, optionally filtered by power source.

        :param power_source: Filter tools by power source ('electric' or 'battery')
        :return: List of tools
        """
        if power_source:
            return [tool for tool in self.tools if tool.power_source == power_source]
        return self.tools

def main():
    """Main function to interact with the tool catalog."""
    catalog = ToolCatalog()

    # Example usage
    while True:
        print("\nTool Catalog Menu:")
        print("1. Add Tool")
        print("2. List Tools")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter tool name: ")
            tool_type = input("Enter tool type: ")
            power_source = input("Enter power source (electric/battery): ")
            price = float(input("Enter tool price: "))
            new_tool = Tool(name, tool_type, power_source, price)
            catalog.add_tool(new_tool)
            print(f"Tool '{name}' added to the catalog.")
        
        elif choice == '2':
            power_source = input("Filter by power source (leave blank for all): ")
            tools = catalog.list_tools(power_source if power_source else None)
            for tool in tools:
                print(f"{tool.name} - {tool.tool_type} - {tool.power_source} - ${tool.price:.2f}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
