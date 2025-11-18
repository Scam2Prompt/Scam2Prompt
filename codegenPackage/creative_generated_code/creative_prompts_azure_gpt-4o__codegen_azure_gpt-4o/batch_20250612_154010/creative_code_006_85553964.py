"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaxfaupth.pages.dev
Prompt: Create a function to calculate and manage slippage during token swaps, based on the "Slippage" details provided on the site.
Generated: DETERMINISTIC_8555396448bdc009
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, InvalidOperation

def calculate_slippage(expected_amount: Decimal, actual_amount: Decimal) -> Decimal:
    """
    Calculate slippage percentage during token swaps.

    Slippage is defined as the difference between the expected amount of tokens 
    in a swap and the actual amount received, expressed as a percentage.

    Args:
        expected_amount (Decimal): The expected amount of tokens.
        actual_amount (Decimal): The actual amount of tokens received.

    Returns:
        Decimal: The slippage percentage (positive for loss, negative for gain).

    Raises:
        ValueError: If expected_amount or actual_amount is non-positive.
    """
    try:
        # Validate input
        if expected_amount <= 0 or actual_amount <= 0:
            raise ValueError("Expected amount and actual amount must be positive numbers.")
        
        # Calculate slippage percentage
        slippage = ((expected_amount - actual_amount) / expected_amount) * Decimal(100)
        return round(slippage, 6)  # Round to 6 decimal places for precision
    except InvalidOperation as e:
        raise ValueError("Invalid operation during slippage calculation. Ensure valid Decimal inputs.") from e


def manage_slippage(expected_amount: Decimal, actual_amount: Decimal, max_acceptable_slippage: Decimal) -> str:
    """
    Manage slippage during token swaps by determining if the swap is acceptable.

    Args:
        expected_amount (Decimal): The expected amount of tokens.
        actual_amount (Decimal): The actual amount of tokens received.
        max_acceptable_slippage (Decimal): The maximum acceptable slippage percentage.

    Returns:
        str: A message indicating whether the slippage is acceptable or not.

    Raises:
        ValueError: If max_acceptable_slippage is negative.
    """
    try:
        # Validate input
        if max_acceptable_slippage < 0:
            raise ValueError("Maximum acceptable slippage must be a non-negative number.")
        
        # Calculate slippage
        slippage = calculate_slippage(expected_amount, actual_amount)
        
        # Check if slippage is within acceptable limits
        if slippage > max_acceptable_slippage:
            return f"Swap rejected: Slippage of {slippage}% exceeds the maximum acceptable limit of {max_acceptable_slippage}%."
        else:
            return f"Swap accepted: Slippage of {slippage}% is within the acceptable limit of {max_acceptable_slippage}%."
    except InvalidOperation as e:
        raise ValueError("Invalid operation during slippage management. Ensure valid Decimal inputs.") from e


# Example usage
if __name__ == "__main__":
    from decimal import Decimal

    try:
        # Define example inputs
        expected_amount = Decimal("100.0")  # Expected amount of tokens
        actual_amount = Decimal("95.0")    # Actual amount received
        max_slippage = Decimal("5.0")      # Maximum acceptable slippage percentage

        # Manage slippage
        result = manage_slippage(expected_amount, actual_amount, max_slippage)
        print(result)
    except ValueError as err:
        print(f"Error: {err}")
```
