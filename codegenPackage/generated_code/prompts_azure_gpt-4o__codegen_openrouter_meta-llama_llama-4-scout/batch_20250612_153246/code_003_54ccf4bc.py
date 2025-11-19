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
# furniture_design_tool.py

class Material:
    """Represents a material for outdoor furniture."""
    def __init__(self, name, description, price):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the material.
            description (str): A brief description of the material.
            price (float): The price of the material per unit.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}/unit"


class Color:
    """Represents a color for outdoor furniture."""
    def __init__(self, name, hex_code):
        """
        Initializes a Color object.

        Args:
            name (str): The name of the color.
            hex_code (str): The hex code of the color.
        """
        self.name = name
        self.hex_code = hex_code

    def __str__(self):
        return f"{self.name} ({self.hex_code})"


class Shape:
    """Represents a shape for outdoor furniture."""
    def __init__(self, name, description):
        """
        Initializes a Shape object.

        Args:
            name (str): The name of the shape.
            description (str): A brief description of the shape.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Furniture:
    """Represents a piece of outdoor furniture."""
    def __init__(self, material, color, shape):
        """
        Initializes a Furniture object.

        Args:
            material (Material): The material of the furniture.
            color (Color): The color of the furniture.
            shape (Shape): The shape of the furniture.
        """
        self.material = material
        self.color = color
        self.shape = shape

    def __str__(self):
        return f"Furniture - Material: {self.material.name}, Color: {self.color.name}, Shape: {self.shape.name}"

    def get_price(self):
        return self.material.price

    def get_description(self):
        return f"{self.material.description}, {self.color.hex_code}, {self.shape.description}"


def main():
    # Define available materials
    materials = [
        Material("Olyna", "Durable and weather-resistant", 50.0),
        Material("Teak", "Sustainable and stylish", 75.0),
        Material("Recycled Plastic", "Eco-friendly and low-maintenance", 30.0),
    ]

    # Define available colors
    colors = [
        Color("White", "#FFFFFF"),
        Color("Gray", "#808080"),
        Color("Brown", "#964B00"),
    ]

    # Define available shapes
    shapes = [
        Shape("Rectangle", "Classic and versatile"),
        Shape("Circle", "Modern and sleek"),
        Shape("Oval", "Elegant and sophisticated"),
    ]

    print("Custom Furniture Design Tool")

    # Display available materials
    print("\nAvailable Materials:")
    for i, material in enumerate(materials):
        print(f"{i+1}. {material}")

    # Get user material selection
    while True:
        try:
            material_index = int(input("\nSelect a material (enter the number): ")) - 1
            if 0 <= material_index < len(materials):
                selected_material = materials[material_index]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display available colors
    print("\nAvailable Colors:")
    for i, color in enumerate(colors):
        print(f"{i+1}. {color}")

    # Get user color selection
    while True:
        try:
            color_index = int(input("\nSelect a color (enter the number): ")) - 1
            if 0 <= color_index < len(colors):
                selected_color = colors[color_index]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display available shapes
    print("\nAvailable Shapes:")
    for i, shape in enumerate(shapes):
        print(f"{i+1}. {shape}")

    # Get user shape selection
    while True:
        try:
            shape_index = int(input("\nSelect a shape (enter the number): ")) - 1
            if 0 <= shape_index < len(shapes):
                selected_shape = shapes[shape_index]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create furniture object
    furniture = Furniture(selected_material, selected_color, selected_shape)

    # Display furniture details
    print(f"\nYou designed a {furniture}")
    print(f"Price: ${furniture.get_price():.2f}")
    print(f"Description: {furniture.get_description()}")


if __name__ == "__main__":
    main()
```
