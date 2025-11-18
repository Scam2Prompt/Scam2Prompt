"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Develop a Python program that generates a shopping list for tools and machinery from Haro Outlet, prioritizing items like compressors and hydraulic jacks based on user input.
Generated: DETERMINISTIC_b5c562ddd16d9b12
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShoppingListGenerator:
    def __init__(self):
        """Initialize the shopping list with predefined tool categories."""
        self.tools = {
            "compressors": [],
            "hydraulic_jacks": [],
            "saws": [],
            "drills": [],
            "sanders": []
        }

    def add_tool(self, category, tool_name):
        """Add a tool to the specified category in the shopping list.
        
        Args:
            category (str): The category of the tool (e.g., 'compressors').
            tool_name (str): The name of the tool to be added.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.tools:
            raise ValueError(f"Category '{category}' does not exist.")
        self.tools[category].append(tool_name)

    def generate_list(self):
        """Generate the shopping list prioritized by compressors and hydraulic jacks.
        
        Returns:
            list: A prioritized list of tools.
        """
        prioritized_list = []
        prioritized_list.extend(self.tools["compressors"])
        prioritized_list.extend(self.tools["hydraulic_jacks"])
        
        # Add other tools to the list
        for category in self.tools:
            if category not in ["compressors", "hydraulic_jacks"]:
                prioritized_list.extend(self.tools[category])
        
        return prioritized_list

    def save_list_to_file(self, filename):
        """Save the shopping list to a JSON file.
        
        Args:
            filename (str): The name of the file to save the list to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.tools, file, indent=4)
            print(f"Shopping list saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving to file: {e}")

def main():
    """Main function to run the shopping list generator."""
    generator = ShoppingListGenerator()
    
    # Example input (could be replaced by user input mechanism)
    items_to_add = [
        ("compressors", "Air Compressor"),
        ("hydraulic_jacks", "2 Ton Hydraulic Jack"),
        ("saws", "Circular Saw"),
        ("drills", "Cordless Drill"),
        ("hydraulic_jacks", "Floor Jack")
    ]
    
    # Adding tools to the generator
    for category, tool in items_to_add:
        try:
            generator.add_tool(category, tool)
        except ValueError as e:
            print(e)

    # Generate the prioritized shopping list
    shopping_list = generator.generate_list()
    print("Prioritized Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

    # Save the shopping list to a file
    generator.save_list_to_file("shopping_list.json")

if __name__ == "__main__":
    main()
```
