"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
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

# Define constants for the Arbius token economic rules
BASE_FEE = 10.0  # Base fee in Arbius tokens
SUPPLY_THRESHOLD = 1000000  # Token supply threshold for fee adjustment
LOW_SUPPLY_MULTIPLIER = 1.5  # Multiplier applied when supply is below threshold
HIGH_SUPPLY_DISCOUNT = 0.8  # Discount applied when supply is above threshold

def calculate_task_fee(token_supply: int, base_reward: Union[int, float]) -> float:
    """
    Calculate the task fee based on the Arbius token supply and reward structure.

    Args:
        token_supply (int): The current total supply of Arbius tokens.
        base_reward (Union[int, float]): The base reward amount for the task.

    Returns:
        float: The calculated task fee.
    """
    try:
        # Ensure valid inputs
        if token_supply < 0:
            raise ValueError("Token supply must be non-negative.")
        if base_reward <= 0:
            raise ValueError("Base reward must be greater than zero.")

        # Calculate the fee multiplier based on supply
        if token_supply < SUPPLY_THRESHOLD:
            fee_multiplier = LOW_SUPPLY_MULTIPLIER
        else:
            fee_multiplier = HIGH_SUPPLY_DISCOUNT

        # Compute the task fee
        task_fee = BASE_FEE + (base_reward * fee_multiplier)

        return round(task_fee, 2)  # Round to two decimal places for precision

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input error: {ve}")
        return 0.0  # Return a default fee in case of error

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0  # Return a default fee in case of unexpected errors

# Example usage:
# task_fee = calculate_task_fee(token_supply=900000, base_reward=50)
# print(task_fee)
```
