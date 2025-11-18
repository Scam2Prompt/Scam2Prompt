"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstarter.cyou
Prompt: Create a program to calculate the cashback earned from purchases made by referred friends on Tonstarter, considering the maximum cashback rate of 35%.
Generated: DETERMINISTIC_48e66a01665c3a27
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate cashback earned from purchases made by referred friends on Tonstarter.

# Import decimal for precise financial calculations
from decimal import Decimal

class CashbackCalculator:
    """
    A class to calculate cashback earned based on purchases made by referred friends.
    """

    def __init__(self, max_cashback_rate: Decimal):
        """
        Initialize the CashbackCalculator with a maximum cashback rate.

        :param max_cashback_rate: Maximum cashback rate (e.g., 0.35 for 35%)
        """
        if max_cashback_rate > Decimal("1") or max_cashback_rate < Decimal("0"):
            raise ValueError("Cashback rate must be between 0 and 1.")
        self.max_cashback_rate = max_cashback_rate

    def calculate_cashback(self, purchases: list[Decimal]) -> Decimal:
        """
        Calculate the total cashback earned from a list of purchases.

        :param purchases: List of purchase amounts (Decimal)
        :return: Total cashback earned (Decimal)
        """
        if not purchases:
            return Decimal("0")
        
        total_cashback = Decimal("0")
        
        for purchase in purchases:
            if purchase < Decimal("0"):
                raise ValueError(f"Purchase amount cannot be negative: {purchase}")
            cashback = purchase * self.max_cashback_rate
            total_cashback += cashback
        
        return total_cashback


# Application entry point
if __name__ == "__main__":
    import sys

    try:
        # Initialize calculator with a 35% cashback rate
        calculator = CashbackCalculator(max_cashback_rate=Decimal("0.35"))

        # Example purchases made by referred friends
        purchases = [
            Decimal("100.00"),  # Purchase 1
            Decimal("200.50"),  # Purchase 2
            Decimal("75.25"),   # Purchase 3
        ]

        # Calculate total cashback
        total_cashback = calculator.calculate_cashback(purchases)
        print(f"Total cashback earned: ${total_cashback:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
