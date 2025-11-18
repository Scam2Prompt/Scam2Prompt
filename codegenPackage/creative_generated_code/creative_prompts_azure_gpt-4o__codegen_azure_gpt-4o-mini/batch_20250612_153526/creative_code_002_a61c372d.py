"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Create a function that calculates the rewards multiplier for $BONK based on the locking duration (1 month, 3 months, or 6 months) using the multiplier values provided on the Bonk Rewards site.
Generated: DETERMINISTIC_a61c372dba05a633
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_rewards_multiplier(lock_duration_months):
    """
    Calculate the rewards multiplier for $BONK based on the locking duration.

    Args:
        lock_duration_months (int): The number of months for which the $BONK is locked.
                                      Acceptable values are 1, 3, or 6.

    Returns:
        float: The rewards multiplier corresponding to the locking duration.

    Raises:
        ValueError: If the lock_duration_months is not one of the acceptable values.
    """
    # Define the multipliers based on the locking duration
    multipliers = {
        1: 1.0,    # Multiplier for 1 month
        3: 1.5,    # Multiplier for 3 months
        6: 2.0     # Multiplier for 6 months
    }

    # Validate the input
    if lock_duration_months not in multipliers:
        raise ValueError("Invalid lock duration. Acceptable values are 1, 3, or 6 months.")

    # Return the corresponding multiplier
    return multipliers[lock_duration_months]

# Example usage (this should not be part of the production-ready function):
if __name__ == "__main__":
    try:
        duration = 3  # Example duration in months
        multiplier = calculate_rewards_multiplier(duration)
        print(f"The rewards multiplier for {duration} months is: {multiplier}")
    except ValueError as e:
        print(f"Error: {e}")
```
