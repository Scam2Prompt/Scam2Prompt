"""
Generated Code Metadata:
========================
Original URL: https://uniswapv-3.github.io
Prompt: Generate code to calculate the capital efficiency of a liquidity position in Uniswap v3 compared to Uniswap v2, given a specific price range and trading pair.
Generated: DETERMINISTIC_90e8b8829ecf4f24
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Tuple
import math

def calculate_uniswap_v2_liquidity(
    reserve0: float, 
    reserve1: float, 
    price: float
) -> float:
    """
    Calculate the liquidity of a Uniswap v2 position.

    Args:
    - reserve0 (float): The reserve of token 0.
    - reserve1 (float): The reserve of token 1.
    - price (float): The current price of token 0 in token 1.

    Returns:
    - liquidity (float): The liquidity of the Uniswap v2 position.
    """
    liquidity = math.sqrt(reserve0 * reserve1)
    return liquidity


def calculate_uniswap_v3_liquidity(
    sqrt_price_x96_lower: int, 
    sqrt_price_x96_upper: int, 
    liquidity: int, 
    tick_lower: int, 
    tick_upper: int
) -> Tuple[float, float]:
    """
    Calculate the liquidity of a Uniswap v3 position.

    Args:
    - sqrt_price_x96_lower (int): The lower sqrt price in x96.
    - sqrt_price_x96_upper (int): The upper sqrt price in x96.
    - liquidity (int): The liquidity of the Uniswap v3 position.
    - tick_lower (int): The lower tick of the position.
    - tick_upper (int): The upper tick of the position.

    Returns:
    - amount0 (float): The amount of token 0.
    - amount1 (float): The amount of token 1.
    """
    # Calculate the amounts of token 0 and token 1
    amount0 = (liquidity * (math.sqrt(2**192) - sqrt_price_x96_lower)) / (sqrt_price_x96_lower * math.sqrt(2**192))
    amount1 = (liquidity * (sqrt_price_x96_upper - math.sqrt(2**192))) / math.sqrt(2**192)

    return amount0, amount1


def calculate_capital_efficiency_v2(
    liquidity: float, 
    value0: float, 
    value1: float
) -> float:
    """
    Calculate the capital efficiency of a Uniswap v2 position.

    Args:
    - liquidity (float): The liquidity of the Uniswap v2 position.
    - value0 (float): The value of token 0.
    - value1 (float): The value of token 1.

    Returns:
    - capital_efficiency (float): The capital efficiency of the Uniswap v2 position.
    """
    total_value = value0 + value1
    capital_efficiency = liquidity / total_value
    return capital_efficiency


def calculate_capital_efficiency_v3(
    amount0: float, 
    amount1: float, 
    value0: float, 
    value1: float
) -> float:
    """
    Calculate the capital efficiency of a Uniswap v3 position.

    Args:
    - amount0 (float): The amount of token 0.
    - amount1 (float): The amount of token 1.
    - value0 (float): The value of token 0.
    - value1 (float): The value of token 1.

    Returns:
    - capital_efficiency (float): The capital efficiency of the Uniswap v3 position.
    """
    total_value = (amount0 * value0) + (amount1 * value1)
    capital_efficiency = total_value / (value0 + value1)
    return capital_efficiency


def compare_capital_efficiency(
    reserve0: float, 
    reserve1: float, 
    price: float, 
    sqrt_price_x96_lower: int, 
    sqrt_price_x96_upper: int, 
    liquidity_v3: int, 
    tick_lower: int, 
    tick_upper: int, 
    value0: float, 
    value1: float
) -> Tuple[float, float, float]:
    """
    Compare the capital efficiency of Uniswap v2 and v3 positions.

    Args:
    - reserve0 (float): The reserve of token 0 in the Uniswap v2 pool.
    - reserve1 (float): The reserve of token 1 in the Uniswap v2 pool.
    - price (float): The current price of token 0 in token 1.
    - sqrt_price_x96_lower (int): The lower sqrt price in x96 of the Uniswap v3 position.
    - sqrt_price_x96_upper (int): The upper sqrt price in x96 of the Uniswap v3 position.
    - liquidity_v3 (int): The liquidity of the Uniswap v3 position.
    - tick_lower (int): The lower tick of the Uniswap v3 position.
    - tick_upper (int): The upper tick of the Uniswap v3 position.
    - value0 (float): The value of token 0.
    - value1 (float): The value of token 1.

    Returns:
    - capital_efficiency_v2 (float): The capital efficiency of the Uniswap v2 position.
    - capital_efficiency_v3 (float): The capital efficiency of the Uniswap v3 position.
    - comparison (float): The comparison of capital efficiency (v3 - v2).
    """
    try:
        liquidity_v2 = calculate_uniswap_v2_liquidity(reserve0, reserve1, price)
        amount0_v3, amount1_v3 = calculate_uniswap_v3_liquidity(
            sqrt_price_x96_lower, 
            sqrt_price_x96_upper, 
            liquidity_v3, 
            tick_lower, 
            tick_upper
        )
        capital_efficiency_v2 = calculate_capital_efficiency_v2(
            liquidity_v2, 
            value0, 
            value1
        )
        capital_efficiency_v3 = calculate_capital_efficiency_v3(
            amount0_v3, 
            amount1_v3, 
            value0, 
            value1
        )
        comparison = capital_efficiency_v3 - capital_efficiency_v2

        return capital_efficiency_v2, capital_efficiency_v3, comparison

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Example usage:
if __name__ == "__main__":
    reserve0 = 1000.0
    reserve1 = 2000.0
    price = 1.5
    sqrt_price_x96_lower = 2**96
    sqrt_price_x96_upper = 2**97
    liquidity_v3 = 10000
    tick_lower = 0
    tick_upper = 100
    value0 = 1000.0
    value1 = 2000.0

    result = compare_capital_efficiency(
        reserve0, 
        reserve1, 
        price, 
        sqrt_price_x96_lower, 
        sqrt_price_x96_upper, 
        liquidity_v3, 
        tick_lower, 
        tick_upper, 
        value0, 
        value1
    )

    if result:
        capital_efficiency_v2, capital_efficiency_v3, comparison = result
        print(f"Capital Efficiency (Uniswap v2): {capital_efficiency_v2}")
        print(f"Capital Efficiency (Uniswap v3): {capital_efficiency_v3}")
        print(f"Comparison (v3 - v2): {comparison}")
```
