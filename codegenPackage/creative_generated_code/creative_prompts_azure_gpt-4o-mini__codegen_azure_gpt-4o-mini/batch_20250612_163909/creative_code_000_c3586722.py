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
import os

class Tool:
    """Class representing a construction tool."""
    
    def __init__(self, name, tool_type, power_source, price):
        """
        Initialize a Tool object.

        Parameters:
        - name (str): The name of the tool.
        - tool_type (str): The type of the tool (e.g., "Drill", "Saw").
        - power_source (str): The power source of the tool (e.g., "Electric", "Battery").
        - price (float): The price of the tool.
        """
        self.name = name
        self.tool_type = tool_type
        self.power_source = power_source
        self.price = price
    
    def to_dict(self):
        """Convert the Tool object to a dictionary."""
        return {
            "name": self.name,
            "tool_type": self.tool_type,
            "power_source": self.power_source,
            "price": self.price
        }

class ToolCatalog:
    """Class for managing a catalog of tools."""
    
    def __init__(self, filename='tool_catalog.json'):
        """
        Initialize ToolCatalog and load tools from a JSON file.

        Parameters:
        - filename (str): The filename of the JSON file to load from.
        """
        self.filename = filename
        self.tools = self.load_tools()
    
    def load_tools(self):
        """Load tools from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    tools_data = json.load(file)
                    return [Tool(**tool) for tool in tools_data]
                except json.JSONDecodeError as e:
                    print(f"Error reading JSON file: {e}")
                    return []
        else:
            return []

    def save_tools(self):
        """Save the current tools to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([tool.to_dict() for tool in self.tools], file, indent=4)

    def add_tool(self, tool):
        """Add a new tool to the catalog."""
        self.tools.append(tool)
        self.save_tools()

    def get_tools_by_power_source(self, power_source):
        """Retrieve tools filtered by power source.

        Parameters:
        - power_source (str): The power source to filter by.

        Returns:
        - List[Tool]: A list of tools matching the power source.
        """
        return [tool for tool in self.tools if tool.power_source == power_source]

def main():
    """Main function to interact with the tool catalog."""
    catalog = ToolCatalog()

    # Adding a few tools to the catalog
    catalog.add_tool(Tool("Electric Drill", "Drill", "Electric", 99.99))
    catalog.add_tool(Tool("Cordless Screwdriver", "Screwdriver", "Battery", 49.99))
    catalog.add_tool(Tool("Electric Saw", "Saw", "Electric", 129.99))
    
    # Example: Retrieve battery-operated tools
    battery_tools = catalog.get_tools_by_power_source("Battery")
    
    print("Battery-operated tools:")
    for tool in battery_tools:
        print(f"{tool.name} - Type: {tool.tool_type}, Price: ${tool.price:.2f}")

if __name__ == "__main__":
    main()
```
