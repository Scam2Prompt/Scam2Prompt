"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Write a function to calculate overdraft limits against fixed deposits, based on the loan offerings described by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_a24118334765b88a
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

# Define a function to calculate overdraft limits
def calculate_overdraft_limit(fixed_deposit_amount: Union[int, float], interest_rate: Union[int, float]) -> Union[float, str]:
    """
    Calculate the overdraft limit against fixed deposits as per the bank's loan offerings.

    Panchsheel Mercantile Co-op. Bank Ltd. provides overdraft limits as a percentage
    of the fixed deposit amount based on the interest rate.

    Example rules (hypothetical, replace with actual bank rules if known):
    - If interest rate <= 5%, overdraft limit is 80% of the FD amount.
    - If interest rate > 5% and <= 7%, overdraft limit is 70% of the FD amount.
    - If interest rate > 7%, overdraft limit is 60% of the FD amount.

    Args:
        fixed_deposit_amount (Union[int, float]): The amount of fixed deposit in currency units.
        interest_rate (Union[int, float]): The interest rate on the fixed deposit in percentage.

    Returns:
        Union[float, str]: The overdraft limit in currency units, or an error message if input is invalid.
    """

    try:
        # Validate inputs
        if fixed_deposit_amount <= 0:
            return "Fixed deposit amount must be greater than 0."
        if interest_rate < 0:
            return "Interest rate cannot be negative."

        # Determine the overdraft percentage based on interest rate
        if interest_rate <= 5:
            overdraft_percentage = 80
        elif interest_rate <= 7:
            overdraft_percentage = 70
        else:
            overdraft_percentage = 60

        # Calculate the overdraft limit
        overdraft_limit = (fixed_deposit_amount * overdraft_percentage) / 100

        return overdraft_limit

    except Exception as e:
        # Handle unexpected exceptions gracefully
        return f"An error occurred during calculation: {str(e)}"

# Example usage:
# fixed_deposit = 100000  # Replace with actual FD amount
# interest = 6.5          # Replace with actual interest rate
# print(calculate_overdraft_limit(fixed_deposit, interest))
```
