"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: Generate a Python script to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
Generated: DETERMINISTIC_e28b0171bb626d55
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_daily_rewards(grt_staked, grt_required, reward_rate):
    """
    Calculate daily rewards based on staked GRT, required GRT levels, and reward rate.

    Parameters:
        grt_staked (float): The amount of GRT staked by the user.
        grt_required (float): The required GRT level to qualify for rewards.
        reward_rate (float): The reward rate (percentage) applied to the staked GRT.

    Returns:
        float: The calculated daily reward.
    """
    if grt_staked < 0 or grt_required < 0 or reward_rate < 0:
        raise ValueError("Inputs must be non-negative values.")
    
    if grt_staked < grt_required:
        return 0.0  # No rewards if staked GRT is below the required level
    
    return grt_staked * (reward_rate / 100)


def main():
    """
    Main function to handle user input and calculate daily rewards.
    """
    try:
        # Prompt user for input
        grt_staked = float(input("Enter the amount of GRT staked: "))
        grt_required = float(input("Enter the required GRT level: "))
        reward_rate = float(input("Enter the reward rate (percentage): "))

        # Calculate daily rewards
        daily_rewards = calculate_daily_rewards(grt_staked, grt_required, reward_rate)

        # Display the result
        print(f"Your daily rewards: {daily_rewards:.2f} GRT")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
