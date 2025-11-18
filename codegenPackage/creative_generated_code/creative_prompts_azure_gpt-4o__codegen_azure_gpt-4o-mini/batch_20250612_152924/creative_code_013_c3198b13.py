"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Create a program to simulate adding car accessories to a shopping cart and calculating the total cost, including VAT, as shown on the Tuning Design website.
Generated: DETERMINISTIC_c3198b13d832728e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Accessory:
    """Represents a car accessory with a name and price."""

    def __init__(self, name: str, price: float):
        """Initialize the accessory with a name and price.

        Args:
            name (str): The name of the accessory.
            price (float): The price of the accessory.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """Represents a shopping cart for car accessories."""

    VAT_RATE = 0.20  # 20% VAT

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_accessory(self, accessory: Accessory):
        """Add an accessory to the shopping cart.

        Args:
            accessory (Accessory): The accessory to add.
        """
        if not isinstance(accessory, Accessory):
            raise ValueError("Only Accessory instances can be added.")
        self.items.append(accessory)

    def calculate_total(self) -> float:
        """Calculate the total cost of items in the shopping cart including VAT.

        Returns:
            float: The total cost including VAT.
        """
        total = sum(item.price for item in self.items)
        total_with_vat = total * (1 + self.VAT_RATE)
        return total_with_vat

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items = []


def main():
    """Main function to simulate adding accessories to the shopping cart."""
    cart = ShoppingCart()

    # Create some accessories
    accessory1 = Accessory("Leather Seats", 1200.00)
    accessory2 = Accessory("Premium Sound System", 800.00)
    accessory3 = Accessory("Sunroof", 1500.00)

    # Add accessories to the cart
    try:
        cart.add_accessory(accessory1)
        cart.add_accessory(accessory2)
        cart.add_accessory(accessory3)

        # Calculate the total cost including VAT
        total_cost = cart.calculate_total()
        print(f"Total cost including VAT: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error adding accessory: {e}")

    # Clear the cart after the purchase
    cart.clear_cart()


if __name__ == "__main__":
    main()
```
