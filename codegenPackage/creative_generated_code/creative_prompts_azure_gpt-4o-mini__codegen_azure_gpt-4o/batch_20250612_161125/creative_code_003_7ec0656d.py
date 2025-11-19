"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20claim-dashboard.pages.dev
Prompt: Generate a function that calculates estimated rewards for DOGE20 staking based on dynamic rewards rates.
Generated: DETERMINISTIC_7ec0656dc5eb8291
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_doge20_staking_rewards(staked_amount, duration_in_days, reward_rate):
    """
    Calculates estimated rewards for DOGE20 staking based on dynamic reward rates.

    Parameters:
        staked_amount (float): The amount of DOGE20 tokens staked.
        duration_in_days (int): The staking duration in days.
        reward_rate (float): The daily reward rate (percentage as a decimal, e.g., 0.01 for 1%).

    Returns:
        float: The estimated staking rewards.

    Raises:
        ValueError: If any input is invalid (negative values or zero).
    """
    try:
        # Validate input parameters
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        if duration_in_days <= 0:
            raise ValueError("Duration in days must be greater than 0.")
        if reward_rate <= 0:
            raise ValueError("Reward rate must be greater than 0.")

        # Calculate rewards using the formula: rewards = staked_amount * reward_rate * duration_in_days
        rewards = staked_amount * reward_rate * duration_in_days
        return rewards

    except ValueError as e:
        # Log the error and re-raise the exception for the caller to handle
        logging.error(f"Input validation error: {e}")
        raise
    except Exception as e:
        # Log any unexpected errors and re-raise the exception
        logging.error(f"An unexpected error occurred: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        staked_amount = 1000.0  # DOGE20 tokens
        duration_in_days = 30  # 30 days
        reward_rate = 0.01  # 1% daily reward rate

        # Calculate rewards
        estimated_rewards = calculate_doge20_staking_rewards(staked_amount, duration_in_days, reward_rate)
        print(f"Estimated rewards for staking {staked_amount} DOGE20 tokens for {duration_in_days} days at {reward_rate*100}% daily rate: {estimated_rewards} DOGE20 tokens")
    except Exception as e:
        print(f"Error: {e}")
```
