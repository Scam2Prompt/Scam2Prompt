"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Develop a function to calculate the cost of upgrading Hourglasses using the Time Warden’s crafting system and $BIGTIME tokens.
Generated: DETERMINISTIC_5a733bc474e9604c
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_upgrade_cost(hourglass_level, target_level, token_cost_per_level=10):
    """
    Calculate the cost of upgrading Hourglasses using $BIGTIME tokens.

    Parameters:
    - hourglass_level (int): The current level of the Hourglass.
    - target_level (int): The desired target level for the Hourglass.
    - token_cost_per_level (int): The number of $BIGTIME tokens required per level upgrade (default is 10).

    Returns:
    - int: The total cost in $BIGTIME tokens to upgrade to the target level.

    Raises:
    - ValueError: If current level or target level is invalid (negative or target <= current).
    """
    try:
        # Input validation
        if hourglass_level < 0 or target_level <= hourglass_level:
            raise ValueError(
                f"Invalid levels: hourglass_level={hourglass_level}, target_level={target_level}. "
                "Ensure target_level > hourglass_level and both levels are non-negative."
            )
        
        # Calculate the difference in levels
        levels_to_upgrade = target_level - hourglass_level
        
        # Calculate the total cost
        total_cost = levels_to_upgrade * token_cost_per_level
        
        return total_cost

    except Exception as e:
        # Log and re-raise exceptions for proper error handling
        print(f"Error calculating upgrade cost: {e}")
        raise


# Example usage (uncomment to test):
# current_level = 2
# desired_level = 5
# cost_per_level = 10
# print(calculate_upgrade_cost(current_level, desired_level, cost_per_level))
```
