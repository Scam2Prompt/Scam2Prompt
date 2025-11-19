"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Using the design philosophy of Linea 7, write code to create a custom kitchen cabinetry layout with minimalistic and functional features. Include options for neutral and earthy color palettes.
Generated: DETERMINISTIC_57637622e331f8b5
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_cabinetry_layout.py

class Cabinet:
    """Represents a kitchen cabinet."""

    def __init__(self, width, height, depth, color):
        """
        Initializes a Cabinet object.

        Args:
            width (float): The width of the cabinet in inches.
            height (float): The height of the cabinet in inches.
            depth (float): The depth of the cabinet in inches.
            color (str): The color of the cabinet.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color

    def __str__(self):
        return f"Cabinet - Width: {self.width}in, Height: {self.height}in, Depth: {self.depth}in, Color: {self.color}"


class KitchenLayout:
    """Represents a kitchen layout."""

    def __init__(self):
        """
        Initializes a KitchenLayout object.
        """
        self.cabinets = []
        self.color_palettes = {
            "neutral": ["white", "gray", "beige"],
            "earthy": ["brown", "green", "tan"]
        }

    def add_cabinet(self, cabinet):
        """
        Adds a cabinet to the kitchen layout.

        Args:
            cabinet (Cabinet): The cabinet to add.
        """
        self.cabinets.append(cabinet)

    def remove_cabinet(self, index):
        """
        Removes a cabinet from the kitchen layout.

        Args:
            index (int): The index of the cabinet to remove.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            del self.cabinets[index]
        except IndexError:
            print("Invalid index.")

    def display_layout(self):
        """
        Displays the kitchen layout.
        """
        print("Kitchen Layout:")
        for i, cabinet in enumerate(self.cabinets):
            print(f"{i+1}. {cabinet}")

    def generate_color_palette(self, palette_type):
        """
        Generates a color palette for the kitchen layout.

        Args:
            palette_type (str): The type of color palette (neutral or earthy).

        Returns:
            list: A list of colors in the palette.

        Raises:
            ValueError: If the palette type is invalid.
        """
        if palette_type in self.color_palettes:
            return self.color_palettes[palette_type]
        else:
            raise ValueError("Invalid palette type.")


def main():
    # Create a kitchen layout
    layout = KitchenLayout()

    # Create cabinets
    cabinet1 = Cabinet(30, 36, 12, "white")
    cabinet2 = Cabinet(24, 30, 12, "gray")
    cabinet3 = Cabinet(36, 36, 12, "brown")

    # Add cabinets to the layout
    layout.add_cabinet(cabinet1)
    layout.add_cabinet(cabinet2)
    layout.add_cabinet(cabinet3)

    # Display the layout
    layout.display_layout()

    # Generate a color palette
    neutral_palette = layout.generate_color_palette("neutral")
    earthy_palette = layout.generate_color_palette("earthy")

    print("\nColor Palettes:")
    print(f"Neutral: {neutral_palette}")
    print(f"Earthy: {earthy_palette}")


if __name__ == "__main__":
    main()
```
