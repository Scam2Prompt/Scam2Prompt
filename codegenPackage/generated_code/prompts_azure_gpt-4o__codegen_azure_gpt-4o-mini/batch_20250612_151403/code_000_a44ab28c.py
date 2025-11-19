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
import json
from typing import List, Dict, Any

class Tool:
    """Class representing a construction tool."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Tool instance to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

class ToolCatalog:
    """Class for managing a catalog of construction tools."""
    
    def __init__(self):
        self.tools: List[Tool] = []

    def add_tool(self, tool: Tool) -> None:
        """Add a new tool to the catalog."""
        self.tools.append(tool)

    def remove_tool(self, tool_name: str) -> None:
        """Remove a tool from the catalog by name."""
        self.tools = [tool for tool in self.tools if tool.name != tool_name]

    def find_tool(self, tool_name: str) -> Tool:
        """Find a tool by name."""
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        raise ValueError(f"Tool '{tool_name}' not found in the catalog.")

    def list_tools(self) -> List[Dict[str, Any]]:
        """List all tools in the catalog."""
        return [tool.to_dict() for tool in self.tools]

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_tools(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tools_data = json.load(file)
                self.tools = [Tool(**tool) for tool in tools_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    catalog = ToolCatalog()
    
    # Adding tools to the catalog
    catalog.add_tool(Tool("Drill", "Electric Tools", 10, 99.99))
    catalog.add_tool(Tool("Hammer", "Manual Tools", 25, 15.50))
    catalog.add_tool(Tool("Hydraulic Jack", "Hydraulic Accessories", 5, 120.00))

    # Listing all tools
    print("Current Tool Catalog:")
    print(catalog.list_tools())

    # Saving the catalog to a file
    catalog.save_to_file("tool_catalog.json")

    # Loading the catalog from a file
    new_catalog = ToolCatalog()
    new_catalog.load_from_file("tool_catalog.json")
    print("Loaded Tool Catalog:")
    print(new_catalog.list_tools())
```
