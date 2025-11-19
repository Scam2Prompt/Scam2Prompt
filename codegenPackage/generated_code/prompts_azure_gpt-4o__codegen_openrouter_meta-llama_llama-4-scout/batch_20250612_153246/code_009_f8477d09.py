"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Create a Python program to simulate the design of a custom deck, incorporating features like size, material, and style options inspired by "The Fence Guys" services.
Generated: DETERMINISTIC_f8477d090add7fb0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# deck_designer.py

class DeckMaterial:
    """Represents a deck material with its properties and price."""

    def __init__(self, name, price_per_sqft):
        """
        Initializes a DeckMaterial object.

        Args:
            name (str): The name of the material.
            price_per_sqft (float): The price per square foot of the material.
        """
        self.name = name
        self.price_per_sqft = price_per_sqft

    def __str__(self):
        return f"{self.name}: ${self.price_per_sqft:.2f}/sqft"


class DeckStyle:
    """Represents a deck style with its description and price multiplier."""

    def __init__(self, name, description, price_multiplier):
        """
        Initializes a DeckStyle object.

        Args:
            name (str): The name of the style.
            description (str): A brief description of the style.
            price_multiplier (float): The price multiplier for the style.
        """
        self.name = name
        self.description = description
        self.price_multiplier = price_multiplier

    def __str__(self):
        return f"{self.name}: {self.description}"


class Deck:
    """Represents a custom deck with its size, material, and style."""

    def __init__(self, width, length, material, style):
        """
        Initializes a Deck object.

        Args:
            width (float): The width of the deck in feet.
            length (float): The length of the deck in feet.
            material (DeckMaterial): The material of the deck.
            style (DeckStyle): The style of the deck.
        """
        self.width = width
        self.length = length
        self.material = material
        self.style = style

    def calculate_area(self):
        """Calculates the area of the deck in square feet."""
        return self.width * self.length

    def calculate_price(self):
        """Calculates the total price of the deck."""
        area = self.calculate_area()
        material_price = area * self.material.price_per_sqft
        style_price = material_price * self.style.price_multiplier
        return style_price

    def __str__(self):
        return (
            f"Deck Size: {self.width} x {self.length} ft\n"
            f"Material: {self.material}\n"
            f"Style: {self.style}\n"
            f"Total Price: ${self.calculate_price():.2f}"
        )


def main():
    # Define available materials
    materials = [
        DeckMaterial("Pressure-Treated Wood", 1.50),
        DeckMaterial("Cedar", 3.00),
        DeckMaterial("Composite", 4.00),
        DeckMaterial("Redwood", 5.00),
    ]

    # Define available styles
    styles = [
        DeckStyle("Standard", "Basic deck design", 1.0),
        DeckStyle("Deluxe", "Premium deck design with railings", 1.5),
        DeckStyle("Elite", "High-end deck design with custom features", 2.0),
    ]

    print("Available Materials:")
    for i, material in enumerate(materials):
        print(f"{i+1}. {material}")

    material_choice = int(input("Choose a material (1-{}): ".format(len(materials)))) - 1
    chosen_material = materials[material_choice]

    print("\nAvailable Styles:")
    for i, style in enumerate(styles):
        print(f"{i+1}. {style}")

    style_choice = int(input("Choose a style (1-{}): ".format(len(styles)))) - 1
    chosen_style = styles[style_choice]

    width = float(input("Enter deck width (ft): "))
    length = float(input("Enter deck length (ft): "))

    deck = Deck(width, length, chosen_material, chosen_style)
    print("\nDeck Design Summary:")
    print(deck)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
