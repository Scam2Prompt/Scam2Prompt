"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skinny-iron-flat.on-fleek.app
Prompt: Create a function that calculates the price impact of a swap on the Zeedex platform for a given token pair.
Generated: DETERMINISTIC_1daf3235f0b0ec24
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZeedexSwap:
    def __init__(self, liquidity_a: float, liquidity_b: float):
        """
        Initialize the ZeedexSwap class with the given liquidity for two tokens.

        :param liquidity_a: The liquidity of token A in the pool.
        :param liquidity_b: The liquidity of token B in the pool.
        """
        if liquidity_a <= 0 or liquidity_b <= 0:
            raise ValueError("Liquidity values must be greater than zero.")
        
        self.liquidity_a = liquidity_a
        self.liquidity_b = liquidity_b

    def calculate_price_impact(self, amount_in: float) -> float:
        """
        Calculate the price impact of a swap given an amount of token A to swap for token B.

        :param amount_in: The amount of token A being swapped.
        :return: The price impact as a percentage.
        """
        if amount_in <= 0:
            raise ValueError("Swap amount must be greater than zero.")
        
        # Calculate the expected amount of token B received before price impact
        expected_out = (amount_in * self.liquidity_b) / (self.liquidity_a + amount_in)

        # Calculate the new liquidity after the swap
        new_liquidity_a = self.liquidity_a + amount_in
        new_liquidity_b = self.liquidity_b - expected_out

        # Calculate the new price
        new_price = new_liquidity_b / new_liquidity_a

        # Calculate the original price
        original_price = self.liquidity_b / self.liquidity_a

        # Calculate price impact
        price_impact = ((new_price - original_price) / original_price) * 100

        return price_impact

# Example usage (commented out for production readiness)
# zeedex = ZeedexSwap(liquidity_a=1000.0, liquidity_b=2000.0)
# price_impact = zeedex.calculate_price_impact(amount_in=100.0)
# print(f"Price Impact: {price_impact:.2f}%")
```
