"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a program that simulates a custom furniture design tool, allowing users to select materials (e.g., Olyna), colors, and shapes for outdoor furniture, inspired by Nodo Italia's customization options.
Generated: DETERMINISTIC_54ccf4bc3d0f6f1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FurnitureDesignTool:
    def __init__(self):
        """Initialize the furniture design tool with available materials, colors, and shapes."""
        self.materials = ["Olyna", "Teak", "Aluminum", "Wicker"]
        self.colors = ["Red", "Blue", "Green", "White", "Black"]
        self.shapes = ["Square", "Round", "Rectangular", "Oval"]
        self.designs = []

    def display_options(self):
        """Display available materials, colors, and shapes to the user."""
        print("Available Materials:")
        for material in self.materials:
            print(f"- {material}")
        
        print("\nAvailable Colors:")
        for color in self.colors:
            print(f"- {color}")
        
        print("\nAvailable Shapes:")
        for shape in self.shapes:
            print(f"- {shape}")

    def create_design(self, material, color, shape):
        """Create a new furniture design with the specified material, color, and shape.
        
        Args:
            material (str): The material of the furniture.
            color (str): The color of the furniture.
            shape (str): The shape of the furniture.
        
        Raises:
            ValueError: If the material, color, or shape is not valid.
        """
        if material not in self.materials:
            raise ValueError(f"Invalid material: {material}. Choose from {self.materials}.")
        if color not in self.colors:
            raise ValueError(f"Invalid color: {color}. Choose from {self.colors}.")
        if shape not in self.shapes:
            raise ValueError(f"Invalid shape: {shape}. Choose from {self.shapes}.")

        design = {
            "material": material,
            "color": color,
            "shape": shape
        }
        self.designs.append(design)
        print(f"Design created: {design}")

    def save_designs(self, filename):
        """Save the created designs to a JSON file.
        
        Args:
            filename (str): The name of the file to save the designs.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.designs, file, indent=4)
            print(f"Designs saved to {filename}.")
        except IOError as e:
            print(f"Error saving designs: {e}")

    def load_designs(self, filename):
        """Load designs from a JSON file.
        
        Args:
            filename (str): The name of the file to load the designs from.
        
        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.designs = json.load(file)
            print(f"Designs loaded from {filename}.")
        except IOError as e:
            print(f"Error loading designs: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

def main():
    """Main function to run the furniture design tool."""
    tool = FurnitureDesignTool()
    tool.display_options()

    while True:
        try:
            material = input("Select a material: ")
            color = input("Select a color: ")
            shape = input("Select a shape: ")
            tool.create_design(material, color, shape)
        except ValueError as e:
            print(e)

        another = input("Would you like to create another design? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    save_file = input("Enter filename to save designs (e.g., designs.json): ")
    tool.save_designs(save_file)

if __name__ == "__main__":
    main()
```
