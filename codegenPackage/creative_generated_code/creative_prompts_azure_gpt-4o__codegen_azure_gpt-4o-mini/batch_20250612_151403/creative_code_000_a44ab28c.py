"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write Python code to create a catalog system for managing construction tools, including categories like "electric tools," "manual tools," and "hydraulic accessories," as described on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_a44ab28c4e24ba95
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Tool:
    """Class representing a tool in the catalog."""
    
    def __init__(self, name: str, category: str, price: float, quantity: int):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Tool instance to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }

class ToolCatalog:
    """Class for managing a catalog of tools."""
    
    def __init__(self):
        self.tools: List[Tool] = []

    def add_tool(self, tool: Tool) -> None:
        """Adds a tool to the catalog."""
        self.tools.append(tool)

    def remove_tool(self, tool_name: str) -> bool:
        """Removes a tool from the catalog by name."""
        for tool in self.tools:
            if tool.name == tool_name:
                self.tools.remove(tool)
                return True
        return False

    def find_tool(self, tool_name: str) -> Tool:
        """Finds a tool in the catalog by name."""
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        raise ValueError(f"Tool '{tool_name}' not found in the catalog.")

    def list_tools(self) -> List[Dict[str, Any]]:
        """Returns a list of all tools in the catalog as dictionaries."""
        return [tool.to_dict() for tool in self.tools]

    def save_to_file(self, file_path: str) -> None:
        """Saves the catalog to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.list_tools(), file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Loads the catalog from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                tools_data = json.load(file)
                self.tools = [Tool(**tool) for tool in tools_data]
        except IOError as e:
            print(f"Error loading catalog from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

def main():
    """Main function to demonstrate the tool catalog system."""
    catalog = ToolCatalog()
    
    # Adding tools to the catalog
    catalog.add_tool(Tool("Drill", "Electric Tools", 99.99, 10))
    catalog.add_tool(Tool("Hammer", "Manual Tools", 19.99, 25))
    catalog.add_tool(Tool("Jack", "Hydraulic Accessories", 150.00, 5))
    
    # Listing tools
    print("Current Tools in Catalog:")
    for tool in catalog.list_tools():
        print(tool)

    # Saving the catalog to a file
    catalog.save_to_file("tools_catalog.json")
    
    # Loading the catalog from a file
    new_catalog = ToolCatalog()
    new_catalog.load_from_file("tools_catalog.json")
    print("\nLoaded Tools from File:")
    for tool in new_catalog.list_tools():
        print(tool)

if __name__ == "__main__":
    main()
```
