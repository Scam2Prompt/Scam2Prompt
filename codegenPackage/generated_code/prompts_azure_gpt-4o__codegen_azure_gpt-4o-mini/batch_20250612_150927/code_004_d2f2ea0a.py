"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Suggest a library or tool to implement a discount system for an online store, including features like "гарантированная скидка от 3%," as mentioned on acula.com.ua.
Generated: DETERMINISTIC_d2f2ea0ab6bb5083
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

class DiscountSystem:
    """
    A class to represent a discount system for an online store.
    
    Attributes
    ----------
    discounts : dict
        A dictionary to store discount codes and their corresponding discount percentages.
    """

    def __init__(self):
        """Initializes the DiscountSystem with an empty discount dictionary."""
        self.discounts = {}

    def add_discount(self, code: str, percentage: float) -> None:
        """
        Adds a discount code with its corresponding percentage to the system.
        
        Parameters
        ----------
        code : str
            The discount code to be added.
        percentage : float
            The discount percentage (should be between 0 and 100).
        
        Raises
        ------
        ValueError
            If the percentage is not between 0 and 100.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        self.discounts[code] = percentage

    def apply_discount(self, code: str, total_amount: float) -> float:
        """
        Applies a discount to the total amount based on the discount code.
        
        Parameters
        ----------
        code : str
            The discount code to apply.
        total_amount : float
            The original total amount before discount.
        
        Returns
        -------
        float
            The total amount after applying the discount.
        
        Raises
        ------
        KeyError
            If the discount code does not exist.
        ValueError
            If the total amount is negative.
        """
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative.")
        
        if code not in self.discounts:
            raise KeyError(f"Discount code '{code}' does not exist.")
        
        discount_percentage = self.discounts[code]
        discount_amount = (discount_percentage / 100) * total_amount
        return total_amount - discount_amount

    def list_discounts(self) -> dict:
        """
        Returns a dictionary of all available discount codes and their percentages.
        
        Returns
        -------
        dict
            A dictionary of discount codes and their corresponding percentages.
        """
        return self.discounts


# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()
    
    # Adding discounts
    try:
        discount_system.add_discount("SAVE3", 3)
        discount_system.add_discount("SAVE10", 10)
    except ValueError as e:
        print(f"Error adding discount: {e}")

    # Applying a discount
    try:
        total = 100.0  # Original total amount
        discounted_total = discount_system.apply_discount("SAVE3", total)
        print(f"Total after discount: {discounted_total:.2f}")
    except (KeyError, ValueError) as e:
        print(f"Error applying discount: {e}")

    # Listing all discounts
    print("Available discounts:", discount_system.list_discounts())
```
