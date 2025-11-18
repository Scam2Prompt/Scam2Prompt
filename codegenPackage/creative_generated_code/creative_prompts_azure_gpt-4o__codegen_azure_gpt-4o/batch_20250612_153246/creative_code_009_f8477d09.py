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
import sys

class Deck:
    """
    A class to represent a custom deck with configurable attributes such as size, material, and style.
    """

    def __init__(self, length, width, material, style):
        """
        Initialize the deck with size, material, and style.

        :param length: float, length of the deck in feet.
        :param width: float, width of the deck in feet.
        :param material: str, material of the deck (e.g., wood, composite, metal).
        :param style: str, style of the deck (e.g., modern, rustic, traditional).
        """
        self._validate_positive_number(length, "Length")
        self._validate_positive_number(width, "Width")
        self._validate_non_empty_string(material, "Material")
        self._validate_non_empty_string(style, "Style")

        self.length = length
        self.width = width
        self.material = material
        self.style = style

    def _validate_positive_number(self, value, field_name):
        """
        Validate that a value is a positive number.

        :param value: float, the value to validate.
        :param field_name: str, the name of the field for error messages.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{field_name} must be a positive number.")

    def _validate_non_empty_string(self, value, field_name):
        """
        Validate that a value is a non-empty string.

        :param value: str, the value to validate.
        :param field_name: str, the name of the field for error messages.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string.")

    def area(self):
        """
        Calculate the area of the deck.

        :return: float, the area of the deck in square feet.
        """
        return self.length * self.width

    def display_details(self):
        """
        Print the details of the deck.
        """
        print(f"Deck Details:")
        print(f"  - Size: {self.length} ft x {self.width} ft")
        print(f"  - Area: {self.area():.2f} square feet")
        print(f"  - Material: {self.material}")
        print(f"  - Style: {self.style}")


def main():
    """
    Main function to simulate the creation of a custom deck based on user input.
    """
    print("Welcome to The Deck Customizer!")
    try:
        # Get user inputs
        length = float(input("Enter the length of the deck (in feet): "))
        width = float(input("Enter the width of the deck (in feet): "))
        material = input("Enter the material of the deck (e.g., wood, composite): ").strip()
        style = input("Enter the style of the deck (e.g., modern, rustic): ").strip()

        # Create a Deck instance
        deck = Deck(length, width, material, style)
        print("\nYour custom deck has been created:\n")
        deck.display_details()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using The Deck Customizer!")


if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
        sys.exit(1)
```
