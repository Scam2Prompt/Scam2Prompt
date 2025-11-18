"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Create a Python program to simulate the design of a custom deck, incorporating features like size, material, and style options inspired by "The Fence Guys" services.
Generated: DETERMINISTIC_f8477d090add7fb0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CustomDeck:
    """
    A class to represent a custom deck with specific features like size, material, and style.
    """

    VALID_MATERIALS = ['wood', 'composite', 'vinyl']
    VALID_STYLES = ['traditional', 'modern', 'rustic']

    def __init__(self, width: float, length: float, material: str, style: str):
        """
        Initializes a CustomDeck instance with size, material, and style.

        :param width: The width of the deck in feet.
        :param length: The length of the deck in feet.
        :param material: The material used for the deck.
        :param style: The style of the deck.
        :raises ValueError: If width or length is non-positive, or if material/style are invalid.
        """
        self.width = self._validate_size(width)
        self.length = self._validate_size(length)
        self.material = self._validate_material(material)
        self.style = self._validate_style(style)

    def _validate_size(self, size: float) -> float:
        """
        Validates that the size is a positive number.

        :param size: The size value to validate.
        :raises ValueError: If size is non-positive.
        :return: The validated size.
        """
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        return size

    def _validate_material(self, material: str) -> str:
        """
        Validates that the material is one of the allowed options.

        :param material: The material to validate.
        :raises ValueError: If the material is not valid.
        :return: The validated material.
        """
        if material not in self.VALID_MATERIALS:
            raise ValueError(f"Invalid material. Choose from: {', '.join(self.VALID_MATERIALS)}")
        return material

    def _validate_style(self, style: str) -> str:
        """
        Validates that the style is one of the allowed options.

        :param style: The style to validate.
        :raises ValueError: If the style is not valid.
        :return: The validated style.
        """
        if style not in self.VALID_STYLES:
            raise ValueError(f"Invalid style. Choose from: {', '.join(self.VALID_STYLES)}")
        return style

    def area(self) -> float:
        """
        Calculates the area of the deck.

        :return: The area of the deck in square feet.
        """
        return self.width * self.length

    def __str__(self) -> str:
        """
        Returns a string representation of the CustomDeck instance.

        :return: A descriptive string of the deck.
        """
        return (f"Custom Deck\n"
                f"Dimensions: {self.width} ft x {self.length} ft\n"
                f"Material: {self.material.capitalize()}\n"
                f"Style: {self.style.capitalize()}\n"
                f"Area: {self.area()} sq ft")

def main():
    """
    Main function to create a custom deck instance and display its details.
    """
    try:
        # Example values (can be modified or taken as input)
        width = 12.0  # Width in feet
        length = 20.0  # Length in feet
        material = 'composite'  # Material type
        style = 'modern'  # Style type

        # Create a CustomDeck object
        deck = CustomDeck(width, length, material, style)

        # Print the deck details
        print(deck)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
