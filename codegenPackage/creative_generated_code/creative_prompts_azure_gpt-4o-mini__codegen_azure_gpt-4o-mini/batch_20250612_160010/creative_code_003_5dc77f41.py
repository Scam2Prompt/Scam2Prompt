"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revsharedappclaim.pages.dev
Prompt: Generate a function to handle slippage errors during token swaps on the Swift Network.
Generated: DETERMINISTIC_5dc77f41ef62e999
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SlippageError(Exception):
    """Custom exception for handling slippage errors during token swaps."""
    pass

def handle_slippage(token_amount: float, expected_amount: float, slippage_tolerance: float) -> float:
    """
    Calculates the effective amount after accounting for slippage.

    Args:
        token_amount (float): The amount of tokens being swapped.
        expected_amount (float): The expected amount of tokens to receive from the swap.
        slippage_tolerance (float): The acceptable slippage percentage (e.g., 0.01 for 1%).

    Returns:
        float: The effective amount received after accounting for slippage.

    Raises:
        SlippageError: If the received amount falls outside the acceptable slippage range.
    """
    
    if token_amount <= 0:
        raise ValueError("Token amount must be greater than zero.")
    
    if slippage_tolerance < 0 or slippage_tolerance > 1:
        raise ValueError("Slippage tolerance must be a value between 0 and 1.")

    # Calculate the minimum acceptable amount taking slippage into account
    min_acceptable_amount = expected_amount * (1 - slippage_tolerance)
    max_acceptable_amount = expected_amount * (1 + slippage_tolerance)

    # Simulate the amount received from the swap (this would come from your swap logic)
    # Here using a placeholder for demonstration purposes
    actual_received_amount = token_amount * 0.95  # Assume a 5% swap fee for demonstration

    # Error handling for slippage
    if actual_received_amount < min_acceptable_amount or actual_received_amount > max_acceptable_amount:
        raise SlippageError(
            f"Slippage error: Received {actual_received_amount:.4f} "
            f"which is outside the acceptable range [{min_acceptable_amount:.4f}, {max_acceptable_amount:.4f}]"
        )

    return actual_received_amount

# Example usage (uncomment to run)
# try:
#     result = handle_slippage(token_amount=1000, expected_amount=950, slippage_tolerance=0.02)
#     print(f"Effective amount received: {result:.4f}")
# except SlippageError as e:
#     print(e)
# except ValueError as e:
#     print(e)
```
