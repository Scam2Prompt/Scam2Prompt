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
# Discounted Price Calculator for Furniture Items

class FurnitureItem:
    """Represents a furniture item with a name and a price."""

    def __init__(self, name: str, original_price: float):
        """
        Initializes a FurnitureItem.

        Args:
            name (str): The name of the furniture item.
            original_price (float): The original price of the furniture item.
        """
        self.name = name
        self.original_price = original_price

    def calculate_discounted_price(self, discount_percentage: float) -> float:
        """
        Calculates the discounted price of the furniture item.

        Args:
            discount_percentage (float): The discount percentage.

        Returns:
            float: The discounted price.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        discount_amount = self.original_price * (discount_percentage / 100)
        return self.original_price - discount_amount


def calculate_discounted_price(item_name: str, original_price: float, discount_percentage: float) -> tuple:
    """
    Calculates the discounted price for a furniture item.

    Args:
        item_name (str): The name of the furniture item.
        original_price (float): The original price of the furniture item.
        discount_percentage (float): The discount percentage.

    Returns:
        tuple: A tuple containing the item name, original price, discount percentage, and discounted price.
    """
    try:
        item = FurnitureItem(item_name, original_price)
        discounted_price = item.calculate_discounted_price(discount_percentage)
        return item_name, original_price, discount_percentage, discounted_price
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    # Example usage:
    item_name = "Ліжко двоспальне Коко коричневе"
    original_price = 800.0
    discount_percentage = 7.0  # Calculated from $800 to $744

    result = calculate_discounted_price(item_name, original_price, discount_percentage)

    if result:
        item_name, original_price, discount_percentage, discounted_price = result
        print(f"Item: {item_name}")
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount: {discount_percentage}%")
        print(f"Discounted Price: ${discounted_price:.2f}")


if __name__ == "__main__":
    main()
```
