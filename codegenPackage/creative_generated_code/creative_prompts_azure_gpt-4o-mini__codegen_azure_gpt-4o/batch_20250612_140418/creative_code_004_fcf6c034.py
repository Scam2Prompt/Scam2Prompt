"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrade-fegs.pages.dev
Prompt: Explain how to calculate the price impact and minimum output for a FEG Token swap in a decentralized exchange environment.
Generated: DETERMINISTIC_fcf6c0344cc65008
Batch ID: 20250612_140418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class FEGSwap:
    def __init__(self, reserve_in, reserve_out):
        """
        Initializes the FEGSwap instance with reserves for input and output tokens.

        Args:
            reserve_in (float): Reserve of the input token in the liquidity pool.
            reserve_out (float): Reserve of the output token in the liquidity pool.
        """
        self.reserve_in = float(reserve_in)
        self.reserve_out = float(reserve_out)

    def calculate_price_impact(self, amount_in):
        """
        Calculates the price impact for a given swap amount.

        Args:
            amount_in (float): Amount of input tokens being swapped.

        Returns:
            float: Price impact as a percentage.
        """
        if amount_in <= 0:
            raise ValueError("Input amount must be greater than zero.")
        
        original_price = self.reserve_out / self.reserve_in
        new_reserve_in = self.reserve_in + amount_in
        new_reserve_out = self.reserve_out - self.get_amount_out(amount_in)
        new_price = new_reserve_out / new_reserve_in

        price_impact = ((new_price - original_price) / original_price) * 100
        return abs(price_impact)

    def get_amount_out(self, amount_in):
        """
        Calculates the output token amount based on the swap formula.

        Args:
            amount_in (float): Amount of input tokens being swapped.

        Returns:
            float: Amount of output tokens to be received.
        """
        if amount_in <= 0:
            raise ValueError("Input amount must be greater than zero.")

        # Constant product formula: (reserve_in + amount_in) * (reserve_out - amount_out) = reserve_in * reserve_out
        # Simplified formula for output amount:
        numerator = amount_in * self.reserve_out
        denominator = self.reserve_in + amount_in
        return numerator / denominator

    def calculate_minimum_output(self, amount_in, slippage_tolerance):
        """
        Calculates the minimum output amount based on slippage tolerance.

        Args:
            amount_in (float): Amount of input tokens being swapped.
            slippage_tolerance (float): Slippage tolerance as a percentage (e.g., 0.5 for 0.5%).

        Returns:
            float: Minimum amount of output tokens to be received.
        """
        if slippage_tolerance < 0 or slippage_tolerance > 100:
            raise ValueError("Slippage tolerance must be between 0 and 100.")

        amount_out = self.get_amount_out(amount_in)
        slippage_factor = 1 - (slippage_tolerance / 100)
        return amount_out * slippage_factor

# Example Usage:
if __name__ == "__main__":
    try:
        # Initialize reserves (example values)
        reserve_in = 1000.0  # Reserve of input tokens in the pool
        reserve_out = 500.0  # Reserve of output tokens in the pool

        swap = FEGSwap(reserve_in, reserve_out)

        amount_in = 10.0  # Amount of input tokens for swap
        slippage_tolerance = 1.0  # Slippage tolerance in percentage

        # Calculate price impact
        price_impact = swap.calculate_price_impact(amount_in)
        print(f"Price Impact: {price_impact:.2f}%")

        # Calculate minimum output
        min_output = swap.calculate_minimum_output(amount_in, slippage_tolerance)
        print(f"Minimum Output After Slippage: {min_output:.6f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
