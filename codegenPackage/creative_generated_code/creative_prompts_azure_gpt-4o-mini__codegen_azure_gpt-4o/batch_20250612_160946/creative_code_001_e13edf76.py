"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promantleclaim.pages.dev
Prompt: Write a function to calculate the estimated $COOK rewards based on the MNT locked in the Mantle LSP.
Generated: DETERMINISTIC_e13edf76dd28708d
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate estimated $COOK rewards based on MNT locked in Mantle LSP.

def calculate_cook_rewards(mnt_locked: float, reward_rate: float, duration_days: int) -> float:
    """
    Calculate the estimated $COOK rewards based on the MNT locked in Mantle LSP.

    Parameters:
        mnt_locked (float): The amount of MNT tokens locked in the Mantle LSP.
        reward_rate (float): The reward rate in $COOK per MNT per day.
        duration_days (int): The duration (in days) for which the MNT is locked.

    Returns:
        float: The estimated $COOK rewards.
    
    Raises:
        ValueError: If any of the parameters are negative.
    """
    try:
        # Input validation
        if mnt_locked < 0:
            raise ValueError("MNT locked cannot be negative.")
        if reward_rate < 0:
            raise ValueError("Reward rate cannot be negative.")
        if duration_days < 0:
            raise ValueError("Duration cannot be negative.")

        # Calculate estimated rewards
        cook_rewards = mnt_locked * reward_rate * duration_days
        return cook_rewards

    except ValueError as e:
        # Log and re-raise the error for better debugging and error handling
        print(f"Error: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        # Example values
        mnt_locked = 5000.0  # e.g., 5000 MNT tokens locked
        reward_rate = 0.05   # e.g., 0.05 $COOK per MNT per day
        duration_days = 30   # e.g., locked for 30 days
        
        # Calculate $COOK rewards
        rewards = calculate_cook_rewards(mnt_locked, reward_rate, duration_days)
        print(f"Estimated $COOK rewards: {rewards}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
