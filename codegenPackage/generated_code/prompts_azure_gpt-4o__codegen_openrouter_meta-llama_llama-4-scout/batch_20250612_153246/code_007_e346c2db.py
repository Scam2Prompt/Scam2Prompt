"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Write a Python script to simulate a shopping cart system for surgical instruments, referencing product categories like "Bone Rongeurs," "Autopsy Knives," and "Resection Knives" from the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_e346c2db8c3d8ce0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class SurgicalInstrument:
    """Represents a surgical instrument with a name, price, and category."""

    def __init__(self, name, price, category):
        """
        Initializes a SurgicalInstrument.

        Args:
            name (str): The name of the instrument.
            price (float): The price of the instrument.
            category (str): The category of the instrument.
        """
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"


class ShoppingCart:
    """Simulates a shopping cart for surgical instruments."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.instruments = []

    def add_instrument(self, instrument):
        """
        Adds a surgical instrument to the cart.

        Args:
            instrument (SurgicalInstrument): The instrument to add.

        Raises:
            TypeError: If the instrument is not a SurgicalInstrument.
        """
        if not isinstance(instrument, SurgicalInstrument):
            raise TypeError("Only SurgicalInstrument instances can be added to the cart")
        self.instruments.append(instrument)

    def remove_instrument(self, instrument_name):
        """
        Removes a surgical instrument from the cart by name.

        Args:
            instrument_name (str): The name of the instrument to remove.

        Raises:
            ValueError: If the instrument is not found in the cart.
        """
        for instrument in self.instruments:
            if instrument.name == instrument_name:
                self.instruments.remove(instrument)
                return
        raise ValueError("Instrument not found in cart")

    def calculate_total(self):
        """Calculates the total cost of the instruments in the cart."""
        return sum(instrument.price for instrument in self.instruments)

    def __str__(self):
        cart_contents = "\n".join(str(instrument) for instrument in self.instruments)
        return f"Shopping Cart:\n{cart_contents}\nTotal: ${self.calculate_total():.2f}"


def main():
    # Define some surgical instruments
    bone_rongeur = SurgicalInstrument("Bone Rongeur", 50.0, "Bone Rongeurs")
    autopsy_knife = SurgicalInstrument("Autopsy Knife", 20.0, "Autopsy Knives")
    resection_knife = SurgicalInstrument("Resection Knife", 30.0, "Resection Knives")

    # Create a shopping cart
    cart = ShoppingCart()

    try:
        # Add instruments to the cart
        cart.add_instrument(bone_rongeur)
        cart.add_instrument(autopsy_knife)
        cart.add_instrument(resection_knife)

        # Print the cart contents
        print(cart)

        # Remove an instrument from the cart
        cart.remove_instrument("Autopsy Knife")

        # Print the updated cart contents
        print("\nAfter removing Autopsy Knife:")
        print(cart)

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
