"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enosysglobal.net
Prompt: Create a function to calculate the minimum received amount for a token swap on the Ēnosys DEX, factoring in price impact and swap fees.
Generated: DETERMINISTIC_1c0ced6a4835eff8
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_min_received_amount(
    input_amount: float,
    price_impact: float,
    swap_fee: float,
    slippage_tolerance: float
) -> float:
    """
    Calculate the minimum received amount for a token swap on the Ēnosys DEX.

    Args:
        input_amount (float): The amount of input tokens for the swap.
        price_impact (float): The price impact of the swap (as a decimal, e.g., 0.01 for 1%).
        swap_fee (float): The swap fee (as a decimal, e.g., 0.003 for 0.3%).
        slippage_tolerance (float): The allowed slippage tolerance for the swap 
                                    (as a decimal, e.g., 0.005 for 0.5%).

    Returns:
        float: The minimum amount of tokens expected to receive after the swap.

    Raises:
        ValueError: If any of the input values are negative or exceed 1.
    """
    # Input validation
    if not (0 <= price_impact <= 1):
        raise ValueError("Price impact must be between 0 and 1.")
    if not (0 <= swap_fee <= 1):
        raise ValueError("Swap fee must be between 0 and 1.")
    if not (0 <= slippage_tolerance <= 1):
        raise ValueError("Slippage tolerance must be between 0 and 1.")
    if input_amount < 0:
        raise ValueError("Input amount must be non-negative.")

    # Calculate effective amount after price impact and fees
    effective_amount = input_amount * (1 - price_impact) * (1 - swap_fee)

    # Factor in slippage tolerance
    min_received_amount = effective_amount * (1 - slippage_tolerance)

    return min_received_amount


# Example Usage:
if __name__ == "__main__":
    try:
        input_amount = 1000  # Example token input amount
        price_impact = 0.02  # 2% price impact
        swap_fee = 0.003     # 0.3% swap fee
        slippage_tolerance = 0.005  # 0.5% slippage tolerance

        result = calculate_min_received_amount(
            input_amount, price_impact, swap_fee, slippage_tolerance
        )
        print(f"Minimum received amount: {result:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
