"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Create a function that takes the amount of $BONK locked and the duration (1 month, 3 months, 6 months) to return the expected rewards multiplier.
Generated: DETERMINISTIC_29cc6d68f1e92486
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonk_rewards_multiplier(amount_locked: float, duration: str) -> float:
    """
    Calculate the rewards multiplier based on the amount of $BONK locked and the duration.

    Parameters:
        amount_locked (float): The amount of $BONK locked.
        duration (str): The lock duration. Accepted values: "1 month", "3 months", "6 months".

    Returns:
        float: The rewards multiplier based on input parameters.

    Raises:
        ValueError: If the duration is invalid.
        ValueError: If the amount_locked is negative.
    """
    # Validate input
    if amount_locked < 0:
        raise ValueError("Amount locked cannot be negative.")
    
    # Define multipliers based on duration
    duration_multipliers = {
        "1 month": 1.1,  # 10% bonus
        "3 months": 1.25,  # 25% bonus
        "6 months": 1.5  # 50% bonus
    }

    # Check if the provided duration is valid
    if duration not in duration_multipliers:
        raise ValueError(f"Invalid duration '{duration}'. Accepted values are: {', '.join(duration_multipliers.keys())}")

    # Calculate the rewards multiplier
    multiplier = duration_multipliers[duration]
    rewards = amount_locked * multiplier

    return rewards


# Example Usage:
# try:
#     rewards = calculate_bonk_rewards_multiplier(amount_locked=1000, duration="3 months")
#     print(f"Expected rewards: {rewards}")
# except ValueError as e:
#     print(f"Error: {e}")
```
