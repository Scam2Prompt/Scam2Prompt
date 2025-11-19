"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Generate a function to check if a user qualifies for rewards based on their $BANANA holdings and the time held.
Generated: DETERMINISTIC_ab06cc8be75da4e6
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

# Define a custom exception for invalid input
class InvalidInputError(Exception):
    pass

def qualifies_for_rewards(banana_holdings, holding_period_days):
    """
    Function to check if a user qualifies for rewards based on their $BANANA holdings and time held.

    Parameters:
        banana_holdings (float): The amount of $BANANA the user holds.
        holding_period_days (int): The number of days the user has held the $BANANA.

    Returns:
        bool: True if the user qualifies for rewards, False otherwise.

    Raises:
        InvalidInputError: If either input is invalid.
    """
    # Validate inputs
    if not isinstance(banana_holdings, (int, float)) or banana_holdings < 0:
        raise InvalidInputError("banana_holdings must be a non-negative number.")
    if not isinstance(holding_period_days, int) or holding_period_days < 0:
        raise InvalidInputError("holding_period_days must be a non-negative integer.")

    # Define reward qualification criteria
    MIN_BANANA_HOLDINGS = 1000  # Minimum $BANANA required to qualify
    MIN_HOLDING_PERIOD = 30  # Minimum holding period (in days) to qualify

    # Check qualification
    if banana_holdings >= MIN_BANANA_HOLDINGS and holding_period_days >= MIN_HOLDING_PERIOD:
        return True  # User qualifies for rewards
    return False  # User does not qualify

# Usage Example:
try:
    user_qualifies = qualifies_for_rewards(1200.5, 45)
    if user_qualifies:
        print("User qualifies for rewards!")
    else:
        print("User does not qualify for rewards.")
except InvalidInputError as e:
    print(f"Error: {e}")
```
