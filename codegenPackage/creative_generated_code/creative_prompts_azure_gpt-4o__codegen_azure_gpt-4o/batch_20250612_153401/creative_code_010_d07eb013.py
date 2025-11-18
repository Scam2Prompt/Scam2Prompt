"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Generate code in Python to calculate trading fee discounts for $ETFS token holders based on their holdings, as outlined in ETFSwap's benefits.
Generated: DETERMINISTIC_d07eb01373ae346a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

class ETFSwapFeeCalculator:
    """
    A class to calculate trading fee discounts for $ETFS token holders based on their holdings.
    Attributes:
        base_fee (float): The base trading fee percentage.
        discount_tiers (Dict[int, float]): A dictionary mapping $ETFS token thresholds to discount percentages.
    """

    def __init__(self, base_fee: float = 0.1):
        """
        Initialize the ETFSwapFeeCalculator with a base fee and discount tiers.
        
        Args:
            base_fee (float): The base trading fee percentage. Default is 0.1% (0.001).
        """
        self.base_fee = base_fee  # Base trading fee in percentage
        self.discount_tiers = {
            1000: 0.10,  # 10% discount for holdings of 1000 or more $ETFS
            5000: 0.20,  # 20% discount for holdings of 5000 or more $ETFS
            10000: 0.30, # 30% discount for holdings of 10000 or more $ETFS
        }

    def calculate_discount(self, etfs_holdings: int) -> float:
        """
        Calculate the discount percentage based on $ETFS token holdings.
        
        Args:
            etfs_holdings (int): Amount of $ETFS tokens held by the user.

        Returns:
            float: Discount percentage for the given holdings.
        """
        discount = 0.0
        for threshold, tier_discount in sorted(self.discount_tiers.items(), reverse=True):
            if etfs_holdings >= threshold:
                discount = tier_discount
                break
        return discount

    def calculate_final_fee(self, etfs_holdings: int) -> float:
        """
        Calculate the final trading fee percentage after applying the discount.

        Args:
            etfs_holdings (int): Amount of $ETFS tokens held by the user.

        Returns:
            float: Final trading fee percentage after discount.
        """
        try:
            discount = self.calculate_discount(etfs_holdings)
            final_fee = self.base_fee * (1 - discount)
            return round(final_fee, 4)  # Round to 4 decimal places for precision
        except Exception as e:
            # Handle unexpected errors and return a safe default
            print(f"Error calculating final fee: {e}")
            return self.base_fee

# Example usage:
if __name__ == "__main__":
    fee_calculator = ETFSwapFeeCalculator(base_fee=0.1)  # Initialize with a base fee of 0.1%
    
    # Sample user holdings
    user_holdings = [500, 1000, 7500, 15000, 0]  # Example $ETFS token holdings
    
    for holdings in user_holdings:
        final_fee = fee_calculator.calculate_final_fee(holdings)
        print(f"$ETFS Holdings: {holdings}, Final Fee: {final_fee}%")
```
