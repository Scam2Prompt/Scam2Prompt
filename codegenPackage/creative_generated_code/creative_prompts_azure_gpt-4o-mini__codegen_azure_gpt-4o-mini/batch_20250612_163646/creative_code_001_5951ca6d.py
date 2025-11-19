"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard0x0.com
Prompt: Write a function that calculates the estimated APY based on the total distributed and claimed rewards from the 0x0 Dashboard.
Generated: DETERMINISTIC_5951ca6d4c8f2d2b
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(total_distributed: float, total_claimed: float, duration_days: int) -> float:
    """
    Calculate the estimated Annual Percentage Yield (APY) based on the total distributed
    and claimed rewards.

    Parameters:
    total_distributed (float): The total amount of rewards distributed.
    total_claimed (float): The total amount of rewards claimed.
    duration_days (int): The duration over which rewards were distributed, in days.

    Returns:
    float: The estimated APY as a percentage.

    Raises:
    ValueError: If total_distributed or total_claimed are negative, or if duration_days is zero or negative.
    """

    # Validate input parameters
    if total_distributed < 0:
        raise ValueError("Total distributed rewards cannot be negative.")
    if total_claimed < 0:
        raise ValueError("Total claimed rewards cannot be negative.")
    if duration_days <= 0:
        raise ValueError("Duration in days must be greater than zero.")

    # Calculate the reward rate
    reward_rate = total_claimed / total_distributed

    # Calculate the APY based on the reward rate and duration
    apy = ((1 + reward_rate) ** (365 / duration_days) - 1) * 100

    return round(apy, 2)  # Return APY rounded to 2 decimal places

# Example usage:
if __name__ == "__main__":
    try:
        total_distributed = 10000.0  # Example total distributed rewards
        total_claimed = 5000.0        # Example total claimed rewards
        duration_days = 30             # Example duration in days

        apy = calculate_apy(total_distributed, total_claimed, duration_days)
        print(f"Estimated APY: {apy}%")
    except ValueError as e:
        print(f"Error calculating APY: {e}")
```
