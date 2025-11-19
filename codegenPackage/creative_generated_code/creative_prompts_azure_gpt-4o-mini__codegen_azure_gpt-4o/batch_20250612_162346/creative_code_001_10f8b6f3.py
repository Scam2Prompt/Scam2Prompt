"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkswap-bya.pages.dev
Prompt: Write a Python function that calculates the slippage for a swap transaction on BonkSwap based on the provided liquidity and price impact.
Generated: DETERMINISTIC_10f8b6f32579efd4
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_slippage(liquidity_pool, amount_in, price_impact_percent):
    """
    Calculate the slippage for a swap transaction on BonkSwap.

    Parameters:
    ----------
    liquidity_pool : dict
        A dictionary containing the liquidity of the two tokens in the pool.
        Example: {"tokenA": 100000, "tokenB": 200000}
    amount_in : float
        The amount of the input token being swapped.
    price_impact_percent : float
        The estimated price impact of the swap (in percentage).

    Returns:
    -------
    float
        The calculated slippage as a percentage.
    """

    # Validate inputs
    if not isinstance(liquidity_pool, dict) or "tokenA" not in liquidity_pool or "tokenB" not in liquidity_pool:
        raise ValueError("Invalid liquidity_pool. Must be a dictionary with keys 'tokenA' and 'tokenB'.")
    if not isinstance(amount_in, (float, int)) or amount_in <= 0:
        raise ValueError("amount_in must be a positive number.")
    if not isinstance(price_impact_percent, (float, int)) or price_impact_percent <= 0:
        raise ValueError("price_impact_percent must be a positive number.")

    # Extract liquidity values
    token_a_liquidity = liquidity_pool["tokenA"]
    token_b_liquidity = liquidity_pool["tokenB"]

    if token_a_liquidity <= 0 or token_b_liquidity <= 0:
        raise ValueError("Liquidity values must be positive.")

    # Calculate the slippage
    # Slippage formula: (Price Impact / 100) * (amount_in / total liquidity)
    price_impact = price_impact_percent / 100
    total_liquidity = token_a_liquidity + token_b_liquidity
    slippage = price_impact * (amount_in / total_liquidity)

    # Return slippage as a percentage
    return slippage * 100


# Example usage:
try:
    liquidity_pool = {"tokenA": 100000, "tokenB": 200000}
    amount_in = 5000
    price_impact_percent = 2.5
    result = calculate_slippage(liquidity_pool, amount_in, price_impact_percent)
    print(f"Slippage: {result:.2f}%")
except ValueError as e:
    print(f"Error: {e}")
```
