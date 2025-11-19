"""
Generated Code Metadata:
========================
Original URL: https://stlink.vip
Prompt: "Compare the average reward rate of 5.60% from stakelink's staking pool with a custom staking pool, provide a recommendation on which one to use for staking LINK tokens."
Generated: DETERMINISTIC_152f9d58bd62a98e
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def get_custom_pool_reward_rate():
    """
    Function to get the reward rate of a custom staking pool.
    Prompts the user for input and validates it.
    Returns:
        float: The reward rate of the custom staking pool.
    """
    try:
        # Prompt user for the custom pool reward rate
        reward_rate = float(input("Enter the reward rate (%) for the custom staking pool: "))
        if reward_rate < 0:
            raise ValueError("Reward rate cannot be negative.")
        return reward_rate
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

def compare_reward_rates(stakelink_rate, custom_rate):
    """
    Function to compare the reward rates of two staking pools.
    Args:
        stakelink_rate (float): The reward rate of the Stakelink staking pool.
        custom_rate (float): The reward rate of the custom staking pool.
    Returns:
        str: Recommendation on which staking pool to use.
    """
    if custom_rate > stakelink_rate:
        return f"Recommendation: Use the custom staking pool with a higher reward rate of {custom_rate:.2f}%."
    elif custom_rate < stakelink_rate:
        return f"Recommendation: Use the Stakelink staking pool with a higher reward rate of {stakelink_rate:.2f}%."
    else:
        return "Recommendation: Both staking pools offer the same reward rate. Choose based on other factors like reliability and fees."

def main():
    """
    Main function to execute the staking pool comparison.
    """
    # Define the average reward rate for Stakelink's staking pool
    stakelink_reward_rate = 5.60  # in percentage

    print(f"Stakelink's staking pool offers an average reward rate of {stakelink_reward_rate:.2f}%.")

    # Get the reward rate for the custom staking pool
    custom_reward_rate = get_custom_pool_reward_rate()

    # Compare the reward rates and provide a recommendation
    recommendation = compare_reward_rates(stakelink_reward_rate, custom_reward_rate)
    print(recommendation)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
