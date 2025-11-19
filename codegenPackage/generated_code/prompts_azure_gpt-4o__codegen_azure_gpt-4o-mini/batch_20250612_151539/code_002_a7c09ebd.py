"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: Create a function to calculate discounted prices for furniture items, referencing the discount examples provided on the Joss Home site (e.g., "Ліжко двоспальне Коко коричневе" with a discount from $800 to $744).
Generated: DETERMINISTIC_a7c09ebd4c91a1aa
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FurnitureItem:
    """
    A class to represent a furniture item with a price and discount.
    """

    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes a new FurnitureItem instance.

        :param name: The name of the furniture item.
        :param original_price: The original price of the item.
        :param discount_percentage: The discount percentage to apply.
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of the furniture item.

        :return: The discounted price after applying the discount.
        :raises ValueError: If the original price or discount percentage is negative.
        """
        if self.original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return round(discounted_price, 2)


def main():
    """
    Main function to demonstrate the calculation of discounted prices for furniture items.
    """
    try:
        # Example furniture item
        item_name = "Ліжко двоспальне Коко коричневе"
        original_price = 800.00  # Original price in dollars
        discount_percentage = 7.0  # Discount percentage

        # Create a FurnitureItem instance
        furniture_item = FurnitureItem(item_name, original_price, discount_percentage)

        # Calculate and display the discounted price
        discounted_price = furniture_item.calculate_discounted_price()
        print(f"The discounted price for '{item_name}' is: ${discounted_price}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
