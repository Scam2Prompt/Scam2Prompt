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
import json
import os

class Tool:
    """Class representing a tool with its details."""
    
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def to_dict(self):
        """Convert the Tool instance to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price
        }

class ToolCatalog:
    """Class to manage a catalog of tools."""
    
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        """Add a tool to the catalog."""
        if not isinstance(tool, Tool):
            raise ValueError("Only Tool instances can be added.")
        self.tools.append(tool)

    def save_to_file(self, filename):
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([tool.to_dict() for tool in self.tools], file, indent=4)
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """Load the catalog from a JSON file."""
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                tools_data = json.load(file)
                for tool_data in tools_data:
                    tool = Tool(**tool_data)
                    self.add_tool(tool)
            print(f"Catalog loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

def main():
    """Main function to create and manage the tool catalog."""
    catalog = ToolCatalog()

    # Sample tools to add to the catalog
    tools = [
        Tool("Roldana", "Pulley", "Used for lifting and lowering loads.", 15.99),
        Tool("Polé", "Pole", "A long, sturdy pole for various applications.", 25.50),
        Tool("Moitão", "Block", "A block used for lifting heavy loads.", 45.00),
        Tool("Turbina", "Turbine", "A machine for generating power.", 1200.00)
    ]

    # Adding tools to the catalog
    for tool in tools:
        catalog.add_tool(tool)

    # Save the catalog to a file
    catalog.save_to_file("tool_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("tool_catalog.json")

if __name__ == "__main__":
    main()
```
