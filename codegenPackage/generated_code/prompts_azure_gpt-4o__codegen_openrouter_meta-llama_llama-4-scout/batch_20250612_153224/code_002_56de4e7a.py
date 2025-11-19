"""
Generated Code Metadata:
========================
Original URL: https://futureswap.pages.dev
Prompt: Generate code to calculate the maximum slippage (0.3%) for a stablecoin swap transaction using the exchange rate of 1:1, as described on the Future Swap platform.
Generated: DETERMINISTIC_56de4e7ad68aae07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_max_slippage(amount: float, exchange_rate: float = 1.0, max_slippage_percentage: float = 0.003) -> float:
    """
    Calculates the maximum slippage for a stablecoin swap transaction.

    Args:
    - amount (float): The amount of the stablecoin to be swapped.
    - exchange_rate (float): The exchange rate of the swap (default is 1.0 for 1:1).
    - max_slippage_percentage (float): The maximum allowed slippage as a percentage (default is 0.3%).

    Returns:
    - float: The maximum slippage amount.

    Raises:
    - ValueError: If the amount or exchange rate is not a positive number.
    - ValueError: If the max_slippage_percentage is not between 0 and 1.
    """

    # Validate input values
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be a positive number.")
    if max_slippage_percentage < 0 or max_slippage_percentage > 1:
        raise ValueError("Max slippage percentage must be between 0 and 1.")

    # Calculate the maximum slippage amount
    max_slippage_amount = amount * exchange_rate * max_slippage_percentage

    return max_slippage_amount


def main():
    try:
        # Example usage
        amount = 1000.0  # Amount of stablecoin to swap
        exchange_rate = 1.0  # 1:1 exchange rate
        max_slippage_percentage = 0.003  # 0.3% max slippage

        max_slippage = calculate_max_slippage(amount, exchange_rate, max_slippage_percentage)
        print(f"Maximum slippage: {max_slippage:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
