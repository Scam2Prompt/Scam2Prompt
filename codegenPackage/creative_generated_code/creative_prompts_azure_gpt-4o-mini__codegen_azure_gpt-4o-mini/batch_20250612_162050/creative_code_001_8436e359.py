"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Write a function that calculates discounts for clothing items during seasonal sales, like the 30% off offer mentioned on Vaarabella's site.
Generated: DETERMINISTIC_8436e359962ac066
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiscountCalculator:
    """
    A class to calculate discounts on clothing items during seasonal sales.
    """

    def __init__(self, original_price: float, discount_percentage: float):
        """
        Initializes the DiscountCalculator with the original price and discount percentage.

        :param original_price: The original price of the clothing item.
        :param discount_percentage: The discount percentage to apply.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of the clothing item.

        :return: The price after applying the discount.
        """
        discount_amount = (self.original_price * self.discount_percentage) / 100
        discounted_price = self.original_price - discount_amount
        return round(discounted_price, 2)

    def calculate_savings(self) -> float:
        """
        Calculates the amount saved due to the discount.

        :return: The amount saved with the discount applied.
        """
        savings = (self.original_price * self.discount_percentage) / 100
        return round(savings, 2)


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of DiscountCalculator with an original price of $100 and a 30% discount
        item = DiscountCalculator(original_price=100.0, discount_percentage=30.0)
        
        # Calculate the discounted price and savings
        discounted_price = item.calculate_discounted_price()
        savings = item.calculate_savings()

        print(f"Original Price: ${item.original_price}")
        print(f"Discounted Price: ${discounted_price}")
        print(f"Total Savings: ${savings}")

    except ValueError as e:
        print(f"Error: {e}")
```
