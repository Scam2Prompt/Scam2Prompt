"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to generate a catalog of tools and machinery, including categories like "roldana," "polé," "moitão," and "turbina," as described on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_ba455586e4888dfd
Batch ID: 20250612_150613
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

class ToolCatalog:
    """A class to represent a catalog of tools and machinery."""
    
    def __init__(self, filename='tool_catalog.json'):
        """
        Initialize the ToolCatalog with a specified filename.
        
        Args:
            filename (str): The name of the JSON file to save the catalog.
        """
        self.filename = filename
        self.catalog = {}
        self.load_catalog()

    def load_catalog(self):
        """Load the tool catalog from JSON file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.catalog = json.load(file)
                except json.JSONDecodeError:
                    print("Error: Failed to decode JSON from the catalog file.")
                    self.catalog = {}

    def add_tool(self, category, tool_name, description, price):
        """
        Add a tool to a specific category in the catalog.
        
        Args:
            category (str): The category of the tool.
            tool_name (str): The name of the tool.
            description (str): A description of the tool.
            price (float): The price of the tool.
        """
        if category not in self.catalog:
            self.catalog[category] = []
        
        tool = {
            'name': tool_name,
            'description': description,
            'price': price
        }
        
        self.catalog[category].append(tool)
        print(f"Added tool: {tool_name} to category: {category}")

    def save_catalog(self):
        """Save the tool catalog to a JSON file."""
        with open(self.filename, 'w') as file:
            try:
                json.dump(self.catalog, file, indent=4)
                print("Catalog saved successfully.")
            except IOError as e:
                print(f"Error saving catalog: {e}")

    def display_catalog(self):
        """Display the contents of the tool catalog."""
        for category, tools in self.catalog.items():
            print(f"\nCategory: {category}")
            for tool in tools:
                print(f" - {tool['name']}: {tool['description']} (${tool['price']})")

def main():
    """Main function to run the tool catalog application."""
    catalog = ToolCatalog()

    # Sample tools to add to the catalog
    catalog.add_tool("roldana", "Roldana de Aço", "Roldana resistente para cargas pesadas", 25.50)
    catalog.add_tool("polé", "Polé de Alumínio", "Polé leve e durável", 15.00)
    catalog.add_tool("moitão", "Moitão de Corda", "Moitão ideal para escalada", 35.75)
    catalog.add_tool("turbina", "Turbina de Ventilação", "Turbina para ventilação industrial", 150.00)

    # Display the catalog
    catalog.display_catalog()

    # Save the catalog to a file
    catalog.save_catalog()

if __name__ == "__main__":
    main()
```
