"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Suggest a library or tool to implement a discount system for an online store, including features like "гарантированная скидка от 3%," as mentioned on acula.com.ua.
Generated: DETERMINISTIC_d2f2ea0ab6bb5083
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# discount_system.py

class Discount:
    """
    Class representing a discount system for an online store.
    Features:
        - Guaranteed discount of at least 3%
    """

    def __init__(self):
        # Dictionary to store discount rates for different categories
        self.discount_rates = {
            "default": 0.03,  # Default guaranteed discount of 3%
        }

    def add_discount_rate(self, category: str, rate: float) -> None:
        """
        Add a new discount rate for a specific category.

        Args:
            category (str): The category for which the discount is applicable.
            rate (float): The discount rate (0 to 1).

        Raises:
            ValueError: If the rate is not between 0 and 1.
        """
        if not (0 <= rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")
        
        self.discount_rates[category] = rate

    def calculate_discount(self, category: str, amount: float) -> float:
        """
        Calculate the discount amount based on category and original amount.

        Args:
            category (str): The category for which the discount is applicable.
            amount (float): The original amount before discount.

        Returns:
            float: The amount of discount applied.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        # Get the discount rate for the specified category or default
        discount_rate = self.discount_rates.get(category, self.discount_rates['default'])
        
        # Calculate and return the discount amount
        discount_amount = amount * discount_rate
        return discount_amount

    def apply_discount(self, category: str, amount: float) -> float:
        """
        Apply the calculated discount to the original amount.

        Args:
            category (str): The category for which the discount is applicable.
            amount (float): The original amount before discount.

        Returns:
            float: The final amount after applying the discount.

        Raises:
            ValueError: If the amount is negative.
        """
        discount_amount = self.calculate_discount(category, amount)
        final_amount = amount - discount_amount
        return final_amount


# Example usage
if __name__ == "__main__":
    discount_system = Discount()

    try:
        # Example category with a specific discount rate
        discount_system.add_discount_rate("electronics", 0.10)  # Adding a 10% discount for electronics
        
        original_amount = 100.00  # Example original amount
        category = "electronics"
        
        # Calculate the final amount after discount
        final_amount = discount_system.apply_discount(category, original_amount)
        print(f"Original Amount: {original_amount}, Final Amount after discount: {final_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
