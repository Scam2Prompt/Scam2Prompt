"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-shakryfi.pages.dev
Prompt: Create a function that calculates the total weighted stake for a user based on their locked $SHARK amount, duration multiplier, and average weight, as described on the Sharky staking platform.
Generated: DETERMINISTIC_dd9a0e51e7cb564a
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_weighted_stake(locked_amount, duration_multiplier, average_weight):
    """
    Calculates the total weighted stake for a user based on their locked $SHARK amount,
    duration multiplier, and average weight.

    Parameters:
        locked_amount (float): The amount of $SHARK tokens locked by the user.
        duration_multiplier (float): The multiplier based on the lock duration.
        average_weight (float): The average weight of the stake.

    Returns:
        float: The total weighted stake.

    Raises:
        ValueError: If any of the inputs are invalid (e.g., negative values).
    """
    try:
        # Input validation
        if locked_amount < 0:
            raise ValueError("locked_amount cannot be negative.")
        if duration_multiplier < 0:
            raise ValueError("duration_multiplier cannot be negative.")
        if average_weight < 0:
            raise ValueError("average_weight cannot be negative.")

        # Calculate the total weighted stake
        total_weighted_stake = locked_amount * duration_multiplier * average_weight

        return total_weighted_stake
    except ValueError as e:
        # Log the error and re-raise it
        print(f"Error: {e}")
        raise
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage:
# locked_amount = 1000.0
# duration_multiplier = 1.5
# average_weight = 0.8
# print(calculate_weighted_stake(locked_amount, duration_multiplier, average_weight))
```
