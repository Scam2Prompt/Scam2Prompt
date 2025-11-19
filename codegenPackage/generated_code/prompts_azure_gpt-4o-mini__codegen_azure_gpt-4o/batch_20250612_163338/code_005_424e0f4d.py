"""
Generated Code Metadata:
========================
Original URL: https://uniswapv-3.github.io
Prompt: Write a function that calculates the capital efficiency of a liquidity position in Uniswap v3 compared to Uniswap v2, considering the new concentrated liquidity feature.
Generated: DETERMINISTIC_424e0f4df2af0c52
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_capital_efficiency(liquidity_v3: float, price_lower: float, price_upper: float, liquidity_v2: float) -> float:
    """
    Calculate the capital efficiency of a liquidity position in Uniswap v3 compared to Uniswap v2.

    Parameters:
        liquidity_v3 (float): The liquidity provided in Uniswap v3.
        price_lower (float): The lower bound of the price range in Uniswap v3.
        price_upper (float): The upper bound of the price range in Uniswap v3.
        liquidity_v2 (float): The liquidity provided in Uniswap v2.

    Returns:
        float: The capital efficiency ratio (Uniswap v3 efficiency / Uniswap v2 efficiency).

    Raises:
        ValueError: If price_lower or price_upper is non-positive, or if price_lower >= price_upper.
        ValueError: If liquidity_v2 is non-positive.
    """
    # Validate inputs
    if price_lower <= 0 or price_upper <= 0:
        raise ValueError("Price bounds must be positive.")
    if price_lower >= price_upper:
        raise ValueError("Price lower bound must be less than price upper bound.")
    if liquidity_v2 <= 0:
        raise ValueError("Liquidity in Uniswap v2 must be positive.")

    # Calculate the price range width in Uniswap v3
    price_range_width_v3 = price_upper - price_lower

    # Calculate the capital efficiency for Uniswap v3
    # Uniswap v3 concentrates liquidity within a specific price range
    capital_efficiency_v3 = liquidity_v3 / price_range_width_v3

    # Calculate the capital efficiency for Uniswap v2
    # Uniswap v2 spreads liquidity across the entire price range
    capital_efficiency_v2 = liquidity_v2 / math.inf  # Liquidity is spread across infinite range

    # Compare efficiencies (Uniswap v3 vs Uniswap v2)
    # Since Uniswap v2 spreads liquidity across infinite range, its efficiency is effectively 0
    # Thus, the efficiency ratio is infinite for Uniswap v3
    efficiency_ratio = capital_efficiency_v3 / capital_efficiency_v2 if capital_efficiency_v2 > 0 else float('inf')

    return efficiency_ratio


# Example usage:
try:
    v3_liquidity = 1000.0
    lower_bound = 1.0
    upper_bound = 2.0
    v2_liquidity = 1000.0

    efficiency = calculate_capital_efficiency(v3_liquidity, lower_bound, upper_bound, v2_liquidity)
    print(f"Capital Efficiency Ratio (Uniswap v3 vs Uniswap v2): {efficiency}")
except ValueError as e:
    print(f"Error: {e}")
```
