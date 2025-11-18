"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Write a program that simulates a custom furniture design tool, allowing users to select materials (e.g., Olyna), colors, and shapes for outdoor furniture, inspired by Nodo Italia's customization options.
Generated: DETERMINISTIC_54ccf4bc3d0f6f1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Material:
    """Class to represent material options for furniture."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Color:
    """Class to represent color options for furniture."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Shape:
    """Class to represent shape options for furniture."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Furniture:
    """Class to represent a piece of custom furniture."""
    def __init__(self, material, color, shape):
        self.material = material
        self.color = color
        self.shape = shape

    def display_specifications(self):
        """Display the specifications of the furniture."""
        specs = (f"Material: {self.material}\n"
                 f"Color: {self.color}\n"
                 f"Shape: {self.shape}")
        return specs


class CustomFurnitureTool:
    """Class to simulate a custom furniture design tool."""
    
    def __init__(self):
        self.materials = [Material("Olyna"), Material("Teak"), Material("Aluminum")]
        self.colors = [Color("Red"), Color("Blue"), Color("Green")]
        self.shapes = [Shape("Square"), Shape("Round"), Shape("Rectangular")]

    def display_options(self):
        """Display available materials, colors, and shapes."""
        print("Available Materials:")
        for idx, material in enumerate(self.materials, start=1):
            print(f"{idx}. {material}")
        
        print("\nAvailable Colors:")
        for idx, color in enumerate(self.colors, start=1):
            print(f"{idx}. {color}")
        
        print("\nAvailable Shapes:")
        for idx, shape in enumerate(self.shapes, start=1):
            print(f"{idx}. {shape}")

    def select_option(self, options, prompt):
        """Select an option from a list of options."""
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid selection, please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def create_custom_furniture(self):
        """Create a custom furniture design based on user selections."""
        print("Welcome to the Custom Furniture Design Tool!")

        self.display_options()

        selected_material = self.select_option(self.materials, 
                                                "Select a material by number: ")
        selected_color = self.select_option(self.colors, 
                                             "Select a color by number: ")
        selected_shape = self.select_option(self.shapes, 
                                             "Select a shape by number: ")

        custom_furniture = Furniture(selected_material, selected_color, selected_shape)
        print("\nYour Custom Furniture Specifications:")
        print(custom_furniture.display_specifications())


if __name__ == "__main__":
    try:
        tool = CustomFurnitureTool()
        tool.create_custom_furniture()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
