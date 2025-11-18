"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secured-everlodge.pages.dev
Prompt: Write a function to calculate token discounts for trading fees and purchases within a blockchain ecosystem, inspired by Everlodge's token utility features.
Generated: DETERMINISTIC_81643bc76e32c574
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDiscountCalculator:
    """
    A class to calculate token discounts for trading fees and purchases
    within a blockchain ecosystem inspired by Everlodge's token utility features.
    """

    def __init__(self, base_fee: float, discount_rate: float):
        """
        Initializes the TokenDiscountCalculator with a base fee and discount rate.

        :param base_fee: The base trading fee or purchase cost.
        :param discount_rate: The discount rate as a percentage (e.g., 10 for 10%).
        """
        if base_fee < 0:
            raise ValueError("Base fee must be a non-negative value.")
        if not (0 <= discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")

        self.base_fee = base_fee
        self.discount_rate = discount_rate

    def calculate_discounted_fee(self) -> float:
        """
        Calculates the discounted fee based on the base fee and discount rate.

        :return: The discounted fee after applying the discount.
        """
        discount_amount = (self.discount_rate / 100) * self.base_fee
        discounted_fee = self.base_fee - discount_amount
        return discounted_fee

    def calculate_total_cost(self, quantity: int) -> float:
        """
        Calculates the total cost for a given quantity of items, applying the discount.

        :param quantity: The number of items being purchased.
        :return: Total cost after applying the discounted fee.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        discounted_fee = self.calculate_discounted_fee()
        total_cost = discounted_fee * quantity
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a base fee of 100 and a discount rate of 10%
        calculator = TokenDiscountCalculator(base_fee=100.0, discount_rate=10.0)
        
        # Calculate the discounted fee
        discounted_fee = calculator.calculate_discounted_fee()
        print(f"Discounted Fee: {discounted_fee}")

        # Calculate total cost for purchasing 5 items
        total_cost = calculator.calculate_total_cost(quantity=5)
        print(f"Total Cost for 5 items: {total_cost}")

    except ValueError as e:
        print(f"Error: {e}")
```
